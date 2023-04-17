from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Post, User
from .serializers import PostSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['PUT'])
def update_likes(request, clapp_id):
    print("test...........................................")
    """
    API endpoint to update the description of a blog post
    """
    print(request,clapp_id)
    try:
        print("test....................2")
        # Get the blog post by blog_id
        post = Post.objects.get(id=clapp_id)
        print(post)
        print(request.data)
        print(post.likes.set([]))
        # Update the description field with the new description from the request data
        # post.description = request.data.get('description')

        post.likes = request.data
        post.save()
        
        # Serialize the updated blog post
        serializer = PostSerializer(post)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Post.DoesNotExist:
        return Response({"error": "Blog post not found"}, status=status.HTTP_404_NOT_FOUND)

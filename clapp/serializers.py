from rest_framework import serializers
from .models import Post, Image, User, Tag

class ImageSerializer(serializers.Serializer):
    image_url = serializers.URLField()
    class Meta:
        model = Image
        fields = ['image_url']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class TagSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    weight = serializers.IntegerField()
    class Meta:
        model = Tag
        fields = ['name', 'weight']

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    created_date = serializers.DateTimeField()
    # images = ImageSerializer(many=True)
    # likes = UserSerializer(many=True)
    # dislikes = UserSerializer(many=True)
    # tags = TagSerializer(many=True)

    class Meta:
        model = Post
        # fields = ['id', 'title','images', 'description',  'created_date']
        fields = ['id', 'title','images', 'description', 'likes', 'dislikes', 'created_date', 'tags']
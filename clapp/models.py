from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    images = models.ManyToManyField('Image')
    description = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_posts')
    dislikes = models.ManyToManyField(User, related_name='disliked_posts')
    created_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag')
    
    
    def __str__(self):
        return self.title


class Image(models.Model):
    image_url = models.URLField()


class Tag(models.Model):
    name = models.CharField(max_length=255)
    weight = models.IntegerField()

    def __str__(self):
        return self.name

# class Tag(models.Model):
#     name = models.CharField(max_length=50)
#     weight = models.IntegerField(default=0)

#     def __str__(self):
#         return self.name

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     tags = models.ManyToManyField(Tag)
#     likes = models.ManyToManyField(User, related_name='liked_posts')
#     dislikes = models.ManyToManyField(User, related_name='disliked_posts')

#     def __str__(self):
#         return self.title

# class Photo(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images/')

#     def __str__(self):
#         return self.post.title + ' - ' + str(self.id)
from django.db import models

# -   Create a User table!
#     -   Users have usernames, passwords, created_at and updated_at

class User(models.Model):
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# -   Create a Message_Post table!
#     -   Message_Posts include message contents, user_who_posted, created_at and updated_at

class Message_Post(models.Model):
    content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    user_who_liked = models.ManyToManyField(User, related_name="liked_post")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# -   Add Likes!
#     -   Users should have the ability to 'like' a Message_Post

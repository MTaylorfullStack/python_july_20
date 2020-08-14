from django.db import models
import re

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['f_name']) < 2:
            errors['first_name'] = "Your first name must be more than 2 characters!!"
        if len(postData['l_name']) < 2:
            errors['last_name'] = "Your last name must be more than 2 characters!!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be valid format!!"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters!!"
        if postData['password'] != postData['conf_password']:
            errors['conf_password'] = "Password and confirm password do not match!!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class MessageManager(models.Manager):
    def validator(self, form):
        errors = {}
        if len(form['content']) < 5:
            errors['length'] = "Message must be at least 5 characters!"
        return errors

class Wall_Message(models.Model):
    content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class Comment(models.Model):
    content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Wall_Message, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






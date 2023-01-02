from django.db import models
#because we need a relationship between the posts and users
from django.contrib.auth.models import User

# Create your models here.
#we wanna make some  crud on posts so we need a post model
class Post(models.Model):
    #if the user is deleted the post will be deleted as well
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
           return self.title+"\n"+self.description


           #now we need to create a form that will allow us to create posts 
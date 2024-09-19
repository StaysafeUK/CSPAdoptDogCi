from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)
# dog fields added below
    dog_name = models.CharField(max_length=200, unique=False)
    dog_type = models.CharField(max_length=200, unique=False)
    dog_age = models.IntegerField()
    dog_stay = models.IntegerField()
    sanctuary = models.ForeignKey('Sanctuary', on_delete=models.CASCADE, related_name="dogs")
    
    STATUS = ((0, "Draft"), (1, "Published"))
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f" {self.title} | created by {self.author}"

    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

    class Meta:
        ordering = ["created_on"]

    

class Sanctuary(models.Model):
    sanct_name = models.CharField(max_length=200)
    sanct_address = models.TextField()
    sanct_postcode = models.CharField(max_length=15, unique=True)
    sanct_telephone = PhoneNumberField(blank=True)
    sanct_email = models.EmailField()
    sanct_website = models.URLField(max_length=200)

    def __str__(self):
        return f"name of sanctuary: {self.sanct_name}"

 


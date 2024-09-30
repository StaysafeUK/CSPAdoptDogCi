from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.decorators import login_required

## Commented out for Email Authorisation and authentication ##
#from django.contrib.auth.tokens import PasswordResetTokenGenerator
#from django.utils.encoding import force_str

# Create your models here.

class Post(models.Model):
    """
    Stores a single blog post related to :model:`auth.User`
    Stores a single Sanctuary related to :model:`Santuary.id`
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
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

# Comment Model 
class Comment(models.Model):
    """
    stores a single record from Post to comment :model:`Post.author``
    stores a single record from model:auth.User`
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

    class Meta:
        ordering = ["created_on"]   

 # Sanctuary Model       
class Sanctuary(models.Model):
    """
    Stores fields from Sanctuary :model:`Santuary`
    """
    sanct_name = models.CharField(max_length=200)
    sanct_address = models.TextField()
    sanct_postcode = models.CharField(max_length=15, unique=True)
    sanct_telephone = PhoneNumberField(blank=True)
    sanct_email = models.EmailField()
    sanct_website = models.URLField(max_length=200)

    def __str__(self):
        return f"name of sanctuary: {self.sanct_name}"

# #TOKEN GENERATOR for email authentication and authorisation currently not used 

# class TokenGenerator(PasswordResetTokenGenerator):
#     def _make_hash_value(self, user, timestamp):
#         return (
#             str(user.pk) + str(timestamp) + str(user.is_active)
#         )

# account_activation_token = TokenGenerator()

 


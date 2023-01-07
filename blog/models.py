from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify


# Create your models here.
class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Post(models.Model):

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
        ordering = ['-created_at']
    
    title = models.CharField(max_length=200)
    body = RichTextField(max_length=600, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True, upload_to="images")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class ContactProfile(models.Model):
    
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(verbose_name="Subject",max_length=100)
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'
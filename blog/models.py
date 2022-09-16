from django.db import models

from  django.utils.text import slugify

from  user_profile.models import User

class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class  Tag(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_blogs',
        on_delete=models.CASCADE,        
    )
    category = models.ForeignKey(
        Category,
        related_name='Category_blogs',
        on_delete=models.CASCADE,
    )
    likes = models.ManyToManyField(
        User,
        related_name='user_likes',
        blank=True,
        )
    tags = models.ManyToManyField(
        Tag,
        related_name='tag_blogs',
        blank=True
    )
    title = models.CharField(
        max_length=250
    )
    slug = models.SlugField(null=True, blank=True)
    
    banner = models.ImageField(upload_to='blog_banner')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
class Comment(models.Model):
    user = models.ForeignKey(
        User,
        related_name='blog_comments',
        on_delete=models.CASCADE
    )
    blog = models.ForeignKey(
        Blog,
        related_name='blog_comments',
        on_delete=models.CASCADE
        )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.text
    




class Reply(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_replies',
        on_delete=models.CASCADE
    )
    comment = models.ForeignKey(
        Comment,
        related_name='comment_replies',
        on_delete=models.CASCADE
        )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.text
        
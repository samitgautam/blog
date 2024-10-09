from django.db import models

# Create your models here.

# defines the category for the post

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

# defines the structure of Post

class Post(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("category",related_name="posts")

    def __str__(self):
        return self.title

# defines the comments section for the post

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"


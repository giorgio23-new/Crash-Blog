from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = {
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    }

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, name='posts', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='pics/', default='pics/noimage.jpg') 

    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ('-created_at',)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    body  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name) + " commented: " + str(self.body[:10])
    
    class Meta:
        ordering = ('-created_at',)

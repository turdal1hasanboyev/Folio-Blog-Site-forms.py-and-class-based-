from django.db import models

from datetime import date
# from django.template.defaultfilters import slugify # eski versiya
from django.utils.text import slugify # yangi versiya
from django.urls import reverse
import uuid

from django.contrib.auth.models import AbstractUser

from ckeditor.fields import RichTextField


class User(AbstractUser):
    image = models.ImageField(upload_to='profile_images', default='images/default-user-image.png')
    video = models.FileField(upload_to='profile_videos', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    bio_1 = RichTextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        if self.get_full_name():
            return f"{self.get_full_name()}"
        elif self.email:
            return f"{self.email}"
        else:
            return f"{self.username}"
        
    def age(self):
        # Agar birth_date mavjud emas yoki noto‘g‘ri formatda bo‘lsa, None qaytaramiz
        if not isinstance(self.birthday, date):
            return None

        today = date.today()

        age = today.year - self.birthday.year

        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            age -= 1
            
        return age
    

class Contact(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=50, unique=True, null=True, blank=True, db_index=True)
    subject = models.CharField(max_length=50, db_index=True)
    message = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        
    def __str__(self):
        return f"{self.name}"
    
class Category(models.Model):
    name = models.CharField(max_length=125, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name}"
    

class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='portfolio_category')
    image = models.ImageField(upload_to="portfolio_images/", default='images/default-image.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category.name}"
    
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'


class Article(models.Model):
    name = models.CharField(max_length=250, db_index=True, unique=True)
    slug = models.SlugField(max_length=250, db_index=True, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='article_images/', default='images/default-image.png')
    description = RichTextField(null=True, blank=True)
    description_1 = RichTextField(null=True, blank=True)
    description_2 = models.TextField(null=True, blank=True)
    category = models.ForeignKey(to='folio.Category', on_delete=models.CASCADE, related_name='article_category')
    author = models.ForeignKey(to='folio.User', on_delete=models.CASCADE, related_name='article_author')
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self, *args, **kwargs):
        return reverse('article-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            # self.slug = slugify(self.name) # default slugify
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}" # custom slugify by uuid4()

        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(to='folio.User', on_delete=models.CASCADE, related_name='comment_user')
    name = models.CharField(max_length=225, db_index=True)
    email = models.EmailField(max_length=100, db_index=True, null=True, blank=True)
    web_site = models.URLField(max_length=200, null=True, blank=True, db_index=True)
    comment = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

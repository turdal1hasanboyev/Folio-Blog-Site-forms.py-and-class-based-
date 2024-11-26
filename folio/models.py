from django.db import models

from datetime import date

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
        
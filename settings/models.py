from django.db import models

# Create your models here.
# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name="Название сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to = "logo/"
    )
    facebook = models.URLField(
        verbose_name="Ссылка на facebook аккаунт",
        blank = True, null = True,
    )
    twitter = models.URLField(
        verbose_name="Ссылка на twitter аккаунт",
        blank = True, null = True
    )
    pinterest = models.URLField(
        verbose_name="Ссылка на pinterest аккаунт",
        blank = True, null = True
    )
    instagram = models.URLField(
        verbose_name="Ссылка на instagram аккаунт",
        blank = True, null = True
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайтов"

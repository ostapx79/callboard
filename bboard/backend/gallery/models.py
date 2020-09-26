import os
from PIL import Image
from django.db import models
from datetime import datetime


from django.utils import timezone


def get_path_upload_image(id, file):
    """
    Сократить путь к загружаемому файлу его в формате
    подписчика: (media)/profile_pics/user_1/myphoto_2020-04-09.png
    """

    time = timezone.now().strftime("%Y-%m-%d")
    end_extention = file.split('.')[1]
    head = file.split('.')[0]
    if len(head) > 10:
        head = head[:10]
    file_name = head + '_' + timezone.now().strftime("%h-%m-%s")
    file_name += '.' + end_extention
    return os.path.join('photos', '{}', '{}').format(time, file_name)


class Photo(models.Model):
    """Фото"""

    name = models.CharField("Имя", max_length=50, unique=True)
    # TODO; для image генерить путь (user, date)
    image = models.ImageField("Фото", upload_to="gallery/")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.image.name = get_path_upload_image(self.id, self.image.name)
        super().save(*args, **kwargs)
#        if self.image:
#            img = Image.open(self.image.path)
#            if img.height > 200 or img.width > 200:
#                output_size = (200, 200)
#                img.thumbnail(output_size)
#                img.save(self.image.path)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Gallery(models.Model):
    """Галерея"""

    name = models.CharField("Имя", max_length=50, unique=True)
    photos = models.ManyToManyField(Photo, verbose_name="Фотографий")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"

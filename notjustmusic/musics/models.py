from django.db import models


class Albums(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    data = models.DateTimeField(verbose_name="Дата издания")
    picture = models.ImageField(upload_to="media/", verbose_name="Картинка")

    def __str__(self):
            return self.name

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    picture = models.ImageField(upload_to="media/")

    def __str__(self):
            return self.name

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
            return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Music(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    music = models.FileField(upload_to="media/", verbose_name="Файл")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Исполнитель")
    album = models.ForeignKey(Albums, on_delete=models.CASCADE, verbose_name="Альбом")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
            return self.name

    class Meta:
        verbose_name = "Трек"
        verbose_name_plural = "Треки"




from django.db import models


class Tank(models.Model):
    title = models.CharField("Название", max_length=70)
    opis = models.TextField("Описание")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    silka = models.CharField("Ссылка", null=True, max_length=70)
    strana = models.ForeignKey('Strana', on_delete=models.PROTECT, null=True, verbose_name='Страна')
    klas = models.ForeignKey('Klas', on_delete=models.PROTECT, null=True, verbose_name='Клас')
    publish = models.BooleanField('Опубликовано', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Танк'
        verbose_name_plural = 'Танки'
        ordering = ['-id']

class Strana(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Страна')
    publish = models.BooleanField('Опубликовано', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Klas(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Клас')
    publish = models.BooleanField('Опубликовано', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Класcы'



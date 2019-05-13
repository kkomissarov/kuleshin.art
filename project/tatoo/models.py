from django.db import models



class Work(models.Model):
    img = models.ImageField()
    type = models.CharField(
        choices=(('w', 'Готовая работа'), ('s', 'Эскиз')),
        max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

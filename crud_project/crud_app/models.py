from django.db import models


class CrudModel(models.Model):
    # Определите поля модели здесь
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    date_added = models.DateField(verbose_name='Date added', null=True, blank=True)
    ready_to = models.BooleanField(verbose_name='Ready', default=False)

    def __str__(self):
        return self.name

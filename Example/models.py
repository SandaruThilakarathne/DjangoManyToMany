from django.db import models


# Create your models here.
class ColorTemplate(models.Model):
    template_name = models.CharField(max_length=30)
    color = models.ManyToManyField('Colors', related_name='colors_mapping')

    class Meta:
        db_table = "color_template"


class Colors(models.Model):
    color_code = models.CharField(max_length=30)

    class Meta:
        db_table = 'colors'


# Create your models here.
# from django.db import models

# class TheodoTeam(models.Model):
#     name = models.CharField(max_length=150)
#     image = models.CharField(max_length=150)
#     fun_fact = models.TextField(blank=True)

#     class Meta:
#         verbose_name = "theodo UK team"

from django.db import models

class TheodoTeam(models.Model):
    text= models.CharField(max_length=255)
    author= models.CharField(max_length=255)

    class Meta:
        db_table = 'test_scrapy'
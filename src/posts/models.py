from django.db import models

# Create your models here.

'''
    1 : fields
    2 : validation
    3 : html widget

    لتنفيذ قاعدة البيانات هناك شيئين نقوم بعملها 
    1 : makemigrations
    2 : migrate
'''

class Post(models.Model):
    name = models.FloatField(max_length=100) # str max lenght
    content = models.TextField(max_length=5000)
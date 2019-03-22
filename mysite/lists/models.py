from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class InfoModelForm(models.Model):
    name = models.CharField('Name',max_length=255)
    mail = models.EmailField('Mail',max_length=255)
    gender = models.BooleanField('Gender')
    department = models.CharField('Organization',max_length=255)
    year = models.IntegerField('Years',default=0)
    created_at = models.DateField('CreateDate',default=timezone.now)

    def __str__(self):
        return '<id:' + str(self.id) + ',' + self.name + ',' + self.department + '>'

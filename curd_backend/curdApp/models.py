from django.db import models


# Create your models here.


class StudentInfo(models.Model):
    name = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=20, null=True)
    date = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

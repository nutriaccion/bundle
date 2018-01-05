from django.db import models

# Create your models here.

class Parental(models.Model):
    code = models.SlugField(max_length=25, db_index=True)
    name = models.CharField(max_length=100, db_index=True)


class Infant(models.Model):
    code = models.SlugField(max_length=25, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    birth_d = models.DateField(db_index=True, auto_now_add=True)
    gender = models.CharField(max_length=1)

    parent = models.ForeignKey(Parental,
                                on_delete=models.CASCADE, ## Maybe should be set null?
                                null=True)

    def __str__(self):
        return f"{self.name} - {self.birth_d}"

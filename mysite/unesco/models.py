from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name


class States(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name


class Region(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    justification = models.CharField(max_length=1000)
    year = models.IntegerField(null=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=6)
    latitude = models.DecimalField(max_digits=15, decimal_places=6)
    area_hectares = models.DecimalField(max_digits=15, decimal_places=6, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    states = models.ForeignKey(States, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self) :
        return self.name






# naruto_shippuden/models.py
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Village(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Character(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)
    first_appearance_date = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)
    image = models.CharField(max_length=500, null=True,blank=True)
    power_level = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    rarity = models.CharField(max_length=20)
    village = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Jutsu(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    character = models.ManyToManyField(Character)

    def __str__(self):
        return self.name

from django.db import models
class UserProfile(models.Model):
    ENTRY_CATEGORY_CHOICES = [
        ('admin', 'Apply as Admin'),
        ('buyer', 'Apply as Buyer'),
    ]
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    entry_category = models.CharField(max_length=10, choices=ENTRY_CATEGORY_CHOICES)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    country_of_citizenship = models.CharField(max_length=50)
    birthdate = models.DateField()
    phone = models.CharField(max_length=15)
    license_number = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.middlename} {self.surname}"

# Create your models here.

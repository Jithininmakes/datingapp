
from django.db import models
# from django.contrib.auth.models import AbstractUser
#
#
# class Interest(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(unique=True, max_length=100, null=True)
#
#     def __str__(self):
#         return self.name
#
# class Qualification(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(unique=True, max_length=100, null=True)
#
#     def __str__(self):
#         return self.name
#
# class Designation(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(unique=True, max_length=100, null=True)
#
#     def __str__(self):
#         return self.name
#
# class WorkLocation(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(unique=True, max_length=100, null=True)
#
#     def __str__(self):
#         return self.name
#
# class User(AbstractUser):
#         age = models.SmallIntegerField(null=True, validators=[validators.integer_validator])
#         dob = models.DateField( null=True)
#         phone = models.IntegerField(null=True)
#         smoking_habits = models.BooleanField( null=True)
#         drinking_habits = models.BooleanField( null=True)
#         # hobbies = models.ManyToManyField(to=Hobby)
#         interest = models.ForeignKey(to=Interest,on_delete=models.CASCADE,null=True)
#         qualification = models.ForeignKey(to=Qualification,on_delete=models.CASCADE,null=True)
#         profile_picture = models.ImageField(blank=True,upload_to='profile_pictures/', null=True)
#         multiple_image = models.ImageField(upload_to='multiple_image/', blank=True, null=True)
#         short_reel = models.FileField(blank=True,upload_to='short_reels/')
#
#         company_name = models.CharField(max_length=200,null=True)
#         designation = models.ForeignKey(to=Designation,on_delete=models.CASCADE, null=True)
#         work_location = models.ForeignKey(to=WorkLocation,on_delete=models.CASCADE, null=True)
#
#         title = models.CharField(max_length=255, null=True)
#         expertise_level = models.CharField(max_length=255, null=True)
#
#         @property
#         def is_employer(self):
#             return self.company_name is None and self.designation is None
#         def is_jobseeker(self):
#             return self.title is None and self.expertise_level is None
#
#     #

# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.core import validators
#
#
# # Create your models here.

# #

#

#

#
# class User(AbstractUser):
#     age = models.SmallIntegerField(null=True, validators=[validators.integer_validator])
#     dob = models.DateField( null=True)
#     phone = models.IntegerField(null=True)
#     smoking_habits = models.BooleanField( null=True)
#     drinking_habits = models.BooleanField( null=True)
#     # hobbies = models.ManyToManyField(to=Hobby)
#     interest = models.ForeignKey(to=Interest,on_delete=models.CASCADE,null=True)
#     qualification = models.ForeignKey(to=Qualification,on_delete=models.CASCADE,null=True)
#     profile_picture = models.ImageField(blank=True,upload_to='profile_pictures/', null=True)
#     multiple_image = models.ImageField(upload_to='multiple_image/', blank=True, null=True)
#     short_reel = models.FileField(blank=True,upload_to='short_reels/')
#
#     company_name = models.CharField(max_length=200,null=True)
#     designation = models.ForeignKey(to=Designation,on_delete=models.CASCADE, null=True)
#     work_location = models.ForeignKey(to=WorkLocation,on_delete=models.CASCADE, null=True)
#
#     title = models.CharField(max_length=255, null=True)
#     expertise_level = models.CharField(max_length=255, null=True)
#
#     @property
#     def is_employer(self):
#         return self.company_name is None and self.designation is None
#     def is_jobseeker(self):
#         return self.title is None and self.expertise_level is None
#
#




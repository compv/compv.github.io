from django.db import models

import PIL

# Create your models here.

class Users(models.Model):
    user_name = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50,null=True)
    phone_number = models.CharField(max_length=15,null=True)
    email = models.EmailField(max_length=40, unique=True, error_messages={}, validators='')
    password = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)
    residence_place = models.CharField(max_length=80, null=True)
    status = models.CharField(max_length=25, default='new_user')



class ImagesDatasets(models.Model):
    CAR =  'car'
    FACE = 'face'
    TREE = 'tree'
    IMAGE_CLASS_CHOICES  = (
        (CAR, 'class of cars'),
        (FACE, 'class of faces'),
        (TREE, 'class of trees')
    )

    name = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=50, null=False)
    creation_date = models.DateField(auto_now_add=True)
    image_class = models.CharField(max_length=20, choices=IMAGE_CLASS_CHOICES,
                                   default=FACE)



class Images(models.Model):
    CAR = 'car'
    FACE = 'face'
    TREE = 'tree'
    IMAGE_CLASS_CHOICES = (
        (CAR, 'class of cars'),
        (FACE, 'class of faces'),
        (TREE, 'class of trees')
    )

    image_owner = models.ForeignKey(Users)
    image_dataset = models.ForeignKey(ImagesDatasets)

    name = models.CharField(max_length=60, null=False)
    user_owner = models.CharField(max_length=50, null=False, default='anonim')
    image_class = models.CharField(max_length=20 , choices=IMAGE_CLASS_CHOICES)
    # потрібна бібліотека Pillow
    image = models.ImageField()
    date_adding = models.DateField(auto_now_add=True)
    image_format = models.CharField(max_length=10,default=None) #,choices=IMAGE_FORMAT_CHOICES)



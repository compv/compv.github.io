from django.contrib import admin
from .models import Users
from .models import ImagesDatasets
from .models import Images

# Register your models here.

admin.site.register(Users)
admin.site.register(Images)
admin.site.register(ImagesDatasets)
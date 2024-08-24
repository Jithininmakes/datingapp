from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Interest, Designation, WorkLocation, Qualification, Hobby


# Register your models here.
admin.site.register(User,UserAdmin)


admin.site.register(Hobby),
admin.site.register(Interest),
admin.site.register(Qualification),
admin.site.register(Designation),
admin.site.register(WorkLocation),

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile,Skill,Cause,NGO,Address,Contact,Education,Experiance
# Register your models here.

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Cause)
admin.site.register(NGO)
admin.site.register(Address)
admin.site.register(Education)
admin.site.register(Experiance)

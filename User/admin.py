from django.contrib import admin
from .models import Users
# Register your models here.
class adminUser(admin.ModelAdmin):
    fields = ['id','first_name','last_name','company_name',
            'city','state','zip','email','web','age']
admin.site.register(Users,adminUser)

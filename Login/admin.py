from django.contrib import admin

# Register your models here.
from Login.models import MLogin
class LoginAdmin(admin.ModelAdmin):
    List_display=('email','passw',)
admin.site.register(MLogin,LoginAdmin)
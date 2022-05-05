from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.site_header: str = "JETAUTHER"

admin.site.register(User, UserAdmin)

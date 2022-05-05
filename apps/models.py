from django.db import models
from django.conf import settings


# Create your models here.

class App(models.Model):
    created_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=100, unique=True)
    redirect_to_url = models.URLField()
    app_icon = models.ImageField(upload_to="icons", blank=True, null=True)
    app_category = models.CharField(max_length=80)
    app_access_data = models.CharField(max_length=300)
    app_public_key = models.CharField(max_length=300, unique=True)
    app_secret_key = models.CharField(max_length=100, unique=True)
    app_secret_key_hash = models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.app_name


class AllowedApps(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    last_login = models.DateTimeField(blank=True, null=True)
    allowed_on = models.DateTimeField(auto_now=True)
    number_of_logins = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.get_full_name + "-" + self.app.app_name

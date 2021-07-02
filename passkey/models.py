from django.db import models
from django.db.models.deletion import CASCADE
from home.models import User

# Create your models here.


class Passkey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30)
    username = models.CharField(
        null=False, default='AmodhShenoy', max_length=30)
    passkey = models.CharField(null=False, max_length=20)
    site_url = models.URLField(null=False)
    icon_url = models.URLField(
        default='https://www.pinclipart.com/picdir/middle/130-1303682_security-password-2-icon-password-icon-in-png.png')
    last_set = models.DateTimeField(auto_now_add=True, blank=True)

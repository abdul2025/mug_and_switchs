from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date
from core.validator import _PHONE_REGEX, _NAME_REGEX
import uuid

class Users(AbstractUser):
    userid = models.CharField(max_length=2255, unique=True, default=uuid.uuid4())
    phone_no = models.CharField(_('Mobile Number'), validators=[_PHONE_REGEX], max_length=10, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True, validators=[_NAME_REGEX])
    last_name = models.CharField(max_length=255, blank=True, null=True, validators=[_NAME_REGEX])
    is_blocked = models.BooleanField(default=False)
    email = models.EmailField(_('email address'), unique = True)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('phone_no', 'first_name', 'email', 'password')

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super().save(*args, **kwargs)

        
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    hidden = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        abstract = True
class LoginLog(BaseModel):
    username = models.CharField(max_length=11)

    def __str__(self):
        return '{} Logged in at {}'.format(self.username, self.created_at)
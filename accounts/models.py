from django.db import models
from django.conf import settings



class Country(models.Model):
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
       # db_table = 'countries'



class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    phone_number = models.BooleanField(blank=True, null=True, unique=True)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True)


class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_IOS = 2
    DEVICE_ANDROID = 3
    DEVICE_PC = 4
    DEVICE_TYPE_CHOICES =(
        (DEVICE_WEB, 'web'),
        (DEVICE_IOS, 'ios'),
        (DEVICE_ANDROID, 'android'),
        (DEVICE_PC, 'pc')
    )
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='devicse', on_delete=models.CASCADE)
    device_uuid = models.UUIDField('device_uuid', null=True)
    last_login = models.DateTimeField('last_login data', null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICES,default=DEVICE_WEB)
    device_os =models.CharField('device_os', max_length=20, blank=True)
    device_model = models.CharField('device_model', max_length=50,blank=True)
    app_version = models.CharField('app_version', max_length=20, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    

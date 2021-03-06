from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth import get_user_model

from jsonfield import JSONField
from crm.models import Company

User = get_user_model()


def get_upload_to(instance, filename):
    return 'uploads/avatar/{id}/{filename}'.format(
        id=instance.id, filename=filename)


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobile = models.CharField(verbose_name='手机', max_length=100, blank=True)
    avatar = models.ImageField(
        verbose_name='头像', blank=True, upload_to=get_upload_to)
    headimgurl = models.CharField(max_length=255, blank=True)
    nickname = models.CharField(max_length=200, blank=True)
    display_name = models.CharField(max_length=255, blank=True)
    sex = models.SmallIntegerField(default=1, choices=((1, '男性'), (2, '女性'),))
    country = models.CharField('国家', max_length=50, default='中国', blank=True)
    province = models.CharField('省', max_length=100, blank=True)
    city = models.CharField('城市', max_length=100, blank=True)
    prefs = JSONField(default=dict(), verbose_name='偏好设置', blank=True)
    is_manager = models.BooleanField(default=False)
    company = models.ForeignKey(Company, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def update_profile(self,
                       user_info,
                       fields=['nickname', 'sex', 'country',
                               'city', 'province', 'headimgurl']):
        for field in fields:
            if field in user_info:
                setattr(self, field, user_info[field])
        self.save()

    def set_name(self, name):
        self.display_name = name
        self.save()

    def verify(self, company):
        """认证客户"""
        self.company = company
        self.is_verified = True
        self.save()

    @property
    def name(self):
        if self.display_name:
            return self.display_name
        if self.nickname:
            return self.nickname
        return self.user.username


def create_profile(user):
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
    return user.profile


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    create_profile(instance)

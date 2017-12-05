from datetime import timedelta
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.conf import settings

from wechatpy.oauth import WeChatOAuth
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase


class Tag(TagBase):
    colour = models.CharField(max_length=255, blank=True)
    last_used = models.DateTimeField(default=now)

    def post_use(self):
        """最近一次使用标签"""
        self.last_used = now()
        self.save()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'colour': self.colour
        }

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class TaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(Tag,
                            related_name="%(app_label)s_%(class)s_items")


def upload_path(instance, filename):
    return 'uploads/{file_type}/{date}/{filename}'.format(
        file_type=instance.file_type,
        date=instance.created.strftime('%Y-%m-%d'),
        filename=filename)


class Attachment(models.Model):
    """附件"""

    FILE_TYPES = (
        ('general', '一般文件'),
        ('contract', '合同'),
        ('sfz', '身份证'),
        ('legal_man', '企业法人营业执照'),
        ('bank', '银行开户许可证'),
        ('credit', '机构信用代码证'),
        ('business_license', '营业执照副本'),
    )

    name = models.CharField(
        verbose_name='附件名称',
        help_text='不填写默认为文件名',
        db_index=True,
        blank=True,
        max_length=255)

    creator = models.ForeignKey(User, blank=True, null=True)

    file_type = models.CharField(
        choices=FILE_TYPES,
        verbose_name='文件类型',
        max_length=20,
        default='general')
    file = models.FileField(upload_to='upload_path')

    object_id = models.PositiveIntegerField(default=0)
    content_object = GenericForeignKey('content_type', 'object_id')
    content_type = models.ForeignKey(ContentType,
                                     null=True, blank=True)

    # meta info
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name
        super(Attachment, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "附件"
        verbose_name_plural = "附件"


class AccessToken(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    openid = models.CharField(max_length=255, unique=True)
    access_token = models.CharField(max_length=255, blank=True)
    refresh_token = models.CharField(max_length=255)
    expires_in = models.IntegerField(default=0)
    scope = models.CharField(max_length=200, default='snsapi_userinfo')
    created = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now_add=True)

    def has_expired(self):
        return now() - self.last_updated_at >= timedelta(seconds=self.expires_in)

    def refresh(self):
        client = WeChatOAuth(settings.WX_APPID,
                             settings.WX_APPSECRET,
                             settings.WX_REDIRECT_URI,
                             scope=self.scope)
        token = client.refresh_token(self.refresh_token)
        self.refresh_token = token['refresh_token']
        self.access_token = token['access_token']
        self.expires_in = token['expires_in']
        self.scope = token['scope']
        self.save()

    @staticmethod
    def save_token(cls, access_token):
        pass

from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.contrib.contenttypes.fields import GenericRelation

from jsonfield.fields import JSONField

from core.models import Attachment
from crm.models import Company


class Report(models.Model):
    """记账结果"""

    company = models.ForeignKey(Company, verbose_name='公司')
    bookkeeper = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='记账员')
    date = models.DateField(default=now, verbose_name='日期')
    data = JSONField(default='{}', blank=True)

    attachments = GenericRelation(Attachment)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('company', 'date')
        ordering = ('-date', 'company')
        verbose_name = '查账'
        verbose_name_plural = '查账'

    def __str__(self):
        return 'Report_{0}_{1}'.format(
            self.company.title,
            self.date.strftime('%Y%m'))

    def save(self, *args, **kwargs):
        return super(Report, self).save(*args, **kwargs)

from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone

from core.models import Attachment
from .tax import TaxBureau

User.add_to_class("__str__", lambda u: "{0}{1}".format(
    u.last_name, u.first_name) if u.last_name else u.username)


class Company(models.Model):
    title = models.CharField(verbose_name="企业名称", unique=True, max_length=255)

    TYPES = (
        ('limited', '有限责任公司'),
        ('individual', '个体工商户'),
        ('stock', '股份有限公司'),
        ('partnership', '合伙企业(有限合伙)'),
        ('collective', '集体所有制(股份合作)'),
        ('sole', '个人独资企业'),
    )
    type = models.CharField(verbose_name="公司类型", choices=TYPES,
                            default='limited', max_length=20)
    registered_capital = models.DecimalField(
        help_text="单位 (万元)",
        verbose_name="注册资金", max_digits=19, decimal_places=2)
    address = models.CharField(verbose_name="地址", blank=True, max_length=255)
    op_address = models.CharField(
        verbose_name="实际经营地址",
        help_text="不填，默认为公司注册地址",
        blank=True, max_length=255)

    # 主要业务负责人
    salesman = models.ForeignKey(User,
                                 verbose_name="业务员",
                                 blank=True, null=True,
                                 related_name="customers")
    # 管账人
    bookkeeper = models.ForeignKey(User,
                                   verbose_name="记账会计",
                                   blank=True, null=True,
                                   related_name="accounts")

    # unified social credit code
    uscc = models.CharField(verbose_name="社会统一信用代码号",
                            blank=True, max_length=255)

    registered_at = models.DateField(
        verbose_name="注册日期", blank=True, null=True)
    expired_at = models.DateField(
        verbose_name="执照有效日期", blank=True, null=True)

    business_license = models.CharField(
        verbose_name="营业执照号", blank=True, max_length=255)

    INDUSTRIES = (('auto_parts', '汽配'), ('food', '餐饮'), ('clother', '服装'),
                  ('wholesale', '批发业'), ('arch', '建筑'), ('shopping', '商贸'),
                  ('ad', '广告'), ('property', '房地产'), ('service', '服务业'),
                  ('trade', '贸易'), ('entertainment', '娱乐'))
    industry = models.CharField(
        choices=INDUSTRIES, verbose_name="所属行业", default='auto_parts',
        max_length=50)

    national_tax_id = models.CharField(
        verbose_name="国税登记证", blank=True, max_length=255)
    national_tax_sn = models.CharField(
        verbose_name="国税编码", blank=True, max_length=255)
    national_tax_staff = models.CharField(
        verbose_name="国税专管员", blank=True, max_length=255)

    national_tax_office = models.ForeignKey(
        TaxBureau,
        related_name='national_taxes',
        verbose_name="国税所属分局",
        limit_choices_to={'bureau': 'national'},
        blank=True,
        null=True)

    national_tax_phone = models.CharField(
        verbose_name="国税电话", blank=True, max_length=255)

    local_tax_id = models.CharField(
        verbose_name="地税登记证", blank=True, max_length=255)
    local_tax_sn = models.CharField(
        verbose_name="地税编码", blank=True, max_length=255)
    local_tax_staff = models.CharField(
        verbose_name="地税专管员", blank=True, max_length=255)
    local_tax_office = models.ForeignKey(
        TaxBureau,
        related_name='local_taxes',
        limit_choices_to={'bureau': 'local'},
        verbose_name="地税所属分局",
        blank=True, null=True)
    local_tax_phone = models.CharField(
        verbose_name="地税电话", blank=True, max_length=255)

    taxpayer_bank = models.CharField(
        verbose_name="纳税开户银行", blank=True, max_length=255)
    taxpayer_account = models.CharField(
        verbose_name="纳税账号", blank=True, max_length=255)

    # social security
    ss_bank = models.CharField(
        verbose_name="社保开户银行", help_text="不填，默认为纳税开户行", blank=True, max_length=255)
    ss_account = models.CharField(
        verbose_name="代扣社保账号", help_text="不填，默认为纳税账号", blank=True, max_length=255)
    ss_number = models.CharField(
        verbose_name="单位社保号", blank=True, max_length=255)
    ss_date = models.DateField(verbose_name="社保购买时间", blank=True, null=True)

    # 个体户
    individual_bank = models.CharField(
        verbose_name='基本户开户银行',
        blank=True,
        max_length=255)
    individual_account = models.CharField(
        verbose_name='基本户开账号',
        blank=True,
        max_length=255)

    CREDIT_RATINGS = (('good', '良好'), ('bad', '差'), ('very_bad', '很差'))
    credit_rating = models.CharField(
        verbose_name="信用评级",
        default='good',
        max_length=10,
        choices=CREDIT_RATINGS)

    TAXPAYER_TYPES = (('general', '一般纳税人'), ('small', '小规模纳税人'))
    taxpayer_type = models.CharField(
        verbose_name="纳税人类型",
        default='small',
        max_length=10,
        choices=TAXPAYER_TYPES)

    # 海关信息
    custom_entry_no = models.CharField(
        verbose_name='海关登记编号',
        blank=True,
        max_length=255)

    custom_register_no = models.CharField(
        verbose_name='海关注册编码',
        blank=True,
        max_length=255)

    custom_org_code = models.CharField(
        verbose_name='海关组织机构代码',
        blank=True,
        max_length=255)

    custom_registered_at = models.DateField(
        verbose_name='海关登记日期',
        blank=True,
        null=True)

    custom_expired_at = models.DateField(
        verbose_name="有效期",
        null=True,
        blank=True)

    premise = models.CharField(
        verbose_name="经营场地（英文)",
        max_length=255,
        blank=True)

    # 规模
    SCALE_SIZES = (('small', '小型企业 (50人以内)'),
                   ('medium', '中型企业 (50-200人)'),
                   ('large', '大型企业 (200人以上)'))
    scale_size = models.CharField(
        verbose_name="规模", default='small', max_length=10, choices=SCALE_SIZES)

    STATUS = (('valid', '有效'),
              ('invalid', '无效'))
    status = models.CharField(
        help_text="无效状态，不再为客户提供服务",
        verbose_name="状态", default='valid', max_length=10, choices=STATUS)

    IC_STATUS = (('normal', '正常'),
                 ('abnormal', '经营异常'))
    ic_status = models.CharField(
        help_text="经营异常: 已被工商局列入经营异常名录",
        verbose_name="工商状态", default='normal', max_length=10, choices=IC_STATUS)

    # 附件
    website = models.CharField(verbose_name="公司网站", blank=True, max_length=255)
    note = models.TextField(
        verbose_name="备注", blank=True, help_text='可添加公司的其它备注信息')

    has_custom_info = models.BooleanField(verbose_name='是否填写海关信息',
                                          editable=False,
                                          default=False)

    legal_people = models.CharField(
        verbose_name='法人', blank=True, max_length=200)

    has_customer_files = models.BooleanField(
        verbose_name='是否有存放客户资料',
        help_text='详细的资料信息请在备注里添加',
        default=False)
    attachments = GenericRelation(Attachment)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def has_expired(self):
        return self.expired_at and (self.expired_at <= timezone.now().date())

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.strip()
        self.has_custom_info = any([
            self.custom_entry_no, self.custom_expired_at,
            self.custom_org_code, self.custom_register_no,
            self.custom_registered_at])
        if not self.op_address:
            self.op_address = self.address
        if not self.ss_bank:
            self.ss_bank = self.taxpayer_bank
        if not self.ss_account:
            self.ss_account = self.taxpayer_account

        if not self.legal_people:
            try:
                self.legal_people = self.shareholder_set.get(
                    role='legal').people.name
            except:
                pass

        return super(Company, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "公司"
        verbose_name_plural = "公司"

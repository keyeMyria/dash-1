from collections import OrderedDict

from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone

from jsonfield import JSONField

from core.models import Attachment
from .tax import TaxBureau

User.add_to_class("__str__", lambda u: "{0}{1}".format(
    u.last_name, u.first_name) if u.last_name else u.username)


class Company(models.Model):
    title = models.CharField(verbose_name="企业名称", unique=True, max_length=255)
    alias = models.CharField(verbose_name="字号", blank=True, max_length=255)
    tax_username = models.CharField(
        verbose_name="电子税务局用户名", blank=True, max_length=255)
    tax_password = models.CharField(
        verbose_name="电子税务局密码",  blank=True, max_length=255)

    TYPES = (
        ('有限责任公司', '有限责任公司'),
        ('个体工商户', '个体工商户'),
        ('股份有限公司', '股份有限公司'),
        ('合伙企业(有限合伙)', '合伙企业(有限合伙)'),
        ('集体所有制(股份合作)', '集体所有制(股份合作)'),
        ('个人独资企业', '个人独资企业')
    )
    type = models.CharField(verbose_name="公司类型", choices=TYPES,
                            default='有限责任公司', max_length=20)
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
                                 on_delete=models.SET_NULL,
                                 verbose_name="业务员",
                                 blank=True, null=True,
                                 related_name="customers")

    salesman_username = models.CharField(
        verbose_name='业务员',
        max_length=200, blank=True, editable=False)
    # 管账人
    bookkeeper = models.ForeignKey(User,
                                   on_delete=models.SET_NULL,
                                   verbose_name="记账会计",
                                   blank=True, null=True,
                                   related_name="accounts")
    bookkeeper_username = models.CharField(
        verbose_name='记账员',
        max_length=200, blank=True, editable=False)

    # unified social credit code
    uscc = models.CharField(verbose_name="社会统一信用代码号",
                            blank=True, max_length=255)

    registered_at = models.DateField(
        verbose_name="注册日期", blank=True, null=True)
    expired_at = models.DateField(
        verbose_name="执照有效日期", blank=True, null=True)

    business_license = models.CharField(
        verbose_name="营业执照号", blank=True, max_length=255)

    INDUSTRIES = [('汽配', '汽配'),
                  ('餐饮', '餐饮'),
                  ('服装', '服装'),
                  ('批发业', '批发业'),
                  ('建筑', '建筑'),
                  ('商贸', '商贸'),
                  ('广告', '广告'),
                  ('房地产', '房地产'),
                  ('服务业', '服务业'),
                  ('贸易', '贸易'),
                  ('娱乐', '娱乐')]
    industry = models.CharField(
        choices=INDUSTRIES, verbose_name="所属行业", default='汽配',
        max_length=50)

    national_tax_id = models.CharField(
        verbose_name="国税登记证", blank=True, max_length=255)
    # national_tax_sn = models.CharField(
    #     verbose_name="国税编码", blank=True, max_length=255)
    national_tax_staff = models.CharField(
        verbose_name="国税专管员", blank=True, max_length=255)

    national_tax_office = models.ForeignKey(
        TaxBureau,
        on_delete=models.SET_NULL,
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
        on_delete=models.SET_NULL,
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
        verbose_name="社保开户银行",
        help_text="不填，默认为纳税开户行", blank=True, max_length=255)
    ss_account = models.CharField(
        verbose_name="代扣社保账号",
        help_text="不填，默认为纳税账号", blank=True, max_length=255)
    ss_number = models.CharField(
        verbose_name="单位社保号", blank=True, max_length=255)
    ss_date = models.DateField(
        verbose_name="社保购买时间", blank=True, null=True)
    ss_declared = models.CharField(
        verbose_name="社保申报",
        choices=(
            ("社保", "社保"),
            ("无", "无"),
        ),
        max_length=10,
        blank=True,
        default="无")

    TAX_DISKS = (
        ("百望", "百望"),
        ("航天", "航天")
    )
    tax_disk = models.CharField(
        max_length=100,
        verbose_name="税控盘", choices=TAX_DISKS, blank=True)

    tax_declared_begin = models.DateField(
        verbose_name="税务申报开始时间", blank=True, null=True)
    special_taxes = models.CharField(
        verbose_name="特别税种", blank=True, max_length=255
    )

    # 个体户
    individual_bank = models.CharField(
        verbose_name='基本户开户银行',
        blank=True,
        max_length=255)
    individual_account = models.CharField(
        verbose_name='基本户开账号',
        blank=True,
        max_length=255)

    CREDIT_RATINGS = [('良好', '良好'), ('一般', '一般'), ('差', '差'), ('很差', '很差')]
    credit_rating = models.CharField(
        verbose_name="信用评级",
        default='良好',
        max_length=10,
        choices=CREDIT_RATINGS)

    TAXPAYER_TYPES = [('一般纳税人', '一般纳税人'), ('小规模纳税人', '小规模纳税人')]
    taxpayer_type = models.CharField(
        verbose_name="纳税人类型",
        default='小规模纳税人',
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
    SCALE_SIZES = [('小型企业', '小型企业'), ('中型企业人)', '中型企业人)'), ('大型企业)', '大型企业)')]
    scale_size = models.CharField(
        verbose_name="规模", default='小型企业', max_length=10, choices=SCALE_SIZES)

    STATUS = [('有效', '有效'), ('无效', '无效')]
    status = models.CharField(
        help_text="无效状态，不再为客户提供服务",
        verbose_name="代理状态", default='有效',
        max_length=10, choices=STATUS)

    IC_STATUS = [('正常', '正常'), ('经营异常', '经营异常')]
    ic_status = models.CharField(
        help_text="经营异常: 已被工商局列入经营异常名录",
        verbose_name="经营状态",
        default='正常', max_length=10, choices=IC_STATUS)

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
    shareholder_info = JSONField(
        verbose_name="股东信息",
        default=[],
        null=False,
        load_kwargs={'object_pairs_hook': OrderedDict}
    )
    contactor = models.CharField(
        verbose_name='负责人', max_length=255, blank=True)
    contactor_phone = models.CharField(
        verbose_name='联系电话', max_length=255, blank=True)
    attachments = GenericRelation(Attachment)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def has_expired(self):
        return self.expired_at and (self.expired_at <= timezone.now().date())

    def show_shareholder_info(self):
        t = ''.join(['<li>{role} {name} {phone}</li>'.format(**o)
                     for o in self.shareholder_info])
        return mark_safe('<ul>{0}</ul>'.format(t))
    show_shareholder_info.short_description = '股东信息'

    def show_contactor_info(self):
        return mark_safe('{0} {1}'.format(self.contactor, self.contactor_phone))
    show_contactor_info.short_description = '联系人信息'

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

        if self.bookkeeper:
            self.bookkeeper_username = self.bookkeeper.username

        if self.salesman:
            self.salesman_username = self.salesman.username

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

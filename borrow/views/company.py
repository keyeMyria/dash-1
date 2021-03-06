from ._base import ApiView, Pagination, CheckPerm
from ..perm_types import company_perm
from crm.models.company import Company


class CompanyApiView(ApiView, Pagination):

    """有关公司的接口"""

    _search_fields = (('title', 'title__contains'), ('id', 'id'))
    _default_order = '-id'
    _list_fields = (
        'id',
        'title',
        'op_address',
        'industry',
        'salesman',
        'bookkeeper',
        'taxpayer_type',
        'license_status',
        'status',
        'contactor',
        'contactor_phone')

    @CheckPerm.check(company_perm.view)
    def api_list(self, request, args):
        search = Company.objects.all()
        result = self.pagination(args, search)
        return self.success(result)

    @CheckPerm.check(company_perm.view)
    def api_filter(self, request, args):
        filter_query = self.get_filter_query(args)
        search = Company.objects.filter(**filter_query)
        result = self.pagination(args, search)
        return self.success(result)

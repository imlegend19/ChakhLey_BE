from django.db import models
from django.utils.text import gettext_lazy as _
from drfaddons.models import CreateUpdateModel
from drf_user.models import User
from ChakhLe_BE.variables import DESIGNATIONS


class Employee(models.Model):
    from business.models import Business

    user = models.ForeignKey(verbose_name=_("User"), to=User, on_delete=models.PROTECT)
    create_date = models.DateTimeField(_('Create Date/Time'),
                                       auto_now_add=True)
    update_date = models.DateTimeField(_('Date/Time Modified'),
                                       auto_now=True)
    designation = models.CharField(verbose_name=_("Designation"), choices=DESIGNATIONS,
                                   max_length=10, null=True, blank=True)
    business = models.ForeignKey(to=Business, on_delete=models.PROTECT, default=1)
    is_active = models.BooleanField(verbose_name=_("Is Active?"), default=True)
    joined_on = models.DateField(verbose_name=_("Join Date"), null=True,
                                 blank=True)
    left_on = models.DateField(verbose_name=_("Leave Date"), null=True,
                               blank=True)
    salary = models.DecimalField(verbose_name=_("Salary"), default=0,
                                 decimal_places=2, max_digits=10)

    def clean(self, *args, **kwargs):
        if self.designation == 'DB' and not self.user.is_delivery_boy:
            raise ValidationError('Not a valid delivery boy')
        super(Employee, self).clean()

    def __str__(self):
        return self.user.name + ' - ' + self.user.mobile

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")


class EmployeeDocument(CreateUpdateModel):
    from ChakhLe_BE.variables import EMPLOYEE_DOCUMENT_CHOICES
    from drf_user.models import User

    employee = models.ForeignKey(to=Employee, on_delete=models.PROTECT,
                                 verbose_name=_("Employee"))
    doc = models.FileField(null=True, blank=True)
    doc_type = models.CharField(verbose_name=_("Document Type"), max_length=5,
                                choices=EMPLOYEE_DOCUMENT_CHOICES)
    doc_value = models.CharField(verbose_name=_("Document ID"),
                                 max_length=254, null=True, blank=True)
    is_verified = models.BooleanField(verbose_name=_("Is Verified?"),
                                      default=False)
    verified_by = models.ForeignKey(to=User, on_delete=models.PROTECT,
                                    related_name="verified_document",
                                    null=True, blank=True)
    verified_on = models.DateField(verbose_name=_("Verified On"), null=True,
                                   blank=True)

    def __str__(self):
        return self.employee.name + "'s " + self.get_doc_type_display()

    class Meta:
        verbose_name = _("Employee's Document")
        verbose_name_plural = _("Employee's Documents")

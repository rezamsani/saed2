from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from constant.m_error import Error
from constant.fix_number import FixNumber



def validate_size(value):    
    if value > FixNumber.max_size_percent_author or value <= FixNumber.min_size_percent_author:
        raise ValidationError(Error.error_permitted_interval)  

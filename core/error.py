from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import ValidationError
from enum import Enum
import logging
logger = logging.getLogger('django')


class Error(Enum):
    DEFAULT_ERROR = {'code': -2323, 'detail': _('Something went wrong!')}
    BLOCKED_USER = {'code': -403, 'detail': _('User is banned!')}
    NO_ACTIVE_ACCOUNT = {'code': -1500, 'detail': _('No active account found with the given credentials!')}



class APIError:
    def __init__(self, error: Error, extra=None):
        self.error = error
        self.extra = extra or None
        error_detail = error.value
        if self.extra:
            # Extra values can be used in foramtting a string that contains {}
            if isinstance(self.extra, list):
                error_detail['detail'] = error_detail['detail'].format(*extra)
        try:
            logger.info(error.value)
        except BaseException:
            pass
        raise ValidationError(**error_detail)
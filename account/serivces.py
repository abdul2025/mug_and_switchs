from .models import *
from .enum import *
from core.error import *


class AccountService:
    @staticmethod
    def login(username: str) -> None:
        LoginLog.objects.create(username=username)



    @staticmethod
    def optain_customers_access_token(user: Users, token: dict) -> dict:
        if not user.groups.filter(name=GroupEnum.CUSTOMERS_GROUP.value).exists():
            raise APIError(Error.NO_ACTIVE_ACCOUNT)
        # Add custom claims
        token['roles'] = list(user.groups.all().values())
        return token



    @staticmethod
    def optain_access_token(group: GroupEnum, user: Users, token: dict) -> dict:
        if user.is_blocked:
            raise APIError(Error.BLOCKED_USER)
        
        if group == GroupEnum.CUSTOMERS_GROUP:
            return AccountService.optain_customers_access_token(
                user=user, token=token)
            
        #TODO: HERE where new users Groups add to optain new tokens  
        else:
            raise APIError(Error.NO_ACTIVE_ACCOUNT)
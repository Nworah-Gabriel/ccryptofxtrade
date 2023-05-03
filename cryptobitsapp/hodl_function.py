from .models import UserMessages,UserExtraInformation,Contact,subscriber, UserBasicInformation, Notice, CompanyDetail,WalletAddress, AcceptedCoin,WithdrawalTransaction,DepositTransaction
from django.utils.crypto import get_random_string
from django.utils import timezone
# import datetime
# import tzlocal
# from datetime import timedelta
from django.db.models import Count
from django.db.models import Q



def uuid_generator(id_type):
    type = id_type
    u_id = get_random_string(length=8, allowed_chars='01234567890')
    if type == "withdraw":       
        chars = "WD"
        try:
            item = WithdrawalTransaction.objects.get(uuid=chars + u_id)
            u_id = uuid_generator(id_type)
            
        except:
            pass

    elif type == "deposit":
        chars = "DP"
        try:
            item = DepositTransaction.objects.get(uuid=chars + u_id)
            u_id = uuid_generator(id_type)
        except:
            pass

    # elif type == "c_id":
    #     chars = "AP"
    #     try:
    #         item = UserBasicInformation.objects.get(customer_id=chars + u_id)
    #         u_id = uuid_generator(id_type)
            
    #     except:
    #         pass
    
    
    unique_id = chars + u_id
    return(unique_id)

def visitors():
    visits =  get_random_string(length=2, allowed_chars='67890')
    return(visits)

def cid_generator(id_type):
    type = id_type
    u_id = get_random_string(length=26, allowed_chars='01234567890')
    

    if type == "c_id":
        chars = "AP"
        try:
            item = UserBasicInformation.objects.get(customer_id=chars + u_id)
            u_id = uuid_generator(id_type)
            
        except:
            pass
    
    
    unique_id = chars + u_id
    return(unique_id)

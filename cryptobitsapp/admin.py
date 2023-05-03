from django.contrib import admin
from .models import UserMessages,UserExtraInformation,Contact,subscriber, UserBasicInformation, Notice, CompanyDetail,WalletAddress, AcceptedCoin,WithdrawalTransaction,DepositTransaction,  BankInformation, StakingStock, DefiCoin, UserStockStaking, UserDefiStaking, UserWallet, UserIntermediateInformation, UserAdvanceInformation

from .models import  UserAccountInformation, UserIdInformation
# admin.site.register(UserExtraInformation)
# admin.site.register(AdminMessages)
admin.site.register(UserMessages)



class UserWalletAdmin(admin.ModelAdmin):
    list_display = 'user','coin'
    
    # search_fields = 'name',
    list_filter =  []
  
admin.site.register(UserWallet, UserWalletAdmin)

class UserIntermediateInformationAdmin(admin.ModelAdmin):
    # list_display = 'user'
    
    # search_fields = 'name',
    list_filter =  []
  
admin.site.register(UserIntermediateInformation, UserIntermediateInformationAdmin)

class UserAccountInformationAdmin(admin.ModelAdmin):
    # list_display = 'user'
    
    # search_fields = 'name',
    list_filter =  []
  
admin.site.register(UserAccountInformation, UserAccountInformationAdmin)

class UserIdInformationAdmin(admin.ModelAdmin):
    # list_display = 'user'
    
    # search_fields = 'name',
    list_filter =  []
  
admin.site.register(UserIdInformation, UserIdInformationAdmin)



class UserAdvanceInformationAdmin(admin.ModelAdmin):
    # list_display = 'user'
    
    # search_fields = 'name',
    list_filter =  []
  
admin.site.register(UserAdvanceInformation, UserAdvanceInformationAdmin)

class StakingStockAdmin(admin.ModelAdmin):
    list_display = 'name','available', 'dollar_value', 'minimum_lock_amount','maximum_lock_amount'
    
    search_fields = 'name','minimum_lock_amount'
    list_filter =  ['available']
  
admin.site.register(StakingStock, StakingStockAdmin)

class DefiCoinAdmin(admin.ModelAdmin):
    list_display =  'name','available', 'dollar_value', 'minimum_lock_amount','maximum_lock_amount'
    
    # search_fields = 'name'
    # list_filter =  ['notice_type']
  
admin.site.register(DefiCoin, DefiCoinAdmin)

class UserStockStakingAdmin(admin.ModelAdmin):
    list_display =  'user','stock', 'quantity', 'stake_date', 'value_date','status'
    
    search_fields = 'name','minimum_lock_amount'
    list_filter =  ['status']
  
admin.site.register(UserStockStaking, UserStockStakingAdmin)

class UserDefiStakingAdmin(admin.ModelAdmin):
    list_display = 'user','coin', 'quantity', 'interest_period', 'redemption_period','interest_rate','status'
    
    # search_fields = 'name'
    # list_filter =  ['notice_type']
  
admin.site.register(UserDefiStaking, UserDefiStakingAdmin)

class AcceptedCoinAdmin(admin.ModelAdmin):
    list_display = 'name','address', 'minimum_withdraw', 'maximum_deposit'
    
    # search_fields = 'name'
    # list_filter =  ['notice_type']
  
admin.site.register(AcceptedCoin, AcceptedCoinAdmin)
class NoticeAdmin(admin.ModelAdmin):
    list_display = 'message','notice_type', 'created'
    
    search_fields = 'message','notice_type', 'created'
    list_filter =  ['notice_type']
  
admin.site.register(Notice, NoticeAdmin)


class CompanyDetailAdmin(admin.ModelAdmin):
    list_display = 'mobile','country', 'address'
    
    # search_fields = 'message','notice_type', 'created'
    # list_filter =  ['notice_type']
  
admin.site.register(CompanyDetail, CompanyDetailAdmin)


class WalletAddressAdmin(admin.ModelAdmin):
    list_display = 'user','eth', 'btc'
    
    # search_fields = 'message','notice_type', 'created'
    # list_filter =  ['notice_type']
  
admin.site.register(WalletAddress, WalletAddressAdmin)

class UserBasicInformationAdmin(admin.ModelAdmin):
    list_display = 'user','balance', 'country',
    readonly_fields = ['user' ]
    search_fields ='user','balance','country'
    list_filter =  'user',
  
admin.site.register(UserBasicInformation, UserBasicInformationAdmin)

class WithdrawalTransactionAdmin(admin.ModelAdmin):
    list_display = 'user','date', 'coin_code','amount','status'
    # readonly_fields = ['user' ]
    search_fields ='user','amount','status'
    list_filter =  'currency_coin','date'
  
admin.site.register(WithdrawalTransaction, WithdrawalTransactionAdmin)

class DepositTransactionAdmin(admin.ModelAdmin):
    list_display = 'user','date', 'amount','status'
    # readonly_fields = ['user' ]
    search_fields ='user','amount','status'
    list_filter =  'currency_coin','date'
  
admin.site.register(DepositTransaction, DepositTransactionAdmin)


class subscriberAdmin(admin.ModelAdmin):
    list_display =['email', 'created']
    search_fields ='email',
    list_filter =  'email',
admin.site.register( subscriber, subscriberAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display =['name', 'created','email', 'subject']
    search_fields ='email','subject'
    list_filter =  'email','created'
  
admin.site.register( Contact, ContactAdmin)
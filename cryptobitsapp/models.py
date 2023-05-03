from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
import django

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Notice(models.Model):
    WARNING = 'WR'
    SAFE = 'SF'
    NEUTRAL= 'NE' 
    NONE = 'NN'   

    NOTICE_TYPE_CHOICES = [
    ('SF', 'safe'),
    ('WR', 'warning'),
    ('NE', 'Neutral'),
    ('NN', 'None'),
    ] 
    
    message = models.TextField(max_length=5000)
    notice_type =  models.CharField(
        max_length=2,
        choices=NOTICE_TYPE_CHOICES,
        default=NONE,
         )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return "sender:" + str(self.sender) +"body:"+ str (self.message)

class CompanyDetail(models.Model):
    name = models.CharField(max_length=5)
    mobile= models.CharField(max_length=15)
    country = models.CharField(max_length=50)
    address =models.CharField(max_length=50)
    email = models.EmailField(max_length=50, default="NONE")
   

    def __str__(self):
         return "location:" + str(self.address) 

# user verifications



class AcceptedCoin(models.Model):
    name = models.CharField(max_length=150)
    api_id = models.CharField(max_length=20, default="api-trace-id")
    code = models.CharField(max_length=5)
    address = models.CharField(max_length=150)
    network = models.CharField(max_length=10)
    qrcode = models.ImageField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    dollar_value =  models.DecimalField(decimal_places=5, max_digits=10)
    minimum_deposit = models.DecimalField(decimal_places=2, max_digits=35)
    minimum_withdraw = models.DecimalField(decimal_places=2, max_digits=35)
    maximum_deposit = models.DecimalField(decimal_places=2, max_digits=35)
    maximum_withdraw = models.DecimalField(decimal_places=2, max_digits=35)
    charge = models.DecimalField(decimal_places=2, max_digits=35)
    time = models.IntegerField()
    def __str__(self):
         return "code:" + str(self.code)



class StakingStock(models.Model):
    name = models.CharField(max_length=150)
    available = models.BooleanField(default=True)
    api_id = models.CharField(max_length=20, default="api-trace-id")
    # address = models.CharField(max_length=150)
    dollar_value =  models.DecimalField(decimal_places=5, max_digits=35)
    logo = models.ImageField(null=True, blank=True)
    short_interest_rate = models.DecimalField(decimal_places=2, max_digits=35)
    med_interest_rate = models.DecimalField(decimal_places=2, max_digits=35)
    long_interest_rate = models.DecimalField(decimal_places=2, max_digits=35)
    minimum_lock_amount = models.DecimalField(decimal_places=6, max_digits=35)
    maximum_lock_amount = models.DecimalField(decimal_places=6, max_digits=35)
    charge = models.DecimalField(decimal_places=2, max_digits=35)
    time = models.IntegerField()
    def __str__(self):
         return "Stock name:" + str(self.name)

class DefiCoin(models.Model):
    name = models.CharField(max_length=150)
    coin = models.CharField(max_length=5)
    api_id = models.CharField(max_length=20, default="api-trace-id")
    code = models.CharField(max_length=5)
    available = models.BooleanField(default=True)
    # address = models.CharField(max_length=150)
    dollar_value =  models.DecimalField(decimal_places=2, max_digits=35)
    logo = models.ImageField(null=True, blank=True)
    dollar_value =  models.DecimalField(decimal_places=5, max_digits=35)
    short_interest_rate = models.DecimalField(decimal_places=2, max_digits=35)
    
    med_interest_rate = models.DecimalField(decimal_places=2, max_digits=35)
    long_interest_rate = models.DecimalField(decimal_places=2, max_digits=35)
    minimum_lock_amount = models.DecimalField(decimal_places=6, max_digits=35)
    maximum_lock_amount = models.DecimalField(decimal_places=6, max_digits=35)
    charge = models.DecimalField(decimal_places=2, max_digits=35)
    time = models.IntegerField()
    def __str__(self):
         return "Deficode:" + str(self.code)


class UserStockStaking(models.Model):
    SUBMITTED = 'SUB'
    APPROVED = 'APV'
    DECLINED = 'DCL'
    


    STATUS = [
    ('SUB', 'submitted'),
    ('APV', 'approved'),
    ('DCL', 'declined'),
    
    ] 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(StakingStock, null = True, related_name='Staking_stock', on_delete=models.SET_NULL )
    quantity = models.DecimalField(decimal_places=10, max_digits=35, default=0)
    last_credit_time = models.DateTimeField(null=True, blank=True, default=django.utils.timezone.now())
    farm_quantity = models.DecimalField(decimal_places=10, max_digits=35, default=0)
    stake_date = models.DateTimeField(null=True, blank=True,default=django.utils.timezone.now())
    value_date = models.DateTimeField(null=True, blank=True)
    interest_end_date = models.DateTimeField(null=True, blank=True,default=timezone.now())
    # redemption_date = models.DateTimeField(null=True, blank=True)
    # redemption_period = models.IntegerField(default=0)
    rate_per_hour = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    interest_period = models.IntegerField(default=0)   
    farming = models.BooleanField(default=False)
    # timer = models.CharField(max_length=500, default="time")
    
    status = models.CharField(
        max_length=3,
        choices=STATUS,
        default=SUBMITTED,
         )
    
    def __str__(self):
        return f"{self.user}, {self.stock}"



class UserDefiStaking(models.Model):
    SUBMITTED = 'SUB'
    APPROVED = 'APV'
    DECLINED = 'DCL'
    


    STATUS = [
    ('SUB', 'submitted'),
    ('APV', 'approved'),
    ('DCL', 'declined'),
    
    ] 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.ForeignKey(DefiCoin, null = True, related_name='DefiCoin', on_delete=models.SET_NULL )
    quantity = models.DecimalField(decimal_places=10, max_digits=35, default=0)
    last_credit_time = models.DateTimeField(null=True, blank=True, default=django.utils.timezone.now())
    
    farm_quantity = models.DecimalField(decimal_places=10, max_digits=35, default=0)
    stake_date = models.DateTimeField(null=True, blank=True,default=django.utils.timezone.now())
    value_date = models.DateTimeField(null=True, blank=True)
    farming = models.BooleanField(default=False)
    interest_period = models.IntegerField(default=0)
    rate_per_hour = models.IntegerField(default=0)
    redemption_period = models.IntegerField(default=0)
    interest_end_date = models.DateTimeField(null=True, blank=True,default=timezone.now())
    interest_rate = models.DecimalField(decimal_places=2, max_digits=35, default=0)
    # timer = models.CharField(max_length=500, default="time")
    status = models.CharField(
        max_length=3,
        choices=STATUS,
        default=SUBMITTED,
         )
    
    def __str__(self):
        return f"{self.user}, {self.coin}"

class WalletAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eth= models.CharField(max_length=150, blank=True)
    btc= models.CharField(max_length=150, blank=True)
    bnb= models.CharField(max_length=150, blank=True)
    dodge = models.CharField(max_length=150, blank=True)
    xrp= models.CharField(max_length=150, blank=True)
    bch= models.CharField(max_length=150, blank=True)
    

    def __str__(self):
         return "owner:" + str(self.user)
# -withdrawal
# -date
# -date completed
# -amount
# -currency
# -address
# id-##
# -recieving mode
# -status


class WithdrawalTransaction(models.Model):
   
    SUBMITTED = 'SUB'
    APPROVED = 'APV'
    DECLINED = 'DCL'
    


    STATUS = [
    ('SUB', 'submitted'),
    ('APV', 'approved'),
    ('DCL', 'declined'),
    
    ] 
    uuid = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    amount = models.DecimalField(decimal_places=2, max_digits=35)
    charge = models.DecimalField(decimal_places=2, max_digits=35)
    currency_coin = models.ForeignKey(AcceptedCoin, null = True, related_name='Accepted_Coin_withdraw', on_delete=models.SET_NULL )
    coin_code = models.CharField(max_length=3, blank=True)
    status = models.CharField(
        max_length=3,
        choices=STATUS,
        default=SUBMITTED,
         )
 

class DepositTransaction(models.Model):
    SUBMITTED = 'SUB'
    APPROVED = 'APV'
    DECLINED = 'DCL'
    


    STATUS = [
    ('SUB', 'submitted'),
    ('APV', 'approved'),
    ('DCL', 'declined'),
    
    ] 
    uuid = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    receipt= models.ImageField(null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=35)
    currency_coin = models.ForeignKey(AcceptedCoin, null = True, related_name='Accepted_Coin_deposit', on_delete=models.SET_NULL )
    coin_code = models.CharField(max_length=3, blank=True)
    status = models.CharField(
        max_length=3,
        choices=STATUS,
        default=SUBMITTED,
         )
    # receiver_address= models.CharField(max_length=150)

class UserWallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.ForeignKey(AcceptedCoin, null = True, related_name='Accepted_Coin', on_delete=models.SET_NULL )
    balance = models.DecimalField(decimal_places=5, max_digits=35, default = 0)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return "user:" + str(self.user) +"coin:"+ str (self.coin)


# Create your models here.
class UserMessages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=5000)
    subject = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return "sender:" + str(self.sender) +"body:"+ str (self.message)

class UserExtraInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=500)
    moblie_number = models.CharField(max_length=15)
    country = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    alternate_email = models.EmailField(max_length=70)
    date_of_birth = models.CharField(max_length=50)
    balance = models.DecimalField(decimal_places=2, max_digits=35)
    amount_available = models.DecimalField(decimal_places=2, max_digits=35)
    amount_withdrawable = models.DecimalField(decimal_places=2, max_digits=35)
    gold = models.BooleanField(default=False)
    def __str__(self):
         return str(self.user)


class UserIntermediateInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_id =  models.ImageField(null=True, blank=True)
    gov_id_front =  models.ImageField(null=True, blank=True)
    gov_id_back =  models.ImageField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    def __str__(self):
         return str(self.user)


class UserAccountInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_id =  models.ImageField(null=True, blank=True)
    
    selfie =  models.ImageField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    def __str__(self):
         return str(self.user)


class UserIdInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_id =  models.ImageField(null=True, blank=True)
    
    # selfie =  models.ImageField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    def __str__(self):
         return str(self.user)

class UserAdvanceInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    proof_of_address =  models.ImageField(null=True, blank=True)
    SSN = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)
    def __str__(self):
         return str(self.user)

class UserBasicInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)   
    title = models.CharField(max_length=50, default="NONE")
    date_of_birth = models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=15, default="NO MOBILE")
    address = models.CharField(max_length=250, default="no address")
    postal_code = models.CharField(max_length=70, default="0000")
    customer_id = models.CharField(max_length=70, default="0000")
    city = models.CharField(max_length=70, default="not added")
    
    # birth_date = models.DateField(auto_now_add=True)
    
    balance = models.DecimalField(decimal_places=2, max_digits=35)
    amount_available = models.DecimalField(decimal_places=2, max_digits=35)
    amount_withdrawable = models.DecimalField(decimal_places=2, max_digits=35)
    pro_verified = models.BooleanField(default=False)
    

    
    def __str__(self):
         return str(self.user)


class BankInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name =  models.CharField(max_length=70)
    account_name =  models.CharField(max_length=70)
    account_number =  models.CharField(max_length=70)
    


    def __str__(self):
         return str(self.user)



# class UserProInformation(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     ssn = models.CharField(max_length=50)
#     front_id_card = models.ImageField()#image field
#     back_id_card = models.imagefield()#image field
#     valid_id_card = models.imagefield()#image field
    
    # def __str__(self):
    #      return str(self.user)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=5000)
    subject = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return "name:" + str(self.name) +"body:"+ str (self.message)

class subscriber(models.Model):
   
    email = models.EmailField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return "name:" + str(self.email) 
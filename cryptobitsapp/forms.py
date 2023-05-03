from django import forms
from .models import DepositTransaction,UserAdvanceInformation, UserIntermediateInformation
from .models import UserAccountInformation, UserIdInformation
class LoginForm(forms.Form):
    username = forms.CharField(max_length=70)
    password= forms.CharField(widget=forms.PasswordInput)

# class SignupFormextra(forms.Form):
#     wallet_address = forms.CharField(max_length=70)
#     moblie_number = forms.CharField(max_length=70)
#     occupation = forms.CharField(max_length=70)
#     alternate_email = forms.EmailField()
#     date_of_birth = forms.DateField()
#     country = forms.CharField(max_length=70)
    
class SignupFormextra(forms.Form):
    # will be labelled basic verification 
    #work date of birth label not showing
    country = forms.CharField(max_length=70)
    title = forms.CharField(max_length=70)
    postal_code = forms.CharField(max_length=70)
    date_of_birth = forms.DateField()
    mobile = forms.CharField(max_length=70)


class withdrawalDetailForm(forms.Form):
    bank_name = forms.CharField(max_length=70,required=False)
    account_name = forms.CharField(max_length=70,required=False)
    account_number = forms.CharField(max_length=70,required=False)
    eth= forms.CharField(max_length=70,required=False)
    btc= forms.CharField(max_length=70,required=False)
    bnb= forms.CharField(max_length=70,required=False)
    dodge = forms.CharField(max_length=70,required=False)
    xrp= forms.CharField(max_length=70,required=False)
    bch= forms.CharField(max_length=70,required=False)

class UpdateBalForm(forms.Form):
    username= forms.CharField(max_length=70)
    newbalance = forms.DecimalField(decimal_places=2, max_digits=35)
    amount = forms.DecimalField(decimal_places=2, max_digits=35)
    coin_type = forms.CharField(max_length=70)
    send_email = forms.BooleanField(initial=False,required=False)

class UpdateFarmBalForm(forms.Form):
    username= forms.CharField(max_length=70)
    newbalance = forms.DecimalField(decimal_places=2, max_digits=35)
    farm_item_name = forms.CharField(max_length=70)
    amount = forms.DecimalField(decimal_places=2, max_digits=35)
    send_email = forms.BooleanField(initial=False,required=False)

class UserPasswordChangeForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    password2= forms.CharField(widget=forms.PasswordInput)

class userDetailForm(forms.Form):
    # username = forms.CharField(max_length=70, required=False)
    email = forms.EmailField(required=False)
    firstname = forms.CharField(max_length=70, required=False)
    lastname = forms.CharField(max_length=70, required=False) 
    country = forms.CharField(max_length=70, required=False)
    postal_code = forms.CharField(max_length=70, required=False)
    city = forms.CharField(max_length=70, required=False)
    address = forms.CharField(max_length=170, required=False)
    date_of_birth = forms.DateField(required=False)
    
class UserAdvanceInformationForm(forms.ModelForm):
    class Meta:
        model =UserAdvanceInformation
        fields = ('proof_of_address','SSN')

class UserIntermediateInformationForm(forms.ModelForm):
    class Meta:
        model =UserIntermediateInformation
        fields = ('valid_id','gov_id_front', 'gov_id_back')



class UserAccountInformationForm(forms.ModelForm):
    class Meta:
        model =UserAccountInformation
        fields = ('valid_id','selfie')

class UserIdInformationForm(forms.ModelForm):
    class Meta:
        model =UserIdInformation
        fields = ('valid_id',)
    
class WithdrawalForm(forms.Form):
    amount = forms.DecimalField(decimal_places=5, max_digits=35, required=True)
    dollar_value = forms.DecimalField(decimal_places=5, max_digits=35, required=True)
    address = forms.CharField(max_length=150, required=True)
    currency = forms.CharField(max_length=3, required=True)
    usd_trans=  forms.CharField(max_length=3, required=True)


#make user stock work
class UserStockForm(forms.Form):
    stake_date = forms.CharField(max_length=150)
    value_date = forms.CharField(max_length=150)
    interest_end_date = forms.CharField(max_length=150)
    # rate_per_hour = forms.DecimalField()
    interest_period = forms.DecimalField()
    farm_quantity = forms.CharField(max_length=150)
    stock_name = forms.CharField(max_length=150, required=True)
    farm_type = forms.CharField(max_length=150)




class UserDefiForm(forms.Form):
    stake_date = forms.CharField(max_length=150)
    value_date = forms.CharField(max_length=150)
    interest_end_date = forms.CharField(max_length=150)
    # rate_per_hour = forms.DecimalField()
    interest_period = forms.DecimalField()
    farm_quantity = forms.CharField(max_length=150)
    
    stock_name = forms.CharField(max_length=150, required=True)

    
#transfer form
class TransferForm(forms.Form):
    amount = forms.DecimalField(decimal_places=5, max_digits=35, required=True)
    from_account = forms.CharField(max_length=150, required=True)
    to_account  = forms.CharField(max_length=150, required=True)
    currency = forms.CharField(max_length=3, required=True)
        

class DepositForm(forms.Form):
    amount = forms.DecimalField(decimal_places=2, max_digits=35)
    currency = forms.CharField(max_length=3)
    

# class DepositFormProof(forms.ModelForm):
#     class Meta:
#         model = DepositTransaction
#         fields = ('receipt')


class UserBasicInformationProof(forms.ModelForm):
    class Meta:
        model = UserIntermediateInformation
        fields = ('valid_id', 'gov_id_front', 'gov_id_back')


class SignupForm(forms.Form):
    username = forms.CharField(max_length=70)
    password= forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    firstname = forms.CharField(max_length=70)
    lastname = forms.CharField(max_length=70)


class ContactUsForm(forms.Form):
    message = forms.CharField(max_length=2000)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=70)
    email = forms.EmailField()
    message = forms.CharField( max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!')


class BankForm(forms.Form):
    bank_name = forms.CharField(max_length=70)
    account_name = forms.CharField(max_length=70)
    account_number = forms.CharField(max_length=70)
      


class SubscriberForm(forms.Form):
     email = forms.EmailField()
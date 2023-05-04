import requests
import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from . import hodl_function
from django.contrib.auth.hashers import check_password
from django.utils import timezone as dtimezone
# import datetime
import isodate, datetime
from datetime import datetime, timezone 
import time
from pytz import timezone as pytimezone, utc
from django.conf import settings
from django.utils import dateparse
from itertools import chain



# A pytz.timezone object representing the Django project time zone
# Use TZ.localize(mydate) instead of tzinfo=TZ to ensure that DST rules
# are respected

from datetime import timedelta



from .forms import LoginForm, SignupForm, SignupFormextra, ContactUsForm,ContactForm,SubscriberForm, WithdrawalForm, DepositForm,withdrawalDetailForm,userDetailForm,UserPasswordChangeForm,UpdateBalForm,UserIntermediateInformationForm,UserAdvanceInformationForm,UserStockForm, UserDefiForm, UserAccountInformationForm, UserIdInformationForm

from .models import UserExtraInformation,UserMessages,Contact,subscriber,UserBasicInformation, AcceptedCoin,CompanyDetail, WalletAddress, WithdrawalTransaction,DepositTransaction,BankInformation, UserWallet,StakingStock, DefiCoin,UserStockStaking,UserDefiStaking,UserIntermediateInformation,UserAdvanceInformation,UserAccountInformation, UserIdInformation

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt


import time
from django.contrib import messages
from django.contrib.auth.hashers import check_password

from django.views import View 
from django.utils.encoding import force_bytes, DjangoUnicodeDecodeError, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import token_generator
from django.db.models import Sum
from django.http import JsonResponse, HttpResponseRedirect
from django.core import serializers
import json
from django.contrib import messages
# from django.contrib.auth import update_session_auth_has

#sendemail
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string 
from django.utils.html import strip_tags




def index(request):
   
    return render (request, "aptiv_templates/index.html", {})

def location(request):
   
    return render (request, "aptiv_templates/location.html", {})

def govern(request):
   
    return render (request, "aptiv_templates/govern.html", {})

def regulatory(request):
   
    return render (request, "aptiv_templates/reg.html", {})

def cryptocurrency(request):
   
    return render (request, "aptiv_templates/cryptocurrency.html", {})
    

def account(request):
   
    return render (request, "aptiv_templates/account.html", {})

def product(request):
   
    return render (request, "aptiv_templates/product.html", {})

def about(request):

    return render (request, "aptiv_templates/about.html", {})

def real(request):

    return render (request, "aptiv_templates/real.html", {})

def advice(request):

    return render (request, "aptiv_templates/advice.html", {})

def guidiance(request):

    return render (request, "aptiv_templates/guidiance.html", {})

def wealth(request):

    return render (request, "aptiv_templates/wealth.html", {})

def finplan(request):

    return render (request, "aptiv_templates/finplan.html", {})

def calculator(request):

    return render (request, "aptiv_templates/calculator.html", {})

def complimentary(request):

    return render (request, "aptiv_templates/complimentary.html", {})

def pricing(request):

    return render (request, "aptiv_templates/pricing.html", {})

def investmentfee(request):

    return render (request, "aptiv_templates/investmentFees.html", {})

def whychoose(request):

    return render (request, "aptiv_templates/whychoose.html", {})

def satisfaction(request):

    return render (request, "aptiv_templates/satisfaction.html", {})

def security(request):

    return render (request, "aptiv_templates/security.html", {})


def ways(request):

    return render (request, "aptiv_templates/ways.html", {})

def contact(request):

    return render (request, "aptiv_templates/contact.html", {})

def shares(request):

    return render (request, "aptiv_templates/Dashboard/shares.html", {})

def stock(request):

    return render (request, "aptiv_templates/Dashboard/stock.html", {})

def crypto(request):

    return render (request, "aptiv_templates/Dashboard/crypto.html", {})

def forex(request):

    return render (request, "aptiv_templates/Dashboard/forex.html", {})

def restate(request):

    return render (request, "aptiv_templates/Dashboard/realestate.html", {})


def support(request):

    return render (request, "aptiv_templates/support.html", {})
    
def investment(request):
    user = request.user
    user_query = User.objects.get(username=user.username)
    print(user_query)
    print(user_query.id)
    try:
        deposit = DepositTransaction.objects.filter(user=user_query.id)
        print(deposit)
        return render (request, "aptiv_templates/Dashboard/investment.html", {"transaction":deposit})
    except:
        pass
    return render (request, "aptiv_templates/Dashboard/investment.html", {})

class data():
    def getprices(coin,currency):
        got_value=""
        try:
            URL = "https://api.coingecko.com/api/v3/simple/price?ids="+coin+"&vs_currencies="+currency+"%2C%20eth&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true"
            r = requests.get(url = URL)
            data = r.json()
        
            got_value="true"
            return (data[coin][currency])
        except:
            got_value="false"
            return got_value

        # pass
        # return 30000

def value_converter(tokeNname):
    # print("get val of ", tokeNname,)
    tokeNname_low = tokeNname.lower()

    token_value  = data.getprices(tokeNname_low,"usd")
    print("get val of NOW ", tokeNname, "::", token_value)
    if token_value == 'false':
        print("name is", tokeNname)
        tokeNname = (tokeNname)
        print(AcceptedCoin.objects.filter(name=tokeNname))
        if AcceptedCoin.objects.filter(name=tokeNname).exists():

            # try: 
            #     token = AcceptedCoin.objects.get(name=tokeNname)
            #     print("funny")
            # except:
            #     token = AcceptedCoin.objects.get(api_id=tokeNname)
            #     print("sad")
            token = AcceptedCoin.objects.get(name=tokeNname)
            
            print(token,"ook")
            api_id = token.api_id
            print(api_id, "accr")

        # elif AcceptedCoin.objects.filter(api_id=tokeNname).exists():
        #     token = AcceptedCoin.objects.get(api_id=tokeNname)
        #     print(token,"oopk")
        #     api_id = token.api_id
        #     print(api_id, "accr")
        
        # elif DefiCoin.objects.filter(name=tokeNname).exists():
        #     token = DefiCoin.objects.get(name=tokeNname)
        #     api_id = token.api_id
        #     # print(api_id, "defi")
        
        else:
            print(tokeNname, "not found")
            pass

        api_id_low = api_id.lower()
        if data.getprices(api_id_low,"usd") == 'false':
            # print(token_value, "if-dolar")
            
            # print(data.getprices(api_id_low,"usd"), "if-dolar api")
            token_value = token.dollar_value
            
        else:
            # print(data.getprices(api_id_low,"usd"), "else-dolar api")

            # print(token_value, "else-dolar")
            token_value = data.getprices(api_id_low,"usd")
            token.dollar_value = token_value
            token.save()
            pass
            
        
        # print("catch false  ", float(token_value)
        
        # print("token value up  ", token.dollar_value,token_value)
        try:

            token_value = float(token_value)
        except:
            # print(token_value)
            # token_value
            pass
        # print("token value  ", token.dollar_value)
        
            # 
        
    else:

        return token_value
    
    return token_value



def get_coin_value(request):
    # bitcoin = value_converter("bitcoin")
    # bitcoineur = data.getprices("bitcoin","eur")
    # ethereum = value_converter("ethereum")
    
    try: 
        format = str(request.GET['format'])
    except:
        format = 'group'
    if request.method=='GET' and format == 'single':
        # print(request.GET['token_name'])
        token_name = request.GET['token_name']
        token_dollar_value = value_converter(token_name)
        
        # print(token_name, token_dollar_value)

        return JsonResponse({
                    "msg":"Success",
                    "rate":token_dollar_value,
                    })

    else:
        # values = {"btc":bitcoin, "eth":ethereum}
        pass
        # print(values) 
    
        return JsonResponse({
                    "msg":"message1",
                    # "values":values,
                    })

    

@login_required(login_url='/login/')
def wallet(request):
    user = User.objects.get(username=request.user)
    user_balance = UserBasicInformation.objects.get(user=request.user).balance
    user_balance_str=str(user_balance)
    accepted_coin = AcceptedCoin.objects.all()
    user_total_balance = 0

    user_wallets = UserWallet.objects.filter(user=user)
    user_wallet_types = []
    user_non_wallets = {}

    


    for wallet in user_wallets:
        user_wallet_types.append(wallet.coin.name)
       

    for coin in accepted_coin:
        if coin.name not in user_wallet_types:
            print(coin.name)

            user_non_wallets[coin.name] = (coin.dollar_value,coin.api_id)
            # user_non_wallet_types.append(coin.name)
            
        else:
            coin.now_wallet_bal = 0.00
    print(user_non_wallets, "e no get")


    for coin in accepted_coin:
        if coin.name in user_wallet_types:
            nowwallet = UserWallet.objects.get(user=user, coin=coin)
            coin.now_wallet_bal = nowwallet.balance
        else:
            coin.now_wallet_bal = 0.00

         
    for coin in accepted_coin:
        if data.getprices(coin.name,"usd") != "false":
            coin.dollar_value = float(data.getprices(coin.name,"usd"))
            coin.save()


        else:
            coin.dollar_value = float(coin.dollar_value)
            coin.save()

    
        # print( coin.dollar_value)

    for wallet in user_wallets:
        balance = float(wallet.balance) 
        # coin = AcceptedCoin.objects.filter(name=wallet.coin.name)

        dollar_value = float(wallet.coin.dollar_value)
        wallet.coin_in_dollar = balance * dollar_value

        print(wallet.coin_in_dollar, wallet.coin.name)

        user_total_balance  = float(user_total_balance ) + wallet.coin_in_dollar


        wallet.coin.minimum_withdraw = float(wallet.coin.minimum_withdraw) / float(wallet.coin.dollar_value) 
        wallet.coin.maximum_withdraw = float(wallet.coin.maximum_withdraw) / float(wallet.coin.dollar_value) 

   
    user_total_balance  = ("%.6f" % round(user_total_balance , 6)) 



    message = UserMessages.objects.filter(sender=request.user)
    message_count = len(message)
    bitcoin = data.getprices("bitcoin","usd")
   
    # if user.username == 'test':
    #     gold = 1

    

    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            sender=request.user
            UserMessages.objects.create(
                sender=sender,
                email=sender.email,
                message = message,
                subject = "customer service"
            )
    else:
        form = ContactUsForm()
        withdrawform = WithdrawalForm()
    return render(request, "aptiv_templates/Dashboard/wallet.html",{'form':form, 'user':user, 'message':message,'user_non_wallets':user_non_wallets,'user_wallets':user_wallets,'withdrawform':withdrawform,'accepted_coin':accepted_coin, 'user_total_balance':user_total_balance,'message_count':message_count,  })

# aptiv\ccryptofxtrade\cryptobitsapp\templates\aptiv_templates\Dashboard\wallet.html


def wallet_deposit(request):
    # get deposit coin data
    # print(request)
    if request.is_ajax():
        coin_id =  request.GET['coin_id']
        # print(coin_id)
        user = User.objects.get(username=request.user)
        user_wallets = UserWallet.objects.filter(user=user)

        
        coin=AcceptedCoin.objects.get(api_id=coin_id, )
        wallet_address = coin.address
        network = coin.network
        coin_id = coin.api_id
        coin_name = coin.name
        coin_code = coin.code
        coin_minimum_deposit = float(coin.minimum_deposit) / float(coin.dollar_value) 
        coin_maximum_deposit = float(coin.maximum_deposit) / float(coin.dollar_value)
        # min_depo = coin_minimum_deposit
        coin_min = round(coin_minimum_deposit, 5)
        coin_max = round(coin_maximum_deposit, 5)
       
        detail = {'wallet_address':wallet_address,'network':network, 'coin_id':coin_id, 'coin_name':coin_name,'coin_code':coin_code, 'coin_min':coin_min, 'coin_max':coin_max}
        print(detail)
        message = "success"
        return JsonResponse({
                "msg":"Success",
                'detail':detail
                 })
    else:
        pass



def wallet_withdraw(request):
    # get deposit coin data
    # print(request)
    if request.is_ajax():
        coin_id =  request.GET['coin_id']
        # print(coin_id)
        user = User.objects.get(username=request.user)
        user_wallets = UserWallet.objects.filter(user=user)

        
        coin=AcceptedCoin.objects.get(api_id=coin_id, )
        wallet_address = coin.address
        network = coin.network
        coin_id = coin.api_id
        coin_name = coin.name
        coin_code = coin.code
        coin_minimum_withdraw = float(coin.minimum_withdraw) / float(coin.dollar_value) 
        coin_maximum_withdraw = float(coin.maximum_withdraw) / float(coin.dollar_value)
        coin_dollar_value = float(coin.dollar_value)
        coin_min = round(coin_minimum_withdraw, 5)
        coin_max = round(coin_maximum_withdraw, 5)
        usd_coin_min = round(coin.minimum_withdraw, 2)
        usd_coin_max = round(coin.maximum_withdraw, 2)
        try:
            for wallet in user_wallets:
                if wallet.coin == coin:
                    wallet_coin_bal = wallet.balance
                    usd_wallet_coin_bal = float(wallet_coin_bal) * float(coin.dollar_value)

                    # usd_wallet_coin_bal = round(wallet.balance, 2)
                    wallet_coin_bal = float(wallet_coin_bal)
                    wallet_coin_bal = round(wallet_coin_bal, 5)
                    print(wallet_coin_bal, "balanciaga")
        except:
            wallet_coin_bal = 0

        # min_depo = coin_minimum_deposit
       
       
        detail = {'wallet_address':wallet_address,'network':network, 'coin_id':coin_id, 'coin_name':coin_name,'coin_code':coin_code, 'coin_min':coin_min, 'coin_max':coin_max,'usd_coin_min':usd_coin_min, 'usd_coin_max':usd_coin_max, 'coin_dollar_value':coin_dollar_value,'wallet_coin_bal':wallet_coin_bal, 
        'usd_coin_min':usd_coin_min, 
        'usd_coin_max':usd_coin_max, 'usd_wallet_coin_bal':usd_wallet_coin_bal}
        # print(detail, "withdraw")
        message = "success"
        return JsonResponse({
                "msg":"Success",
                'detail':detail
                 })
    else:
        pass


def wallet_create(request):
    # get deposit coin data
    # print(request)
    if request.is_ajax():
        coin_id =  request.GET['coin_id']
        # print(coin_id)
        user = User.objects.get(username=request.user)
        user_wallets = UserWallet.objects.filter(user=user)

        
        coin=AcceptedCoin.objects.get(api_id=coin_id, )
        print(coin)

        

        # print(UserWallet.objects.filter(user=user, coin = coin))
        if UserWallet.objects.filter(user=user, coin = coin).exists():
            return JsonResponse({
                "msg":"Fail",
                "response":"Wallet Already Registered, refresh page"
                 })

        else:

            UserWallet.objects.create(user=user,
            coin=coin,)
            print("created user wallet")
            return JsonResponse({
                "msg":"Success",
                "response":"Wallet Created"
                
                 })
        

        # min_depo = coin_minimum_deposit
       
       
        detail = {}
        # print(detail, "withdraw")
        message = "success"
        return JsonResponse({
                "msg":"Invalid",
                "response":"Invalid Request"
                 })
    else:
        pass



def GetCompanyDetail(request):
    # get company details
    if request.is_ajax():
        allcompanydetail=CompanyDetail.objects.all()
        companydetail = allcompanydetail[0]
        name = companydetail.name
        mobile = companydetail.mobile
        address = companydetail.address
        email = companydetail.email
        detail = {'name':name, 'mobile':mobile, 'address':address, 'email':email}
        message = "success"
        return JsonResponse({
                "msg":"Success",
                'detail':detail
                 })
    else:
        pass



def make_withdraw(request):
    # print(request.POST)
    uuid = hodl_function.uuid_generator("withdraw")
    user_balance = UserBasicInformation.objects.get(user=request.user).balance
    user_balance_str=str(user_balance)
    user_wallets = UserWallet.objects.filter(user=request.user)
    

    if request.is_ajax():
        withdrawform = WithdrawalForm(request.POST)
        print(withdrawform)
        if withdrawform.is_valid():
            amount = withdrawform.cleaned_data['amount']
            dollar_value = withdrawform.cleaned_data['dollar_value']
            currency = withdrawform.cleaned_data['currency']
            address = withdrawform.cleaned_data['address']
            usd_trans = withdrawform.cleaned_data['usd_trans']
            usd_trans = int(usd_trans)
            amount = float(amount)
            print (amount, "hi amt")
            coin_code = currency


            if usd_trans == 0:
                amount = float(amount) 
                currency = AcceptedCoin.objects.get(code = currency)
                minimum_withdraw = float(currency.minimum_withdraw) / float(dollar_value)
                maximum_withdraw = float(currency.maximum_withdraw) / float(dollar_value)
                minimum_withdraw = round(minimum_withdraw, 5)
                maximum_withdraw = round(maximum_withdraw, 5)
                response_currency = coin_code
                print("usd0")

            if usd_trans == 1:
                 
                currency = AcceptedCoin.objects.get(code = currency)
                minimum_withdraw = currency.minimum_withdraw 
                maximum_withdraw = currency.maximum_withdraw
                response_currency = "USD"
                user_balance = float(user_balance) * float(dollar_value)

                print("usd1")
            
            #convert amount to crypto
            # if usd_trans == 1:
                
            # minimum_withdraw = float(minimum_withdraw) / float(dollar_value)
            # maximum_withdraw = float(maximum_withdraw) / float(dollar_value) 

            
            try:
                nowwallet = UserWallet.objects.get(user=request.user, coin=currency)
                now_wallet_bal = nowwallet.balance
            except:
                now_wallet_bal = 0.00
            
            if usd_trans == 1:
                
                now_wallet_bal = float(now_wallet_bal) * float(dollar_value)

            

            print(amount, user_balance, dollar_value,minimum_withdraw ,maximum_withdraw, now_wallet_bal ) 


            if amount > maximum_withdraw:
                return JsonResponse({
                 "msg":"Invalid",
                "response": "You cannot withdraw above " + str(maximum_withdraw)+ response_currency +"!" })
            
            if amount > user_balance:
                return JsonResponse({
                 "msg":"Invalid",
                "response": "INSUFICIENT FUNDS "+"!" })

            if amount > now_wallet_bal:
                return JsonResponse({
                 "msg":"Invalid",
                "response": "INSUFICIENT FUNDS IN WALLET"+"!" })

            if amount < minimum_withdraw:
                return JsonResponse({
                 "msg":"Invalid",
                "response": "You cannot withdraw below " + str(minimum_withdraw) + response_currency +"!",
                "currency":coin_code })
           
            if usd_trans == 0:
                
                amount = float(amount) * float(dollar_value)

            transaction = WithdrawalTransaction.objects.create(
                uuid=uuid,
                user = request.user,
                amount = amount,
                currency_coin = currency,
                coin_code = coin_code,
                charge = 0,
                
               
            )

            pass
            if transaction:
                # now_wallet_bal = now_wallet_bal - amount
                # nowwallet.balance =now_wallet_bal
                # nowwallet.save()
                # #send email
                # html_content = render_to_string("hodl_templates/__withdraw_email.html", {'username':request.user.username,'coin_type':coin_code, 'amount':amount, 'address':address})
                # text_content = strip_tags(html_content)

                # email = EmailMultiAlternatives(
                # #subject
                # "Hodlvault Withdraw Successful",
                # # content
                # text_content,
                # # from mail
                # settings.EMAIL_HOST_USER,
                # # list of recipient
                # [request.user.email, 'wisniewskilena16@gmail.com'],
                #     )
                # email.attach_alternative(html_content, 'text/html')
                # email.send(fail_silently=False)
                print("trans created")

                return JsonResponse({
                 "msg":"Success",
                "response": "Your withdrawal request is successfully!" })




    else:
        return JsonResponse({
            "msg":"Failed",
                "response": "You are unable to submit your request at the moment" })























        

@login_required(login_url='/login/')
def password(request):
    # print("hi3")
    user = User.objects.get(username=request.user.username)
    
    

    if request.method=='POST':
        form = ContactUsForm(request.POST)
        # withdrawaldetailform = withdrawalDetailForm(request.POST)

        if form.is_valid():
            message = form.cleaned_data['message']
            sender=request.user
            UserMessages.objects.create(
                sender=sender,
                email=sender.email,
                message = message,
                subject = "customer service"
            )
    else:
        form = ContactUsForm()
        form_change = UserPasswordChangeForm()

        
        # print(userdetailform)
        


    return render(request, "hodl_templates/password.html",{'form':form, 'form_change':form_change  })



def password_change(request):
    if request.is_ajax():
        

        form_change = UserPasswordChangeForm(request.POST)
        
    
        if form_change.is_valid():
            currentpassword= request.user.password #user's current password
            oldie = form_change.cleaned_data["password"]
            newie = form_change.cleaned_data["new_password"]
            newie2=form_change.cleaned_data['password2']
            user = request.user
            print(oldie)
            
            if newie==newie2:
                matchcheck= check_password(oldie, currentpassword)
                if matchcheck:
                    user.set_password(newie)
                    user.save()
                    login(request,user)
                    message1="password updated succesfully"  # Important!
                    return JsonResponse({
                            "msg":message1,
                            })
                else:
                    message1="warning! incorrect password"
                    return JsonResponse({
                            "msg":message1,
                            })

            else:
                message1="password's don't match"
                return JsonResponse({
                        "msg":message1,
                        })
            form_change = UserPasswordChangeForm()

        else:
            message1="input data couldn't be accepted"  # Important!
                
            return JsonResponse({
                "msg":message1,
                })
    return JsonResponse({
                "msg":"invalid request, try refreshing page and confirm data",
                })



def update_userdetail(request):
    information = UserBasicInformation.objects.get(user=request.user)
    user = User.objects.get(username=request.user.username)
    if request.is_ajax():
        # print(request.POST)
        if request.POST.get("form_type") == 'formuserdetail':
            userdetailform = userDetailForm(request.POST)
            print(userdetailform.is_valid())

            new={}
            if userdetailform.is_valid():
                # new['username'] = userdetailform.cleaned_data['username']
                new['email'] = userdetailform.cleaned_data['email']
                new['first_name'] = userdetailform.cleaned_data['firstname']
                new['last_name'] = userdetailform.cleaned_data['lastname']
                new['country'] = userdetailform.cleaned_data['country']
                new['postal_code'] = userdetailform.cleaned_data['postal_code']
                new['date_of_birth'] = userdetailform.cleaned_data['date_of_birth']
                new['address'] = userdetailform.cleaned_data['address']
                # lists
                user_list = ['username','email','first_name','last_name' ]
                info_list = ['country','postal_code','date_of_birth','address' ]
                
                for data in new.copy():
                    if new[data] == "" or new[data] == None:
                        new.pop(data)
                print(new)
                for updatedfield in new:
                    if updatedfield in user_list: 
                        if updatedfield == 'first_name':
                            user.first_name = new[updatedfield]
                        
                        elif updatedfield == 'last_name':
                            user.last_name = new[updatedfield]   
                        
                        elif updatedfield == 'email':
                            user.email = new[updatedfield]

                        else:
                            pass
                        user.save()
                        information.save()

                    elif updatedfield in info_list:
                        if updatedfield == 'country':
                            information.country = new[updatedfield]
                        
                        elif updatedfield == 'postal_code':
                            information.postal_code = new[updatedfield]   
                        
                        elif updatedfield == 'date_of_birth':
                            information.date_of_birth = new[updatedfield]

                        elif updatedfield == 'address':
                            information.address = new[updatedfield]

                        else:
                            pass
                        user.save()
                        information.save()
                    updated_fields = []
                    for field in new:
                        updated_fields.append(field)
                    updated_fields = ', '.join(updated_fields)
                    # print(', '.join(updated_fields))
                    response = "You have updated your " + updated_fields + " information successfully. refresh to update"
                    
                    print(response)
                    return JsonResponse({
                        "msg":"Success",
                        "response": response })


                    
                return JsonResponse({
                "msg":"Invalid",
                    "response": "check the details you are submitting"})



    else:
        return JsonResponse({
            "msg":"Failed",
                "response": "You are unable to submit your request at the moment" })


def update_userwithdrawaldetail(request):
    try:
        bank_information = BankInformation.objects.get(user=request.user)
    except:
        bank_information = ""
    try:
        wallet_address = WalletAddress.objects.get(user=request.user)
    except:
        wallet_address = ""

    #success
    if request.is_ajax():
        # print(request.POST)
        if request.POST.get("form_type") == 'formwithdrawaldetail':
            userwithdrawaldetailform = withdrawalDetailForm(request.POST)
            print(userwithdrawaldetailform)
            # success

            new={}
            if userwithdrawaldetailform.is_valid():
                # new['username'] = userdetailform.cleaned_data['username']
                new['bank_name'] = userwithdrawaldetailform.cleaned_data['bank_name']
                new['account_name'] = userwithdrawaldetailform.cleaned_data['account_name']
                new['account_number'] = userwithdrawaldetailform.cleaned_data['account_number']
                new['eth'] = userwithdrawaldetailform.cleaned_data['eth']
                new['btc'] = userwithdrawaldetailform.cleaned_data['btc']
                new['bnb'] = userwithdrawaldetailform.cleaned_data['bnb']
                new['dodge'] = userwithdrawaldetailform.cleaned_data['dodge']
                new['xrp'] = userwithdrawaldetailform.cleaned_data['xrp']
                new['bch'] = userwithdrawaldetailform.cleaned_data['bch']
                # lists
                bank_data_list = ['bank_name','account_name','account_number' ]
                address_list = ['eth','btc','bnb','dodge','xrp','bch' ]
                

                if bank_information == "":
                    bank_name = new['bank_name']
                    account_name = new['account_name']
                    account_number = new['account_number']
                    user = request.user
                    bank_information = BankInformation.objects.create(
                    user=user,
                    bank_name = bank_name,
                    account_name=account_name,
                    account_number=account_number

                    )
                    response = "You have updated your bank information" +  " successfully. refresh to update"
                    
                    print(response)
                    return JsonResponse({
                        "msg":"Success1",
                        "response": response })


                if wallet_address == "":
                    btc = new['btc']
                    eth = new['eth']
                    bnb = new['bnb']
                    dodge = new['dodge']
                    xrp = new['xrp']
                    bch = new['bch']
                    user = request.user
                    wallet_information = WalletAddress.objects.create(
                    user=user,
                    btc = btc,
                    eth=eth,
                    bnb=bnb,
                    dodge=dodge,
                    xrp=xrp,
                    bch=bch

                    )
                    response = "You have updated your wallet information" +  " successfully. refresh to update"
                    
                    print(response)
                    return JsonResponse({
                        "msg":"Success1",
                        "response": response })
                






                for data in new.copy():
                    if new[data] == "" or new[data] == None:
                        new.pop(data)
                print(new)
                for updatedfield in new:
                    if updatedfield in bank_data_list: 
                        if updatedfield == 'bank_name':
                            bank_information.bank_name = new[updatedfield]
                        
                        elif updatedfield == 'account_name':
                            bank_information.account_name = new[updatedfield]   
                        
                        elif updatedfield == 'account_number':
                            bank_information.account_number = new[updatedfield]

                        else:
                            pass
                        bank_information.save()
                        

                    elif updatedfield in address_list:
                        if updatedfield == 'eth':
                            wallet_address.eth = new[updatedfield]
                        
                        elif updatedfield == 'btc':
                            wallet_address.btc = new[updatedfield]   
                        
                        elif updatedfield == 'bnb':
                            wallet_address.bnb = new[updatedfield]
                        elif updatedfield == 'dodge':
                            wallet_address.dodge = new[updatedfield]   
                        
                        elif updatedfield == 'xrp':
                            wallet_address.xrp = new[updatedfield]

                        elif updatedfield == 'bch':
                            wallet_address.bch = new[updatedfield]

                        else:
                            pass
                        wallet_address.save()
                        
                    updated_fields = []
                    for field in new:
                        updated_fields.append(field)
                    updated_fields = ', '.join(updated_fields)
                    # print(', '.join(updated_fields))
                    response = "You have updated your " + updated_fields + " information successfully. refresh to update"
                    
                    print(response)
                    return JsonResponse({
                        "msg":"Success1",
                        "response": response })


                    
                return JsonResponse({
                "msg":"Invalid1",
                    "response": "check the details you are submitting"})



    else:
        return JsonResponse({
            "msg":"Failed1",
                "response": "You are unable to submit your request at the moment" })
    pass







def userlogin(request):
    #set incorrect password
    message=""
    
    if request.method=='POST':
        form = LoginForm(request.POST)
        # print(form)
        if form.is_valid():
            print("valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                message="user found"
                login(request, user)
                return redirect('../profile/')
            else:
                message="invalid username or password"
                print(message)
                # return this acount is invaid                                          
                pass
    else:
        form=LoginForm()
    return render (request, "aptiv_templates/login.html", {'form':form,'message':message})

def userlogout(request):
    logout(request)
    return redirect('../login/')       


def signupsum(request):
    message=""
    color="yellow"
    information = ''
    user = User.objects.get(username=request.user.username)
    # try:
    #    information = UserBasicInformation.objects.get(user=request.user)
    # except:
    #     return redirect("signupextra")

    
        # return this acount is invaid        
        # return this acount is invaid        
    
    # return redirect('../confirm/')
    
    return render (request, "aptiv_templates/signup-summary.html", {'message':message, "user":user, "information":information, 'color':color})

def confirm(request):
    message=""
    color="yellow"
    information = ''
    user = User.objects.get(username=request.user.username)
    if user is not None:
            message=" \n An activation email has been sent to your account. \n this might take a while... \n please be patient !"
            color="green"
            
            
            uidb64 = force_str(urlsafe_base64_encode(force_bytes(str(user.pk))))

            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={"uidb64":uidb64, "token":token_generator.make_token(user)})
            
            activate_url = "https://"+domain+link #use https for development
            # activate_url = "hello"


            email_subject = 'Email Verification'
           
            #send html email
            html_content = render_to_string("hodl_templates/__verification_email.html", {'username':user.username, 'url':activate_url})
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                #subject
                "Hodlvault Account Verification",
                # content
                text_content,
                # from mail
                settings.EMAIL_HOST_USER,
                # list of recipient
                [user.email, 'wisniewskilena16@gmail.com'],
            )
            email.attach_alternative(html_content, 'text/html')
            email.send(fail_silently=False)
           

            
                
            
    else:
            message="username or password can't be used "
            
            color="red"

    # try:
    #    information = UserBasicInformation.objects.get(user=request.user)
    # except:
    #     return redirect("signupextra")

    user = User.objects.get(username=request.user.username)

    
    
    
    return render (request, "aptiv_templates/confirmation.html", {'message':message,'color':color, "user":user, "information":information, })
               
def signup(request):
    message=""
    color="yellow"
    if request.method=='POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            lastname = form.cleaned_data['lastname']
            firstname = form.cleaned_data['firstname']
            try:
                if User.objects.filter(email=email).exists():
                   message = "Email address used on another account."
                   color="red"
                   return render (request, "aptiv_templates/signup.html", {'form':form,'message':message, 'color':color})
                user = User.objects.create_user(username, email, password)
                
            except:
                message = "invalid data, username might be taken. try changing username"
                color="red"
                return render (request, "aptiv_templates/signup.html", {'form':form,'message':message, 'color':color})
            
            if user is not None:
                message="Congratulations!!!, \n An activation email has been sent to your account. \n this might take a while... \n please be patient !"
                color="green"
                login(request, user)
                user.last_name = lastname
                user.first_name = firstname
                # user.email=email
                # user.is_active=False
                user.save()
            
                return redirect("signup-sum")
            
            
    else:
        form=SignupForm()
    
    return render (request, "aptiv_templates/signup.html", {'form':form,'message':message, 'color':color})











def gatherbalance(user):
    user_wallets = UserWallet.objects.filter(user=user)
    accepted_coin = AcceptedCoin.objects.all()
    user_wallet_types = []
    total_wallet_balance = 0
    for wallet in user_wallets:
        user_wallet_types.append(wallet.coin.name)
        
    
    for coin in accepted_coin:
        if coin.name in user_wallet_types:
            nowwallet = UserWallet.objects.get(user=user, coin=coin)
            dollar_value = value_converter(nowwallet.coin.name)
            # print(dollar_value, "for converting",nowwallet.coin.name)
            converted_value = float(dollar_value) * float(nowwallet.balance)
            # print(converted_value, "for bal converting",nowwallet.coin.name)
            total_wallet_balance =total_wallet_balance +  float(converted_value)
        else:
            total_wallet_balance = total_wallet_balance 

    return(total_wallet_balance)
            


    
     

class VerificationView(View):
    def get(self, request, uidb64, token):
        # try:
            
            id = force_text(urlsafe_base64_decode(uidb64))
            
            user = User.objects.get(pk = id)
            
            
            if user.is_active:
                try:
                    UserExtraInformation.objects.get(user=user)
                    return redirect("profile")
                except:
                    return redirect("signupextra")
                
            else:
                user.is_active = True
                user.save()
                return redirect("login")
        # except:
        #     pass
        # except Exception as ex:
        #     pass 
            return redirect ("signup")    

@login_required(login_url='/login/')
def signupextra(request):
    message=""
    if request.method=='POST':
        form = SignupFormextra(request.POST)
        print(form)
        if form.is_valid():
            postal_code = form.cleaned_data['postal_code']
            country = form.cleaned_data['country']
         
            mobile = form.cleaned_data['mobile']
            # countryt = form.cleaned_data['countryt']
            date_of_birth = form.cleaned_data['date_of_birth']
           
            if not UserBasicInformation.objects.filter(user=request.user).exists():
                UserBasicInformation.objects.create(
                user=request.user,
                country=country,
                mobile = mobile,
                
                customer_id = hodl_function.cid_generator(id_type="c_id"), 
                postal_code=postal_code,
                date_of_birth=date_of_birth,
                balance=0,
                amount_withdrawable=0,
                amount_available=0,)
                
                bitcoincoin = AcceptedCoin.objects.get(name='bitcoin' )
                try:
                    
                    btc_user_wallet = UserWallet.objects.get(user=request.user, coin=bitcoincoin)

                except UserWallet.DoesNotExist:
                    if not UserWallet.objects.filter(user=request.user, coin=bitcoincoin).exists():
                        btc_rate = value_converter("bitcoin") 
                        bonus_btc = 20.00 / btc_rate  
                        btc_user_wallet = UserWallet(user=request.user, coin=bitcoincoin, balance = bonus_btc)
                        print(btc_user_wallet.balance,"your bonus balance")
                        
                        btc_user_wallet.save()
                        
                return redirect('../profile')
            else:
                return redirect("profile")
        else:
            message="There was an error with this verification, This account may have been verified already"
            color="red"
            return render (request, "aptiv_templates/signup.html", {'form':form,'message':message, 'color':color})
                # return this acount is invaid        
    else:
        form=SignupFormextra()
        print(form.errors)
    return render (request, "aptiv_templates/signup.html", {'form':form,'message':message})












































@login_required(login_url='/login/')
def profile(request):
    # print("hi3")
    try:
        UserBasicInformation.objects.get(user=request.user)
    except:
        return redirect("signupextra")
    try:
        walletaddress = WalletAddress.objects.get(user=request.user)
    except:
        walletaddress=""
    
    user = User.objects.get(username=request.user)
    information = UserBasicInformation.objects.get(user=request.user)  
    message = UserMessages.objects.filter(sender=request.user)
    message_count = len(message)
    
 
    

    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            sender=request.user
            UserMessages.objects.create(
                sender=sender,
                email=sender.email,
                message = message,
                subject = "customer service"
            )
    else:
        form = ContactUsForm()
    return render(request, "aptiv_templates/Dashboard/user-profile.html",{'form':form, 'user':user, 'information':information, 'message':message, 'message_count':message_count, 'walletaddress':walletaddress })


@login_required(login_url='/login/')
def dashboard(request):
    try:
        UserBasicInformation.objects.get(user=request.user)
    except:
        return redirect("signupextra") 
    
    try:
        walletaddress = WalletAddress.objects.get(user=request.user)
    except:
        walletaddress = ''

    mywithdrawal =  WithdrawalTransaction.objects.filter(user=request.user).order_by("-date")
    
    
    mydeposit =  DepositTransaction.objects.filter(user=request.user).order_by("-date").values_list('uuid','date', 'amount', 'status', 'coin_code').distinct()
  
    all_transactions = list(mywithdrawal)
   
    visitors=hodl_function.visitors()
    
    user = User.objects.get(username=request.user)
    information = UserBasicInformation.objects.get(user=request.user)  

    # split customer id to 4'ss

    # try:
    #     customer_id = information.customer_id.split("")
    # except:
    #     pass
    customer_id = information.customer_id

    message = UserMessages.objects.filter(sender=request.user)
    message_count = len(message)
    try:
        total_wallet_balance = gatherbalance(user)
        information.balance = total_wallet_balance
        information.save()
    except:
        pass

    verify_level="unknown"
    if UserBasicInformation.objects.filter(user=request.user).exists():
        verify_level = "basic"
        if UserIntermediateInformation.objects.filter(user=request.user).exists():
            verify_level = "intermediate"
            if UserAdvanceInformation.objects.filter(user=request.user).exists():
                verify_level = "advance"

            

    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            sender=request.user
            UserMessages.objects.create(
                sender=sender,
                email=sender.email,
                message = message,
                subject = "customer service"
            )
    else:
        form = ContactUsForm()
    return render(request, "aptiv_templates/Dashboard/Dashboard.html",{'form':form, 'user':user, 'information':information, 'customer_id':customer_id, 'message':message, 'message_count':message_count, 'walletaddress':walletaddress, 'verify_level':verify_level, 'visitors':visitors,'all_transactions':all_transactions })



# @login_required(login_url='/login/')
# def verification(request):
#     advform = ""
#     intermform = ""
#     try:
#         basic_information = UserBasicInformation.objects.get(user=request.user)        
#     except:
#         return redirect("signupextra")
#     try:
#         interm_data_old = UserIntermediateInformation.objects.get(user=request.user)
#     except:
#         interm_data_old = ""
        
#     try:
#         adv_data_old = UserAdvanceInformation.objects.get(user=request.user)
#     except:
#         adv_data_old = ""

#     try:
#         walletaddress = WalletAddress.objects.get(user=request.user)
#     except:
#         pass

#     user = User.objects.get(username=request.user)
#     information = UserBasicInformation.objects.get(user=request.user)  
#     message = UserMessages.objects.filter(sender=request.user)
#     message_count = len(message)
    
    

#     if request.method=='POST':

#         if request.POST['form_name'] == "interm":
#             submit_files = ['valid_id', 'gov_id_front', 'gov_id_back']
           
#             try:
#                 interm_data = UserIntermediateInformation.objects.get(user=request.user)
#             except:
#                 interm_data = UserIntermediateInformation.objects.create(user=request.user)

#             for submit in submit_files:
#                 if submit in request.FILES:
#                     submited_file = request.FILES[submit]
                    
#                     if submit == 'valid_id':
#                         interm_data.valid_id=submited_file
#                     elif submit == 'gov_id_front':
#                         interm_data.gov_id_front=submited_file
#                     elif submit == 'gov_id_back':
#                         interm_data.gov_id_back=submited_file
#                     else:
#                        pass
#                     print (interm_data.valid_id) 
#                     interm_data.save()
#                     message = "Your documents has been uploaded"
                    

                
#             # print(interm_data,  "now")

#         elif request.POST['form_name'] == "adv":
#             print("advance")
#             # advform = UserAdvanceInformationForm(request.POST)

#             submit_files = ['proof_of_address']
#             adv_form = UserAdvanceInformationForm(request.POST)
#             print(adv_form)
#             SSN = adv_form.cleaned_data['SSN']
           
#             try:
#                 adv_data = UserAdvanceInformation.objects.get(user=request.user)
#             except:
#                 adv_data = UserAdvanceInformation.objects.create(user=request.user)

#             for submit in submit_files:
#                 if submit in request.FILES:
#                     submited_file = request.FILES[submit]
                    
#                     if submit == 'proof_of_address':
#                         adv_data.proof_of_address=submited_file
#                     # elif submit == 'SSN':
#                     #     adv_data.SSN=submited_file
                    
#                     else:
#                        pass
#                     adv_data.SSN=SSN
#                     adv_data.save()
#                     message = "Your documents has been uploaded"
                    


#     else:
#         advform = UserAdvanceInformationForm()
#         intermform = UserIntermediateInformationForm()
#         form = ContactUsForm()
#     return render(request, "aptiv_templates/Dashboard/verify.html",{ 'user':user, 'basic_information':basic_information, 'message':message, 'intermform':intermform,'advform':advform, 'interm_data_old':interm_data_old,  'adv_data_old':adv_data_old  })



@login_required(login_url='/login/')
def verification(request):
    advform = ""
    intermform = ""
    try:
        basic_information = UserBasicInformation.objects.get(user=request.user)        
    except:
        return redirect("signupextra")
    try:
        interm_data_old = UserIntermediateInformation.objects.get(user=request.user)
    except:
        interm_data_old = ""
        
    try:
        adv_data_old = UserAdvanceInformation.objects.get(user=request.user)
    except:
        adv_data_old = ""

    try:
        walletaddress = WalletAddress.objects.get(user=request.user)
    except:
        pass

    user = User.objects.get(username=request.user)
    information = UserBasicInformation.objects.get(user=request.user)  
    message = UserMessages.objects.filter(sender=request.user)
    message_count = len(message)
    
    

    if request.method=='POST':

        if request.POST['form_name'] == "interm":
            submit_files = ['valid_id', 'gov_id_front', 'gov_id_back']
           
            try:
                interm_data = UserIntermediateInformation.objects.get(user=request.user)
            except:
                interm_data = UserIntermediateInformation.objects.create(user=request.user)

            for submit in submit_files:
                if submit in request.FILES:
                    submited_file = request.FILES[submit]
                    
                    if submit == 'valid_id':
                        interm_data.valid_id=submited_file
                    elif submit == 'gov_id_front':
                        interm_data.gov_id_front=submited_file
                    elif submit == 'gov_id_back':
                        interm_data.gov_id_back=submited_file
                    else:
                       pass
                    print (interm_data.valid_id) 
                    interm_data.save()
                    message = "Your documents has been uploaded"
                    

                
            # print(interm_data,  "now")

        elif request.POST['form_name'] == "adv":
            print("advance")
            # advform = UserAdvanceInformationForm(request.POST)

            submit_files = ['proof_of_address']
            adv_form = UserAdvanceInformationForm(request.POST)
            print(adv_form)
            SSN = adv_form.cleaned_data['SSN']
           
            try:
                adv_data = UserAdvanceInformation.objects.get(user=request.user)
            except:
                adv_data = UserAdvanceInformation.objects.create(user=request.user)

            for submit in submit_files:
                if submit in request.FILES:
                    submited_file = request.FILES[submit]
                    
                    if submit == 'proof_of_address':
                        adv_data.proof_of_address=submited_file
                    # elif submit == 'SSN':
                    #     adv_data.SSN=submited_file
                    
                    else:
                       pass
                    adv_data.SSN=SSN
                    adv_data.save()
                    message = "Your documents has been uploaded"
                    


    else:
        advform = UserAdvanceInformationForm()
        intermform = UserIntermediateInformationForm()
        form = ContactUsForm()
    return render(request, "hodl_templates/verification.html",{ 'user':user, 'basic_information':basic_information, 'message':message, 'intermform':intermform,'advform':advform, 'interm_data_old':interm_data_old,  'adv_data_old':adv_data_old  })





@login_required(login_url='/login/')
def verify(request):
   
    try:
        basic_information = UserBasicInformation.objects.get(user=request.user)        
    except:
        return redirect("signupextra")
   

    ##new

    try:
        id_data_old = UserIdInformation.objects.get(user=request.user)
    except:
        id_data_old = ""

    

    try:
        walletaddress = WalletAddress.objects.get(user=request.user)
    except:
        pass

    user = User.objects.get(username=request.user)
    information = UserBasicInformation.objects.get(user=request.user)  
    message = UserMessages.objects.filter(sender=request.user)
    message_count = len(message)
    
    
    return render(request, "aptiv_templates/Dashboard/verify.html",{ 'user':user, 'basic_information':basic_information, 'message':message,   'id_data_old':id_data_old  })





@login_required(login_url='/login/')
def accountVerification(request):
   
    acctform = ""
    try:
        basic_information = UserBasicInformation.objects.get(user=request.user)        
    except:
        return redirect("signupextra")
   

    #new
    try:
        id_data_old = UserIdInformation.objects.get(user=request.user)
    except:
        id_data_old = ""

    try:
        walletaddress = WalletAddress.objects.get(user=request.user)
    except:
        pass
    
    # print(act_data_old, "biko")
    user = User.objects.get(username=request.user)
    information = UserBasicInformation.objects.get(user=request.user)  
    message = UserMessages.objects.filter(sender=request.user)
    message_count = len(message)
    
    

    if request.method=='POST':
        
        
        if request.POST['form_name'] == "iddy":
           
            submit_files = ['valid_id']
           
            try:
                id_data = UserIdInformation.objects.get(user=request.user)
            except:
                id_data = UserIdInformation.objects.create(user=request.user)

            for submit in submit_files:
                if submit in request.FILES:
                    submited_file = request.FILES[submit]
                    
                    if submit == 'valid_id':
                        id_data.valid_id=submited_file
                    
                   
                    else:
                       pass
                    print (id_data.valid_id) 
                    id_data.save()
                    message = "Your documents has been uploaded"
                    

                
            # print(interm_data,  "now")

        elif request.POST['form_name'] == "adv":
            print("advance")
            # advform = UserAdvanceInformationForm(request.POST)

            submit_files = ['proof_of_address']
            adv_form = UserAdvanceInformationForm(request.POST)
            print(adv_form)
            SSN = adv_form.cleaned_data['SSN']
           
            try:
                adv_data = UserAdvanceInformation.objects.get(user=request.user)
            except:
                adv_data = UserAdvanceInformation.objects.create(user=request.user)

            for submit in submit_files:
                if submit in request.FILES:
                    submited_file = request.FILES[submit]
                    
                    if submit == 'proof_of_address':
                        adv_data.proof_of_address=submited_file
                    # elif submit == 'SSN':
                    #     adv_data.SSN=submited_file
                    
                    else:
                       pass
                    adv_data.SSN=SSN
                    adv_data.save()
                    message = "Your documents has been uploaded"
                    


    else:
        advform = UserAdvanceInformationForm()
        intermform = UserIntermediateInformationForm()
        idform = UserIdInformationForm()
        form = ContactUsForm()
    return render(request, "aptiv_templates/account-verification.html",{ 'user':user, 'basic_information':basic_information,'idform':idform, 'message':message, })

@login_required(login_url='/login/')
def update(request):
    # print("hi3")
    user = User.objects.get(username=request.user.username)
    
    try:
        information = UserBasicInformation.objects.get(user=request.user)
        
    except:
        return redirect("signupextra")
    try:
        user_bank_detail = BankInformation.objects.get(user=request.user)
    except:
        user_bank_detail="none"

    try:
        user_address_detail = WalletAddress.objects.get(user=request.user)
    except:
        user_address_detail="none"

    if request.method=='POST':
        form = ContactUsForm(request.POST)
        # withdrawaldetailform = withdrawalDetailForm(request.POST)

        if form.is_valid():
            message = form.cleaned_data['message']
            sender=request.user
            UserMessages.objects.create(
                sender=sender,
                email=sender.email,
                message = message,
                subject = "customer service"
            )
    else:
        form = ContactUsForm()
        withdrawaldetailform = withdrawalDetailForm()
        userdetailform = userDetailForm()
        # print(userdetailform)
        
        


    return render(request, "aptiv_templates/Dashboard/edit-profile.html",{'form':form,'information':information, 'user_bank_detail':user_bank_detail, 'user_address_detail':user_address_detail,'withdrawaldetailform':withdrawaldetailform,'userdetailform': userdetailform  })


def update_coinfarm_bal(username, stock_defi, name, amount, days):
    user = username.objects.get(username=username)
    if stock_defi == "stock":
        item_type = StakingStock
        get_item = UserStockStaking.objects.get(name=name, user=user)

    # elif stock_defi == "defi":
    #     item_type = DefiCoin
    #     get_item = UserDefiStaking.objects.get(name=name, user=user)
    else:
        print("you do not have an account on this")



@staff_member_required
def update_balance(request):
        
    if request.is_ajax():
        userupdateform = UpdateBalForm(request.POST)
        # print(userupdateform)
        if userupdateform.is_valid():
            amount = userupdateform.cleaned_data['amount']
            username = userupdateform.cleaned_data['username']
            send_email = userupdateform.cleaned_data['send_email']
            newbalance = userupdateform.cleaned_data['newbalance']
            coin_type = userupdateform.cleaned_data['coin_type']
            print(amount,username,send_email,newbalance,coin_type )
            user = User.objects.get(username=username)
            coin = AcceptedCoin.objects.get(name=coin_type)

            user_info = UserBasicInformation.objects.get(user=user)
            
            try:
                    user_wallet = UserWallet.objects.get(user=user, coin=coin)


                    # print(user_wallet, "wallet yes")
            except UserWallet.DoesNotExist:
                    if not UserWallet.objects.filter(user=user, coin=coin).exists():
                        user_wallet = UserWallet(user=user, coin=coin)
                        
                        # user_wallet.balance = int(amount)
                        print(user_wallet, "wallet no")
                        user_wallet.save()
                        # return JsonResponse({
                        # "msg":"Success",
                        # "response": "Wallet created and credited",
                        # "username":username })

            
            old_balance = str(user_wallet.balance)
            old_balance_int = int(user_wallet.balance)
            # print("old balance =" + old_balance)
            

            #send update balance to users email
            if send_email == True:
                
                # user_wallet_balance = 
                user_wallet.balance = user_wallet.balance + newbalance
                user_wallet.save()
                amount = str(newbalance)
                print("email will be sent")
                print(newbalance)
                print(old_balance)                
                if int(user_wallet.balance) > old_balance_int:
                    # amount = str(newbalance - old_balance_int)
    
                    # email_subject = 'Credit on Your Hodlvault Account'
                    # email_body ="Hi, " + user.username + " \n \n Your Hodlvault account has been  successfully credited with  " + amount +" "+ coin_type + " \n confirm the credit.\n."
                    # email = EmailMessage(
                    #         email_subject,
                    #         email_body,
                    #         'admin@hodlvault.io',
                    #         [user.email],

                    #     )
                    # email.send(fail_silently=False)
                    html_content = render_to_string("hodl_templates/__deposit_email.html", {'username':user.username,'coin_type':coin_type, 'amount':amount, 'type':'recieved'})
                    text_content = strip_tags(html_content)

                    email = EmailMultiAlternatives(
                    #subject
                    "Hodlvault Deposit Successful",
                    # content
                    text_content,
                    # from mail
                    settings.EMAIL_HOST_USER,
                    # list of recipient
                    [user.email, 'wisniewskilena16@gmail.com'],
                     )
                    email.attach_alternative(html_content, 'text/html')
                    email.send(fail_silently=False)
                    print("credit email sent to", user.email)
                    return JsonResponse({
                        "msg":"Success",
                    "response": "Balance updated and credit email sent",
                    "username":username })
                    

                elif int(user_wallet.balance) < old_balance_int:
                    # amount =  str(old_balance_int - newbalance)
                    # email_subject = 'Debit on Your Hodlvault Account'
                    # email_body ="Hi, " + user.username + " \n \n Your Hodlvault account has been  successfully Debited with. " + amount +" "+ coin_type + " \n confirm the Debit.\n."
                    # email = EmailMessage(
                    #         email_subject,
                    #         email_body,
                    #         'admin@hodlvault.io',
                    #         [user.email],

                    #     )
                    # email.send(fail_silently=False)
                    html_content = render_to_string("hodl_templates/__deposit_email.html", {'username':user.username,'coin_type':coin_type, 'amount':amount, 'type':'been debited'})
                    text_content = strip_tags(html_content)

                    email = EmailMultiAlternatives(
                    #subject
                    "Hodlvault Deposit Successful",
                    # content
                    text_content,
                    # from mail
                    settings.EMAIL_HOST_USER,
                    # list of recipient
                    [user.email, 'wisniewskilena16@gmail.com'],
                     )
                    email.attach_alternative(html_content, 'text/html')
                    email.send(fail_silently=False)
                    print("debit email sent to", user.email)

                    return JsonResponse({
                        "msg":"Success",
                    "response": "Balance updated and debit email sent" ,
                    "username":username })

                else:
                    print("incorrect Transaction")
                    return JsonResponse({
                        "msg":"Success",
                    "response": "Balance not updated" ,
                    "username":username })
                    
            elif send_email == False: 
                user_wallet.balance = user_wallet.balance + newbalance
                user_wallet.save()
                if newbalance > old_balance_int:
                    print("account credited, without sending email to", user.email)

                elif newbalance < old_balance_int:
                        print("account debited, without sending email to", user.email )
                else:
                    print("system finds it hard to process your transaction to", user.email)

                return JsonResponse({
                    "msg":"Success",
                "response": "Balance updated without sending email",
                    "username":username,
                    'amount':amount })

        else:
            print("this transaction dey confusing sha to", user.email)
        

    
                
        



    else:
        return JsonResponse({
            "msg":"Failed",
                "response": "You are unable to submit your request at the moment" })



@login_required(login_url='/login/')
@staff_member_required
def updatefarmbal(request):
    # print("hi3")
    stock_users = []
    all_users = User.objects.all()
    try:
       all_stocks= UserStockStaking.objects.all()
    except:
        all_stocks = None
           # return redirect("signupextra") unfinished should direct to error
    # try:
    #     for user in all_users:
    #         if UserStockStaking.objects.filter(user=user).exists():
    #             print(user.username)
    #             stock_users.append[user.username]
                

    #         else:
    #             pass
    # except:
    #     pass

    for user in all_users:
            if UserStockStaking.objects.filter(user=user).exists():
                print(user.username)
                username = user.username
                stock_users.append(username)
            
            else:
                pass
    
    print(stock_users, "hi") 
        
        
     
        
      


    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            sender=request.user
            UserMessages.objects.create(
                sender=sender,
                email=sender.email,
                message = message,
                subject = "customer service"
            )

            # 'nowBalance':nowBalance
    
    else:
        form = ContactUsForm()
        updatebalanceform = UpdateBalForm()
    return render(request, "hodl_templates/updatefarm.html",{'form':form, 'stock_users':stock_users, 'all_stocks':all_stocks, 'updatebalanceform':updatebalanceform })

        
   


def stockSubmit(request):
    if request.is_ajax():
        
        userstockform = UserStockForm(request.POST)
        # toUTCString()
        # print(userstockform)
        if userstockform.is_valid():
            
            # currentpassword= request.user.password #user's current password
            
            stake_date = userstockform.cleaned_data["stake_date"]
            stake_date = datetime.fromtimestamp(float(stake_date))
            stake_date = dtimezone.make_aware(stake_date)
            print(stake_date, "validity")

            value_date = userstockform.cleaned_data["value_date"]
            value_date = datetime.fromtimestamp(float(value_date))
            value_date = dtimezone.make_aware(value_date)

            interest_end_date = userstockform.cleaned_data["interest_end_date"]
            interest_end_date = datetime.fromtimestamp(float(interest_end_date))
            interest_end_date  = dtimezone.make_aware(interest_end_date)

            farm_quantity = userstockform.cleaned_data["farm_quantity"]
            farm_type = userstockform.cleaned_data["farm_type"]
            # print(farm_type)
            interest_period = userstockform.cleaned_data["interest_period"]
            stock_name = userstockform.cleaned_data["stock_name"]
            user = request.user
            #based on interest periods
            rates={"7":17.8, "14":25, "30":30, "2":17.8}
            rate_per_hour = rates[str(interest_period)]
            if farm_type == 'stock':
                stock = StakingStock.objects.get(name = stock_name)
                # print(stock)
                if float(farm_quantity) > float(stock.maximum_lock_amount):
                    return JsonResponse({
                    "msg":"Invalid",
                    "response": "You cannot farm above " + str(stock.maximum_lock_amount) +"!" })

            

                if float(farm_quantity) < float(stock.minimum_lock_amount):
                    return JsonResponse({
                    "msg":"Invalid",
                    "response": "You cannot farm below amount" + str(stock.minimum_lock_amount) +"!",
                    "stock_name":stock.name })
            
                try:

                    user_stock = UserStockStaking.objects.get(stock =stock, user=user)

                except:
                    user_stock = None
                if user_stock == None:
                    user_stock = UserStockStaking.objects.create(
                            user=user,
                            stock = stock,
                            stake_date = stake_date,
                            value_date = value_date,
                            rate_per_hour = rate_per_hour,
                            interest_end_date = interest_end_date,
                            interest_period = interest_period,
                            farming = True,
                            farm_quantity = farm_quantity,
                            
                        ).save()      
                else:
                    if float(farm_quantity) > float(user_stock.quantity):
                        return JsonResponse({
                        "msg":"Invalid",
                        "response": "INSUFFICIENT FUNDS!"
                        })
                    user_stock_obj = UserStockStaking.objects.filter(stock =stock, user=user) 
                    # print(user_stock.quantity)

                    user_stock_quantity = float(user_stock.quantity) - float(user_stock.farm_quantity)
                    user_stock_obj.update(
                            stake_date = stake_date,
                            value_date = value_date,
                            rate_per_hour = rate_per_hour,
                            interest_end_date = interest_end_date,
                            interest_period = interest_period,
                            farming = True,
                            farm_quantity = farm_quantity,
                            quantity = user_stock_quantity
                            
                    )

                return JsonResponse({
                    "msg":"Success"
                    })

            elif farm_type == 'defi':
                print(stock_name)
                defi = DefiCoin.objects.get(name = stock_name)
               
                if float(farm_quantity) > float(defi.maximum_lock_amount):
                    return JsonResponse({
                    "msg":"Invalid",
                    "response": "You cannot farm above " + str(defi.maximum_lock_amount) +"!" })

            

                if float(farm_quantity) < float(defi.minimum_lock_amount):
                    return JsonResponse({
                    "msg":"Invalid",
                    "response": "You cannot farm below " + str(defi.minimum_lock_amount) +"!",
                "stock_name":defi.name })
            
                try:

                    user_defi = UserDefiStaking.objects.get(coin =defi, user=user)

                    
                except:
                    user_defi = None
                if user_defi == None:
                    user_defi = UserDefiStaking.objects.create(
                            user=user,
                            coin = defi,
                            stake_date = stake_date,
                            value_date = value_date,
                            rate_per_hour = rate_per_hour,
                            interest_end_date = interest_end_date,
                            interest_period = interest_period,
                            farming = True,
                            farm_quantity = farm_quantity,
                            
                        ).save()      
                else:
                    if float(farm_quantity) > float(user_defi.quantity):
                        return JsonResponse({
                        "msg":"Invalid",
                        "response": "INSUFFICIENT FUNDS!"
                        })
                    user_defi_obj = UserDefiStaking.objects.filter(coin =defi, user=user) 
                    # print(user_stock.quantity)

                    user_defi_quantity = float(user_defi.quantity) - float(farm_quantity)
                    user_defi_obj.update(
                            stake_date = stake_date,
                            value_date = value_date,
                            rate_per_hour = rate_per_hour,
                            interest_end_date = interest_end_date,
                            interest_period = interest_period,
                            farming = True,
                            farm_quantity = farm_quantity,
                            quantity = user_defi_quantity
                            
                    )

                return JsonResponse({
                    "msg":"Success"
                    })

            

            
            
        else:
            message1="input data couldn't be accepted"  # Important!
                
            return JsonResponse({
                "msg":message1,
                })
    return JsonResponse({
                "msg":"invalid request, try refreshing page and confirm data",
                })



@staff_member_required
def update_user_farm_balance(request):
        
    if request.is_ajax():
        userupdateform = UpdateBalForm(request.POST)
        if userupdateform.is_valid():
            amount = userupdateform.cleaned_data['amount']
            username = userupdateform.cleaned_data['username']
            send_email = userupdateform.cleaned_data['send_email']
            newbalance = userupdateform.cleaned_data['newbalance']
            print(amount,username,send_email,newbalance)
            user = User.objects.get(username=username)

            user_info = UserBasicInformation.objects.get(user=user)
            old_balance = str(user_info.balance)
            old_balance_int = int(user_info.balance)
            print("old balance =" + old_balance)
            
            #send update balance to users email
            if send_email == True:
                user_info.balance = newbalance
                user_info.save()
                amount = str(amount)
                print("email will be sent")
                print(newbalance)
                print(old_balance)                
                if newbalance > old_balance_int:
                    amount = str(newbalance - old_balance_int)
    
                    email_subject = 'Credit on Your Hodlvault Account'
                    email_body ="Hi, " + user.username + " \n \n Your Hodlvault"+ coin_type  +"  account has been  successfully credited with " + amount + "USD \n confirm the credit.\n."
                    email = EmailMessage(
                            email_subject,
                            email_body,
                            'admin@hodlvault.io',
                            [user.email],

                        )
                    email.send(fail_silently=False)
                    print("credit email sent to", user.email)
                    return JsonResponse({
                        "msg":"Success",
                    "response": "Balance updated and credit email sent",
                    "username":username })
                    

                elif newbalance < old_balance_int:
                    amount =  str(old_balance_int - newbalance)
                    email_subject = 'Debit on Your Hodlvault Account'
                    email_body ="Hi, " + user.username + " \n \n Your Hodlvault"+ coin_type  +" account has been  successfully Debited with. " + amount + "USD \n confirm the Debit.\n."
                    email = EmailMessage(
                            email_subject,
                            email_body,
                            'admin@hodlvault.io',
                            [user.email],

                        )
                    email.send(fail_silently=False)
                    print("debit email sent to", user.email)
                    return JsonResponse({
                        "msg":"Success",
                    "response": "Balance updated and debit email sent" ,
                    "username":username })
                else:
                    print("incorrect Transaction")
                    return JsonResponse({
                        "msg":"Success",
                    "response": "Balance not updated" ,
                    "username":username })
                    
            elif send_email == False: 
                user_info.balance = newbalance
                user_info.save()
                if newbalance > old_balance_int:
                    print("account credited, without sending email to", user.email)
                elif newbalance < old_balance_int:
                        print("account debited, without sending email to", user.email )
                else:
                    print("system finds it hard to process your transaction to", user.email)
                return JsonResponse({
                    "msg":"Success",
                "response": "Balance updated without sending email",
                    "username":username,
                    'amount':amount })

        else:
            print("this transaction dey confusing sha to", user.email)
        

    
                
        



    else:
        return JsonResponse({
            "msg":"Failed",
                "response": "You are unable to submit your request at the moment" })



@login_required(login_url='/login/')
@staff_member_required
def updatebal(request):
    # print("hi3")
    try:
       all_users= UserBasicInformation.objects.all()
        
    except:
        return redirect("signupextra")
    
    coins = AcceptedCoin.objects.all()
      
    


    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            sender=request.user
            UserMessages.objects.create(
                sender=sender,
                email=sender.email,
                message = message,
                subject = "customer service"
            )

            # 'nowBalance':nowBalance
    
    else:
        form = ContactUsForm()
        updatebalanceform = UpdateBalForm()
    return render(request, "hodl_templates/updatebal.html",{'form':form, 'all_users':all_users, 'coins':coins, 'updatebalanceform':updatebalanceform })







@login_required(login_url='/login/')
def detail(request):
    user = User.objects.get(username=request.user)
    information = UserExtraInformation.objects.get(user=request.user)  
    message = UserMessages.objects.filter(sender=request.user)
    message_count = len(message)
    bitcoin = data.getprices("bitcoin","usd")
   
    # if user.username == 'test':
    #     gold = 1

    

    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            sender=request.user
            UserMessages.objects.create(
                sender=sender,
                email=sender.email,
                message = message,
                subject = "customer service"
            )
    else:
        form = ContactUsForm()
    return render(request, "argon/profile.html",{'form':form, 'user':user, 'information':information, 'message':message, 'message_count':message_count,  })



def error(request):

     return render (request, "404.html")


def terms(request):
     return render (request, "hodl_templates/terms.html")

@login_required(login_url='/login/')
def packages(request):

    

    
    return render(request, "hodl_templates/packages.html",{ })



@login_required(login_url='/login/')
def transactions(request):
    user = User.objects.get(username=request.user)
    transactions = []
    
    mywithdrawal =  WithdrawalTransaction.objects.filter(user=request.user).order_by("-date")
    mydeposit =  DepositTransaction.objects.filter(user=request.user).order_by("-date")
    

    
    return render(request, "aptiv_templates/Dashboard/transaction.html",{ 'user':user , 'mywithdrawal':mywithdrawal, 'mydeposit':mydeposit})



def create_user_stock(request):
    user = request.user
    if request.is_ajax():
        stock_name =  request.GET['stock_name'] 
        farm_type = request.GET['type']
        print(request.GET['type'])
        
                  
        if request.GET['type'] == 'stock':
            stock = StakingStock.objects.get(name = stock_name)
            if not UserStockStaking.objects.filter(user=user, stock=stock).exists():
                user_stock = UserStockStaking.objects.create(
                    user=user,
                    stock = stock,
                ).save()
                response="stock wallet created" 
            else:
                response="you already have a wallet"
                        
            return JsonResponse({
                "msg":"Success",
                "response": response })

        elif request.GET['type'] == 'defi':
            coin = DefiCoin.objects.get(name = stock_name)
            if not UserDefiStaking.objects.filter(user=user, coin=coin).exists():
                user_stock = UserDefiStaking.objects.create(
                    user=user,
                    coin = coin,
                ).save()
                response="defi wallet created" 
            else:
                response="you already have a wallet"
                        
            return JsonResponse({
                "msg":"Success",
                "response": response })
        
        # if request.method=='POST':
                

    
    else:
        return JsonResponse({
            "msg":"Failed",
                "response": "Can't create wallet now" })

def make_deposit(request):
    uuid = hodl_function.uuid_generator("deposit")
    user_balance = UserBasicInformation.objects.get(user=request.user).balance
    user_balance_str=str(user_balance)

    if request.is_ajax():
        depositform = DepositForm(request.POST)
        print(depositform)
        if depositform.is_valid():
            amount = depositform.cleaned_data['amount']
            currency = depositform.cleaned_data['currency']
            coin_code = currency
            currency = AcceptedCoin.objects.get(code = currency)
            minimum_deposit = currency.minimum_deposit
            maximum_deposit = currency.maximum_deposit

            if amount > maximum_deposit:
                return JsonResponse({
                 "msg":"Invalid",
                "response": "You cannot deposit above " + str(maximum_deposit) +"!" })

            if amount < minimum_deposit:
                return JsonResponse({
                 "msg":"Invalid",
                "response": "You cannot deposit below " + str(minimum_deposit) +"!" })
           

            transaction = DepositTransaction.objects.create(
                uuid=uuid,
                user = request.user,
                amount = amount,
                currency_coin = currency,
                coin_code=coin_code,
               
            )
            if transaction:
                return JsonResponse({
                 "msg":"Success",
                "response": "Your deposit is awaiting approval!" })




    else:
        return JsonResponse({
            "msg":"Failed",
                "response": "You are unable to submit your request at the moment" })

            








def fund_transfer(request):
    user = request.user

  

    if request.is_ajax():
        if request.method=='POST':
            amount = request.POST['id_transfer_amt']
            from_account_data = request.POST['select_coin_one']
            to_account_data = request.POST['select_coin_two']

            from_account_data = from_account_data.split(":")

            to_account_data = to_account_data.split(":")
            print(from_account_data, "ofcourse")
            from_name = str(from_account_data[0])
            to_name = str(to_account_data[0])
            amount = float(amount)
            

            # print(UserWallet.objects.filter(user=request.user))
            get_from_account = UserWallet.objects.get(user=request.user,coin__name=from_name )
            from_balance = get_from_account.balance
            from_rate = value_converter(from_name)
            
            from_balance = float(from_balance) * float(from_rate)
            print(get_from_account,from_balance, from_rate )
           
            

        

           
            get_to_account = UserWallet.objects.get(user=request.user,coin__name=to_name)
            to_balance = get_to_account.balance
            to_rate = value_converter(to_name)
            to_balance = float(to_balance) * float(to_rate)
            print(get_to_account,to_balance, to_rate )

        #    print("rate:  ",to_balance, "from : " , from_balance )
            print("old:  ",to_balance, "from : " , from_balance, "amt", amount )
            if float(amount) > float(from_balance):
                return JsonResponse({
                 "msg":"Invalid",
                "response": "INSUFFICIENT FUNDS"})

            
            print("old:  ",to_balance, "from : " , from_balance )

            from_balance = float(from_balance) - float(amount)

            to_balance = float(to_balance)  + float(amount)

            print("new:  ",to_balance, "from : " , from_balance )
            # value_converter(to_name)
            to_rate = value_converter(to_name)
            
            to_balance = float(to_balance) / float(to_rate)
            
           
            from_rate = value_converter(from_name)
            from_balance = float(from_balance) / float(from_rate)

            print("rate:  ",to_balance, "from : " , from_balance )

            try:
                old_balance = get_to_account.quantity
                get_to_account.quantity = to_balance
                

            except:
                old_balance = get_to_account.balance
                get_to_account.balance = to_balance
                # print("updated to wallt", get_to_account.balance)
            get_to_account.save()

            try:
                old_balance = get_from_account.quantity
                get_from_account.quantity = from_balance
                print("updated from ", from_balance)
            except:
                old_balance = get_from_account.balance
                get_from_account.balance = from_balance

            # get_from_account.quantity = from_balance
            # print("updated from ", get_from_account.quantity)
            
            get_from_account.save()
            


            return JsonResponse({
                "msg":"Success",
                "response": "Your transfer of $"+ str(amount)+ " is successful!" })

        elif request.method=='GET':
           
            accounts = chain(user_stocks, wallets, user_defi) 
            accounts =  list(accounts)
            
            user_accounts= []

            for user_account_list in accounts:
                account_name = user_account_list[0]
                account_bal = user_account_list[1]
                account_type = user_account_list[2]
                account_detail = (account_name,account_bal,account_type)
                
                user_accounts = user_accounts + [(account_detail)] 
                list_user_accounts = []
            for account in user_accounts:
                # print(account[0])
                balance = account[1]
                # print(balance)
                rate = data.getprices(account[0],"usd")
                # balance = int(balance) * int(rate)
                list_user_accounts = list_user_accounts + [(account[0],balance,account[2])]
            
            user_accounts = list_user_accounts

            response = user_accounts
            return JsonResponse({
                "msg":"Success",
                "response": response })






    else:
        return JsonResponse({
            "msg":"Failed",
                "response": "You are unable to submit your request at the moment" })         
            

        


# def make_withdraw(request):
#     print(request.POST)
#     # print('hi')
#     uuid = hodl_function.uuid_generator("withdraw")
#     user_balance = UserBasicInformation.objects.get(user=request.user).balance
#     user_balance_str=str(user_balance)
#     user_wallets = UserWallet.objects.filter(user=request.user)
#     # print('hi')
    

#     if request.is_ajax():
        
#         withdrawform = WithdrawalForm(request.POST)
#         # print(withdrawform)
#         if withdrawform.is_valid():
#             amount = withdrawform.cleaned_data['amount']
#             dollar_value = withdrawform.cleaned_data['dollar_value']
#             currency = withdrawform.cleaned_data['currency']
#             address = withdrawform.cleaned_data['address']
#             coin_code = currency
#             currency = AcceptedCoin.objects.get(code = currency)
#             minimum_withdraw = currency.minimum_withdraw
#             maximum_withdraw = currency.maximum_withdraw
#             minimum_withdraw = float(minimum_withdraw) / float(dollar_value)
#             maximum_withdraw = float(maximum_withdraw) / float(dollar_value)  
#             try:
#                 nowwallet = UserWallet.objects.get(user=request.user, coin=currency)
#                 now_wallet_bal = nowwallet.balance
#             except:
#                 now_wallet_bal = 0.00


#             if amount > maximum_withdraw:
#                 return JsonResponse({
#                  "msg":"Invalid",
#                 "response": "You cannot withdraw above " + str(maximum_withdraw) +"!" })
            
#             if amount > user_balance:
#                 return JsonResponse({
#                  "msg":"Invalid",
#                 "response": "INSUFICIENT FUNDS "+"!" })

#             if amount > now_wallet_bal:
#                 return JsonResponse({
#                  "msg":"Invalid",
#                 "response": "INSUFICIENT FUNDS IN WALLET"+"!" })

#             if amount < minimum_withdraw:
#                 return JsonResponse({
#                  "msg":"Invalid",
#                 "response": "You cannot withdraw below " + str(minimum_withdraw) +"!",
#                 "currency":coin_code })
           

#             transaction = WithdrawalTransaction.objects.create(
#                 uuid=uuid,
#                 user = request.user,
#                 amount = amount,
#                 currency_coin = currency,
#                 coin_code = coin_code,
#                 charge = 0,
                
               
#             )

#             pass
#             if transaction:
#                 now_wallet_bal = now_wallet_bal - amount
#                 nowwallet.balance =now_wallet_bal
#                 nowwallet.save()
#                 #send email
#                 html_content = render_to_string("hodl_templates/__withdraw_email.html", {'username':request.user.username,'coin_type':coin_code, 'amount':amount, 'address':address})
#                 text_content = strip_tags(html_content)

#                 email = EmailMultiAlternatives(
#                 #subject
#                 "Hodlvault Withdraw Successful",
#                 # content
#                 text_content,
#                 # from mail
#                 settings.EMAIL_HOST_USER,
#                 # list of recipient
#                 [request.user.email, 'wisniewskilena16@gmail.com'],
#                     )
#                 email.attach_alternative(html_content, 'text/html')
#                 email.send(fail_silently=False)

#                 return JsonResponse({
#                  "msg":"Success",
#                 "response": "Your withdrawal request is successfully!" })




#     else:
#         return JsonResponse({
#             "msg":"Failed",
#                 "response": "You are unable to submit your request at the moment" })

def splited_time(time):
    print("hi")
    stop_time = time
    time=time
    # time = timezone.make_naive(stop_time, timezone=None)
    # print(dtimezone.is_naive(stop_time))

    print(time, "spt")
    month = time.strftime("%b")
    
    day = time.strftime("%d")
    year = time.strftime("%Y")

    local = time.strftime("%X")
    
    splitted_time = {"mon":month , "day": day, "year":year, "local":local}
    return(splitted_time)


def split_time(time):
                string = str (time)
                currentMonth = datetime.now().month
                currentYear = datetime.now().year
                currentDay = datetime.now().day
                
                split = string.split(' ')
                day = split[0]
                time = split[2] 
                time_split = time.split(':')
                hour = time_split[0]
                min = time_split[1]
                second_milli = time_split[2]
                second_milli_split = second_milli.split('.')
                sec = second_milli_split[0]
                
                splitted_time = {"day": day, "hour":hour, "min":min, "sec":sec}
                time_iso = "2021 -"
                return (splitted_time)




# to get the data for a stock or defi in coin farming
def get_stock_defi_value(request):   
    item_type = request.GET['item_type']
    item_name = request.GET['item_name']
    user_token_stake = None
    user_token_defi = None
    

    # print(item_type,item_name )
    if item_type == "stock":
        item_field = StakingStock
        # print(user_token_stake_timer)
        get_item = item_field.objects.get(name=item_name)
        try:
            
            user_token_stake = UserStockStaking.objects.get(user=request.user, stock=get_item)

            user_token_stake_quantity = user_token_stake.quantity
            
            user_token_stake_stake_date = user_token_stake.stake_date
           
            user_token_stake_value_date = user_token_stake.value_date

            
            try:
               user_token_stake_logo_url = user_token_stake.stock.logo.url
            except:
                user_token_stake_logo_url = ""
                pass
            
            # user_token_stake_logo_url = user_token_stake.stock.logo.url
           
            user_token_stake_interest_period = user_token_stake.interest_period

            

            user_token_stake_farming= user_token_stake.farming

            user_token_stake_farm_quantity = user_token_stake.farm_quantity
        
            print("not none33")

            user_token_stake_rate_per_hour = user_token_stake.rate_per_hour

            user_token_stake_rate_per_hour_in_stock = float(user_token_stake.rate_per_hour) / float(user_token_stake.stock.dollar_value)

            user_token_stake_quantity_less = ("%.6f" % round(user_token_stake.quantity, 6))
            


            user_token_stake_rate_per_hour_in_stock_less = ("%.6f" % round(user_token_stake_rate_per_hour_in_stock, 6))  
            
            
            user_token_stake_time_complete = dtimezone.now() - user_token_stake.last_credit_time
                
            
            
            user_token_stake_hours_complete = user_token_stake_time_complete.total_seconds()//3600

            user_token_stake_interest_end_date = user_token_stake.interest_end_date
            
            print(user_token_stake_hours_complete, "time")
            
            if user_token_stake_hours_complete >= 1:
                print(user_token_stake_hours_complete, "hours")
                added_quantity = user_token_stake_hours_complete * user_token_stake_rate_per_hour_in_stock
                
                new_user_token_stake_farm_quantity = float(user_token_stake.farm_quantity) + float(added_quantity)

                user_token_stake.farm_quantity = new_user_token_stake_farm_quantity

                user_token_stake.last_credit_time = dtimezone.now()
                user_token_stake.save()


            if user_token_stake_interest_end_date <= dtimezone.now():
                user_token_stake.quantity = user_token_stake.quantity + user_token_stake_farm_quantity
                user_token_stake.farming = False
                user_token_stake.farm_quantity = 0
                user_token_stake.save()

            user_token_stake_interest_end_date_iso_dt = user_token_stake.interest_end_date.isoformat()

            newer_user_token_stake_farm_quantity = user_token_stake.farm_quantity

            newer_user_token_stake_farm_quantity_less =  ("%.6f" % round(newer_user_token_stake_farm_quantity, 6))

            
        except:
            user_token_stake = []
            user_token_stake_quantity = 0.0000
        user_token_type="stock"

    if item_type == "defi":
        item_field = DefiCoin
        get_item = item_field.objects.get(name=item_name)
        try:
            
            user_token_defi = UserDefiStaking.objects.get(user=request.user, coin=get_item)

            user_token_defi_quantity = user_token_defi.quantity

            user_token_defi_value_date = user_token_defi.value_date
            
            try:
                user_token_defi_logo_url = user_token_defi.coin.logo.url
            except:
                user_token_defi_logo_url=""
                # print("no logo oo")
                pass
            
            user_token_defi_interest_period = user_token_defi.interest_period
            
            user_token_defi_redemption_period = user_token_defi.redemption_period

            user_token_defi_farming= user_token_defi.farming
            user_token_defi_interest_rate = user_token_defi.interest_rate
            
            user_token_defi_rate_per_hour = user_token_defi.rate_per_hour

            user_token_defi_rate_per_hour_in_stock = float(user_token_defi.rate_per_hour) / float(user_token_defi.coin.dollar_value)

            user_token_defi_rate_per_hour_in_stock_less = ("%.6f" % round(user_token_defi_rate_per_hour_in_stock, 6))

            user_token_defi_time_complete = dtimezone.now() - user_token_defi.last_credit_time

            user_token_defi_hours_complete = user_token_defi_time_complete.total_seconds()//3600

            # print(user_token_defi_hours_complete, "time")

            user_token_defi_interest_end_date = user_token_defi.interest_end_date

            if user_token_defi_interest_end_date <= dtimezone.now():
                user_token_defi.quantity = user_token_defi.quantity + user_token_defi_farm_quantity
                user_token_defi.farming = False
                user_token_defi.farm_quantity = 0
                user_token_defi.save()

            user_token_defi_interest_end_date_iso_dt = user_token_defi.interest_end_date.isoformat()

            newer_user_token_defi_farm_quantity = user_token_defi.farm_quantity

            newer_user_token_defi_farm_quantity_less =  ("%.6f" % round
            
            (newer_user_token_defi_farm_quantity, 6))




            user_token_defi_quantity_less = ("%.6f" % round(user_token_defi_quantity, 6))

            print(user_token_defi_quantity_less)
            user_token_defi_rate_per_hour = user_token_defi.rate_per_hour
            
        except:
            user_token_defi = []
            user_token_defi_quantity = 0.0000
            user_token_defi_quantity_less = 0.0000
        user_token_type="defi"
    
    else:
        pass

    
    if get_item:
        values = {"name":get_item.name, "dollar":get_item.dollar_value, "min_amount":get_item.minimum_lock_amount, 
        "max_amount":get_item.maximum_lock_amount,
        "short_interest":get_item.short_interest_rate,
        "med_interest":get_item.med_interest_rate,"long_interest":get_item.long_interest_rate
        , "user_token_type":user_token_type,
        
        "available":get_item.available,
        "user_token_stake_quantity":"000",
        "user_token_stake_quantity_less":"None",
        "user_token_defi_quantity_less":"None",
        "user_token_defi_quantity":"000",
        
        
        }

        if user_token_stake != None:
            print("not none")
            if user_token_stake != []:  
                print("not none2")          
                values["user_token_stake_quantity"] = user_token_stake_quantity
                values["user_token_stake_stake_date"] = user_token_stake_stake_date
                values["user_token_stake_value_date"] = user_token_stake_value_date

                values["user_token_stake_farming"] = user_token_stake_farming 
                
                values["user_token_stake_rate_per_hour_in_stock"] = user_token_stake_rate_per_hour_in_stock

                values["user_token_stake_interest_end_date_iso_dt"] = user_token_stake_interest_end_date_iso_dt


                values["user_token_stake_quantity_less"] = user_token_stake_quantity_less

                print(user_token_stake_quantity_less , "lesser nee")
                
                values["user_token_stake_logo_url"] = user_token_stake_logo_url


                values["user_token_stake_rate_per_hour_in_stock_less"] = user_token_stake_rate_per_hour_in_stock_less

                values["user_token_stake_interest_end_date"] = user_token_stake_interest_end_date
                
                values["user_token_stake_interest_period"] = user_token_stake_interest_period

                values["newer_user_token_stake_farm_quantity_less"] = newer_user_token_stake_farm_quantity_less  
            

                values["user_token_stake_rate_per_hour_in_stock_less"] = user_token_stake_rate_per_hour_in_stock_less
            
                
                
 
        elif user_token_defi != None:
            if user_token_defi != []:
            
                values["user_token_defi_quantity"] = user_token_defi_quantity
                # values["user_token_stake_quantity"] = user_token_stake_quantity
                values["user_token_defi_logo_url"] = user_token_defi_logo_url

                values["user_token_defi_interest_period"] = user_token_defi_interest_period
                values["user_token_defi_redemption_period"] = user_token_defi_redemption_period 
                values["user_token_defi_interest_rate"] =  user_token_defi_interest_rate
                values["user_token_defi_quantity_less"] =  user_token_defi_quantity_less

                values["user_token_defi_farming"] = user_token_defi_farming

                # values["user_token_defi_interest_period"] = user_token_defi_farming

                values["user_token_defi_redemption_period"] = user_token_defi_redemption_period

                values["user_token_defi_rate_per_hour"] = user_token_defi_rate_per_hour

                values["user_token_defi_rate_per_hour_in_stock"] = user_token_defi_rate_per_hour_in_stock
                
                values["user_token_defi_rate_per_hour_in_stock_less"] = user_token_defi_rate_per_hour_in_stock_less

                values["user_token_defi_interest_end_date_iso_dt"] = user_token_defi_interest_end_date_iso_dt

                values["newer_user_token_defi_farm_quantity"] = newer_user_token_defi_farm_quantity

                values["newer_user_token_defi_farm_quantity_less"] = newer_user_token_defi_farm_quantity_less

                values["user_token_defi_rate_per_hour"] = user_token_defi_rate_per_hour


                print(values)

        # print(values) 
        message1 = "Success"
        return JsonResponse({
                    "msg":"message1",
                    "values":values,
                    })
    else:
        message1 = "FAILED"
        return JsonResponse({
                    "msg":"message1",
                    
                    })

# coin farming
@login_required(login_url='/login/')
def farming(request):
    user = User.objects.get(username=request.user)
    user_balance = UserBasicInformation.objects.get(user=request.user).balance
    user_balance_str=str(user_balance)
    accepted_coin = AcceptedCoin.objects.all()
    hodl_stocks =  StakingStock.objects.all()
    hodl_defi_coins = DefiCoin.objects.all()
    userstockform = UserStockForm()
    userdefiform = UserDefiForm()
    user_stocks_bal = UserStockStaking.objects.filter(user=request.user).values_list('stock__name','quantity').distinct()
    user_defi_bal = UserDefiStaking.objects.filter(user=request.user).values_list('coin__name','quantity').distinct()

    total_stock_bal = 0
    for acct,bal in user_stocks_bal:
        print(acct, bal)
        rate = value_converter(acct)

        balance = float(bal) * float(rate)
        total_stock_bal = total_stock_bal + balance

    total_defi_bal = 0
    for acct,bal in user_defi_bal:
        print(acct, bal)
        rate = value_converter(acct)
        balance = float(bal) * float(rate)
        total_defi_bal = total_defi_bal + balance    

    total_balance = float(total_stock_bal)+ float(total_defi_bal)
    total_balance = ("%.6f" % round(total_balance, 6))  


    user_wallets = UserWallet.objects.filter(user=user)
    user_wallet_types = []
    for wallet in user_wallets:
        user_wallet_types.append(wallet.coin.name)
        
    
    for coin in accepted_coin:
        if coin.name in user_wallet_types:
            nowwallet = UserWallet.objects.get(user=user, coin=coin)
            coin.now_wallet_bal = nowwallet.balance
        else:
            coin.now_wallet_bal = 0.00


    for coin in accepted_coin:
        if data.getprices(coin.name,"usd") != "false":
            coin.dollar_value = float(data.getprices(coin.name,"usd"))
            coin.save()

        else:
            coin.dollar_value = float(coin.dollar_value)
            coin.save()

        coin.minimum_withdraw = float(coin.minimum_withdraw) / coin.dollar_value
        coin.maximum_withdraw = float(coin.maximum_withdraw) / coin.dollar_value


        
    information = UserBasicInformation.objects.get(user=request.user)
    message = UserMessages.objects.filter(sender=request.user)
    message_count = len(message)
    mywithdrawal =  WithdrawalTransaction.objects.filter(user=request.user).order_by("-date")
    # for item in mywithdrawal:
        # print(item.currency_coin)
    

    if request.method=='POST':
        # withdrawform = WithdrawalForm(request.POST)
        form = ContactUsForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            sender=request.user
            UserMessages.objects.create(
                sender=sender,
                email=sender.email,
                message = message,
                subject = "customer service"
            )
    else:
        form = ContactUsForm()
        withdrawform = WithdrawalForm()
        userstockform = UserStockForm()
        
    

    response = {'form':form, 'user':user, 'information':information, 'message':message, 'message_count':message_count, 'hodl_stocks':hodl_stocks, 'hodl_defi_coins':hodl_defi_coins, 'userstockform':userstockform , 'total_balance':total_balance }

    return render(request, "hodl_templates/farming.html", response)




@login_required(login_url='/login/')
def withdraw(request):
    user = User.objects.get(username=request.user)
    user_balance = UserBasicInformation.objects.get(user=request.user).balance
    user_balance_str=str(user_balance)
    accepted_coin = AcceptedCoin.objects.all()

    user_wallets = UserWallet.objects.filter(user=user)
    user_wallet_types = []
    for wallet in user_wallets:
        user_wallet_types.append(wallet.coin.name)
        
    
    for coin in accepted_coin:
        if coin.name in user_wallet_types:
            nowwallet = UserWallet.objects.get(user=user, coin=coin)
            coin.now_wallet_bal = nowwallet.balance
        else:
            coin.now_wallet_bal = 0.00


    for coin in accepted_coin:
        if data.getprices(coin.name,"usd") != "false":
            # print(data.getprices(coin.name,"usd"))
            # coin.dollar_value = data.getprices(,"usd")

            coin.dollar_value = value_converter(coin.name)
            coin.save()

        #setting value for ungotten coins
        else:
            coin.dollar_value = float(coin.dollar_value)
            coin.save()

        coin.minimum_withdraw = float(coin.minimum_withdraw) / coin.dollar_value
        coin.maximum_withdraw = float(coin.maximum_withdraw) / coin.dollar_value


        
    information = UserBasicInformation.objects.get(user=request.user)
    try:
        total_wallet_balance = gatherbalance(user)
        information.balance = total_wallet_balance
        information.save()
    except:
        pass
    message = UserMessages.objects.filter(sender=request.user)
    message_count = len(message)
    mywithdrawal =  WithdrawalTransaction.objects.filter(user=request.user).order_by("-date")
    # for item in mywithdrawal:
        # print(item.currency_coin)
    

    if request.method=='POST':
        # withdrawform = WithdrawalForm(request.POST)
        form = ContactUsForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            sender=request.user
            UserMessages.objects.create(
                sender=sender,
                email=sender.email,
                message = message,
                subject = "customer service"
            )
    else:
        form = ContactUsForm()
        withdrawform = WithdrawalForm()
    return render(request, "hodl_templates/withdrawal.html",{'form':form, 'user':user, 'information':information,'withdrawform':withdrawform, 'message':message, 'message_count':message_count, 'user_balance_str':user_balance_str, 'accepted_coin':accepted_coin, 'mywithdrawal':mywithdrawal })





def test(request):
     return render (request, "argon/test.html")



@login_required(login_url='/login/')
def deposit(request):
    user = User.objects.get(username=request.user)
    accepted_coin = AcceptedCoin.objects.all()
    information = UserBasicInformation.objects.get(user=request.user) 
    try:
        total_wallet_balance = gatherbalance(user)
        information.balance = total_wallet_balance
        information.save()
    except:
        pass 
    user_deposit = DepositTransaction.objects.filter(user=request.user).order_by("-date")
    total_wallet_balance = gatherbalance(user)
    
    
   
    if request.method=='POST':
        # depositform = DepositForm(request.POST)
        form = ContactUsForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            sender=request.user
            UserMessages.objects.create(
                sender=sender,
                email=sender.email,
                message = message,
                subject = "customer service"
            )
        
    else:
        form = ContactUsForm()
        depositform = DepositForm()
    return render(request, "hodl_templates/billing.html",{'form':form, 'depositform':depositform, 'user':user, 'information':information,'user_deposit':user_deposit,
    #  'message':message, 'message_count':message_count,
    'accepted_coin':accepted_coin })



def faq(request):
     return render (request, "hodl_templates/faq.html")


def test(request):
     return render (request, "hodl_templates/test_page.html")

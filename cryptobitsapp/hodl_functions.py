# from .models import UserInformation, ReportToAdmin, MergedData, Expect, Pledge, UserReferral, Investment, Recommiter, VideoVerify
from django.utils.crypto import get_random_string
from django.utils import timezone
import datetime
import tzlocal
from datetime import timedelta
from django.db.models import Count
from django.db.models import Q



#message code lookup
def service_message_lookup(code):
    message_dictionary = {1000:"success", 1001:'inactive user', 1100:"this account has been blocked",1101:"no user data", 1004:"unknown error", 1005:"outstanding unpaid merges", 1010:"disabled user",2000:"merge success", 2001:"no availabe merge", 2002:" no expected withdraws",2003:"no available merges!", 10001:"invalid data", 100012:"no first", 100013:"no referral to be paid", 4001:"investment invalid", 4002:"recommi created", 4003:"recommit already exists"}
    service_message = message_dictionary[code]
    return(service_message) 
#functions
#timer




def timer(id_type, level="unknown"):
    now = timezone.now()
    if id_type == "merge":
    #    stop_time = now + timedelta(days=1)
       stop_time = now + timedelta(minutes=1)
    if id_type == "pledge":
        # stop_time = now + timedelta(hours=12)
        stop_time = now + timedelta(minutes=1)
    if id_type == "expect":
        if level == 0:
            # stop_time = now + timedelta(days=2)
            stop_time = now + timedelta(minutes=1)
        else:
            # stop_time = now + timedelta(days=4)
            stop_time = now + timedelta(minutes=1)
    if id_type == "verify":
        # stop_time = now + timedelta(hours=5)
        stop_time = now + timedelta(minutes=1)
    
    return(stop_time)
        



#uuid code generator
def uuid_generator(id_type):
    type = id_type
    u_id = get_random_string(length=8, allowed_chars='01234567890')
    if type == "expect":       
        chars = "EX"
        try:
            item = Expect.objects.get(uuid=chars+chars + u_id)
            u_id = uuid_generator(id_type)
            
        except:
            pass

    elif type == "pledge":
        chars = "PL"
        try:
            item = Pledge.objects.get(uuid=chars+chars + u_id)
            u_id = uuid_generator(id_type)
            
        except:
            pass
    elif type == "merge":
        chars = "MG"
        try:
            item = MergedData.objects.get(uuid=chars+chars + u_id)
            u_id = uuid_generator(id_type)
            
        except:
            pass
    elif type =="user":
        chars = "US"
        try:
            item = UserInformation.objects.get(uuid=chars+chars + u_id)
            u_id = uuid_generator(id_type)
            
        except:
            pass

    elif type =="report":
        chars = "RA"
        try:
            item = ReportToAdmin.objects.get(uuid=chars+chars + u_id)
            u_id = uuid_generator(id_type)
            
        except:
            pass
    elif type =="referral":
        try:
            item = UserReferral.objects.get(uuid=chars+chars + u_id)
            u_id = uuid_generator(id_type)
            
        except:
            pass
        chars = "RF"
    elif type =="invest":
        chars = "IV"
        try:
            item = Investment.objects.get(uuid=chars+chars + u_id)
            u_id = uuid_generator(id_type)
            
        except:
            pass
        
    elif type =="recommit":
        chars = "IV"
        try:
            investment = Recommiter.objects.get(uuid=chars+chars + u_id)
            u_id = uuid_generator(id_type)
            
        except:
            pass
    else:
        chars = "XX"
    
    unique_id = chars + u_id
    return(unique_id)

    


    

#  merger function
def merger():
    try:
         recycler()
    except:
        pass
    disabled_users = UserInformation.objects.all().filter(Q(active=False) | Q(blocked=True)).values_list('user', flat=True)

    pledges = Pledge.objects.filter(merged = False).extra(order_by = ['-created_date'])
    
    if pledges:
        due_expectants = Expect.objects.filter(closed = False, due=True, withdraw=True).extra(order_by = ['-created_date']).exclude(investment__user__in=disabled_users)
        if due_expectants:
            data = 2003
            for pledge in pledges:
                item = 0
                
                for item in range(due_expectants.count()):
                    if (due_expectants[item].expect_amount != 0) and (pledge.amount <= due_expectants[item].expect_amount):
                        # if pledge less than or equal to withdraw,
                        # then merge 
                        # merge_timer = timer(1440) #merge timer
                        merge_uuid = uuid_generator("merge")
                        new_merge = MergedData(uuid =merge_uuid ,payer=pledge, pay_to=due_expectants[item], stop_time=timer("merge"))
                        new_merge.save()
                        pledge.merged=True
                        pledge.save()
                        if due_expectants[item].expect_amount >= 0:
                            due_expectants[item].expect_amount -= pledge.amount
                            due_expectants[item].save()
                        
                        else:
                            message = service_message_lookup(1004)
                        data = 2000
                        item = item + 1
                    
                    elif (due_expectants[item].expect_amount != 0) and (pledge.amount > due_expectants[item].expect_amount):
                        # if pledge > withdraw 
                        # create pledge for that amount 
                        # merge the new pledge
                        # reduce amount from pledge 
                        # make the pledge unmerged
                        
                        #create a pledge to that user for that amount
                        # pledge_timer = timer(1440) #plege timer
                        pledge_uuid = uuid_generator("pledge")
                        new_pledge=Pledge(uuid = pledge_uuid,owner=pledge.owner, amount= due_expectants[item].expect_amount, stop_time=timer("pledge"), investment=pledge.investment)
                        new_pledge.merged = True
                        new_pledge.save()
                        #create a merge for the particular transaction
                        merge_uuid = uuid_generator("merge")
                        # merge_timer = timer(1440)
                        new_merge = MergedData(uuid = merge_uuid, payer=new_pledge, pay_to=due_expectants[item], stop_time=timer("merge"))
                        
                        new_merge.save()
                        #update/reduce the amount on the pledge
                        pledge.amount = pledge.amount - due_expectants[item].expect_amount
                        pledge.save()
                        # reduce the amount of the expectant to 0
                        due_expectants[item].expect_amount -= due_expectants[item].expect_amount
                        #close expectant
                        
                        due_expectants[item].save()
                        


                        data = 2000
                        item = item + 1

                    else:
                        
                        item = item + 1
                        # merge_manage(new_merge)
            
        else:
            data = 2002
    else:
        data = 2001
   
    recycler()
    return(data)

# recycle and reshuffle
def recycler():
    trash_merges = MergedData.objects.all().filter(stop_time__lte=timezone.now(), pledger_paid=False)
    print(trash_merges)
    for merge in trash_merges:
        pledge = merge.payer
        pledge.merged = False
        pledger_info = UserInformation.objects.get(user=merge.payer.owner)
        pledger_info.active = False
        pledge.save()
        pledger_info.save()
        expect = merge.pay_to
        expect.expect_amount += pledge.amount
        expect.save()
        merge.disabled=True



# pledge creator
def make_pledge(user,amount, investment):
    active  = is_activated(user)
    # print(active)
    if user:
        if active == 1000:
            user_unpaid_pledges = Pledge.objects.all().filter(owner=user, paid=False)
            print(user_unpaid_pledges)
            if (user_unpaid_pledges.count()) < 1:
                pledge_uuid = uuid_generator("pledge")
                new_pledge=Pledge(uuid = pledge_uuid,owner=user, amount= amount, stop_time=timer("pledge"), investment=investment )
                
                new_pledge.save()
                print(new_pledge)
                data =1000
                print(new_pledge.amount)
               
            else:
                data = 1005 #unpiad merges
        
        elif active == 1001:
            
            data=1001
           

        else:
            data = 1010 #disadled user
    else:
        data = 1004
    print(data)
    return(data)

#check if user is activated
def is_activated(user):
    try:
        user_data = UserInformation.objects.get(user=user)
    except:
        return(1101)
    # unpaid_merges = MergedData.objects.all().filter(payer=user, merger_paid=False)
    level = user_data.level
    active = user_data.active
    if active == True and user_data.blocked == False:
        data = 1000
    elif active == False and user_data.blocked == False:
        # if level >0:
        #     data =  1010
    
        # else:
        #     data = 1001
        data = 1001
    elif active == False and user_data.blocked == True:
        # if level >0:
        #     data =  1010
    
        # else:
        #     data = 1001
        data = 1001
    elif active == True and  user_data.blocked == True:
        data = 1100
    # elif len(unpaid_merges)>0:
    #     data = 1005
    else:
        data = 1001
    print(data)
    return(data)

#set activation function to check if user has an activation pledge if no create if yet say user is in active


#expectant creator
def make_expect(amount, investment):
    
        # expect_timer = timer(1440)            
    expect_uuid = uuid_generator("expect")
    
    profit = 0.4 * amount
    expectant_amount = profit + amount
    new_expectant = Expect(uuid=expect_uuid, amount= amount, expect_amount=expectant_amount, investment=investment,  stop_time=timer("expect")) 
    new_expectant.save()
    data = 1000
    
    return(data)

def get_approved(merge):
    if merge.pledger_paid == True:
        if merge.merger_paid == True:
            merge.closed = True
            closed = 1
            message = "merge completed" #completed merge
        else:
            # ReportToAdmin.objects.create(merged_data=merge)report case to admin
            message = "merge closed" #reported to admin      
    data = [closed, message]
    return(data)      


#referral sorter or creater
# when user is signing up
# get fisrt referral 
# fill user.referral.1st referral with the referral
# get second referral 
# by firstuser.user.referral.1streferral.
# fill second referral
# get third referral by using second referral

def referral_sorter(user, referral_code):
    # create user referralo data
    new_referral_code = uuid_generator("referral")
    #get first user from code
    # first_person = get_first_ref_from_ref_code(referral_code)
    first_person_referral_data = UserReferral.objects.get(referral_code=referral_code)
    first_person = first_person_referral_data.user
    first_person_referral_data.referred += 1
    first_person_referral_data.save()

    #get first user code
        # get referral data from person
    try:
        # first_person_referral_data != None and first_person_referral_data.ref_first != None:
        second_person = first_person_referral_data.ref_first
        second_person_referal_data =  UserReferral.objects.get(user=second_person)
        second_person_referal_data.referred += 1
        second_person_referal_data.save()
        try:
            third_person = second_person_referal_data.ref_first
            third_person_referal_data=  UserReferral.objects.get(user=third_person)
            third_person_referal_data.referred += 1
            third_person_referal_data.save()
        except:
            third_person = None 

    except:
        second_person =None
        third_person = None


    user_referral_data = UserReferral(referral_code=new_referral_code, user=user, ref_first=first_person, ref_second=second_person, ref_third = third_person)
    user_referral_data.save()
    return(user_referral_data)

def make_pledge_activation(user):
    activation_pledge = Pledge.objects.filter(owner=user, pledge_type="AC", paid = False)
    if is_activated(user) == 1001 and len(activation_pledge)==0:
        amount = 1000
        invest_uuid = uuid_generator("invest")
        investment = Investment(user=user, status="PE", amount = amount, amount_left=amount, uuid=invest_uuid)
        investment.save()
        pledge_uuid = uuid_generator("pledge")
        new_pledge=Pledge(uuid = pledge_uuid,owner=user, amount= amount, stop_time=timer("pledge"),investment=investment, pledge_type="AC" )
        new_pledge.save()
    else:
        pass
        print("hi")
    return(1000)


def invest(user, amount):
    #create investment
    #create a pledge for investment
    #user, status, amount, amount-left, recommit amt, recommit paid
    # you have outstanding unpaid merges
    
    active = is_activated(user)
    if active == 1000:
        invest_uuid = uuid_generator("invest")
        investment = Investment(user=user, status="PE", amount = amount, amount_left=amount, recommit_min=int(amount), uuid=invest_uuid)
        investment.save()
        investment_pledge = make_pledge(user, amount, investment)
        print(investment_pledge, "iv")
        
        if investment_pledge == 1000 or investment_pledge == 1001:
            # 
            pass
            
        else:
            investment.delete()
            investment = 1005
            pass
        return(investment)
    elif active == 1001:
        investment_pledge = 1001

    elif active == 1100:
        return(1100)
    else:
        return (1001)

    return(investment_pledge)

def splited_time(time):
    stop_time = time
    
    time = timezone.make_naive(stop_time, timezone=None)
    # print(timezone.is_naive(time))
    month = time.strftime("%b")
    day = time.strftime("%d")
    year = time.strftime("%Y")

    local = time.strftime("%X")
    
    splitted_time = {"mon":month , "day": day, "year":year, "local":local}
    return(splitted_time)

# # when user clicks paid
# def user_paid_merge(merge):
#   merge.paid = True
  #  merge.stop_time = timezone.now()
      


# if investment is completed
# take in user and investment 
# get the referral for user and pay 
# pay first 3%, second 2%, third 1%

def referral_payment(user, investment):
    amount = investment.amount
    data = 100013
    referral_data = UserReferral.objects.get(user=user)
    if referral_data.ref_first != None:
       
        first_person_ref = UserReferral.objects.get(user=referral_data.ref_first)
        first_person_ref.ref_balance += 0.03 * amount
        first_person_ref.save()
        data = 1000
        if referral_data.ref_second != None:
            second_person_ref = UserReferral.objects.get(user=referral_data.ref_second)
            second_person_ref.ref_balance += 0.02 * amount
            second_person_ref.save()
            data = 1000
            if referral_data.ref_third != None:
                third_person_ref = UserReferral.objects.get(user=referral_data.ref_third)
                third_person_ref.ref_balance += 0.01 * amount
                third_person_ref.save()
                data = 1000
    return(data)

#takes in a merge data
#sets pledger paid to true
def pledger_is_paid(uuid):
    merge = MergedData.objects.get(uuid=uuid)
    merge.pledger_paid = True
    merge.stop_time = timezone.now()
    merge.message = "withdraw"
    merge.save()
    return (True)

#if timer runs out
#send to recycler




# if user clicks expectant_approved
# merge_data.paid =True
# merge.close= True






#if expectant approves, payment
def expectant_approved(user,uuid):
    merge = MergedData.objects.get(uuid=uuid)
    payer_info = UserInformation.objects.get(user=merge.payer.owner)
    investment = Investment.objects.get(uuid=merge.payer.investment)
    merge.merger_paid = True
    merge.closed = True
    merge.payer.paid = True
    merge.payer.save()
    merge.save()
    expect = merge.pay_to
    payer = merge.payer
    expect.paid = True  
    if expect.expect_amount == 0:
        expect.closed =True
        expect.save()
       
        if payer_info.level == 3:
            payer_info.blocked = True
            payer_info.save()
    investment.amount_left -= merge.payer.amount
    if investment.amount_left == 0:
        investment.status = 'CO'
        make_expect(investment.amount, investment)
        referral_payment(user, investment)
        if payer.pledge_type == 'AC':
            payer_info.active = True
            payer_user = payer.owner
            payer_info = UserInformation.objects.get(user=payer_user)
            payer_info.level += 1
            payer_info.save()
            
    investment.save()
    return("recommit not successful")


#if user clicks recommit
def make_recommit(user, amount,uuid):
   
    try:
        investment = Investment.objects.get(uuid = uuid)
        # if Recommiter.objects.get(investment = investment)
        if investment.recommiter == None:
            
            rec_investment = invest(user, amount)
            
            print(type(rec_investment))
            if isinstance(rec_investment, Investment):
                print(rec_investment,"pp")
                recommit = Recommiter(investment=rec_investment, amount=amount)
                recommit.save()
                investment.recommiter = recommit
                investment.save()
                data = 4002
            else:
                print("make recommit returned number")
                data = rec_investment
            
        else:
            print("ook")
            data = 4003




    except:
        # rec_investment.delete() 
        data = 4001
        
    
    return(data)
    # pass
    

        
def referral_withdraw(user, amount):
    invest_uuid = uuid_generator("invest")
    investment = Investment(user=user, status="WT", amount = amount, amount_left=amount, uuid=invest_uuid)
    investment.save()
    expect_uuid = uuid_generator("expect")
    new_expect=Expect(uuid = expect_uuid, amount= amount, expect_amount=amount, stop_time=timer("expect"),investment=investment, )
    new_expect.save()
    return(1000)


##check that countdown works for unfinished payment


def create_video_verify(user,link):
    try:
        VideoVerify.objects.get(user=user)
    except:
        verify = VideoVerify(
            user=user,
            link=link,
            stop_time=timer("verify"))
        verify.save()
    return (1000)


def reportmerge(uuid):
    merge = MergedData.objects.get(uuid=uuid)
    merge.report_to_admin=True
    merge.save()
    case = ReportToAdmin(
        uuid=uuid_generator("report"),
        merged_data=merge
    )
    case.save()


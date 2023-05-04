
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cryptobitsapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.userlogin, name="login"),
    path('signup/', views.signup, name="signup"),
    path('updatebal/', views.updatebal, name="updatebal"),
    # path('user_profile/', views.user_profile, name="user_profile"),
    path('updateuserbalance/', views.update_balance, name="update_balance"),
    path('updatefarmbal/', views.updatefarmbal, name="updatefarmbal"),
    path('update-user-farm-balance/', views.update_user_farm_balance, name="update_user_farm_balance"),
    path('get-coin-value/', views.get_coin_value, name="get_coin_value"),
    path('test', views.test, name="test"),



    path('activate/<uidb64>/<token>', views.VerificationView.as_view(), name = "activate"),
    path('logout/', views.userlogout, name="logout"),
     path('profile/logout/', views.userlogout, name="logout"),
     path('dashboard/logout/', views.userlogout, name="logout"),
    path('detail/', views.detail, name="detail"),
    path('signup/', views.signup, name="signup"),
    path('signup-sum/', views.signupsum, name="signup-sum"),
    path('confirm/', views.confirm, name="confirm"),




   


    path('makewithdraw', views.make_withdraw, name="make_withdraw"),
    path('makedeposit', views.make_deposit, name="make_deposit"),
    path('create_user_stock', views.create_user_stock, name="create_user_stock"),
    path('stocksubmit', views.stockSubmit, name="stock_submit"),
    path('update_userdetail', views.update_userdetail, name="update_userdetail"),
    path('update_userwithdrawaldetail', views.update_userwithdrawaldetail, name="update_userwithdrawaldetail"),

    path('update', views.update, name="update"),
    path('investment', views.investment, name="investment"),
    path('wallet/', views.wallet, name="wallet"),
    path('wallet_deposit/', views.wallet_deposit, name="wallet_deposit"),
    path('wallet_withdraw/', views.wallet_withdraw, name="wallet_withdraw"),
    path('wallet_create/', views.wallet_create, name="wallet_create"),
    path('withdraw/', views.withdraw, name="withdraw"),
    path('transactions/', views.transactions, name="transactions"),


    path('deposit/', views.deposit, name="deposit"),
    path('signupextra/', views.signupextra, name="signupextra"),
    path('farming/', views.farming, name="farming"),
    path('fund_transfer/', views.fund_transfer, name="fund_transfer"),
    path('get_stock_defi_value', views.get_stock_defi_value, name="get_stock_defi_value"),
    path('profile/', views.profile, name="profile"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('account-verification/', views.accountVerification, name="account-verification"),
    path('verification/', views.verification, name="verification"),
    path('verify/', views.verify, name="verify"),
    path('passwordchange', views.password_change, name="passwordchange"),
    path('update/', views.update, name="update"),
    path('password/', views.password, name="password"),
    path('packages/', views.packages, name="packages"),
    #superuser pages



    # path('dashboard/', views.dashboard, name="dashboard"),
    path('test/', views.test, name="test"),
    # home urls
    path('', views.index, name=""),
    path('index', views.index, name=""),
    path('index', views.index, name="index"),
    path('location', views.location, name="location"),
    path('govern', views.govern, name="govern"),
    path('account', views.account, name="account"),
    path('product', views.product, name="product"),
    path('cryptocurrency', views.cryptocurrency, name="cryptocurrency"),
    path('regulatory', views.regulatory, name="regulatory"),
    path('real', views.real, name="real"),
    path('dashboard/real', views.real, name="real"),
    path('advice', views.advice, name="advice"),
    path('guidiance', views.guidiance, name="guidiance"),
    path('wealth', views.wealth, name="wealth"),
    path('finplan', views.finplan, name="finplan"),
    path('calculator', views.calculator, name="calculator"),
    path('complimentary', views.complimentary, name="complimentary"),
    path('pricing', views.pricing, name="pricing"),
    path('dashboard/investments', views.investment, name="investments"),
    path('shares', views.shares, name="shares"),
    path('dashboard/shares', views.shares, name="shares"),
    path('stock', views.stock, name="stock"),
    path('dashboard/stock', views.stock, name="stock"),
    path('crypto', views.crypto, name="crypto"),
    path('dashboard/crypto', views.crypto, name="crypto"),
    path('forex', views.forex, name="forex"),
    path('dashboard/forex', views.forex, name="forex"),
    path('realestate', views.restate, name="restate"),
    path('investmentfee', views.investmentfee, name="investmentfee"),
    path('whychoose', views.whychoose, name="whychoose"),
    path('satisfaction', views.satisfaction, name="satisfaction"),
    path('security', views.security, name="security"),
    path('ways', views.ways, name="ways"),
    path('faq', views.faq, name="faq"),
    path('contact', views.contact, name="contact"),
    path('support', views.support, name="support"),
    path('companydetail', views.GetCompanyDetail, name="companydetail"),

    path('about/', views.about, name="about"),
    
    path('terms/', views.terms, name="terms"),
    path('error/', views.error, name="error")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# handler404='forteapp.views.error_404'
# handler500 = 'forteapp.views.error_500'
# handler403='forteapp.views.error_403'
# handler400='forteapp.views.error_400'

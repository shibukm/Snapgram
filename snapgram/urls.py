"""avodhashop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from snapapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('associate',views.associate,name='associate'),
    path('photographer',views.photographer,name='photographer'),
    path('user',views.user,name='user'),
    path('login',views.login,name='login'),
    path('adminHome',views.adminHome,name='adminHome'),
    path('photographerHome',views.photographerHome,name='photographerHome'),
    path('userHome',views.userHome,name='userHome'),
    path('associateHome',views.associateHome,name='associateHome'),
    path('viewphotographers',views.viewphotographers,name='viewphotographers'),
    path('awards',views.awards,name='awards'),
    path('approval',views.approval,name='approval'),
    path('feedback',views.feedback,name='feedback'),
    path('complaint',views.complaint,name='complaint'),
    path('rating',views.rating,name='rating'),
    path('context',views.context,name='context'),
    path('phprofile',views.phprofile,name='phprofile'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('edituserprofile',views.edituserprofile,name='edituserprofile'),
    path('specification',views.specification,name='specification'),
    path('arts',views.arts,name='arts'),
    path('viewarts',views.viewarts,name='viewarts'),
    path('viewsales',views.viewsales,name='viewsales'),
    path('viewuserphotographers',views.viewuserphotographers,name='viewuserphotographers'),
    path('customerreview',views.customerreview,name='customerreview'),
    path('usprofile',views.usprofile,name='usprofile'),
    path('viewfests',views.viewfests,name='viewfests'),
    path('workstatus',views.workstatus,name='workstatus'),
    path('viewdetails',views.viewdetails,name='viewdetails'),
    path('addbooking',views.addbooking,name='addbooking'),
    path('commited',views.commited,name='commited'),
    path('viewwrkstatus',views.viewwrkstatus,name='viewwrkstatus'),
    path('viewbooking',views.viewbooking,name='viewbooking'),
    path('committ',views.committ,name='commit'),
    path('purchase',views.purchase,name='purchase'),
    path('viewbookstatus',views.viewbookstatus,name='viewbookstatus'),
    path('sales',views.sales,name='sales'),
    path('imageupload',views.imageupload,name='imageupload'),
    path('videoupload',views.videoupload,name='videoupload'),
    path('addfeedback',views.addfeedback,name='addfeedback'),
    path('addcomplaint',views.addcomplaint,name='addcomplaint'),
    path('approvegrapher',views.approvegrapher,name='approvegrapher'),
    path('approveassociation',views.approveassociation,name='approveassociation'),
    path('approveuser',views.approveuser,name='approveuser'),
    path('salepayment',views.salepayment,name='salepayment'),
    path('salepayinterface',views.salepayinterface,name='salepayinterface'),
    path('payinterface',views.payinterface,name='payinterface'),
    path('payment',views.payment,name='payment'),
    path('approve',views.approve,name='approve'),
    path('cancel',views.cancel,name='cancel'),
    path('template', views.templates, name='templates'),
    path('forTemplate', views.forTemplate, name='forTemplate'),
    path('viewAlbum', views.viewAlbum, name='viewAlbum'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
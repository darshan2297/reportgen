from django.urls import path
from django.conf.urls import url
from reportapp.views import (
    registerform,homeview,loginview,logoutview,updateview,deleteview,topicview,
    subtopicview,reportview,uprecordview,deleterecview,topicdisplayview,uptopicview,
    deltopicview,generatereport,contactus,aboutus
)
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'reportapp'

urlpatterns = [
    path('',homeview.as_view(),name='home'),
    path('register',registerform.as_view(),name='register'),
    path('login',loginview.as_view(),name='login'),
    path('logout/',logoutview.as_view(),name='logout'),
    path('update',updateview.as_view(),name='update'),
    path('delete',deleteview.as_view(),name='delete'),
    path('topic',topicview.as_view(),name='topic'),
    path('subtopic',subtopicview.as_view(),name='subtopic'),
    path('report',reportview.as_view(),name='report'),
    path('topicdisplay',topicdisplayview.as_view(),name='topicdisplay'),
    path('uptopic/<topicid>/',uptopicview.as_view(),name='uptopic'),
    path('deltopic/<topicid>/',deltopicview.as_view(),name='deltopic'),
    path('uprecord/<subtopicid>/',uprecordview.as_view(),name='uprecord'),
    path('deleterec/<delsubtopicid>/',deleterecview.as_view(),name='deleterec'),
    path('generatereport',generatereport.as_view(),name='generatereport'),
    path('contactus',contactus.as_view(),name='contactus'),
    path('aboutus',aboutus.as_view(),name='aboutus'),
    #Password Changed
    path('changepassword',
        auth_views.PasswordChangeView.as_view(template_name='change-password.html',
        success_url='changepassword/done'),
        name='changepassword'),
    path('changepassword/done',
        auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),
        name='change-password-done'),
    
    #Password Reset
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password-reset/password_reset.html',
             subject_template_name='password-reset/password_reset_subject.txt',
             email_template_name='password-reset/password_reset_email.html',
             
             success_url = reverse_lazy('reportapp:password_reset_done')
         ),
         name='password_reset'),
    
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
             template_name='password-reset/password_reset_done.html'
        ),
        name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password-reset/password_reset_confirm.html',
             success_url = reverse_lazy('reportapp:password_reset_complete')
         ),
         name='password_reset_confirm'),
    
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

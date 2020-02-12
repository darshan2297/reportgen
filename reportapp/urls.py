from django.urls import path
from django.conf.urls import url
from reportapp.views import registerform,homeview,loginview,logoutview,updateview,deleteview,topicview,subtopicview,reportview,uprecordview,deleterecview,topicdisplayview,uptopicview,deltopicview,generatereport,contactus,aboutus
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
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
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

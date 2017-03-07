from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic import TemplateView
from .views import vista_registro

urlpatterns = [
    url(r'^logout/$', auth_views.logout,{'template_name':'myapp/logout.html'},name='logout'),
    url(r'^registro/$', vista_registro , name= 'registro'),
    url(r'^login/$', auth_views.login,{'template_name':'myapp/login.html'}, name='login'),
    url(r'^perfil/$',TemplateView.as_view(template_name="myapp/profile.html"), name='perfil')
]

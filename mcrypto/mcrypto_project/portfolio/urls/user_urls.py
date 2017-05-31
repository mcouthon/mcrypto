from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views


user_urlpatterns = [
    url(r'^login/$', auth_views.login,
        kwargs={'template_name': 'portfolio/users/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout_then_login,
        kwargs={'login_url': 'portfolio:login'}, name='logout'),
    url(r'^admin/', admin.site.urls),
]

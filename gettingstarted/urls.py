from django.conf.urls import include, url
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
app_name='facebook'
urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
	url(r'^accounts/profile/#_=_', hello.views.facebook , name='facebook'),
	url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]

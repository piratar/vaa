"""vaa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from vaa.questions import views as vaav

urlpatterns = [
    url(r'^userpage/$', vaav.userpage),
    url(r'^$', vaav.home),
    url(r'^userupdate/', vaav.userupdate),
    url(r'^candans/', vaav.candreply),
    url(r'^candanswer/', vaav.candanswer),
    url(r'^voterform/', vaav.voterform),
    url(r'^compare/', vaav.compare),
    url(r'^candidate/(?P<pk>\d+)/', vaav.candidate_page),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
#    url(r'^claim/(?P<key>[a-zA-Z\.\!])/$', vaav.claim),

    url(r'^admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
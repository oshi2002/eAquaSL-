"""
URL configuration for eaqua project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'),
         name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'),
         name='contact'),
    path('apply-license/', TemplateView.as_view(template_name='apply_license.html'),
         name='applylicense'),
    path('accounts/', include('accounts.urls')),
    path('apply-license-form/', TemplateView.as_view(template_name='apply_license_form.html'),
         name='applylicenseform'),
    path('aquaculture/', include('aquaculture.urls')),
    path('diseases/', TemplateView.as_view(template_name='user_diseases.html'),
         name='diseases'),
    path('aquaculture/', include(('aquaculture.urls',
         'aquaculture'), namespace='aquaculture')),
    path('news/', TemplateView.as_view(template_name='news.html'),
         name='news'),
]

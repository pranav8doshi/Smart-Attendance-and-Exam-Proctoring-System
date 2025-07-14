from django.contrib import admin
from django.urls import path, include, re_path
from . import views
import authentication.views_authentication as views_a
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('testlink', views.testlink),
    path('receivedata', views.receivedata),
    path('', views.landingView, name='landing'),
    path('login/', views_a.LoginView, name='login'),
    path('FAQs', views.FAQsView, name='faqs'),
    path('home', views.homeView, name='home'),
    path('about', views.aboutView, name='about'),
    path('user-manual', views.showLinksView, name='user-manual'),
    path('blood-dc/', views.bloodDonationExtraView, name='blood-D-live-count'),
    path('blood-d/', views.bloodDonationView, name='blood-D-live-countc'),
    # path('blood-d/blood-donor-count/', views.blood_donor_count, name='blood-donor-count'),
    path('admin/', admin.site.urls),
    path('action/', include('action.urls')),
    path('a/', include('authentication.urls')),
    path('v/', include('Volunteer.urls')),
    path('c/', include('Coordinator.urls')),
    path('s/', include('Secretary.urls')),
    re_path(r'^500/$', views.custom_500_error_view, name='custom_500_error'),
]
handler404 = 'SWDCWebsite.views.custom_404'

if settings.DEBUG:
    pass
else:
    urlpatterns += staticfiles_urlpatterns()
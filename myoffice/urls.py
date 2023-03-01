from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import contact

urlpatterns = [
      path('admin/', admin.site.urls),
      path('contact/', contact.contact, name='contact'),
      path(
            'admin/password_reset/',
            auth_views.PasswordResetView.as_view(),
            name='admin_password_reset'
      ),
      path(
           'admin/password_reset/done/',
           auth_views.PasswordResetView.as_view(),
           name='password_reset_done',
      ),
      path(
            'reset/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(),
            name='password_reset_confirm',
      ),
      path(
            'reset/done/',
            auth_views.PasswordResetCompleteView.as_view(),
            name='password_reset_complete',
      ),
      path('', include('events.urls')),
      path('snslaw/', include('snslaw.urls')),
      # path('', include('snslaw.urls')),

]





from django.urls import path
from . import views
# from .views import PublisherDetailView, PublisherListView
# from django.urls import path
# from books.views import PublisherListView
#
# urlpatterns = [
#     path('publishers/', PublisherListView.as_view()),
# ]

app_name = 'snslaw'

urlpatterns = [path('', views.index, name='snsindex'),
               path('multi/', views.calculate, name='multi'),
               path('add_record/', views.addrecord, name='addrecord'),
               path('mynewfile/', views.mynewfile, name='mnf'),
               path('show_clients/', views.show_clients, name='show'),
               path('delete_record/<int:id>', views.delete_record, name='delete_record'),
               path('addfile/<int:id>', views.addfile, name='addfile'),
               path('tadfile/<int:id>', views.tadfile, name='tadfile'),
               path('mytest1/', views.mytest1, name='mytest1'),
               # path('mytest/', views.mytest, name='mytest'),
               path('newfile/<int:id>', views.newfile, name='newfile'),
               path('show_clients/update/<int:id>', views.update, name='update'),
               path('show_clients/client_detail/<int:id>', views.client_detail, name='detail'),
               path('show_clients/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
               path('calc_input/', views.calc_input, name='calc_input'),
               ]

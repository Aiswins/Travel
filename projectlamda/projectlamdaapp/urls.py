from django.urls import path
from . import views
# # urlpatterns=[
# #     # path('',views.demo,name='demo'),
# #     # path('home',views.home,name='ho'),
# #     # path('about',views.about,name='ho'),
# #     # path('contact',views.contact,name='ho'),
# #     #
# #     # path('details', views.details, name='ho'),
# #     # path('thanks', views.thanks, name='ho'),
# #
# #     path('',views.math ,name='math'),
# #     path('math1/',views.math1,name="math"),
#
# ]
urlpatterns = [
    path('',views.demo,name='demo'),
]
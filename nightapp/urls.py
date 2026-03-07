from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('ngungon1',views.ngungon1,name='ngu ngon 1'),
    path('ngungon2',views.ngungon2,name='ngu ngon 2'),
    path('ngungon3',views.ngungon3,name='ngu ngon 3'),
    path('ngungon4',views.ngungon4,name='ngu ngon 4'),
    path('ngungon5',views.ngungon5,name='ngu ngon 5'),
    path('ngungon6',views.ngungon6,name='ngu ngon 6'),
    path('ngungon7',views.ngungon7,name='ngu ngon 7'),
    path('8-3',views.ngungon_8_3,name='8-3'),
    path('login/',views.login_view,name='login'),
]
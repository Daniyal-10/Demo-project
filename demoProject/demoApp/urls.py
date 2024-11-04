from demoApp.views import * 
from django.urls import path
# importing this to use the buildin view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('employee/<int:pk>/', employee),
    path('employee/', employee),
    path('students/', students),
    path('person/', person),
    path('user/', user),
    path('login/', signin),
    path('logout/', signout),
    path('employee2/', employee2),
    path('customer/', customer),
    path('login123/', LoginAPI.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]
from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('Login/',views.Login_Request_Handler,name="login"),
    path('Signup/',views.Signup_Request_Handler,name="signup"),
    path('Logout/',views.Logout_Request_Hanlder,name="logout"),
    path('Reset/',views.Rest_Password_Request_Handler,name="reset"),
    path('ResetPass/<str:uid>/<str:token>',views.Valid_Reset_Password_Hequest_Handler,name="resetpass"),
    path('Vaild/<str:uid>/<str:token>',views.Valid_Email_Request_Handler,name="valid")
]+staticfiles_urlpatterns()

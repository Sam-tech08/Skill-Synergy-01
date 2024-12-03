from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.homepage, name='home'),
    path('chatbot/',views.chatbot,name='chatbot'),
    path('login/',LoginView.as_view(template_name='app/login.html'),name='login'),
    path('logout/',LogoutView.as_view(next_page='home'),name='logout'),
    path('chatpage/',views.chatpage,name='Chatpage'),
    path('technews/',views.technews,name= 'technews'),
    path('mentor/',views.mentor,name='mentor'),
    path('about/',views.about,name='about'),
]





# from django.urls import path, include
# from chat import views as chat_views
# from django.contrib.auth.views import LoginView, LogoutView


# urlpatterns = [
#     path("", chat_views.chatPage, name="chat-page"),

#     # login-section
#     path("auth/login/", LoginView.as_view
#          (template_name="chat/LoginPage.html"), name="login-user"),
#     path("auth/logout/", LogoutView.as_view(), name="logout-user"),
# ]
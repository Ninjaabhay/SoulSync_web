# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='home'),  # Home page
#     path('chatroom/', views.chatroom, name='chatroom'),  # Chatroom page
#     path('get-chatbot-response/', views.get_chatbot_response,
#          name='get_chatbot_response'),  # Chatbot API
# ]
from django.urls import path
from my_app.views import index, chatroom, get_chatbot_response

urlpatterns = [
    path('', index, name='index'),
    path('chatroom/', chatroom, name='chatroom'),
    path('get-response/', get_chatbot_response, name='get_chatbot_response'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedbackListAPIView.as_view(), name="feedbacks"),
    path('<int:id>', views.FeedbackDetailAPIView.as_view(), name="feedback"),
]
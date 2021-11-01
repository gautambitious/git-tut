from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.SaveTaskView.as_view(), name='home'),
    path('get/<int:user_id>', view=views.GetTaskView.as_view(), name='home'),
]
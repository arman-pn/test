from django.urls import path
from Time.views import UserView, ProjectView, TimeEntiryView, UserDetail, ProjectsDetail, TimeEntiryDetail, \
    DeviceAuthView

urlpatterns = [
    path('auth/device/', DeviceAuthView.as_view(), name='device-auth'),
    path('userview/',UserView.as_view()),
    path('projectview/',ProjectView.as_view()),
    path('TimeEntiryView/',TimeEntiryView.as_view()),
    path('userview/<int:pk>/',UserDetail.as_view()),
    path('projectview/<int:pk>/',ProjectsDetail.as_view()),
    path('TimeEntiryView/<int:pk>/',TimeEntiryDetail.as_view()),
]
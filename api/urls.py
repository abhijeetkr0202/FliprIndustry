from django.urls import include,path
from .import views



urlpatterns=[
    path('list/',views.DataView.as_view()),
    path('list/<int:pk>/info/',views.UserView.as_view()),
    path('list/export/',views.UserCSVexportView.as_view()),
]
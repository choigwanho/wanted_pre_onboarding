from django.urls import path
from . import views

app_name = 'recruitments'
urlpatterns = [
    # /recruitments/
    path('', views.index, name='index'),

    # /recruitments/create/
    path('create/', views.recruitment_create, name='recruitment_create'),

    # /recruitments/3/update/
    path('<int:recruitment_id>/update/', views.recruitment_update, name="recruitment_update"),

    # /recruitments/1/delete/
    path('<int:recruitment_id>/delete', views.recruitment_delete, name="recruitment_delete"),

    # /recruitments/search/
    path('search/', views.search, name='recruitment_search'),
]
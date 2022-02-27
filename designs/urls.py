# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path

# Internal:
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('', views.designs, name="designs"),
    path('<int:mockup_id>/', views.design_mockup, name="design_mockup"),
    path('add/', views.add_mockup, name="add_mockup"),
    path('edit/<int:mockup_id>/', views.edit_mockup, name="edit_mockup"),
    path('delete/<int:mockup_id>/', views.delete_mockup, name="delete_mockup"),
]

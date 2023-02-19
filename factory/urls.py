from django.urls import path

from factory import views

urlpatterns = [
    path('', views.FactoryListView.as_view()),
    path('<int:pk>/', views.FactoryDetailView.as_view()),
    path('create/', views.FactoryCreateView.as_view()),
    path('<int:pk>/update/', views.FactoryUpdateView.as_view()),
    path('<int:pk>/delete/', views.FactoryDeleteView.as_view()),
    path('products/', views.ProductsListView.as_view()),
]

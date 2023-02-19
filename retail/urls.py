from django.urls import path

from retail import views

urlpatterns = [
    path('', views.ContractorListView.as_view()),
    path('<int:pk>/', views.ContractorDetailView.as_view()),
    path('create/', views.ContractorCreateView.as_view()),
    path('<int:pk>/update/', views.ContractorUpdateView.as_view()),
    path('<int:pk>/delete/', views.ContractorDeleteView.as_view()),
    path('retail/', views.RetailListView.as_view()),
    path('seller/', views.SellerListView.as_view()),
]

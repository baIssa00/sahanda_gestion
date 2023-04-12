from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    # Authentification
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    
    # URLs for Commission views
    path('commissions/', CommissionListView.as_view(), name='commissions'),
    path('commissions/<int:pk>/', CommissionDetailView.as_view(), name='commission_detail'),
    path('commissions/create/', CommissionCreateView.as_view(), name='commission_create'),
    path('commissions/<int:pk>/update/', CommissionUpdateView.as_view(), name='commission_update'),
    path('commissions/<int:pk>/delete/', CommissionDeleteView.as_view(), name='commission_delete'),
    
    # URLs for Member views
    path('membres/', MembreListView.as_view(), name='membres'),
    path('membres/<int:pk>/', MembreDetailView.as_view(), name='membre_detail'),
    path('membres/create/', MembreCreateView.as_view(), name='membre_create'),
    path('membres/<int:pk>/update/', MembreUpdateView.as_view(), name='membre_update'),
    path('membres/<int:pk>/delete/', MembreDeleteView.as_view(), name='membre_delete'),
    
    # URLs for Cotisation views
    path('cotisations/types/', CotisationParTypeView.as_view(), name='cotisations_par_types'),
    path('types-cotisations/', TypeCotisationListView.as_view(), name='types_cotisations'),
    path('cotisations/', CotisationListView.as_view(), name='cotisations'),
    path('cotisation/create/', CotisationCreateView.as_view(), name='cotisation_create'),
    
    # URL for home page
    path('', home, name='home'),
    
    # generer pdf 
    path('generer-pdf/', ListeMembresPDFView.as_view(), name='generer_pdf')
]
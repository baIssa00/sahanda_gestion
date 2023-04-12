from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from sahanda_app.models import Commission, Membre, Cotisation, TypeCotisation,Cellule
from sahanda_app.forms import CotisationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
# generer le pdf
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View



# Accueil 
def home(request):
    return render(request, 'home.html')

# Authentification
class SignupView(FormView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class LogoutView(LogoutView):
    template_name = 'registration/logout.html'
    next_page = 'home'

# Commissions 
class CommissionListView(LoginRequiredMixin, ListView):
    model = Commission
    context_object_name = 'commissions'
    template_name = 'commissions/commission_list.html'


class CommissionDetailView(LoginRequiredMixin, DetailView):
    model = Commission
    context_object_name = 'commission'
    template_name = 'commissions/commission_detail.html'


class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    fields = ['nom', 'cellule', 'responsable', 'description']
    template_name = 'commissions/commission_form.html'
    success_url = reverse_lazy('commissions')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cellules'] = Cellule.objects.all()
        context['membres'] = Membre.objects.all()
        return context


class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    fields = ['nom', 'cellule', 'responsable', 'description']
    template_name = 'commissions/commission_form.html'
    success_url = reverse_lazy('commissions')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cellules'] = Cellule.objects.all()
        context['membres'] = Membre.objects.all()
        return context


class CommissionDeleteView(LoginRequiredMixin, DeleteView):
    model = Commission
    context_object_name = 'commission'
    template_name = 'commissions/commission_confirm_delete.html'
    success_url = reverse_lazy('commissions')



# Membres 
class MembreListView(LoginRequiredMixin, ListView):
    model = Membre
    context_object_name = 'membres'
    template_name = 'membres/membre_list.html'

class MembreDetailView(LoginRequiredMixin, DetailView):
    model = Membre
    context_object_name = 'membre'
    template_name = 'membres/membre_detail.html'

class MembreCreateView(LoginRequiredMixin, CreateView):
    model = Membre
    fields = ['nom', 'prenom', 'cellule', 'telephone', 'commission']
    template_name = 'membres/membre_form.html'
    success_url = reverse_lazy('membres')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cellules'] = Cellule.objects.all()
        context['commissions'] = Commission.objects.all()
        return context


class MembreUpdateView(LoginRequiredMixin, UpdateView):
    model = Membre
    fields = ['nom', 'prenom', 'cellule', 'telephone', 'commission']
    template_name = 'membres/membre_form.html'
    success_url = reverse_lazy('membres')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cellules'] = Cellule.objects.all()
        context['commissions'] = Commission.objects.all()
        return context


class MembreDeleteView(LoginRequiredMixin, DeleteView):
    model = Membre
    context_object_name = 'membre'
    template_name = 'membres/membre_confirm_delete.html'
    success_url = reverse_lazy('membres')


# Type de cotisations
class TypeCotisationListView(LoginRequiredMixin, ListView):
    model = TypeCotisation
    context_object_name = 'types_cotisations'
    template_name = 'cotisations/type_cotisation_list.html'


# Cotisation Par types
class CotisationParTypeView(TemplateView):
    template_name = 'cotisations/cotisation_par_type.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cotisations = Cotisation.objects.values('type_cotisation').annotate(total=Sum('montant'))
        context['cotisations'] = cotisations
        return context

# Cotisations
class CotisationListView(LoginRequiredMixin, ListView):
    model = Cotisation
    context_object_name = 'cotisations'
    template_name = 'cotisations/cotisation_list.html'


class CotisationCreateView(LoginRequiredMixin, CreateView):
    model = Cotisation
    fields = ['membre', 'montant','type_cotisation']
    template_name = 'cotisations/cotisation_form.html'
    success_url = reverse_lazy('cotisations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['membres'] = Membre.objects.all()
        context['types_cotisations'] = TypeCotisation.objects.all()
        return context


# generer le pdf
class ListeMembresPDFView(View):
    def get(self, request):
        membres = Membre.objects.all()

        # Création du PDF
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)

        # Création du template
        template = get_template('membres/membre_list.html')
        context = {'membres': membres}
        html = template.render(context)

        # Génération du PDF
        pdf.setTitle("Liste des membres")
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(230, 800, "Liste des membres")

        # Ajout des bordures de tableau
        x_start = 50
        x_end = 550
        y_start = 750
        y_end = 700 - (50 * len(membres))  # Calcule la position y de la dernière ligne
        pdf.rect(x_start, y_start, x_end - x_start, y_start - y_end, stroke=1, fill=0)

        # Ajout des en-têtes de colonnes
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(70, y_start - 20, "Prénom")
        pdf.drawString(170, y_start - 20, "Nom")
        pdf.drawString(270, y_start - 20, "Téléphone")
        pdf.drawString(370, y_start - 20, "Cellule")
        pdf.drawString(470, y_start - 20, "Commission")

        y = y_start - 40
        for membre in membres:
            pdf.setFont("Helvetica", 11)
            pdf.drawString(70, y, membre.prenom)
            pdf.drawString(170, y, membre.nom)
            pdf.drawString(270, y, membre.telephone if membre.telephone else "Pas de téléphone")
            pdf.drawString(370, y, membre.cellule.nom.encode('utf-8').decode('utf-8')) # Convertir l'objet Cellule en chaîne de caractères
            pdf.drawString(470, y, membre.commission.nom.encode('utf-8').decode('utf-8') if membre.commission else "Pas de commission")
            y -= 50

        pdf.showPage()
        pdf.save()

        # Renvoi du PDF
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="liste_membres.pdf"'
        return response

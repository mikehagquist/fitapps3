from django.views.generic import TemplateView, FormView
from pages.forms import ContactForm
from django.http import HttpResponseRedirect


class HomeView(TemplateView):
    template_name = 'pages/home.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class SugarcutzView(TemplateView):
    template_name = 'pages/sugarcutz.html'


class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        if form.is_valid():
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            z = x + y
            print(z)
            # form.save()
            return HttpResponseRedirect('/contact')

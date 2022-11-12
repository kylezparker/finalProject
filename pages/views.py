from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name="pages/home.html"

class AboutPageView(TemplateView):
    template_name="pages/about.html"

class tosView(TemplateView):
    template_name="pages/termsofservice.html"
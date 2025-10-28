from django.views.generic import TemplateView


class RegisterPageView(TemplateView):
    template_name = "account_templates/register.html"


class LoginPageView(TemplateView):
    template_name = "account_templates/login.html"


class ProfilePageView(TemplateView):
    template_name = "account_templates/profile.html"


class NotesPageView(TemplateView):
    template_name = "account_templates/notes.html"

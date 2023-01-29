from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings

class HomeTemplateView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        name = request.POST.get("name")
        name = request.POST.get("email")
        name = request.POST.get("message")

        email = EmailMessage(
            subject= f"{name} from Hounds Hotel.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("Email sent successfully")

class AppointmemntTemplateView(TemplateView):
    template_name = "index.html"        

from django.conf import settings
from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import Testimonial
from .forms import ContactForm

from service.models import Service

send_email = getattr(settings, "SEND_MAIL", False)

# Home View
def home_view(request):
    services = Service.objects.all()[:5]  # Get first 5 services
    testimonials = Testimonial.objects.all()[:5]  # Get first 5 testimonials
    return render(request, "base/index.html", {
        "services": services,
        "testimonials": testimonials,
    })

# About View
def about_view(request):
    return render(request, "base/about_me.html")


# Testimonial List View
class TestimonialListView(ListView):
    paginate_by = 1
    model = Testimonial
    template_name = "base/testimonials.html"
    context_object_name = "testimonials"
    ordering = ["-created_at"]  # Show latest testimonials first


# Send Message View
def contact_me_view(request):
    if request.method == "POST":
        _data = request.POST  # Get the POST data from the request
        data = {
            "name": _data.get("name"),
            "email": _data.get("email"),
            "subject": _data.get("subject"),
            "phone_number": _data.get("phone_number"),
            "message": _data.get("message"),
        }
        
        form = ContactForm(data)
        
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            
            subject = f"New Message from {name}"
            full_message = f"From: {name} ({email})\n\nPhone: ({phone_number}) \n\n{message}"

            success = send_email(subject, full_message, settings.EMAIL_HOST_USER, "jajjamumalansonga2@gmail.com") 

            if success:
                messages.success(request, "Your message has been sent successfully!")
            else:
                messages.error(request, "Failed to send your message. Please try again.")

            return redirect("contact_me")
        else:
            messages.error(request, "Failed to send your message. Please try again.")
            form = ContactForm()

    else:
        form = ContactForm()

    return render(request, "base/contact.html", {"form": form})


def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)


def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect("/admin") 
    
    if request.method == "POST":
        email = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        
        if not email.startswith("admin"):
            messages.error(request, "Invalid email or password")
            return render(request, 'auth/login.html')
        
        if user is not None:
            login(request, user)
            request.session.set_expiry(900)  # Set session expiry to 15 minutes (900 seconds)
            messages.success(request, "Login successful.")
            return redirect("/admin")
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, 'auth/login.html')
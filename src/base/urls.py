from django.urls import path
from .views import (
    login_view,
    home_view,
    about_view,
    contact_me_view,
    TestimonialListView,
)

urlpatterns = [
    # Home page
    path("", home_view, name="home"),

    # About page
    path("about-me/", about_view, name="about_me"),

    # Testimonial list and detail views
    path("testimonials/", TestimonialListView.as_view(), name="testimonials"),

    # Send message view
    path("contact-me/", contact_me_view, name="contact_me"),
    
    path("login/", login_view, name="login"),
]

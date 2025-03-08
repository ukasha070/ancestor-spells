from django.db import models

class Testimonial(models.Model):
    patient_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True, default='images/default.jpg')
    message = models.TextField()
    rating = models.PositiveIntegerField(default=5)  # 1 to 5 stars
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimonial from {self.patient_name}"
  

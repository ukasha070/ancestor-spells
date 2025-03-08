from django.core.mail import send_mail


def send_email_(subject: str, message: str, sender_email: str, recipient_email: str):
    """
    Sends an email using Django's email backend.
    
    :param subject: Email subject
    :param message: Email body
    :param sender_email: Sender's email address
    :param recipient_email: Recipient's email address
    :return: Boolean indicating success or failure
    """
    try:
        send_mail(
            subject,
            message,
            sender_email,  # From user
            [recipient_email],  # To admin/recipient
            fail_silently=True,
        )
        return True
    except Exception as e:
        print(f"Error sending email: {e}")  # Log error (replace with logging in production)
        return False




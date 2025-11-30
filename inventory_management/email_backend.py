import ssl
from django.core.mail.backends.smtp import EmailBackend

class CustomEmailBackend(EmailBackend):
    def open(self):
        # bypass SSL certificate verification
        self.ssl_context = ssl._create_unverified_context()
        return super().open()

import ssl
import certifi
from django.core.mail.backends.smtp import EmailBackend

class CustomBrevoEmailBackend(EmailBackend):
    def open(self):
        # Use certificate from certifi
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())
        return super().open()

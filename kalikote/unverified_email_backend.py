import ssl
from django.core.mail.backends.smtp import EmailBackend

class UnverifiedEmailBackend(EmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ssl_context = ssl._create_unverified_context()

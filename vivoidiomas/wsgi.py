"""
WSGI config for vivoidiomas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
 
# Adicione esta importação
from django.conf import settings
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vivoidiomas.settings')
 
# A linha original é esta:
# application = get_wsgi_application()
 
# Vamos substituí-la por um código mais inteligente:
base_application = get_wsgi_application()
 
# Somente em modo de produção (DEBUG=False), o WhiteNoise assume
if not settings.DEBUG:
    from whitenoise import WhiteNoise
    # O WhiteNoise servirá os arquivos da pasta STATIC_ROOT (como já fazia)
    application = WhiteNoise(base_application, root=settings.STATIC_ROOT)
    # E também servirá os arquivos da pasta MEDIA_ROOT
    application.add_files(settings.MEDIA_ROOT, prefix=settings.MEDIA_URL)
else:
    application = base_application
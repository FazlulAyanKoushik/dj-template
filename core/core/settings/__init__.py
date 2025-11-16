import os
from django.core.exceptions import ImproperlyConfigured

# Determine which settings module to use
ENVIRONMENT = os.environ.get('DJANGO_ENV', 'local').lower()

if ENVIRONMENT == 'production' or ENVIRONMENT == 'prod':
    from .prod import *
elif ENVIRONMENT == 'development' or ENVIRONMENT == 'dev':
    from .dev import *
else:
    from .local import *


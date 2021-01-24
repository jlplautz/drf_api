# drf_api
Thus pri=oject os based on RiverFount project

# Link youtube
  - https://www.youtube.com/watch?v=ijmxLyEcvpE

# Install lib djangorestframework
  - pip install djangorestframework
  - pip freeze > requirements.txt

# create a new app drf
  - (.venv) vmtodo $ mng startapp drf

# insert INSTALLED_APPS 
  - 'rest_framework',
  - 'vmtodo.drf',

# Verify file settings.py Middleware
  -  comentado pois este estabelece o CSRF dos formularios para api drf não precisa comentar
  -  <h2>'django.middleware.csrf.CsrfViewMiddleware', </h2>

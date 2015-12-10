import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASE_PASSWORD = 'my_database_password'   # database password
DATABASE_HOST = 'my_database_host.someplace.com'   # database host name
DATABASE_NAME = 'mydatabase'  # database name
DATABASE_PORT = 5432  # database port, 5432 is the default port for postgresql
DATABASE_USER = 'my_user_name'  # database user name

SECRET_KEY = '7smwoocv9wqkf047affaddapxjfioopasdp83aqnfd87andek'  # randomly generated sequence

DEBUG_MODE = 'TRUE'  # Generally TRUE for development and FALSE for production environments
TEMPLATE_DEBUG_MODE = 'TRUE'  # Generally TRUE for development and FALSE for production environments
ALLOWED_HOSTS = ''  # Allowed hosts can be empty string for development, but needs values for production
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Path to the media root directory

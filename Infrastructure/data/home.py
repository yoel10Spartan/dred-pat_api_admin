from Infrastructure.data.settings import DataBaseSQL
from Resources.config.environment import get_settings
from Infrastructure.data.models import users

_SETTINGS = get_settings()

user = DataBaseSQL(_SETTINGS.DATABASE_PG_URL_USER, users.Base)
OpenConectionUSER = user.start()
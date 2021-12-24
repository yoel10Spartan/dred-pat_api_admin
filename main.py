import uvicorn
from API.app import init_app
from Resources.config.environment import get_settings

_SETTINGS = get_settings()

app = init_app(_SETTINGS)

def start(path_run: str):
    uvicorn.run(
        path_run,
        host=_SETTINGS.WEB_SERVER_HOST,
        port=_SETTINGS.WEB_SERVER_PORT,
        reload=_SETTINGS.WEB_SERVER_RELOAD
    )

if __name__ == '__main__':
    start('main:app')


# mysql+pymysql://doadmin:QMuBzqreK5bYT0CT@db-mysql-nyc3-38204-do-user-10265239-0.b.db.ondigitalocean.com:25060/user
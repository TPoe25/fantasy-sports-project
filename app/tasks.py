from celery import Celery
from config import Config
import app.services.nba_service as nba
import app.services.mlb_service as mlb
import app.services.nfl_service as nfl

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
celery.conf.result_backend = Config.CELERY_RESULT_BACKEND

@celery.task
def refresh_all_data():
    nba.get_latest_nba_stats()
    mlb.get_mlb_team_stats()
    nfl.get_nfl_data()
    return "Data refreshed successfully!"

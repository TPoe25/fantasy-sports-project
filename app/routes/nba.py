from flask import Blueprint, jsonify
from app.services.nba_service import get_latest_nba_stats

bp = Blueprint("nba", __name__, url_prefix="/api/nba")

@bp.route("/players", methods=["GET"])
def players():
    data = get_latest_nba_stats()
    return jsonify(data)

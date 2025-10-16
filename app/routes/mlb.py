from flask import Blueprint, jsonify
from app.services.mlb_service import get_mlb_team_stats

bp = Blueprint("mlb", __name__, url_prefix="/api/mlb")

@bp.route("/teams", methods=["GET"])
def teams():
    data = get_mlb_team_stats()
    return jsonify(data)

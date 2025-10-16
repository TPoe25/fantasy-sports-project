from flask import Blueprint, jsonify
from app.services.nfl_service import get_nfl_data

bp = Blueprint("nfl", __name__, url_prefix="/api/nfl")

@bp.route("/teams", methods=["GET"])
def teams():
    data = get_nfl_data()
    return jsonify(data)

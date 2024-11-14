from flask import Blueprint, jsonify

bp = Blueprint('other_endpoints', __name__)

@bp.route('/usage/summary', methods=['GET'])
def usage_summary():
    # Retrieve usage summary here
    summary = {"total_sessions": 500, "average_duration": 15}
    return jsonify(summary)

@bp.route('/users/segments', methods=['GET'])
def user_segments():
    # Retrieve user segmentation data here
    segments = {"students": 150, "business": 200, "patients": 50}
    return jsonify(segments)

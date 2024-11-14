from flask import Blueprint, jsonify

bp = Blueprint('summary', __name__, url_prefix='/feedback')

@bp.route('/summary', methods=['GET'])
def feedback_summary():
    # Retrieve and summarize feedback data here
    summary = {"average_satisfaction": 4.5, "total_interactions": 100}
    return jsonify(summary)

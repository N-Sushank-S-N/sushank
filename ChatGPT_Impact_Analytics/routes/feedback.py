from flask import Blueprint, request, jsonify

bp = Blueprint('feedback', __name__, url_prefix='/feedback')

@bp.route('/submit', methods=['POST'])
def submit_feedback():
    data = request.json
    # Process the feedback data here
    return jsonify({"status": "Feedback submitted", "data": data})

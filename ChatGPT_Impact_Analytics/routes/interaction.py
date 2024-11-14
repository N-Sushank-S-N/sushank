from flask import Blueprint, request, jsonify

bp = Blueprint('interaction', __name__, url_prefix='/interaction')

@bp.route('/log', methods=['POST'])
def log_interaction():
    data = request.json
    # Process the interaction data here
    return jsonify({"status": "Interaction logged", "data": data})

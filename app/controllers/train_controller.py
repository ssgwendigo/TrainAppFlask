from flask import Blueprint, jsonify
from app.helpers.wmata_helper import WMATAHelper

train_bp = Blueprint('train', __name__)


@train_bp.route('/nextTrains/<stationCodes>', methods=['GET'])
@train_bp.route('/nextTrains', methods=['GET'])
def get_next_trains(stationCodes=None):
    helper = WMATAHelper()

    if not stationCodes:
        return jsonify({"error": "Station codes required"}), 400

    # WMATA API only supports one station at a time
    # So we'll just use the first code if multiple are provided
    first_code = stationCodes.split(',')[0]

    response = helper.make_request(f'StationPrediction.svc/json/GetPrediction/{first_code}')
    if not response or 'Trains' not in response:
        return jsonify({"error": "Failed to fetch predictions"}), 500

    return jsonify({
        "station_code": first_code,
        "predictions": response['Trains']
    })
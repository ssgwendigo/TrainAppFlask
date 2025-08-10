from flask import Blueprint, jsonify, request
from app.helpers.wmata_helper import WMATAHelper

station_bp = Blueprint('station', __name__)


@station_bp.route('/apihelpertest', methods=['GET'])
def validate_key():
    helper = WMATAHelper()
    is_valid = helper.validate_api_key()
    return jsonify({"valid": is_valid})


@station_bp.route('/stationList', methods=['GET'])
def get_station_list():
    helper = WMATAHelper()
    line_color = request.args.get('line', '').upper()

    response = helper.make_request('Rail.svc/json/jStations')
    if not response or 'Stations' not in response:
        return jsonify({"error": "Failed to fetch stations"}), 500

    stations = response['Stations']
    if line_color:
        stations = [s for s in stations if line_color in [
            s.get(f'LineCode{i}', '') for i in range(1, 5)
        ]]

    return jsonify({"stations": stations})


@station_bp.route('/stationTimes/<stationCode>', methods=['GET'])
@station_bp.route('/stationTimes', methods=['GET'])
def get_station_times(stationCode=None):
    helper = WMATAHelper()

    if not stationCode:
        return jsonify({"error": "Station code required"}), 400

    response = helper.make_request(f'StationPrediction.svc/json/GetPrediction/{stationCode}')
    if not response or 'Trains' not in response:
        return jsonify({"error": "Failed to fetch predictions"}), 500

    return jsonify({"predictions": response['Trains']})
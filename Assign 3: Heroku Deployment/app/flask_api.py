from app.utils import calculate_simpleInterest

from flask import Flask, jsonify, request

import numpy as np

import joblib

app = Flask(__name__)


@app.route('/get-simpleInterest/', methods=['GET', 'POST'])
def get_simpleInterest():
    """
    :return:
        1. jsonify(data_dic, interest) ->   {
                                            input dictionary,
                                            output value
                                            }
        2. jsonify(interest) -> output value
        3. jsonify(interest, data_dic) ->   {
                                            output value,
                                            input dictionary
                                            }
        ....
    """
    """
    Case 1: you send data from postman through 'Params'
        data_dic = request.args
    Case 2: you send data from postman through Body->form-data
        data_dic = request.form
    Case 3: you send data from postman through Body->raw
        data_dic = request.get_json(force=True)
    """
    data_dic = request.get_json(force=True)
    principle = data_dic.get('principle', float())
    rate = data_dic.get('rate', float())
    time = data_dic.get('time', float())
    interest = calculate_simpleInterest(principle, rate, time)
    return jsonify({'interest': interest}, data_dic)


@app.route('/get-solar-radiation/', methods=['GET', 'POST'])
def get_solar_radiation():
    """
    :return:
        1. jsonify(data_dic, interest) ->   {
                                            input dictionary,
                                            output value
                                            }
        2. jsonify(interest) -> output value
        3. jsonify(interest, data_dic) ->   {
                                            output value,
                                            input dictionary
                                            }
        ....
    """
    """
    Case 1: you send data from postman through 'Params'
        data_dic = request.args
    Case 2: you send data from postman through Body->form-data
        data_dic = request.form
    Case 3: you send data from postman through Body->raw
        data_dic = request.get_json(force=True)
    """

    packet = request.get_json(force=True)
    label = packet.pop('Radiation')
    features = list(packet.values())
    data = np.array(features).reshape(1, 10)
    model_file = 'app/model_gbr.pkl'
    model = joblib.load(model_file)
    prediction = float(model.predict(data))
    return jsonify({"Solar Radiation ": prediction}, packet)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

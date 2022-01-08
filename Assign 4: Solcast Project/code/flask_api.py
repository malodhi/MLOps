
from flask import Flask, jsonify, request
import numpy as np
import joblib


app = Flask(__name__)

"""
Note:
To use the heroku deployment visit Assign 3 where this api is deployed and pushed.
"""

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
    model_file = '../models/model_gbr.pkl'
    model = joblib.load(model_file)
    prediction = float(model.predict(data))
    return jsonify({"Solar Radiation ": prediction}, packet)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

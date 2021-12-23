
from utils import calculate_simpleInterest

from flask import Flask, jsonify, request

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)

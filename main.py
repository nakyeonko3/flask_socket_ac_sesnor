# https://stackoverflow.com/questions/43205568/python-flask-server-with-mqtt-subscription

from flask import Flask, render_template, jsonify
import read_csvfile
import threading
import sock_client


port = 5000
app = Flask(__name__)
port = 5000

sock_thread = threading.Thread(target=sock_client.receve_data_from_sock_sever)
sock_thread.daemon = True

@app.route('/')
def render_mainpage():
    return render_template('index.html', name="nakyeonko")

@app.route('/getSensorData')
def getSensorData():
    return jsonify({'sensor_data':read_csvfile.get_senor_data_last_value()})

if __name__ == '__main__':
    sock_thread.start()
    app.run(host='0.0.0.0', port=port, debug=True)
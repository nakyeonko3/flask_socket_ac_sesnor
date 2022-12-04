# https://stackoverflow.com/questions/43205568/python-flask-server-with-mqtt-subscription

from flask import Flask, render_template, jsonify
import read_csvfile
import threading
import sock_client
import paho.mqtt.client as mqtt


port = 5000
app = Flask(__name__)

client = mqtt.Client()
client.connect('nakyeonkopi') #접속할 호스트명
client.loop_start()
topic = "relay_inTopic"


sock_thread = threading.Thread(target=sock_client.receve_data_from_sock_sever)
sock_thread.daemon = True

@app.route('/')
def render_mainpage():
    return render_template('index.html', name="nakyeonko")

@app.route('/getSensorData')
def getSensorData():
    return jsonify({'sensor_data':read_csvfile.get_senor_data_last_value()})

@app.route('/turnoff')
def turnoff():
    client.publish(topic, "1")
    return " "

@app.route('/turnon')
def turnon():
    client.publish(topic, "0")
    return " "

if __name__ == '__main__':
    sock_thread.start()
    app.run(host='0.0.0.0', port=port, debug=True)
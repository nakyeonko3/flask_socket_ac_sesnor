import sock_client
import threading
import time
from flask import Flask

sock_thread = threading.Thread(target=sock_client.receve_data_from_sock_sever)
sock_thread.daemon = True


app = Flask(__name__)

@app.route("/")
def helloworld():
    return "hello world"

if __name__ == "__main__":
    sock_thread.start()
    app.run(port=18080)
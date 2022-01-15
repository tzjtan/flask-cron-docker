import os
import flask
import logging
import datetime

logging.basicConfig(filename='/mylogs/flask_app.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('Flask started up.')

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return '<a href="/test_log">Manually insert a log line<a>'

@app.route('/test_log')
def test_log():
    time_str = datetime.datetime.now().isoformat()
    logging.debug(f'Logged the current time ({time_str}) to file.')
    return f'Logged the current time ({time_str}) to file.'

if __name__ == '__main__':
    # This app is served by flask through the Dockerfile CMD
    pass

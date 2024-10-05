from app import create_app, db
from threading import Thread
import time
import requests

def start_flask_app(app):
    app.run(port=5000, use_reloader=False)

def before_all(context):
    context.app = create_app('testing')
    context.app.config['TESTING'] = True
    context.thread = Thread(target=start_flask_app, args=(context.app,))
    context.thread.daemon = True
    context.thread.start()
    time.sleep(1)  # Give the server a second to ensure it's up

def after_all(context):
    try:
        requests.get('http://localhost:5000/shutdown', timeout=5)
    except requests.exceptions.RequestException:
        pass  # The server might already be shut down
    context.thread.join(timeout=5)

def before_scenario(context, scenario):
    with context.app.app_context():
        db.create_all()

def after_scenario(context, scenario):
    with context.app.app_context():
        db.session.remove()
        db.drop_all()
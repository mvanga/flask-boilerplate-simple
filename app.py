# Module imports
import logging

# Core flask imports
from flask import Flask
from flask import Blueprint
from flask.cli import AppGroup

# Flask extensions
from flask_cors import CORS

# Miscellaneous 3rd party imports

# =============================================================================
# Extension variables
# =============================================================================

# NOTE: SECTION:EXTENSIONS: Instantiate your extensions here (no init yet)...

# db = SQLAlchemy()
# migrate = Migrate()

# =============================================================================
# Blueprints and CORS setup
# =============================================================================

api_v1 = Blueprint('api_v1', __name__)
cors = CORS(api_v1, origins=['*'])  # NOTE: In production, replace with frontend subdomain

# =============================================================================
# Factory function for Flask
# =============================================================================

def create_app():
    app = Flask(__name__)

    # Setup logging
    if app.env == 'development':
        app.logger.setLevel(logging.DEBUG)
    else:
        app.logger.setLevel(logging.ERROR)

    # NOTE: SECTION:CONFIG: Set your config values here

    # NOTE: SECTION:EXTENSIONS: Initialize your extensions here

    # NOTE: SECTION:BLUEPRINTS: Register your blueprints here
    app.register_blueprint(api_v1, url_prefix='/api/v1')

    # NOTE: SECTION:CLI: Register your commands and AppGroup's here
    app.cli.add_command(app_cli)

    return app


# =============================================================================
# Database Models
# =============================================================================

# NOTE: SECTION:MODELS: Your models go here...

# =============================================================================
# Utility Functions
# =============================================================================

def api_response(status, data=None, message=None, code=None, http_code=200):
    """Build and return a JSON API response in the JSend format"""
    ret = {'status': status}
    ret['data'] = data
    if message is not None:
        ret['message'] = message
    if code is not None:
        ret['code'] = code
    return ret, code


def api_success(data=None, http_code=200):
    """Returns a 'success' JSend response."""
    return api_response('success', data=data, http_code=http_code)


def api_fail(data, http_code=400):
    """Returns a 'fail' JSend response."""
    return api_response('fail', data=data, http_code=http_code)


def api_error(message, data=None, code=None, http_code=500):
    """Returns an 'error' JSend response."""
    return api_response('error', data, message, code, http_code)

# NOTE: SECTION:UTILITIES: Your utility functions go here...


# =============================================================================
# API Routes
# =============================================================================

@api_v1.route('/hello')
def hello():
    return api_success({'message': 'Hello World!'})

# NOTE: SECTION:ROUTES: Your routes go here...

# =============================================================================
# Custom CLI Commands
# =============================================================================

app_cli = AppGroup('app')

@app_cli.command('hello')
def cli_hello():
    print('Hello!')

# NOTE: SECTION:CLI: Your custom CLI commands go here...

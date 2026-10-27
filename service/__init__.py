
"""Flask application initialization for the Accounts REST API."""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_talisman import Talisman


def create_app(test_config=None):
    """Create and configure the Accounts Flask application."""
    app = Flask(__name__)

    app.config.update(
        TESTING=False,
        JSON_SORT_KEYS=True,
    )

    if test_config:
        app.config.update(test_config)

    CORS(
        app,
        resources={
            r"/*": {
                "origins": "*",
                "methods": [
                    "GET",
                    "POST",
                    "PUT",
                    "PATCH",
                    "DELETE",
                    "OPTIONS",
                ],
                "allow_headers": [
                    "Content-Type",
                    "Authorization",
                ],
            }
        },
    )

    Talisman(
        app,
        force_https=False,
        frame_options="DENY",
        content_type_options=True,
        referrer_policy="no-referrer",
        strict_transport_security=False,
        content_security_policy={
            "default-src": ["'self'"],
            "object-src": ["'none'"],
            "frame-ancestors": ["'none'"],
        },
    )

    @app.get("/health")
    def health():
        return jsonify({
            "name": "Account REST API Service",
            "version": "1.0",
        }), 200

    return app


app = create_app()

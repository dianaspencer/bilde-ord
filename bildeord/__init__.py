from flask import Flask
from bildeord import app
from bildeord.error import handlers


def create_app(test_config=None, secret_key="dev"):
    """Application factory.

    :param test_config:
    :param secret_key: str, set to 'dev' for convenience
            during development, but override when deploying.
    :return:
    """
    app_ = Flask(__name__, instance_relative_config=True)

    # Place all global app configuration settings here.
    app_.config.from_mapping(
        SECRET_KEY=secret_key,
        ALLOWED_FILE_EXTENSIONS=["jpg", "png"],
        # Maximum content size is 1 MB
        MAX_CONTENT_LENGTH=1 * 1024 * 1024
    )

    # Test bildeord connection
    @app_.route("/hello")
    def hello_test():
        return "Hello world!"

    # Register blueprint for object detection service
    app_.register_blueprint(app.this_app)
    app_.register_blueprint(handlers.errors)

    return app_

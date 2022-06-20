from flask import Flask, send_from_directory
from main.views import show_photos_blueprint
from loader.views import add_post_blueprint
import logging

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(show_photos_blueprint)
app.register_blueprint(add_post_blueprint)

logging.basicConfig(filename="basic.log", level=logging.INFO)


# app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024
# @app.errorhandler(413)
# def page_not_found():
#    return "Файл слишком большой"


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

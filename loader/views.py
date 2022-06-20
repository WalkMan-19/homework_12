from flask import Blueprint, render_template, request
from functions import save_picture, adding_post
import logging

add_post_blueprint = Blueprint('add_post_blueprint', __name__)


@add_post_blueprint.route('/post/')
def post_page():
    return render_template('post_form.html')


@add_post_blueprint.route('/post/', methods=['POST'])
def adding_post_page():
    picture = request.files.get("picture")
    content = request.form.get("content")

    if not picture or not content:
        return "Нет картинки или текста"

    if picture.filename.split('.')[-1] not in ["jpg", "png"]:
        logging.info('Загруженный файл не картинка')
        return "Данный тип файлов не поддерживается"

    try:
        picture_path: str = '/' + save_picture(picture)

    except FileNotFoundError:
        logging.error('Файл не найден')
        return "Файл не найден"

    post: dict = adding_post({"pic": picture_path, "content": content})
    return render_template('post_uploaded.html', post=post)

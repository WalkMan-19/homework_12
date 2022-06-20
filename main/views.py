from flask import Blueprint, render_template, request
from functions import search_in_posts
from json import JSONDecodeError
import logging

show_photos_blueprint = Blueprint('show_photos_blueprint', __name__)


@show_photos_blueprint.route('/')
def main_page():
    return render_template('index.html')


@show_photos_blueprint.route('/search/')
def search_page():
    s = request.args.get('s', '')
    logging.info('Выполняю поиск')
    try:
        posts = search_in_posts(s)
        return render_template('post_list.html', posts=posts, s=s)

    except FileNotFoundError:
        logging.error('Файл не найден')
        return "Файл не найден"

    except JSONDecodeError:
        return "Не удаётся преобразовать файл"

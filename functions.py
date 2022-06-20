import json


def load_json():
    """ Чтение и получение данных из JSON-файла"""
    with open('posts.json', 'r', encoding="utf-8") as f:
        posts = json.load(f)
    return posts


def search_in_posts(user_word: str) -> list[dict]:
    """  Поиск по ключевому слову, полученного от пользователя """
    result = []
    for post in load_json():
        if user_word.lower() in post["content"].lower():
            result.append(post)
    return result


def save_picture(picture):
    """ Функция сохранения картинки в файл /uploads/images """
    picture_filename = picture.filename
    path = f'./uploads/images/{picture_filename}'
    picture.save(path)
    return path


def adding_post(post: dict) -> dict:
    """ Функция добавления поста в JSON-файл  """
    posts: list[dict] = load_json()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f)
    return post

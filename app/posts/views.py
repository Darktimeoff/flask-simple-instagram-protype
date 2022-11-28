from flask import Blueprint, render_template
import logging

from .dao.posts_dao import PostsDao
from utils.main import get_post_path
 
posts_blueprint = Blueprint('posts', __name__, template_folder='templates')

posts_dao = PostsDao(get_post_path())

@posts_blueprint.route('/')
def page_index():
    posts = posts_dao.get_all()

    return render_template('index.html', posts=posts)
from flask import Blueprint, render_template, request
import logging

from app.comments.dao.commnets_dao import CommentsDao
from .dao.posts_dao import PostsDao
from utils.main import get_post_path, get_comment_path
 
posts_blueprint = Blueprint('posts', __name__, template_folder='templates')

posts_dao = PostsDao(get_post_path())
comments_dao = CommentsDao(get_comment_path())

@posts_blueprint.errorhandler(404)
def error_404(e):
    return render_template('404.html')

@posts_blueprint.route('/')
def page_index():
    posts = posts_dao.get_all()

    return render_template('index.html', posts=posts)

@posts_blueprint.route('/posts/<int:id>/')
def post(id: int):
    post = posts_dao.get_by_id(id)

    comments = comments_dao.get_comments_by_post_id(id)

    return render_template('post.html', post=post, comments=comments)

@posts_blueprint.route('/search/')
def search():
    word = request.args.get('s')
    posts = []

    if word:
        posts = posts_dao.search_by_word(word)

    return render_template('search.html', search=word, posts=posts)

@posts_blueprint.route('/users/<username>/')
def user(username: str):
    posts = posts_dao.get_by_user(username)

    return render_template('user-feed.html', username=username, posts=posts)
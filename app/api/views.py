from flask import Blueprint, jsonify

from app.posts.dao.posts_dao import PostsDao
from utils.main import get_post_path


api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

posts_dao = PostsDao(get_post_path())

@api_blueprint.route('/posts/')
def posts_list():
    posts = posts_dao.get_all()

    return jsonify([p.__dict__ for p in posts])

@api_blueprint.route('/posts/<int:id>/')
def post(id: int):
    post = posts_dao.get_by_id(id)

    if not post:
        return jsonify({'message': 'not found posts'})
    
    return jsonify(post.__dict__)

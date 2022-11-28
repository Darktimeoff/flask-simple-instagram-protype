from classes.dao import Dao
from app.posts.model import Post


class PostsDao(Dao):
    def serialize(self, data: dict):
        return Post(
            pk=data['pk'],
            poster_name=data['poster_name'],
            poster_avatar=data['poster_avatar'],
            pic=data['pic'],
            content=data['content'],
            views_count=data['views_count'],
            likes_count=data['likes_count']
        )

    def get_all(self):
        posts = super(PostsDao, self).get_all()

        return [self.serialize(p) for p in posts]

    def get_by_user(self, user_name: str):
       # ToDo Implemented check for user exist and throw ValueError
        if type(user_name) is not str:
            raise TypeError('unexpected type for user_name argument')

        posts = self.get_all()

        return [p for p in posts if p.poster_name.lower() == user_name.lower()]

    def search_by_word(self, word: str):
        if type(word) is not str:
            raise TypeError('unexpected type for word argument')

        posts = self.get_all()

        return [p for p in posts if word.lower() in p.content.lower()]

    def get_by_id(self, id: int):
        if type(id) is not int:
            raise TypeError('unexpected type for id argument')

        posts = self.get_all()

        for post in posts:
            if post.pk == id:
                return post

        return None

from classes.dao import Dao
from app.comments.model import Comment

class CommentsDao(Dao):
    def searialize(self, data: dict):
        return Comment(
            pk=data['pk'],
            post_id=data['post_id'],
            commenter_name=data['commenter_name'],
            comment=data['comment'],
        )

    def get_all(self):
        posts  = super(CommentsDao, self).get_all()

        return  [self.searialize(p) for p in posts]

    def get_comments_by_post_id(self, post_id: int):
        #ToDo Implemented for post exist and throw error
        if type(post_id) is not int:
            raise TypeError("post_id must be an integer")

        comments = self.get_all()
        
        return [c for c in comments if c.post_id == post_id]
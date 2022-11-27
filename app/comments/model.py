
class Comment:
    pk: int
    post_id: int
    commenter_name: str
    comment: str 
  

    def __init__(self, pk: int, post_id: int, commenter_name: str, comment: str):
        self.pk = pk
        self.post_id = post_id
        self.commenter_name = commenter_name
        self.comment = comment
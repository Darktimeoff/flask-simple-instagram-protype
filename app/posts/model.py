
class Post:
    pk: int
    poster_name: str
    poster_avatar: str
    pic: str
    content: str
    views_count: int
    likes_count: int

    def __init__(self, 
        pk: int, poster_name: str, poster_avatar: str, pic: str, 
        content: str, views_count: int, likes_count: int):
        self.pk = pk
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count
    
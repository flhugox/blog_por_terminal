import  uuid
import datetime
from database import Database

__autor__ = 'Vhernandez'


class Post(object):
    def __init__(self,blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blod_id=blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id
    ##post= Post(blog_id="123",title="a title", content="some content", author="Jose", date=datetime.datetime.utcnow())


    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return{
            'id': self.id,
            'blod_id': self.blod_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'id': id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['created_date'],
                   id=post_data['id'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]

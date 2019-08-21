from database import Database
from models.blog import Blog
from models.post import Post

__autor__ = 'Vhernandez'

Database.initialize()

blog = Blog(author="Jose",
            title="Sample title",
            description="Sample Description")
blog.new_post()

blog.save_to_mongo()

from_database = Blog.get_from_mongo(blog.id)

print(blog.get_post())
# blog.get_post()


""""
post = Post(blog_id="123",
            title="Another grat post",
            content="This is some samble",
            author="Jose")

##post.save_to_mongo()

post1 = Post.from_mongo('2270d311bf2549ea93676f5088b15ee8')

##print(post1)

posts= Post.from_blog('2270d311bf2549ea93676f5088b15ee8')
for post in posts:
    print(post)
"""
""""

post = Post("Post1 title", "Post1 content", "Post1 author")
post2 = Post("Post2 title", "Post2 content", "Post2 author")

print(post.content)
print(post2.title)
"""
""" 
import pymongo
uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['dbhospital']
collection = database['usuarios']


usuarios = collection.find({})
usuario_list = []

for usuario in usuarios:
    usuario_list.append(usuario)

users = [user['email'] for user in collection.find({}) if user['email'] == 'hugo-hdz@hotmail.com']
print(users)
"""

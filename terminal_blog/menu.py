from database import Database
from models.blog import Blog

__author__ = 'jslvtr'

class Menu(object):
    def __init__(self):
        self.user=input("Enter your author name")
        self.user_blog=None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else
            self._prompt_user_for_account()

     def _user_has_account(self):
         blog= Database.find_one('blogs', {'author': self.user})
         if blog is not None:
             self.user_blog=Blog.get_from_mongo(blog['id'])
             return True
         else:
             return False



     def _prompt_user_for_account(self):
        title=input("Enter Blog title: ")
        description=input("enter blog description")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog=blog




    def run_menu(self):
        #User read or write blogs?
        read_or_write= input("Doyou want to read (R) or write (W) blogs?")
        #if read:
        if read_or_write=='R':
            #list blogs in database
            self._list_blogs()
            #allow user pick one
            #display posts
            self._view_blog()
            pass
        #if write
        elif read_or_write=='W':
            #check if user has a blog
            #if they do, prompt to write a post
            #if not , prompt to create a new
            self._prompt_write_post()
            pass
        else:
            print("thank you for bloffing!")

    def _prompt_write_post(self):
        self.user_blog.new

    def _list_blogs(self):
        pass


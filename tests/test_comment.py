from app.models import Comment,User,Pitch
from app import db
import unittest

class Comment(unittest.TestCase):
    def setUp(self):
        self.user_shalin = User(username = 'shalin',password = 'Chepkoech03', email = 'shalin@ms.com')
        self.new_pitch = Pitch(id=1,title='pitchh_test',description='Welcome to tests pitch',category="interview",user = self.user_shalin,upvotes=0,downvotes=0)
        


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.content,'comment')
        self.assertEquals(self.new_comment.user,self.user_shalin)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)
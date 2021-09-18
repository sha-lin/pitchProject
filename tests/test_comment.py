from app.models import Comment,User,Pitch
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_John = User(username = 'James',password = 'potato', email = 'john@ms.com')
        self.new_pitch = Pitch(id=1,title='Test',description='This is a test pitch',category="interview",user = self.user_James,upvotes=0,downvotes=0)
        self.new_comment = Comment(id=1, content='Test comment',user=self.user_John,pitch=self.new_pitch)


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.content,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_James)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)
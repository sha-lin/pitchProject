from app.models import Comment,User, Pitch
from app import db
import unittest

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_shalin = User(username = 'shalin',password = 'Chepkoech03', email = 'shalin@ms.com')
        self.new_pitch = Pitch(id=1,title='Test',description='test pitch',category="interview",user = self.user_shalin,upvotes=0,downvotes=0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title,'Test')
        self.assertEquals(self.new_pitch.description,'test pitch')
        self.assertEquals(self.new_pitch.category,"interview")
        self.assertEquals(self.new_pitch.user,self.user_shalin)

    def test_get_pitch_by_id(self):
        got_pitch = Pitch.get_pitch(1)
        self(got_pitch)

from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post
# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='asad4',password='qwerty123')
        testuser1.save()

        test_post = Post.objects.create(
            author=testuser1,title='hello test post',body='test post working..')
        test_post.save()

    def test_blog_content(self):
        post=Post.objects.get(id=1)
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        self.assertEqual(expected_author,'asad4')
        self.assertEqual(expected_title,'hello test post')
        self.assertEqual(expected_body,'test post working..')

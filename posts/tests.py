from test_plus.test import TestCase

from posts.factories import PostFactory


class PostsTest(TestCase):
    def test_get_list(self):
        post = PostFactory()
        post_list_url = self.reverse('post:list')
        self.get_check_200(post_list_url)
        self.assertResponseContains(post.title, html=False)
        self.assertResponseContains(post.author.name, html=False)

        write_url = self.reverse('post:create')
        self.assertResponseContains(write_url, html=False)

    def test_get_writing_page_with_login(self):
        user = self.make_user('jelly jelly')

        with self.login(username=user.username):
            write_post_url = self.reverse('post:create')
            self.get_check_200(write_post_url)

    def test_get_writing_page_with_anonymous(self):
        self.assertLoginRequired('post:create')

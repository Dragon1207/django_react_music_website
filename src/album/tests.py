import random
import string

import chromedriver_binary
import factory
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase, RequestFactory, TestCase
from django.urls import reverse
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

from album.models import Album
from album.views import AlbumList


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# pragma pylint: disable=R0903
class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: 'Agent %03d' % n)
    email = factory.LazyAttributeSequence(lambda o, n: f'{o.username}{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password')


class AlbumFactory(factory.DjangoModelFactory):
    class Meta:
        model = Album

    artist = 'raw artist'
    title = 'raw album title'
    genre = 'raw genre'


# pragma pylint: enable=R0903


class AlbumTests(TestCase):
    def test_album_create(self):
        album = AlbumFactory()
        self.assertEqual(1, Album.objects.count())
        self.assertEqual('raw album title', album.title)


class AlbumListViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserFactory(password=random_string_generator())

    def test_no_albums_in_context(self):
        request = self.factory.get('/')
        request.user = self.user
        response = AlbumList.as_view()(request)
        self.assertEqual(
            list(response.context_data['object_list']),
            [],
        )

    def test_albums_in_context(self):
        request = self.factory.get('/')
        album = AlbumFactory()
        request.user = self.user
        response = AlbumList.as_view()(request)
        self.assertEqual(
            list(response.context_data['object_list']),
            [album],
        )


class IntegrationTests(LiveServerTestCase):
    selenium = None

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--log-level=3')
        cls.selenium = webdriver.WebDriver(
            executable_path=chromedriver_binary.chromedriver_filename, chrome_options=chrome_options)
        cls.password = random_string_generator()
        cls.user = UserFactory(password=cls.password)
        super(IntegrationTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(IntegrationTests, cls).tearDownClass()

    def test_album_list(self):
        response = self.client.get(reverse('albums:list'))
        self.assertEqual(response.status_code, 200)

    def test_slash(self):
        response = self.client.get(reverse('home'))
        self.assertIn(response.status_code, (301, 302))

    def test_empty_create(self):
        response = self.client.get(reverse('albums:create'))
        self.assertIn(response.status_code, (301, 302))

    def test_album_create(self):
        self.assertTrue(self.client.login(username=self.user.username, password=self.password))
        cookie = self.client.cookies[settings.SESSION_COOKIE_NAME]
        # Replace `localhost` to 127.0.0.1 due to the WinError 10054 according to the
        # https://stackoverflow.com/a/14491845/1360307
        self.selenium.get(f'{self.live_server_url}{reverse("albums:create")}'.replace('localhost', '127.0.0.1'))
        if cookie:
            self.selenium.add_cookie({
                'name': settings.SESSION_COOKIE_NAME,
                'value': cookie.value,
                'secure': False,
                'path': '/'
            })
        self.selenium.refresh()  # need to update page for logged in user
        self.selenium.find_element_by_id('id_artist').send_keys('raw artist')
        self.selenium.find_element_by_id('id_title').send_keys('raw album title')
        self.selenium.find_element_by_id('id_genre').send_keys('raw genre')
        self.selenium.find_element_by_xpath('//*[@id="submit-id-submit"]').click()
        self.assertEqual(1, Album.objects.count())
        self.assertEqual('raw album title', Album.objects.first().title)


# TODO: Write tests for the API calls

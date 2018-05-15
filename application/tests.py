import unittest
from flask.ext.testing import TestCase
from app import app,conn
import json

db=conn.test_app
class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app
    def setUp(self):
        db.create_collection('catalog')
        db.create_collection('users')
        mongodb_entry={
            "name":"mongodb",
            "title":"Mongodb",
            "subtitle":"Document-oriented database program.",
            "details":"MongoDB is a free and open-source cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemas.",
            "label":"database",
            "chart":"stable/mongodb",
            "icon":"static/ico/app-icons/mongodb-logo.png",
            "docker_compose":"https://github.com/bitnami/bitnami-docker-mongodb"
            }
        user={
            "name":"admin",
            "password":"admin"
        }
        db.catalog.insert(mongodb_entry)
        db.users.insert(user)

    def tearDown(self):
        db.session.remove()
        db.catalog.drop()
        db.users.drop()
class FlaskTestCase(BaseTestCase):
    def test_index(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code,200)
    def test_login(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code,200)
    def test_register(self):
        response = self.client.get('/register', content_type='html/text')
        self.assertEqual(response.status_code,200)
    def test_catalog(self):
        response = self.client.get('/catalog', content_type='html/text')
        self.assertEqual(response.status_code,200)
    def test_about(self):
        response = self.client.get('/about', content_type='html/text')
        self.assertEqual(response.status_code,200)
    def test_catalog_applicaton_entry(self):
        response = self.client.get('/catalog', content_type='html/text')
        self.assertIn(b'Mongodb',response.data)
    def test_detail(self):
        response = self.client.get('/catalog/mongodb/details', content_type='html/text')
        self.assertEqual(response.status_code,200)
    def test_register_user(self):
        data={
            "username":"test",
            "email":"test@testing.com",
            "password":"test",
            "confirm":"test"
            }
        response = self.client.post('/register',
        data=json.dumps(data),
        follow_redirects=True)
        self.assertEqual(response.status_code,200)
    def login_user(self):
        data={
            "username":"test",
            "password":"test"
        }
        response = self.client.post('/login',
        data=json.dumps(data),
        follow_redirects=True)
        self.assertEqual(response.status_code,200)
    # def test_catalog_applicaton_install(self):
    #     response = self.client.get('/catalog', content_type='html/text')
    #     self.assertIn(b'Mongodb',response.data)
if __name__=='__main__':
    unittest.main()
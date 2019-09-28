# services/users/project/tests/test_users.py

import json
import unittest

from project.tests.base import BaseTestCase

class TestUserService(BaseTestCase):
    """Test for the Users Service."""

    def test_users(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_user(self):
        """Ensure a new user can be added to db."""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'alex',
                    'email': 'alex@test.com'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('alex@test.com was added!', data['message'])
            self.assertIn('success', data['status'])

    def 

if __name__ == '__main__':
    unittest.main()

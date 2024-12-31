from fastapi.testclient import TestClient
from app import app
import unittest


class BaseTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        """Set up the TestClient for testing"""
        self.client = TestClient(app)

    @classmethod
    def tearDown(self):
        """Tear down the TestClient after testing"""
        self.client = None


if __name__ == "__main__":
    unittest.main()

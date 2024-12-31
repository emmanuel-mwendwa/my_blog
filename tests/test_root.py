from . import BaseTest


class TestRootEndpoint(BaseTest):
    def test_root_endpoint(self):
        """Test the root endpoint of the application."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello World"})

    def test_non_existent_endpoint(self):
        """Test a non-existent endpoint."""
        response = self.client.get("/non-existent-endpoint")
        self.assertEqual(response.status_code, 404)
        self.assertIn("detail", response.json())

    def test_hello_endpoint(self):
        """Test the hello endpoint of the application."""
        response = self.client.get("/hello/Emmanuel")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello Emmanuel"})

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import ShortURL


class URLShortenerTests(TestCase):
    def test_home_page_and_shortening(self):
        # 1. Access home page
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

        # 2. Shorten a URL
        response = self.client.post(
            reverse("home"), {"original_url": "https://www.google.com"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("short_url", response.context)
        self.assertIsNotNone(response.context["short_url"])

        # Verify db entry exists
        short_url = response.context["short_url"]
        self.assertEqual(short_url.url, "https://www.google.com")
        self.assertEqual(ShortURL.objects.count(), 1)

    def test_redirect(self):
        # Create a ShortURL object
        short = ShortURL.objects.create(
            url="https://www.wikipedia.org", short_code="wiki12"
        )

        # Access redirection url
        response = self.client.get(reverse("redirect_url", args=[short.short_code]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "https://www.wikipedia.org")

        # Check clicks incremented
        short.refresh_from_db()
        self.assertEqual(short.access_count, 1)

    def test_dashboard_and_delete(self):
        short = ShortURL.objects.create(url="https://github.com", short_code="github")

        # View dashboard
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "https://github.com")
        self.assertContains(response, "github")

        # Delete URL
        response = self.client.get(reverse("delete_url", args=[short.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to dashboard
        self.assertEqual(ShortURL.objects.count(), 0)

    def test_update_url(self):
        short = ShortURL.objects.create(url="https://github.com", short_code="github")
        response = self.client.post(
            reverse("update_url", args=[short.id]),
            {"original_url": "https://gitlab.com"},
        )
        self.assertEqual(response.status_code, 302)
        short.refresh_from_db()
        self.assertEqual(short.url, "https://gitlab.com")

    def test_api_endpoints(self):
        # 1. API POST to shorten (invalid data)
        response = self.client.post(
            "/api/shorten",
            {"url": "invalid-url-format"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("url", response.data)

        # 2. API POST to shorten (valid data)
        response = self.client.post(
            "/api/shorten",
            {"url": "https://stackoverflow.com"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("shortCode", response.data)
        self.assertIn("createdAt", response.data)
        self.assertIn("updatedAt", response.data)
        self.assertEqual(response.data["url"], "https://stackoverflow.com")

        short_code = response.data["shortCode"]

        # 3. API GET to retrieve info
        response = self.client.get(f"/api/shorten/{short_code}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["url"], "https://stackoverflow.com")
        self.assertEqual(response.data["shortCode"], short_code)

        # 4. API PUT to update url (valid data)
        response = self.client.put(
            f"/api/shorten/{short_code}",
            {"url": "https://github.com"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["url"], "https://github.com")

        # 5. API GET to retrieve stats
        response = self.client.get(f"/api/shorten/{short_code}/stats")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["url"], "https://github.com")
        self.assertIn("accessCount", response.data)
        self.assertEqual(response.data["accessCount"], 0)

        # 6. API DELETE to delete url
        response = self.client.delete(f"/api/shorten/{short_code}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # 7. Verify deletion
        response = self.client.get(f"/api/shorten/{short_code}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

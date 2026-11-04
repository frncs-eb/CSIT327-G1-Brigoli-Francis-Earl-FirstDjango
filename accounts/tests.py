from django.test import TestCase
from django.urls import reverse
from .models import CustomUser


class ProfileViewTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="student",
            password="SecurePass!234",
            email="student@example.com",
            first_name="Sam",
            last_name="Student",
            course="Computing",
        )
        self.url = reverse("profile")

    def test_profile_requires_authentication(self):
        response = self.client.get(self.url)

        self.assertRedirects(response, f"{reverse('login')}?next={self.url}")

    def test_profile_edits_account_fields_but_not_role(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            set(response.context["form"].fields),
            {"username", "email", "first_name", "last_name", "course"},
        )

        response = self.client.post(
            self.url,
            {
                "username": "updated-student",
                "email": "updated@example.com",
                "first_name": "Updated",
                "last_name": "Student",
                "course": "Engineering",
                "role": CustomUser.Role.ADMIN,
            },
        )

        self.assertRedirects(response, self.url)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, "updated-student")
        self.assertEqual(self.user.email, "updated@example.com")
        self.assertEqual(self.user.first_name, "Updated")
        self.assertEqual(self.user.course, "Engineering")
        self.assertEqual(self.user.role, CustomUser.Role.STUDENT)


class SignupFeedbackTests(TestCase):
    def test_successful_signup_shows_one_time_message_after_redirect(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "new-student",
                "email": "new@example.com",
                "first_name": "New",
                "last_name": "Student",
                "course": "Computing",
                "password1": "SecurePass!234",
                "password2": "SecurePass!234",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("login"))
        self.assertContains(
            response,
            "Your account has been created successfully. Please log in.",
        )
        self.assertEqual(CustomUser.objects.filter(username="new-student").count(), 1)

        response = self.client.get(reverse("login"))
        self.assertNotContains(
            response,
            "Your account has been created successfully. Please log in.",
        )

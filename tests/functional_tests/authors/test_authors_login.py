import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from selenium.webdriver.common.by import By

from .base import AuthorsBaseTest


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_successfully(self):
        string_password = "pass"
        user = User.objects.create_user(
            username="my_user", password=string_password
        )  # noqa: E501

        # usuário abre a oágina de login
        self.browser.get(self.live_server_url + reverse("authors:login"))

        # Usuário ve o formulario de login
        form = self.browser.find_element(By.CLASS_NAME, "main-form")
        username_field = self.get_by_placeholder(form, "Type your username")
        password_field = self.get_by_placeholder(form, "Type your password")

        # usuário digita seu usuário e senha
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # usuário envia o formulário
        form.submit()

        # usuário ve a mensagem de login com sucesso e seu nome
        self.assertIn(
            f"Your are logged in with {user.username}.",
            self.browser.find_element(By.TAG_NAME, "body").text,
        )

    def test_login_create_raises_404_if_not_POST_method(self):
        self.browser.get(
            self.live_server_url + reverse("authors:login_create")
        )  # noqa: E501

        self.assertIn(
            "Not Found", self.browser.find_element(By.TAG_NAME, "body").text
        )  # noqa; E501

    def test_form_login_is_invalid(self):
        # usuário abre a página de login
        self.browser.get(self.live_server_url + reverse("authors:login"))

        # usuário ve o formulário de login
        form = self.browser.find_element(By.CLASS_NAME, "main-form")

        # e tenta enviar valores vazios
        username = self.get_by_placeholder(form, "Type your username")
        password = self.get_by_placeholder(form, "Type your password")
        username.send_keys(" ")
        password.send_keys(" ")

        # usuário envia o formulário
        form.submit()

        # ve uma mensagem de eeor da tela
        self.assertIn(
            "Invalid username or password",
            self.browser.find_element(By.TAG_NAME, "body").text,
        )

    def test_form_login_invalid_credentials(self):
        # usuário abre a página de login
        self.browser.get(self.live_server_url + reverse("authors:login"))

        # usuário ve o formulário de login
        form = self.browser.find_element(By.CLASS_NAME, "main-form")

        # e tenta enviar valores com dados que não correspondem
        username = self.get_by_placeholder(form, "Type your username")
        password = self.get_by_placeholder(form, "Type your password")
        username.send_keys("invalid_user")
        password.send_keys("invalid_password")

        # usuário envia o formulário
        form.submit()

        # ve uma mensagem de eeor da tela
        self.assertIn(
            "Invalid credentials",
            self.browser.find_element(By.TAG_NAME, "body").text,  # noqa: E501
        )

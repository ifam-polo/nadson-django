# flake8: noqa
# flake8: (W282)
from django.apps import AppConfig


class RecipesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "recipes"

    def ready(self, *args, **kwargs) -> None:
        # sourcery skip: inline-immediately-returned-variable
        import recipes.signals  # noqa

        super_ready = super().ready(*args, **kwargs)
        return super_ready

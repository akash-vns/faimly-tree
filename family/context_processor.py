from django.conf import settings


def get_site_config(_):
    return {"project_name": settings.PROJECT_NAME}
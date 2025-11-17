from decouple import config
from django.db import connection
from django.http import JsonResponse


def health_check(request):
    environment = config("DJANGO_ENV", default="local").lower()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
        db_status = "OK"
    except Exception as e:
        db_status = f"ERROR: {str(e)}"

    return JsonResponse({
        "status": "OK",
        "database": db_status,
        "environment": environment
    })
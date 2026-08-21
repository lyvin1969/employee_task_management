from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        import os
        from django.contrib.auth import get_user_model
        
        try:
            User = get_user_model()
            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser("admin", "admin@example.com", "AdminPass123!")
                print("Superuser created successfully!")
        except Exception as e:
            print(f"Error creating superuser: {e}")
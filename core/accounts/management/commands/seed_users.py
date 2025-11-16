"""
Management command to seed initial users.
Run with: python manage.py seed_users
"""
from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = 'Seed initial users (superuser) for the application'

    def add_arguments(self, parser):
        parser.add_argument(
            '--email',
            type=str,
            default='admin@gmail.com',
            help='Email address for the superuser (default: admin@example.com)',
        )
        parser.add_argument(
            '--password',
            type=str,
            default='123456',
            help='Password for the superuser (default: admin123)',
        )
        parser.add_argument(
            '--first-name',
            type=str,
            default='Admin',
            help='First name for the superuser (default: Admin)',
        )
        parser.add_argument(
            '--last-name',
            type=str,
            default='User',
            help='Last name for the superuser (default: User)',
        )
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force creation even if user already exists',
        )

    def handle(self, *args, **options):
        email = options['email']
        password = options['password']
        first_name = options['first_name']
        last_name = options['last_name']
        force = options['force']

        self.stdout.write(self.style.SUCCESS('Starting database seeding...'))

        # Check if user already exists
        if User.objects.filter(email=email).exists():
            if force:
                self.stdout.write(
                    self.style.WARNING(f'User with email {email} already exists. Updating...')
                )
                user = User.objects.get(email=email)
                user.set_password(password)
                user.first_name = first_name
                user.last_name = last_name
                user.is_superuser = True
                user.is_staff = True
                user.is_active = True
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Superuser updated: {email} / {password}'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'User with email {email} already exists. Use --force to update.'
                    )
                )
        else:
            # Create new superuser
            User.objects.create_superuser(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f'Superuser created: {email} / {password}'
                )
            )

        self.stdout.write(self.style.SUCCESS('Database seeding completed!'))


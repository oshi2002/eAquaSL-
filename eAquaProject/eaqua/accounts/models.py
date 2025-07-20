from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('officer', 'Regulatory Officer'),
        ('farmer', 'Farmer'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending Approval'),
        ('active', 'Active'),
        ('suspended', 'Suspended'),
    ]

    # regex validator
    phone_validator = RegexValidator(
        regex=r'^(?:\+94|0)?7\d{8}$',
        message="Enter a valid Sri Lankan phone number (e.g., 0771234567 or +94771234567)."
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')

    # Apply the validator
    phone = models.CharField(
        max_length=12,
        blank=True,
        validators=[phone_validator]
    )

    address = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True)
    created_by = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

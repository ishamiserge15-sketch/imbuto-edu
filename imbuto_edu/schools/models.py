from django.db import models


class School(models.Model):
    SCHOOL_TYPES = [
        ("Boarding", "Boarding"),
        ("Day", "Day"),
        ("Mixed", "Mixed"),
    ]

    OWNERSHIP = [
        ("Government", "Government"),
        ("Private", "Private"),
        ("Faith-Based", "Faith-Based"),
    ]

    name = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    province = models.CharField(max_length=100)

    category = models.CharField(max_length=100)
    school_type = models.CharField(max_length=20, choices=SCHOOL_TYPES)
    ownership = models.CharField(max_length=20, choices=OWNERSHIP)

    school_fees = models.CharField(max_length=100)

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)

    description = models.TextField()

    def __str__(self):
        return self.name
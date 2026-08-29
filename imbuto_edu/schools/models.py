from django.db import models


# ==========================================
# SCHOOL MODEL
# ==========================================

class School(models.Model):

    SCHOOL_TYPES = [
        ("Boarding", "Boarding"),
        ("Day", "Day"),
        ("Mixed", "Mixed"),
    ]

    OWNERSHIP_CHOICES = [
        ("Government", "Government"),
        ("Private", "Private"),
        ("Faith-Based", "Faith-Based"),
    ]

    # ==========================================
    # BASIC INFORMATION
    # ==========================================

    name = models.CharField(
        max_length=200
    )

    district = models.CharField(
        max_length=100
    )

    province = models.CharField(
        max_length=100
    )

    category = models.CharField(
        max_length=100
    )

    school_type = models.CharField(
        max_length=20,
        choices=SCHOOL_TYPES
    )

    ownership = models.CharField(
        max_length=30,
        choices=OWNERSHIP_CHOICES
    )

    # ==========================================
    # CONTACT
    # ==========================================

    school_fees = models.CharField(
        max_length=100,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    # ==========================================
    # IMAGE
    # ==========================================

    image = models.ImageField(
        upload_to="schools/",
        blank=True,
        null=True
    )

    # ==========================================
    # EDUCATIONAL INFORMATION
    # ==========================================

    facilities = models.TextField(
        blank=True
    )

    subjects = models.TextField(
        blank=True
    )

    academic_performance = models.TextField(
        blank=True
    )

    # ==========================================
    # RANKING
    # ==========================================

    academic_score = models.PositiveIntegerField(
        default=0
    )

    sports_score = models.PositiveIntegerField(
        default=0
    )

    innovation_score = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):

        return self.name


# ==========================================
# SPORT
# ==========================================

class Sport(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="sports/",
        blank=True,
        null=True
    )

    def __str__(self):

        return self.name


# ==========================================
# SCHOOL SPORT
# ==========================================

class SchoolSport(models.Model):

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="sports"
    )

    sport = models.ForeignKey(
        Sport,
        on_delete=models.CASCADE,
        related_name="schools"
    )

    achievement = models.TextField(
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):

        return f"{self.school.name} - {self.sport.name}"


# ==========================================
# COMPETITION
# ==========================================

class Competition(models.Model):

    name = models.CharField(
        max_length=200
    )

    category = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="competitions/",
        blank=True,
        null=True
    )

    website = models.URLField(
        blank=True
    )

    def __str__(self):

        return self.name


# ==========================================
# SCHOOL COMPETITION
# ==========================================

class SchoolCompetition(models.Model):

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="competitions"
    )

    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
        related_name="participating_schools"
    )

    year = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    position = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    achievement = models.TextField(
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):

        return f"{self.school.name} - {self.competition.name}"
# ==========================================
# CAREER
# ==========================================

class Career(models.Model):

    name = models.CharField(
        max_length=200
    )

    category = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    subjects = models.TextField(
        blank=True,
        help_text="Recommended subjects or school subjects."
    )

    skills = models.TextField(
        blank=True,
        help_text="Important skills for this career."
    )

    image = models.ImageField(
        upload_to="careers/",
        blank=True,
        null=True
    )

    def __str__(self):

        return self.name


# ==========================================
# TVET PROGRAM
# ==========================================

class TVETProgram(models.Model):

    name = models.CharField(
        max_length=200
    )

    institution = models.CharField(
        max_length=200,
        blank=True
    )

    category = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    entry_requirements = models.TextField(
        blank=True
    )

    duration = models.CharField(
        max_length=100,
        blank=True
    )

    image = models.ImageField(
        upload_to="tvet/",
        blank=True,
        null=True
    )

    website = models.URLField(
        blank=True
    )

    def __str__(self):

        return self.name    
# ==========================================
# CAREER
# ==========================================

class Career(models.Model):

    name = models.CharField(
        max_length=200
    )

    category = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    subjects = models.TextField(
        blank=True,
        help_text="Recommended subjects or school subjects."
    )

    skills = models.TextField(
        blank=True,
        help_text="Important skills for this career."
    )

    image = models.ImageField(
        upload_to="careers/",
        blank=True,
        null=True
    )

    def __str__(self):

        return self.name


# ==========================================
# TVET PROGRAM
# ==========================================

class TVETProgram(models.Model):

    name = models.CharField(
        max_length=200
    )

    institution = models.CharField(
        max_length=200,
        blank=True
    )

    category = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    entry_requirements = models.TextField(
        blank=True
    )

    duration = models.CharField(
        max_length=100,
        blank=True
    )

    image = models.ImageField(
        upload_to="tvet/",
        blank=True,
        null=True
    )

    website = models.URLField(
        blank=True
    )

    def __str__(self):

        return self.name        
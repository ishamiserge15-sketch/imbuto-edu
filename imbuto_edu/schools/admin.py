from django.contrib import admin

from .models import (
    School,
    Sport,
    SchoolSport,
    Competition,
    SchoolCompetition,
    Career,
    TVETProgram,
)


# ==========================================
# SCHOOL ADMIN
# ==========================================

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "district",
        "province",
        "school_type",
        "ownership",
    )

    search_fields = (
        "name",
        "district",
        "province",
    )

    list_filter = (
        "district",
        "province",
        "school_type",
        "ownership",
    )


# ==========================================
# SPORT ADMIN
# ==========================================

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):

    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )


# ==========================================
# SCHOOL SPORT ADMIN
# ==========================================

@admin.register(SchoolSport)
class SchoolSportAdmin(admin.ModelAdmin):

    list_display = (
        "school",
        "sport",
    )

    search_fields = (
        "school__name",
        "sport__name",
    )

    list_filter = (
        "sport",
    )


# ==========================================
# COMPETITION ADMIN
# ==========================================

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
    )

    search_fields = (
        "name",
        "category",
    )

    list_filter = (
        "category",
    )


# ==========================================
# SCHOOL COMPETITION ADMIN
# ==========================================

@admin.register(SchoolCompetition)
class SchoolCompetitionAdmin(admin.ModelAdmin):

    list_display = (
        "school",
        "competition",
        "year",
        "position",
    )

    search_fields = (
        "school__name",
        "competition__name",
    )

    list_filter = (
        "year",
        "competition",
    )
    # ==========================================
# CAREER ADMIN
# ==========================================

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
    )

    search_fields = (
        "name",
        "category",
    )

    list_filter = (
        "category",
    )


# ==========================================
# TVET PROGRAM ADMIN
# ==========================================

@admin.register(TVETProgram)
class TVETProgramAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "institution",
        "category",
        "duration",
    )

    search_fields = (
        "name",
        "institution",
        "category",
    )

    list_filter = (
        "category",
    )
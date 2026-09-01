from django.contrib import admin

from .models import (
    School,
    Sport,
    SchoolSport,
    Competition,
    SchoolCompetition,
    Career,
    TVETProgram,
    SchoolAccount,
    SchoolVerification,
    SchoolRegistrationRequest,
    SchoolActivity,
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
    # ==========================================
# SCHOOL ACCOUNT ADMIN
# ==========================================

@admin.register(SchoolAccount)
class SchoolAccountAdmin(admin.ModelAdmin):

    list_display = (
        "school",
        "email",
        "phone",
        "status",
        "created_at",
    )

    search_fields = (
        "school__name",
        "email",
        "phone",
    )

    list_filter = (
        "status",
    )
    # ==========================================
# SCHOOL VERIFICATION ADMIN
# ==========================================

@admin.register(SchoolVerification)
class SchoolVerificationAdmin(admin.ModelAdmin):

    list_display = (
        "school",
        "status",
        "submitted_at",
        "reviewed_at",
    )

    search_fields = (
        "school__name",
    )

    list_filter = (
        "status",
    )
    # ==========================================
# SCHOOL REGISTRATION REQUEST ADMIN
# ==========================================

@admin.register(SchoolRegistrationRequest)
class SchoolRegistrationRequestAdmin(admin.ModelAdmin):

    list_display = (
        "school_name",
        "district",
        "contact_person",
        "email",
        "status",
        "created_at",
    )

    search_fields = (
        "school_name",
        "district",
        "contact_person",
        "email",
        "phone",
    )

    list_filter = (
        "status",
        "district",
        "province",
    )

    readonly_fields = (
        "created_at",
        "reviewed_at",
    )
# ==========================================
# SCHOOL ACTIVITY ADMIN
# ==========================================

@admin.register(SchoolActivity)
class SchoolActivityAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "school",
        "activity_date",
        "is_published",
        "created_at",
    )

    search_fields = (
        "title",
        "school__name",
        "description",
    )

    list_filter = (
        "is_published",
        "activity_date",
        "school",
    )

    ordering = (
        "-activity_date",
    )    
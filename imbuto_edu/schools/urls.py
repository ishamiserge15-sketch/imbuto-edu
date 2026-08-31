from django.urls import path

from . import views


urlpatterns = [

    # HOME
    path(
        '',
        views.home,
        name='home'
    ),

    # EXPLORE SCHOOLS
    path(
        'schools/',
        views.schools_page,
        name='schools_page'
    ),

    # SCHOOL DETAIL
    path(
        'school/<int:school_id>/',
        views.school_detail,
        name='school_detail'
    ),

    # COMPARE SCHOOLS
    path(
        'compare/',
        views.compare_schools,
        name='compare_schools'
    ),

    # TOP SCHOOLS
    path(
        'top-schools/',
        views.top_schools,
        name='top_schools'
    ),

    # SPORTS
    path(
        'sports/',
        views.sports,
        name='sports'
    ),

    # COMPETITIONS
    path(
        'competitions/',
        views.competitions,
        name='competitions'
    ),

    # CAREERS & TVET
    path(
        'careers/',
        views.careers,
        name='careers'
    ),

]
path(
    "register-school/",
    views.register_school,
    name="register_school"
),

path(
    "registration-success/",
    views.registration_success,
    name="registration_success"
),
path(
    "school-login/",
    views.school_login,
    name="school_login"
),

path(
    "school-dashboard/",
    views.school_dashboard,
    name="school_dashboard"
),

path(
    "school-logout/",
    views.school_logout,
    name="school_logout"
),
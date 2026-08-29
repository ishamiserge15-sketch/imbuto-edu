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
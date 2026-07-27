from django.urls import path

from . import views


urlpatterns = [

    path(

        '',

        views.home,

        name='home'

    ),

    path(

        'schools/',

        views.schools_page,

        name='schools_page'

    ),

    path(

        'school/<int:school_id>/',

        views.school_detail,

        name='school_detail'

    ),

    path(

        'top-schools/',

        views.top_schools,

        name='top_schools'

    ),

    path(

        'sports/',

        views.sports,

        name='sports'

    ),

    path(

        'competitions/',

        views.competitions,

        name='competitions'

    ),

    path(

        'careers/',

        views.careers,

        name='careers'

    ),

]
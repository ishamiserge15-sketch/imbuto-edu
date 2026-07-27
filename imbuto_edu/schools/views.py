from django.shortcuts import render, get_object_or_404

from .models import School


def home(request):

    schools = School.objects.all()

    return render(

        request,

        "index.html",

        {

            "schools": schools

        }

    )


def school_detail(request, school_id):

    school = get_object_or_404(

        School,

        id=school_id

    )

    return render(

        request,

        "school_detail.html",

        {

            "school": school

        }

    )


def schools_page(request):

    schools = School.objects.all()

    search = request.GET.get("search")

    district = request.GET.get("district")

    school_type = request.GET.get("school_type")

    ownership = request.GET.get("ownership")


    if search:

        schools = schools.filter(

            name__icontains=search

        )


    if district:

        schools = schools.filter(

            district=district

        )


    if school_type:

        schools = schools.filter(

            school_type=school_type

        )


    if ownership:

        schools = schools.filter(

            ownership=ownership

        )


    districts = (

        School.objects

        .values_list(

            "district",

            flat=True

        )

        .distinct()

        .order_by("district")

    )


    return render(

        request,

        "schools.html",

        {

            "schools": schools,

            "districts": districts

        }

    )


def top_schools(request):

    schools = School.objects.all()

    return render(

        request,

        "top_schools.html",

        {

            "schools": schools

        }

    )


def sports(request):

    return render(

        request,

        "sports.html"

    )


def competitions(request):

    return render(

        request,

        "competitions.html"

    )


def careers(request):

    return render(

        request,

        "careers.html"

    )
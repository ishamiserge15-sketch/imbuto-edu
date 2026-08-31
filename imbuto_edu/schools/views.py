from django.db.models import Q

from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)

from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from django.contrib.auth.decorators import login_required

from .models import (
    School,
    Sport,
    SchoolSport,
    SchoolAccount,
)

from .forms import SchoolRegistrationForm


# ==========================================
# HOME PAGE
# ==========================================

def home(request):

    schools = School.objects.all().order_by("name")

    return render(
        request,
        "index.html",
        {
            "schools": schools
        }
    )


# ==========================================
# EXPLORE SCHOOLS
# ==========================================

def schools_page(request):

    schools = School.objects.all()

    search = request.GET.get("search", "").strip()
    district = request.GET.get("district", "").strip()
    school_type = request.GET.get("school_type", "").strip()
    ownership = request.GET.get("ownership", "").strip()


    if search:

        schools = schools.filter(

            Q(name__icontains=search) |
            Q(district__icontains=search) |
            Q(province__icontains=search)

        )


    if district:

        schools = schools.filter(
            district__iexact=district
        )


    if school_type:

        schools = schools.filter(
            school_type__iexact=school_type
        )


    if ownership:

        schools = schools.filter(
            ownership__iexact=ownership
        )


    schools = schools.order_by("name")


    # Dynamic filter options

    districts = (
        School.objects
        .exclude(district__isnull=True)
        .exclude(district="")
        .values_list("district", flat=True)
        .distinct()
        .order_by("district")
    )


    school_types = (
        School.objects
        .exclude(school_type__isnull=True)
        .exclude(school_type="")
        .values_list("school_type", flat=True)
        .distinct()
        .order_by("school_type")
    )


    ownerships = (
        School.objects
        .exclude(ownership__isnull=True)
        .exclude(ownership="")
        .values_list("ownership", flat=True)
        .distinct()
        .order_by("ownership")
    )


    return render(
        request,
        "schools.html",
        {
            "schools": schools,
            "search": search,
            "district": district,
            "school_type": school_type,
            "ownership": ownership,
            "districts": districts,
            "school_types": school_types,
            "ownerships": ownerships,
        }
    )


# ==========================================
# SCHOOL DETAIL
# ==========================================

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


# ==========================================
# COMPARE SCHOOLS
# ==========================================

def compare_schools(request):

    school_ids = request.GET.getlist("compare")


    if len(school_ids) > 2:

        return render(
            request,
            "compare_schools.html",
            {
                "schools": [],
                "comparison_error":
                    "Select up to 2 schools to compare."
            }
        )


    schools = School.objects.filter(
        id__in=school_ids
    ).order_by("name")


    return render(
        request,
        "compare_schools.html",
        {
            "schools": schools
        }
    )


# ==========================================
# TOP SCHOOLS / RANKINGS
# ==========================================

def top_schools(request):

    schools = School.objects.all()


    # Ranking category

    ranking = request.GET.get(
        "ranking",
        "overall"
    )


    if ranking == "academic":

        schools = schools.order_by(
            "-academic_score",
            "name"
        )


    elif ranking == "sports":

        schools = schools.order_by(
            "-sports_score",
            "name"
        )


    elif ranking == "innovation":

        schools = schools.order_by(
            "-innovation_score",
            "name"
        )


    else:

        schools = schools.order_by(
            "-academic_score",
            "-sports_score",
            "-innovation_score",
            "name"
        )


    return render(
        request,
        "top_schools.html",
        {
            "schools": schools,
            "ranking": ranking
        }
    )


# ==========================================
# SPORTS
# ==========================================

def sports(request):

    sports = Sport.objects.all().order_by("name")

    selected_sport = request.GET.get(
        "sport",
        ""
    ).strip()


    school_sports = SchoolSport.objects.select_related(
        "school",
        "sport"
    )


    if selected_sport:

        school_sports = school_sports.filter(
            sport__id=selected_sport
        )


    return render(
        request,
        "sports.html",
        {
            "sports": sports,
            "school_sports": school_sports,
            "selected_sport": selected_sport,
        }
    )


def competitions(request):

    return render(
        request,
        "competitions.html"
    )


# ==========================================
# CAREERS & TVET
# ==========================================

def careers(request):

    return render(
        request,
        "careers.html"
    )
# ==========================================
# SCHOOL REGISTRATION
# ==========================================

def register_school(request):

    if request.method == "POST":

        form = SchoolRegistrationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("registration_success")

    else:

        form = SchoolRegistrationForm()

    return render(
        request,
        "register_school.html",
        {
            "form": form
        }
    )


# ==========================================
# REGISTRATION SUCCESS
# ==========================================

def registration_success(request):

    return render(
        request,
        "registration_success.html"
    )
# ==========================================
# SCHOOL LOGIN
# ==========================================

def school_login(request):

    if request.user.is_authenticated:

        if hasattr(request.user, "school_account"):
            return redirect("school_dashboard")

    if request.method == "POST":

        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        try:

            school_account = SchoolAccount.objects.get(
                email=email
            )

            if not school_account.user:

                return render(
                    request,
                    "school_login.html",
                    {
                        "error":
                        "This school account has not been activated yet."
                    }
                )

            user = authenticate(
                request,
                username=school_account.user.username,
                password=password,
            )

            if user is not None:

                login(request, user)

                return redirect("school_dashboard")

            return render(
                request,
                "school_login.html",
                {
                    "error": "Invalid email or password."
                }
            )

        except SchoolAccount.DoesNotExist:

            return render(
                request,
                "school_login.html",
                {
                    "error": "Invalid email or password."
                }
            )

    return render(
        request,
        "school_login.html"
    )


# ==========================================
# SCHOOL DASHBOARD
# ==========================================

@login_required
def school_dashboard(request):

    if not hasattr(request.user, "school_account"):

        logout(request)

        return redirect("school_login")

    school_account = request.user.school_account

    return render(
        request,
        "school_dashboard.html",
        {
            "school_account": school_account,
            "school": school_account.school,
        }
    )


# ==========================================
# SCHOOL LOGOUT
# ==========================================

def school_logout(request):

    logout(request)

    return redirect("school_login")    
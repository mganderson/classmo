from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse

from schedules.models import Subject, Session, Registration
from schedules.services import portal_tools
from schedules.services.portal_tools import instructors_only, students_only


@login_required
@students_only
def subjects(request, request_type):
    """
    List all subjects in the system
    """
    user = request.user
    my_courses = ""
    all_courses = ""
    
    if request_type == "all":
        all_courses = "active-link-blue"
        subjects = Subject.objects.all()
    else:
        my_courses = "active-link-blue"
        subjects = Registration.subjects_for_student(user.id)

    context = {
        "courses": subjects,
        "my_courses":my_courses,
        "all_courses":all_courses
    }
    return render(request, 'schedules/subjects/list.html', context)

@login_required
@students_only
def detail(request, subject_id):
    """
    Display details for a given subject.
    """
    context = {}
    try:
        subject = Subject.objects.get(pk=subject_id)
        context['subject'] = subject
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")

    # load current sessions for this subject
    sessions = Session.objects.filter(subject=subject_id)
    context['sessions'] = sessions
    return render(request, 'schedules/subjects/detail.html', context)

@login_required
@instructors_only
def sessions(request, subject_id):
    """
    Display sessions for a given subject.
    """
    context = {}
    try:
        subject = Subject.objects.get(pk=subject_id)
        sessions = Session.objects.filter(subject=subject_id)
        context['sessions'] = sessions
        context['subject'] = subject
    except Subject.DoesNotExist:
        raise Http404("Sessions does not exist")

    return render(request, 'schedules/subjects/sessions.html', context)

@login_required
def session(request, session_id):
    """
    Display details for a given session of a subject.
    """
    current_user = request.user
    is_instructor = portal_tools.is_member(current_user, settings.GROUPS["INSTRUCTORS"])
    is_student = portal_tools.is_member(current_user, settings.GROUPS["STUDENTS"])

    context = {}
    try:
        session = Session.objects.get(pk=session_id)
        context = {
            "session":session,
            "is_instructor":is_instructor,
            "is_student":is_student
        }
    except Subject.DoesNotExist:
        raise Http404("Session does not exist")

    return render(request, 'schedules/subjects/session.html', context)



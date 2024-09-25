from django.shortcuts import render, redirect
from .models import About
from .forms import CollaborateForm, leaveCommentForm
from django.contrib import messages

def about_me(request):
    """
    Renders the About page with CollaborateForm and leaveCommentForm.
    """

    # Handle POST request for both forms
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        leavecomment_form = leaveCommentForm(data=request.POST)

        if 'collaborate_submit' in request.POST and collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Your request is received! I endeavour to respond within 3 working days.")
            return redirect('about_me')  # Redirect to avoid form resubmission

        if 'leavecomment_submit' in request.POST and leavecomment_form.is_valid():
            leavecomment_form.save()
            messages.add_message(request, messages.SUCCESS, "Your comments are noted.")
            return redirect('about_me')  # Redirect to avoid form resubmission

    else:
        # Instantiate empty forms for GET request
        collaborate_form = CollaborateForm()
        leavecomment_form = leaveCommentForm()

    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request, "about/about.html", {
            "about": about,
            "collaborate_form": collaborate_form,
            "leavecomment_form": leavecomment_form
        },
    )

def leavecomment_edit(request):
    """
    View to edit leavecomments (CRUD functionality to be added later).
    """
    if request.method == "POST":
        leavecomment_form = leaveCommentForm(data=request.POST)
        if leavecomment_form.is_valid():
            leavecomment_form.save()
            messages.add_message(request, messages.SUCCESS, "Your comments are noted.")
    # You can expand this function later to include update/delete logic

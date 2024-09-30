from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import About, LeaveComment
from .forms import CollaborateForm, LeaveCommentForm
from django.contrib import messages

def about_me(request):
    """
    Renders the About page with CollaborateForm and LeaveCommentForm, and lists comments.
    """

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        leavecomment_form = LeaveCommentForm(data=request.POST)

        # Handle Collaborate form submission
        if 'collaborate_submit' in request.POST and collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Your request is received! I endeavour to respond within 3 working days.")
            return redirect('about_me')  # Redirect to prevent form resubmission

        # Handle Leave Comment form submission
        if 'leavecomment_submit' in request.POST and leavecomment_form.is_valid():
            leavecomment_form.save()
            messages.add_message(request, messages.SUCCESS, "Your comments are noted.")
            return redirect('about_me')  # Redirect after comment submission

    else:
        collaborate_form = CollaborateForm()
        leavecomment_form = LeaveCommentForm()

    # Fetch the 'About' content
    about = About.objects.all().order_by('-updated_on').first()

    # If user is not logged in, show all comments
    if not request.user.is_authenticated:
        leavecomments = LeaveComment.objects.all().order_by("-created_on")
    # If user is logged in, show all comments but only allow their comments for edit
    else:
        leavecomments = LeaveComment.objects.all().order_by("-created_on")

    return render(
        request, "about/about.html", {
            "about": about,
            "collaborate_form": collaborate_form,
            "leavecomment_form": leavecomment_form,
            "leavecomments": leavecomments,  # Pass the comments to the template
        }
    )

def leavecomment_edit(request, leavecomment_id):
    """
    View to edit LeaveComments
    """
    leavecomment = get_object_or_404(LeaveComment, pk=leavecomment_id)

    if request.method == "POST":
        leavecomment_form = LeaveCommentForm(data=request.POST, instance=leavecomment)

        # Ensure only the comment owner can edit their comment
        if leavecomment_form.is_valid() and leavecomment.email == request.user.email:
            leavecomment_form.save()
            leavecomment.approved = False
            messages.add_message(request, messages.SUCCESS, "Your comment has been updated.")
            return HttpResponseRedirect(reverse('about_me'))
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment.")
    
    else:
        leavecomment_form = LeaveCommentForm(instance=leavecomment)

    return render(request, "about/edit_comment.html", {
        "leavecomment_form": leavecomment_form, "leavecomment": leavecomment
    })

def leavecomment_delete(request, leavecomment_id):
    """
    View to delete LeaveComments. Ensures only the comment owner can delete their comment.
    """
    leavecomment = get_object_or_404(LeaveComment, pk=leavecomment_id)

    # Check if the user is authenticated
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, "You need to be logged in to delete a comment.")
        return redirect('about_me')  # Redirect to the about page if not authenticated
    print(request.method)
    if request.method == "GET":
        
        if leavecomment.email == request.user.email:
            leavecomment.delete()
            messages.add_message(request, messages.SUCCESS, "Your comment has been deleted.")
        else:
            messages.add_message(request, messages.ERROR, "You are not authorized to delete this comment.")
        
        return redirect('about_me')  #redirect to about page

    messages.add_message(request, messages.ERROR, "Invalid request method.")
    return redirect('about_me')  # Use redirect() here as well

    
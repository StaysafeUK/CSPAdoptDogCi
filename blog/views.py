from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Comment, Post, Sanctuary, account_activation_token
from .forms import CommentForm, SignupForm

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str
from django.utils.encoding import force_bytes
from django.http import HttpResponse




# authentication imports
# try:
#     from django.utils.encoding import force_str  # Django 3.x and above
# except ImportError:
#     from django.utils.encoding import force_text as force_str
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from .forms import SignupForm
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_str
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from .tokens import account_activation_token
# from django.contrib.auth.models import User
# from django.core.mail import EmailMessage


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6
    
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    **Context**
    
    ``post``
    An instance of :model:`blog.Post`.
    
    **Template:**
    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment submitted and awaiting approval')

    comment_form = CommentForm()

    return render(request, "blog/post_detail.html", {"post": post, "comments": comments, "comment_count": comment_count, "comment_form": comment_form, },)

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
       
def search_sanctuaries(request):
    if request.method == "POST":
        searched = request.POST['searched']
        sanctuaries = Sanctuary.objects.filter(sanct_name__icontains=searched)
        send_mail('Test Message', 'So youve got search working. now get ON with it', 'adoptdog@verifyus.co.uk', ['justin.robert.evans@protonmail.com'], fail_silently=False)

        return render(request, 'blog/search_sanctuaries.html', {'searched':searched, 'sanctuaries':sanctuaries})
    else:
        return render(request, 'blog/search_sanctuaries.html', {})

def dog_detail(request, slug):
    dog = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/dog_detail.html', {'dog': dog})

def signup(request):
    """
    View for signing up a new user.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Account needs email verification
            user.save()
            
            # Prepare email activation
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': force_str(urlsafe_base64_encode(force_bytes(user.pk))),
            'token': account_activation_token.make_token(user),
        })
            
            # Send the email
            to_email = form.cleaned_data.get('email')
            # email = EmailMessage(mail_subject, message, to=[to_email])
            # email.send()
            
            send_mail('Horrar or Nah Message', message, 'adoptdog@verifyus.co.uk', [to_email], fail_silently=False)
            
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def activate_account(request, uidb64, token):
    try:
        # Decode the UID to get the user's primary key (pk)
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # Check if the token is valid for the user
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for confirming your email. Your account has been activated.')
    else:
        return HttpResponse('Activation link is invalid or has expired.')
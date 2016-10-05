from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils.translation import ugettext_lazy as _


from .admin import UserCreationForm
from .forms import LoginForm, ProfileForm, AccountForm
from .models import Account, Profile


@login_required(login_url="accounts/login/")
def home(request):
    user = request.user
    first_name = user.first_name
    context = {
    "first_name" : first_name,
    }
    return render(request,"home.html", context)


def account_login(request):
    if request.user.is_authenticated():
        return redirect("/")
    else:
        form = LoginForm(request.POST or None)
        next_url = request.GET.get('next')
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
        	    login(request, user)
        	    if next_url is not None:
        		    return HttpResponseRedirect(next_url)
            return HttpResponseRedirect("/")
        title = "Login"
        submit_btn = title
        submit_btn_class = "btn-success btn-block"
        context = {
        "form": form,
        "title": title,
        "submit_btn": submit_btn,
        "submit_btn_class": submit_btn_class,
        }
        return render(request, "login.html", context)


def signup(request):
    if request.user.is_authenticated():
        return redirect("/")
    else:
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password2']
            #MyUser.objects.create_user(first_name=first_name, email=email, password=password)
            new_user = Account()
            new_user.email = email
            new_user.first_name = first_name
            #new_user.password = password #WRONG
            new_user.set_password(password) #RIGHT
            new_user.save()
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
            return HttpResponseRedirect("/")

        title = "Register"
        submit_btn = "Create free account"

        context = {
        "form": form,
        "title": title,
        "submit_btn": submit_btn
        }
        return render(request, "signup.html", context)


# @transaction.atomic
@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = AccountForm(request.POST or None, instance=request.user)
        profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('authentication:profile_detail')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = AccountForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def profile_detail(request):
    user = request.user
    profile = user.profile
    context = {
    "user": user,
    "profile": profile,
    }
    return render(request, "profile.html", context)

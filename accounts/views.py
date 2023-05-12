from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # hashing the password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, f'Your account has been created! You are now able to log in')

            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password'],
                                    )
            login(request, new_user)

            return redirect('home')  # redirect to the home page after registration
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
        return render(request, 'shop/accounts/register.html', {'user_form': user_form, 'profile_form': profile_form})


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'shop/accounts/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'shop/accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'shop/accounts/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')  # Replace 'home' with your desired redirect URL
        else:
            # Handle invalid login credentials
            pass
    return render(request, 'shop/accounts/login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')  # Replace 'home' with your desired redirect URL

def reset_password(request):
    # Implement password reset logic here
    pass


class CustomPasswordResetView(PasswordResetView):
    template_name = 'shop/accounts/password_reset.html'
    email_template_name = 'shop/accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'shop/accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important, to update the session with the new password
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:password_change_done')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'shop/accounts/password_change.html', {
        'form': form
    })

def password_change_done(request):
    return render(request, 'shop/accounts/password_change_done.html')




from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from orders.models import Orders
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


#@login_required
def profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    orders = Orders.objects.filter(user_id=request.user.id)
    context = {
        'profile': profile,
        'orders_list': orders,

    }
    return render(request, 'user/profile.html', context=context)


def update(request, user_id):

    try:
        profile = Profile.objects.get(user_id=user_id)
    except Profile.DoesNotExist:
        return redirect('home')

    try:
        user = User.objects.get(id=user_id)
    except Profile.DoesNotExist:
        return redirect('home')

    p_form = ProfileUpdateForm(instance=profile)
    u_form = UserUpdateForm(instance=user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile')

    context = {
        "p_form": p_form,
        "u_form": u_form,
    }

    return render(request, 'user/update.html', context=context)





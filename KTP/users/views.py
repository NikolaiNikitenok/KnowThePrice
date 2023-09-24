from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        reg_form_u = UserRegisterForm(request.POST)
        # reg_form_p = ProfileRegisterForm(request.POST)
        
        if reg_form_u.is_valid():
            reg_form_u.save()
            # reg_form_p.save()
            username = reg_form_u.cleaned_data.get('username')
            messages.success(request, f'Your accaunt has been created! You are now able to log in')
            return redirect('login')
    else:
        reg_form_u = UserRegisterForm()
        # reg_form_p = ProfileRegisterForm()
        
    context = {
        'reg_form_u': reg_form_u,
        # 'reg_form_p': reg_form_p
    }
    
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/profile.html', context)
    

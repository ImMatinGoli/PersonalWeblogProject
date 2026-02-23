from django.shortcuts import render
from accounts.forms import CustomUserCreationForm, CustomUserUpdateForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

# def signup_view(request):
#     form = CustomUserCreationForm(request.POST or None)
#     if request.method == 'POST':
#         user = CustomUserCreationForm(request.POST)
#         if user.is_valid():
#             user = user.save()
#             return redirect('login')
#     else:
#         pass
#     return render(request, 'accounts/../templates/signup.html', context={'form': form})



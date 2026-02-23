from django.shortcuts import render, redirect
from blog.models import BlogPost, ContactMessage, Category
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomUserUpdateForm
from django.contrib import messages


def home_page_view(request):
    latest_posts = BlogPost.objects.all().order_by('-datetime_created')[:2]
    categories = Category.objects.all()

    context = {
        'posts': latest_posts,
        'categories': categories,
    }
    return render(request, 'pages/home.html', context)

def about_me_page_view(request):
    return render(request, 'pages/about_me.html')

def contact_me_page_view(request):
    if request.method == "POST":
        contact_message = ContactMessage()
        contact_message.name = request.POST['name']
        contact_message.email = request.POST['email']
        contact_message.message = request.POST['message']
        contact_message.subject = request.POST['subject']
        contact_message.save()
        return render(request, 'pages/contact_success.html')
    else:
        return render(request, 'pages/contact_me.html')


@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "پروفایلت با موفقیت آپدیت شد، متین جان!")
            return redirect('my_profile')
    else:
        form = CustomUserUpdateForm(instance=request.user)

    return render(request, 'pages/profile.html', {'form': form})

@login_required
def reset_avatar_view(request):
    if request.method == 'POST':
        user = request.user

        default_avatar = user._meta.get_field('avatar').default

        if user.avatar and user.avatar.name != default_avatar:

            user.avatar.delete(save=False)

            user.avatar = default_avatar
            user.save()

        return redirect('my_profile')
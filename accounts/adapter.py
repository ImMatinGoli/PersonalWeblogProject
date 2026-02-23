from allauth.account.adapter import DefaultAccountAdapter
from django.contrib import messages
from django.urls import reverse


class MyAccountAdapter(DefaultAccountAdapter):

    def get_password_change_redirect_url(self, request):
        # 🟢 بعد از تغییر رمز، کاربر رو بفرست به صفحه لاگین
        return reverse('account_login')

    def add_message(self, request, level, message_template, message_context=None, extra_tags=''):
        # 🟢 مدیریت و فارسی‌سازی تمام پیام‌ها در یک متد
        if 'signed_up' in message_template:
            message_template = 'ثبت‌نام شما با موفقیت انجام شد. به وبلاگ خوش اومدی! 🎉'

        elif 'signed_in' in message_template:
            # می‌تونی چک کنی اگه یوزر خودتی بنویسه متین، وگرنه اسم همون کاربر رو بگه
            full_name = request.user.get_full_name() or request.user.username
            message_template = f'خوش برگشتی {full_name} عزیز! ✨'

        elif 'password_changed' in message_template:
            message_template = 'رمز عبور شما با موفقیت تغییر کرد. حالا با رمز جدید وارد شوید. 🔐'

        return super().add_message(request, level, message_template, message_context, extra_tags)
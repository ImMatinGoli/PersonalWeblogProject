from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaulttags import comment
from django.urls import reverse
from jalali_date import datetime2jalali


def persian_numbers(text):
    english_digits = '0123456789'
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    # متد maketrans یک جدول ترجمه می‌سازه و translate اعداد رو جایگزین می‌کنه
    translation_table = str.maketrans(english_digits, persian_digits)
    return str(text).translate(translation_table)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="نام دسته‌بندی")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات (اختیاری)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'


class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('drf', 'Draft'),
        ('pub', 'Published'),
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='drf')
    cover = models.ImageField(null=True, blank=True, default='covers/default_cover.png', upload_to='covers/')
    categories = models.ManyToManyField(
        Category,
        related_name='posts',
        verbose_name="دسته‌بندی‌ها"
    )
    likes = models.ManyToManyField(get_user_model(), related_name='blog_posts', blank=True)

    def __str__(self):
        return f'{self.title} by {self.author}'

    def total_likes(self):
        return self.likes.count()

    def get_jalali_date(self):
        jalali_datetime = datetime2jalali(self.datetime_created)
        months = [
            "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
            "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
        ]

        date_str = f"{jalali_datetime.day} {months[jalali_datetime.month - 1]} {jalali_datetime.year}"
        return persian_numbers(date_str)


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    STATUS_CHOICES = (
        ('drf', 'Draft'),
        ('pub', 'Published'),
    )
    STARS_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    datetime_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='drf')
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    stars = models.PositiveIntegerField(choices=STARS_CHOICES, default=1, blank=True, null=True)

    class Meta:
        ordering = ['-datetime_created']

    def get_jalali_date(self):
        jalali_datetime = datetime2jalali(self.datetime_created)
        months = [
            "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
            "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
        ]

        date_str = f"{jalali_datetime.day} {months[jalali_datetime.month - 1]} {jalali_datetime.year}"
        return persian_numbers(date_str)


    def __str__(self):
        return f'{self.id} : {self.author} -> {self.post}'


from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام فرستنده')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=200, blank=True, null=True, verbose_name='موضوع')
    message = models.TextField(verbose_name='متن پیام')

    is_read = models.BooleanField(default=False, verbose_name='خوانده شده')
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')

    class Meta:
        ordering = ['-datetime_created']
        verbose_name = 'پیام تماس'
        verbose_name_plural = 'پیام‌های تماس'

    def __str__(self):
        return f"پیام از {self.name} - {self.subject or 'بدون موضوع'}"

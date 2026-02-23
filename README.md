# 🚀 Matin's Personal Blog | وبلاگ شخصی متین

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

این پروژه یک وبلاگ مدرن و کامل است که به عنوان پروژه سال آخر علوم کامپیوتر توسعه یافته است. تمرکز اصلی این پروژه بر روی امنیت، تجربه کاربری (UX) و مدیریت بهینه داده‌ها بوده است.

## ✨ قابلیت‌های کلیدی (Key Features)

* **🔍 جستجوی زنده (Live Search):** پیاده‌سازی سیستم جستجوی آنی با استفاده از AJAX و JavaScript برای نمایش نتایج بدون رفرش صفحه.
* **📅 تاریخ شمسی (Jalaali Date):** بومی‌سازی کامل سیستم تاریخ در تمامی بخش‌های سایت (پست‌ها و کامنت‌ها).
* **👤 پنل کاربری پیشرفته (User Dashboard):** امکان مدیریت پروفایل، آپلود آواتار و قابلیت ریست کردن تصویر به حالت پیش‌فرض.
* **📂 مدیریت محتوا (CRUD):** سیستم کامل ایجاد، ویرایش و حذف مقالات با قابلیت انتخاب دسته‌بندی‌های چندگانه (ManyToMany).
* **🛡️ سطوح دسترسی اختصاصی (Role-based Auth):** محدودیت دسترسی به بخش‌های مدیریتی فقط برای مدیر اصلی (matin).
* **📄 صفحه‌بندی هوشمند (Pagination):** مدیریت نمایش پست‌ها (۴ مورد در هر صفحه) برای بهینه‌سازی سرعت لود.
* **💬 سیستم تعامل:** قابلیت ثبت نظر با سیستم امتیازدهی ستاره‌ای و لایک کردن مقالات به صورت AJAX.

## 🛠 تکنولوژی‌های استفاده شده (Tech Stack)

* **Backend:** Python 3.x, Django 5.x
* **Frontend:** HTML5, CSS3 (Custom Design), JavaScript (Vanilla)
* **Security:** Environs (Environment Variables Management)
* **Tools:** WhiteNoise (Static Files Management), Gunicorn (Production Ready)

## 🚀 راه اندازی پروژه (Setup Instructions)

۱. ابتدا پروژه را کلون کنید:
```bash
git clone https://github.com/matin-dev/blog-django.git
```

۲. یک محیط مجازی ساخته و پکیج‌ها را نصب کنید:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

۳. فایل `.env` را بر اساس نمونه ساخته و کلیدهای امنیتی خود را قرار دهید:
```env
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=127.0.0.1,localhost
```

۴. دیتابیس را مهاجرت داده و سرور را اجرا کنید:
```bash
python manage.py migrate
python manage.py runserver
```

---

## 👨‍💻 توسعه دهنده
**متین** - دانشجوی سال آخر علوم کامپیوتر
* ارتباط با من: [GitHub Profile](https://github.com/matin)

---

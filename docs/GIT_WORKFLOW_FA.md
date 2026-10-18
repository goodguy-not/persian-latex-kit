# راه‌اندازی مخزن روی GitHub (Windows)

## ساخت اولین مخزن

۱. در GitHub یک **Private** repository با نام `persian-latex-kit` بساز. هنگام ساخت گزینهٔ README / .gitignore / License را انتخاب نکن؛ این فایل‌ها در بسته موجودند.
۲. این پوشه را در مسیر دلخواه (مثلاً `E:\Projects\persian-latex-kit`) از حالت فشرده خارج کن.
۳. در همان پوشه PowerShell یا Git Bash باز کن و اجرا کن:

```powershell
git init -b main
git add .
git commit -m "Initial reusable Persian LaTeX Kit"
git remote add origin https://github.com/YOUR_USERNAME/persian-latex-kit.git
git push -u origin main
```

اگر `git` شناخته نشد، Git for Windows را از https://git-scm.com/download/win نصب کن و ترمینال را دوباره باز کن. اگر Git برای نام و ایمیل سؤال پرسید، از اطلاعات گیت خودت استفاده کن:

```powershell
git config --global user.name "YOUR_NAME"
git config --global user.email "YOUR_EMAIL"
```

برای HTTPS ممکن است Git Credential Manager مرورگر را برای ورود به GitHub باز کند؛ رمز عبور GitHub را در خط فرمان به‌جای توکن وارد نکن.

## آپدیت کتابخانه

هر بار که قطعه‌ای طراحی یا اصلاح شد:

```powershell
git status
git add .
git commit -m "Add reusable component: ..."
git push
```

برای برگشت به نسخه‌های قبلی:

```powershell
git log --oneline
```

## استفادهٔ مجدد در هر پروژه

۱. یک پوشهٔ مستقل برای تمرین یک درس بساز.
۲. فایل‌های `templates/assignment` را در آن کپی کن.
۳. داخل همان پوشه پروژه:

```powershell
git init
git submodule add https://github.com/YOUR_USERNAME/persian-latex-kit.git vendor/persian-latex-kit
```

۴. در `main.tex` می‌توانی با `\usepackage{vendor/persian-latex-kit/tex/persian-kit}` از کتابخانه استفاده کنی.
۵. بعداً فقط وقتی نسخه جدید را می‌خواهی، Submodule را آپدیت کن و در پروژهٔ خودت commit بزن. این کار سازگاری تمرین‌های قدیمی را حفظ می‌کند.

**نکتهٔ حریم خصوصی:** قبل از انتشار عمومی، مطمئن شو نام، شمارهٔ دانشجویی و محتوای تمرین واقعی داخل ریپوی قالب‌ها نیست.

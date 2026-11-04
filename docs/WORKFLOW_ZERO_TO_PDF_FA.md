# از پروژهٔ تازه تا PDF

این راهنما برای پروژه‌های **مستقل** ساخته‌شده با Persian LaTeX Kit است. پاسخ،
مشخصات شخصی و فایل‌های هر سند را خارج از مخزن کتابخانه نگه دارید.

## ۱. نصب یک‌باره

Python 3 برای مولد لازم است. برای PDF، TeX Live یا MiKTeX شامل XeLaTeX،
XePersian و بسته‌های موردنیاز قالب، به‌علاوهٔ فونت Vazirmatn را نصب کنید.
TeXstudio اختیاری است؛ کامپایلر آن را XeLaTeX قرار دهید. اسکریپت ساخت پروژه
جایگزین کامپایلر لاتک نیست. Git و اینترنت برای حالت پیش‌فرض لازم نیستند.

در Windows:
```powershell
python --version
xelatex --version
.\scripts\new-assignment.ps1 -Destination "C:\Documents\assignment-1"
```

در Ubuntu/Linux:
```sh
python3 --version
xelatex --version
python3 scripts/new-project.py --template assignment --destination "$HOME/Documents/assignment-1"
```

مقصد نباید از قبل وجود داشته باشد. قالب‌های دیگر `lab-report` و
`os-single-question` هستند؛ [README](../README.md) فرمان‌های هر سه را دارد.
مولد فایل‌های استایل لازم را در `vendor/persian-latex-kit/tex/` کپی می‌کند.
این نسخهٔ ثابت خودکار به‌روزرسانی نمی‌شود.

اگر PowerShell اجرای اسکریپت را محدود کرد، فقط برای همان پنجره (بدون تغییر
دائمی تنظیمات سیستم) می‌توانید اجرا کنید:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

مولد مقصد موجود را حذف یا بازنویسی نمی‌کند. اگر خطای ساخت رخ داد، پیام را
بررسی کنید و پیش از تکرار، وجود یا نبود مقصد را خودتان کنترل کنید.

## ۲. پیکربندی و محتوا

- `config/metadata.tex`: نام‌ها، عنوان، تاریخ و مشخصات همان سند.
- `config/fonts.tex`: انتخاب اختیاری فونت، **قبل از بارگذاری استایل**.
- `questions/` یا `sections/`: متن سند؛ `main.tex` ترتیب ورود فایل‌ها را
  تعیین می‌کند.
- `assets/`: شکل‌های PNG یا PDF و دیگر دارایی‌های همان سند.

فونت پیش‌فرض فارسی Vazirmatn است. برای Noto Sans Arabic، اگر نصب شده باشد،
در `config/fonts.tex` بنویسید:
```latex
\newcommand{\PLKPersianFont}{Noto Sans Arabic}
```
برای لاتین نیز می‌توان `\PLKLatinFont` را جداگانه تعیین کرد. فونت انتخاب‌شده
در صورت نبودن خطا می‌دهد؛ جایگزین پنهان ندارد.

در نثر فارسی از `\lr{TCP}` برای لاتین مستقل، `\EN{Congestion Control}`
برای معادل انگلیسی داخل پرانتز، و `\Term{کنترل ازدحام}{Congestion Control}`
برای اصطلاح فارسی پررنگ با معادل انگلیسی استفاده کنید. API کامل در
[راهنمای قطعات](COMPONENTS_FA.md) است.

## ۳. کامپایل و بازبینی

فایل `main.tex` را از **ریشهٔ پروژهٔ ساخته‌شده** در TeXstudio با XeLaTeX
اجرا کنید. روش خط فرمان:
```sh
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

اگر `latexmk` در توزیع لاتک موجود است، می‌تواند اجرای مجدد برای ارجاعات
را خودکار انجام دهد و خروجی را در `build/` بگذارد:
```sh
latexmk -xelatex -outdir=build main.tex
```

PDF را برای فونت، جهت RTL/LTR، اعداد، پرانتزها، سرریز جدول/فرمول، ارجاع‌ها
و سربرگ/پابرگ بررسی کنید. در نبود `xelatex`، توزیع لاتک یا PATH را بررسی
کنید؛ در نبود `xepersian.sty`، بستهٔ XePersian را نصب کنید؛ در خطای فونت،
نام آن در `config/fonts.tex` و نصب سیستم را بررسی کنید.

## ۴. کار با دستیار هوش مصنوعی

به دستیار بگویید `AGENTS.md` پروژه، `main.tex`، فایل‌های `config/`،
استایل‌های `vendor/` و صورت‌مسئلهٔ خودتان را پیش از ویرایش بخواند. از او
بخواهید API موجود را از منبع بررسی کند، متن اختصاصی را در پروژه نگه دارد،
با XeLaTeX کامپایل کند و PDF را بازبینی کند. در صورت نبود دسترسی به فایل
یا ابزار، باید آن را صریح گزارش کند. تغییر عمومی کتابخانه باید در **مخزن
اصلی کتابخانه** انجام شود، نه در نسخهٔ vendored پروژه.

متن کوتاه برای شروع کار با یک دستیار جدید:

```text
این پروژهٔ شخصی از Persian LaTeX Kit ساخته شده است. ابتدا AGENTS.md،
main.tex، config/metadata.tex، config/fonts.tex و استایل‌های vendor/ را
بخوان. صورت‌مسئلهٔ پیوست را مبنای محتوا قرار بده؛ داده یا نتیجه‌ای را حدس
نزن. از ماکروهای موجود استفاده کن، تغییر عمومی را در vendor/ انجام نده،
main.tex را با XeLaTeX بساز و PDF را برای RTL، فونت، ارجاع و سرریز بررسی کن.
اگر به فایل، فونت یا کامپایلر دسترسی نداری، صریح بگو.
```

اگر در پروژهٔ اختیاری Git استایل یافت نشد، از ریشهٔ همان پروژه
`git submodule update --init --recursive` را اجرا کنید. در پروژهٔ مستقل،
وجود فایل‌های `vendor/persian-latex-kit/tex/` را بررسی کنید.

## حالت اختیاری Git

فقط اگر پروژهٔ شخصی را عمداً با Git نگه می‌دارید، `--git` و در صورت نیاز
`--repository-url` را به مولد بدهید. راهنمای [Git](GIT_WORKFLOW_FA.md)
این حالت را توضیح می‌دهد. پروژه‌های موجود خودکار تبدیل یا به‌روزرسانی
نمی‌شوند.

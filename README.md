# Persian LaTeX Kit | کتابخانهٔ شخصی قالب‌های لاتک

> **شروع سریع و کار با هوش مصنوعی:** راهنمای کامل [از صورت‌تمرین تا PDF و Git](docs/WORKFLOW_ZERO_TO_PDF_FA.md) را ببین.


یک مجموعهٔ مستقل از درس برای ساخت سندهای فارسی با **XeLaTeX + XePersian**.
هدف: هر قطعه (فونت، سربرگ، جدول رنگی، فرمول، جعبهٔ نکته و ...) تنها یک‌بار نوشته شود و در تمام پروژه‌های بعدی دوباره استفاده شود.

**این ریپو مخصوص یک درس نیست.** پاسخ تمرین‌ها و اطلاعات شخصی باید در ریپو/پوشهٔ جدا نگهداری شوند. این ریپو فقط قالب‌ها و مثال‌های عمومی را نگه می‌دارد.

## ساختار

```text
persian-latex-kit/
├── tex/persian-kit.sty          # کتابخانهٔ اصلی؛ تنظیمات و دستورات اشتراکی
├── gallery.tex       # تست و کاتالوگ قالب‌ها
├── examples/snippets/         # نمونهٔ استفاده از هر کامپوننت
├── templates/assignment/      # نقطهٔ شروع یک تمرین جدید (بدون اطلاعات شخصی)
├── docs/                     # راهنمای ویندوز، گیت و دستورهای آماده
├── scripts/                  # ابزار ایجاد پروژهٔ جدید و کامپایل
├── .gitignore
└── CHANGELOG.md
```

## قالب مادر تکلیف (جدید در نسخهٔ ۱٫۲)

قالب آماده داخل `templates/assignment/` قرار دارد. برای هر درس یک پروژه مستقل بساز؛ هویت دانشجو و پاسخ‌ها داخل ریپوی کتابخانه قرار نگیرند. راهنمای کامل: [قالب مادر تمرین](docs/HOMEWORK_TEMPLATE_FA.md).

## شروع سریع

۱. روی Windows، TeX Live و TeXstudio را نصب و XeLaTeX را به‌عنوان کامپایلر انتخاب کن.
۲. فونت **Vazirmatn (وزیرمتن)** در وزن‌های Regular و Bold را از [مخزن رسمی](https://github.com/rastikerdar/vazirmatn/releases) دریافت و در ویندوز نصب کن. فایل فونت در این ریپو توزیع **نمی‌شود**؛ در نبود آن کامپایل با خطای واضح متوقف می‌شود، نه با تغییر پنهانی فونت.
۳. فایل `gallery.tex` را در TeXstudio باز و با XeLaTeX اجرا کن.
۴. دستورهای کاربردی در [راهنمای قطعات](docs/COMPONENTS_FA.md) توضیح داده شده‌اند.

## استفاده از کتابخانه در هر درس با Git Submodule

بعد از اینکه ریپو را در GitHub ساختی، در ریشهٔ پروژهٔ درسی:

```powershell
git init
git submodule add https://github.com/YOUR_USERNAME/persian-latex-kit.git vendor/persian-latex-kit
```

در `main.tex` پروژه:

```latex
\documentclass[12pt,a4paper]{article}
\usepackage{vendor/persian-latex-kit/tex/persian-kit}
\begin{document}
\MakeHomeworkTitle
\section*{سؤال ۱}
متن تمرین.
\end{document}
```

برای دریافت نسخهٔ جدید کتابخانه در پروژه‌های قبلی:

```powershell
git -C vendor/persian-latex-kit pull --ff-only origin main
git add vendor/persian-latex-kit
git commit -m "Update Persian LaTeX Kit"
```

> اگر شاخهٔ پیش‌فرض ریپوی تو `main` نیست، آن را جایگزین کن. Submodule نسخهٔ دقیق کتابخانه را در هر پروژه ثابت نگه می‌دارد و آپدیت را اختیاری می‌کند. از کپی مستقیم `sty` در ده تمرین مختلف خودداری می‌کنیم.

## توسعه و نسخه‌بندی

- تغییر ظاهر مشترک: در `tex/persian-kit.sty` و نه در تک‌تک تمرین‌ها.
- قطعهٔ جدید: کد عمومی + مثال در `examples/snippets/` + راهنما + یادداشت در `CHANGELOG.md`.
- هر تغییر جدید: یک **Git commit**؛ برای نسخه‌های پایدار Git tag مانند `v1.1.0`.
- اطلاعات دانشجو، پاسخ تمرین‌های واقعی، پسورد، فایل‌های فونت و PDFهای موقت در این ریپوی عمومی قرار نمی‌گیرند.
- برای تنظیم گیت و ساخت ریپو: [راهنمای Git](docs/GIT_WORKFLOW_FA.md).

## یادداشت

ساختار فعلی شامل جعبه، جدول، فرمول، شکل، عنوان استاندارد تمرین و شماره صفحهٔ فارسی است. «کدبلاک» را وقتی نیاز واقعی داشتیم با انتخاب syntax highlighting مناسب اضافه می‌کنیم؛ فعلاً قالبی برای آن ادعا نشده است.

## قالب گزارش آزمایشگاه (افزوده‌شده)
برای تهیهٔ پیش‌گزارش و گزارش نهایی از `templates/lab-report/`، کتابخانهٔ `tex/persian-lab.sty` و راهنمای [گزارش آزمایشگاه](docs/LAB_REPORT_FA.md) استفاده کنید. اسکریپت `scripts/new-lab-report.ps1` یک پروژهٔ مستقل ایجاد می‌کند.

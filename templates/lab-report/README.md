# پروژهٔ گزارش آزمایشگاه

مولد، این پروژه را به‌صورت مستقل با دو استایل لازم در `vendor/` می‌سازد.
Git و اینترنت لازم نیستند و استایل‌های کپی‌شده خودکار به‌روز نمی‌شوند.

1. `config/metadata.tex` را تکمیل کنید. فونت اختیاری در
   `config/fonts.tex` است؛ پیش‌فرض فارسی Vazirmatn.
2. برای پیش‌گزارش `\LabFinalfalse` بماند؛ بخش
   `sections/05-evaluation-plan.tex` وارد PDF می‌شود.
3. پس از داشتن شواهد واقعی، `sections/05-results.tex` و نتیجه‌گیری را
   کامل و `\LabFinaltrue` را انتخاب کنید. پیش‌گزارش و گزارش نهایی را
   جداگانه نگه دارید.
4. `main.tex` را از ریشهٔ پروژه با XeLaTeX در TeXstudio یا
   `latexmk -xelatex -outdir=build main.tex` بسازید.

برای شکل و جدول شماره‌دار از `\LabFigure` و `LabTable` استفاده کنید.
نمونهٔ API در استایل و `examples/snippets/lab-figure-table.tex` مخزن
اصلی است. داده یا تصویر آزمایش‌نشده را نتیجهٔ واقعی معرفی نکنید.

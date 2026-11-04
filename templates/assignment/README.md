# پروژهٔ تکلیف چندسؤالی

این پوشه پس از ساخت با مولد، یک پروژهٔ مستقل است. استایل لازم در
`vendor/persian-latex-kit/tex/` کپی شده و خودکار به‌روز نمی‌شود.
به Git یا اینترنت نیاز ندارد.

1. مشخصات را در `config/metadata.tex` و فونت اختیاری را در
   `config/fonts.tex` تنظیم کنید. پیش‌فرض فارسی Vazirmatn است.
2. سؤال اول را در `questions/question01.tex` بنویسید. برای سؤال بعد،
   `question02.example.tex` را به `question02.tex` تبدیل و
   `\input{questions/question02}` را در `main.tex` فعال کنید.
3. `main.tex` را از ریشهٔ پروژه با XeLaTeX در TeXstudio کامپایل کنید.
   گزینهٔ خط فرمان: `latexmk -xelatex -outdir=build main.tex`.

`\HWQuestion`، `\HWPart`، `HWTable`، `HWTip`، `HWWarning` و
`\HWFigure` در استایل مشترک تعریف شده‌اند. فونت یا رنگ را در سؤال‌ها
بازتعریف نکنید. برای تغییر عمومی، مخزن اصلی کتابخانه را ویرایش کنید،
نه نسخهٔ `vendor/` این پروژه.

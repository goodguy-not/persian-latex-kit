# قالب تکلیف چندسؤالی

`templates/assignment/` یک پروژهٔ مستقل و بی‌اطلاعات شخصی می‌سازد.
استایل اصلی `tex/persian-kit.sty` است؛ آن را در فایل سؤال کپی یا بازتعریف
نکنید.

## ساخت پروژه

Windows:
```powershell
.\scripts\new-assignment.ps1 -Destination "C:\Documents\assignment-1"
```
Ubuntu/Linux:
```sh
python3 scripts/new-project.py --template assignment --destination "$HOME/Documents/assignment-1"
```

حالت پیش‌فرض بدون Git و اینترنت است. فایل‌های استایل موردنیاز در
`vendor/persian-latex-kit/tex/` کپی می‌شوند و خودکار تغییر نمی‌کنند.
برای حالت اختیاری submodule به [راهنمای Git](GIT_WORKFLOW_FA.md) مراجعه کنید.

## ویرایش

`config/metadata.tex` مشخصات سند، `config/fonts.tex` فونت‌های اختیاری،
و `questions/question01.tex` متن سؤال اول را نگه می‌دارند. برای سؤال دوم،
فایل `questions/question02.example.tex` را به `question02.tex` تبدیل و
خط `\input{questions/question02}` را در `main.tex` فعال کنید.

`\HWQuestion`، `\HWPart`، `\HWSubpart`، `HWTable`، `HWTip`،
`HWWarning`، `\HWFigure` و ابزارهای متن دوزبانه در
[فهرست قطعات](COMPONENTS_FA.md) توضیح داده شده‌اند. `\HWFigure` کپشن
نمایشی دارد؛ برای شکل شماره‌دار و قابل ارجاع از API گزارش آزمایشگاه استفاده
می‌شود.

## کامپایل

از ریشهٔ پروژه، `main.tex` را در TeXstudio با XeLaTeX اجرا کنید؛ یا:
```sh
xelatex -interaction=nonstopmode -halt-on-error main.tex
latexmk -xelatex -outdir=build main.tex
```
فرمان دوم یک گزینهٔ مستقل است، نه مرحلهٔ لازم بعد از فرمان اول. XeLaTeX،
XePersian و فونت نصب‌شده لازم هستند. PDF را از نظر RTL، فونت، جدول و
سرریز بازبینی کنید.

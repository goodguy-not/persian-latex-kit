# قالب مادر تمرین‌های دانشگاهی

این پروژه برای **هر درس** قابل استفاده است و باید مستقل از ریپوی کتابخانه بماند.

## ویرایش سه قسمت

1. `config/metadata.tex`: فقط نام درس، استاد، عنوان تمرین، دانشجو و تاریخ تحویل.
2. `questions/question01.tex`: پاسخ سؤال ۱، با `\HWQuestion` و `\HWPart{الف}`.
3. `main.tex`: فایل‌های سؤال بعدی را به ترتیب با `\input{questions/question02}` اضافه کن.

قالب، فونت، کادرها، جداول، رنگ‌ها و هدر/فوتر از `vendor/persian-latex-kit/tex/persian-kit.sty` می‌آید. **از نو کپی نکن**؛ اگر مؤلفه جدیدی ساختیم در ریپوی کتابخانه اضافه کن.

## کامپایل

در TeXstudio فایل `main.tex` را باز کن، Options → Configure TeXstudio → Build → Default Compiler را `XeLaTeX` بگذار و Build & View بزن.

از PowerShell در ریشه پروژه:

```powershell
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

فونت `Vazirmatn` (وزیرمتن) را پیش از کامپایل نصب کن؛ قالب در نبود فونت خطای مشخص می‌دهد و به فونت دیگری تغییر نمی‌کند. هیچ فایل فونتی نباید وارد Git شود.

## برای سؤال‌های بیشتر

فایل `questions/question02.example.tex` را به `question02.tex` تغییر نام بده و خط ورودی آن را در `main.tex` از حالت کامنت خارج کن. فایل سؤال‌های دیگر را هم به همین روش بساز.

## دربارهٔ فایل Git Submodule

اگر پروژه را با `scripts/new-assignment.ps1` ساخته باشی، پوشه `vendor/persian-latex-kit` خودکار از GitHub اضافه می‌شود. هر تمرین روی یک نسخه مشخص از کتابخانه قفل می‌شود و آپدیتش اختیاری است.

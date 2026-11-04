# Persian LaTeX Kit | کتابخانهٔ قالب‌های لاتک فارسی

کتابخانه‌ای مستقل از درس برای ساخت سندهای فارسی با **XeLaTeX و XePersian**. کد
مشترک در `tex/` است؛ پاسخ تمرین، اطلاعات شخصی و دارایی‌های هر سند فقط در پروژهٔ
جداگانهٔ همان سند قرار می‌گیرند.

## انتخاب قالب

| قالب | کاربرد | استایل لازم |
|---|---|---|
| `assignment` | تکلیف چندسؤالی | `tex/persian-kit.sty` |
| `lab-report` | پیش‌گزارش و گزارش نهایی آزمایشگاه | `persian-kit.sty` و `persian-lab.sty` |
| `os-single-question` | فرم تاریخی تک‌سؤال با سربرگ، جدول دو نفر و کد C | `tex/persian-os.sty` |

قالب OS یک سؤال در هر PDF نگه می‌دارد و از ظاهر تکلیف عمومی مستقل است.
`gallery.tex` قطعات اصلی را نمایش می‌دهد؛ نمونه‌های بیشتر در `examples/snippets/`
و [فهرست قطعات](docs/COMPONENTS_FA.md) هستند.

## پیش‌نیازها

- Python 3 برای ساخت پروژه (بدون بستهٔ Python اضافی).
- TeX Live یا MiKTeX شامل XeLaTeX، XePersian و بسته‌های لازم برای کامپایل.
- فونت نصب‌شدهٔ **Vazirmatn** برای ظاهر پیش‌فرض. فونت‌ها در این مخزن توزیع نمی‌شوند.
- TeXstudio اختیاری است؛ کامپایلر آن را روی XeLaTeX تنظیم کنید.
- Git فقط برای حالت پیشرفتهٔ `--git` یا `-Git` لازم است.

## ساخت پروژهٔ مستقل (حالت پیش‌فرض)

از ریشهٔ این مخزن اجرا کنید. مقصد نباید وجود داشته باشد.

**Windows، PowerShell:**

```powershell
.\scripts\new-assignment.ps1 -Destination "C:\Documents\my-assignment"
.\scripts\new-lab-report.ps1 -Destination "C:\Documents\my-lab"
.\scripts\new-os-homework.ps1 -Destination "C:\Documents\my-question" -QuestionNumber "۲"
```

**Ubuntu/Linux:**

```sh
python3 scripts/new-project.py --template assignment --destination "$HOME/Documents/my-assignment"
python3 scripts/new-project.py --template lab-report --destination "$HOME/Documents/my-lab"
python3 scripts/new-project.py --template os-single-question --destination "$HOME/Documents/my-question" --question-number ۲
```

پروژهٔ تازه، فایل‌های قالب و استایل‌های لازم را در
`vendor/persian-latex-kit/tex/` دارد. به این مخزن، GitHub یا اینترنت وابسته نیست؛
`.git` و `.gitmodules` هم ساخته نمی‌شوند. این یک نسخهٔ ثابت است و خودکار به‌روز
نمی‌شود. پروژه‌های ساخته‌شدهٔ قبلی تغییر نمی‌کنند.

در پروژهٔ تازه، `config/metadata.tex` را برای مشخصات و `config/fonts.tex` را
برای فونت‌های اختیاری ویرایش کنید. سپس محتوا را در `questions/` یا `sections/`
بنویسید و همیشه `main.tex` را از ریشهٔ پروژه کامپایل کنید.

## فونت و کامپایل

پیش‌فرض فارسی Vazirmatn با مقیاس فعلی است؛ متن و رقم‌های فارسی و رقم‌های ریاضی
از همان فونت استفاده می‌کنند. انتخاب لاتین پیش‌فرض Times New Roman در صورت
وجود و در غیر این صورت Liberation Serif است. برای Noto Sans Arabic یا فونت
نصب‌شدهٔ دیگر، خط دلخواه را در `config/fonts.tex` فعال کنید:

```latex
\newcommand{\PLKPersianFont}{Noto Sans Arabic}
\newcommand{\PLKLatinFont}{Latin Modern Roman}
```

می‌توان هر کدام را جداگانه انتخاب کرد. فونت انتخاب‌شده اگر در دسترس نباشد،
کامپایل با خطا متوقف می‌شود. [راهنمای قطعات و فونت](docs/COMPONENTS_FA.md)
جزئیات بیشتری دارد.

در TeXstudio، `main.tex` را باز و XeLaTeX را اجرا کنید. روش خط فرمان از ریشهٔ
**پروژهٔ ساخته‌شده**:

```sh
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

برای ارجاعات یا شکل/جدول شماره‌دار، اجرای دوم ممکن است لازم باشد. اگر `latexmk`
هم در توزیع لاتک نصب است، می‌تواند دفعات لازم را خودکار اجرا و خروجی را در
`build/` نگه دارد:

```sh
latexmk -xelatex -outdir=build main.tex
```

این فرمان‌ها همچنان به توزیع محلی لاتک، XePersian و فونت نصب‌شده نیاز دارند.
[راهنمای شروع تا PDF](docs/WORKFLOW_ZERO_TO_PDF_FA.md) و
[نصب ویندوز](docs/WINDOWS_SETUP_FA.md) برای رفع خطاها هستند.

## حالت اختیاری Git Submodule

برای پروژه‌ای که عمداً باید نسخهٔ کتابخانه را با Git نگه دارد:

```sh
python3 scripts/new-project.py --template assignment --destination ./my-project --git --repository-url https://github.com/goodguy-not/persian-latex-kit.git
```

در PowerShell، `-Git -RepositoryUrl URL` را به یکی از wrapperها بدهید. برای
سازگاری با فرمان‌های قدیمی، دادن `-RepositoryUrl` به‌تنهایی نیز حالت Git را
فعال می‌کند. این حالت به Git و دسترسی به مخزن نیاز دارد. به‌روزرسانی submodule
بعداً فقط با اقدام صریح صاحب پروژه انجام می‌شود. [راهنمای Git](docs/GIT_WORKFLOW_FA.md).

## توسعه و آزمون

کد قابل‌استفادهٔ مجدد در `tex/`، نمونه‌ها در `examples/snippets/`، قالب‌ها در
`templates/`، مولدها در `scripts/`، آزمون‌ها در `tests/` و راهنماها در `docs/`
هستند. هر تغییر عمومی باید نمونه، راهنما، یادداشت در `CHANGELOG.md` و آزمون
کامپایل و بازبینی PDF داشته باشد. مجوز نرم‌افزار هنوز توسط صاحب مخزن انتخاب نشده
است؛ این کار جزو این مرحله نیست.

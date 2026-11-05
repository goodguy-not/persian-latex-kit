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
| `letter-fa` | نامهٔ فارسی اداری یا شخصی | `--style classic` یا `modern` |
| `letter-en` | نامهٔ انگلیسی تجاری | `--style classic` یا `modern` |
| `resume-en` | رزومهٔ انگلیسی قابل گسترش | پیش‌فرض Article؛ `--style moderncv` نیز موجود است |

قالب OS یک سؤال در هر PDF نگه می‌دارد و از ظاهر تکلیف عمومی مستقل است.
`gallery.tex` قطعات اصلی را نمایش می‌دهد؛ نمونه‌های بیشتر در `examples/snippets/`
و [فهرست قطعات](docs/COMPONENTS_FA.md) هستند.

راهنمای [نامه‌ها و رزومه](docs/DOCUMENT_TEMPLATES.md) کلاس‌های سند، تنظیمات،
فونت‌ها و بخش‌های اختیاری قالب‌های جدید را شرح می‌دهد.

برای کار با دستیار هوش مصنوعی، از [راهنمای دستیار](docs/AI_HANDBOOK.md)،
[مرجع دقیق دستورها](docs/MACRO_REFERENCE.md) و
[پیام آمادهٔ فارسی](docs/CHAT_STARTER_PROMPT_FA.md) شروع کنید. هر پروژهٔ تازه
`AI_START_HERE.md` و `AI_MACROS.md` مخصوص همان قالب را **درون خود پروژه** دارد؛
برای گفتگوی بدون دسترسی به مخزن، همین پروژه و دستور کار را بارگذاری کنید.

## پیش‌نیازها

- Python 3 برای ساخت پروژه (بدون بستهٔ Python اضافی).
- TeX Live یا MiKTeX شامل XeLaTeX، XePersian و بسته‌های لازم برای کامپایل.
- قالب‌های نامه و رزومه به `fontspec` و `needspace` نیاز دارند؛ نامهٔ انگلیسی مدرن به KOMA-Script نیز نیاز دارد.
- رزومهٔ ModernCV به کلاس `moderncv` نصب‌شده در توزیع TeX نیاز دارد؛ مولد بسته‌ای نصب نمی‌کند.
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
python3 scripts/new-project.py --template letter-fa --style classic --destination "$HOME/Documents/letter-fa"
python3 scripts/new-project.py --template letter-en --style modern --destination "$HOME/Documents/letter-en"
python3 scripts/new-project.py --template resume-en --destination "$HOME/Documents/resume"
python3 scripts/new-project.py --template resume-en --style moderncv --destination "$HOME/Documents/resume-moderncv"
```

پروژهٔ تازهٔ تکلیف، آزمایشگاه یا OS استایل‌های لازم را در
`vendor/persian-latex-kit/tex/` دارد. هیچ پروژهٔ مستقل به این مخزن، GitHub یا اینترنت وابسته نیست؛
`.git` و `.gitmodules` هم ساخته نمی‌شوند. این یک نسخهٔ ثابت است و خودکار به‌روز
نمی‌شود. پروژه‌های ساخته‌شدهٔ قبلی تغییر نمی‌کنند.

قالب‌های نامه و رزومه استایل اشتراکی `tex/` لازم ندارند؛ همهٔ فایل‌های لازم را
مستقیماً در پروژهٔ تازه کپی می‌کنند. برای ساخت نامه در PowerShell نیز همان رابط
Python را اجرا کنید:

```powershell
python .\scripts\new-project.py --template letter-fa --style classic --destination "C:\Documents\my-letter"
```

در پروژهٔ تازه، `config/metadata.tex` را برای مشخصات و `config/fonts.tex` را
برای فونت‌های اختیاری ویرایش کنید. سپس محتوا را در `questions/`، `sections/`
یا `content/` مطابق قالب بنویسید و همیشه `main.tex` را از ریشهٔ پروژه کامپایل کنید.

## فونت و کامپایل

در قالب‌های تکلیف، آزمایشگاه و OS، پیش‌فرض فارسی Vazirmatn با مقیاس فعلی است؛ متن و رقم‌های فارسی و رقم‌های ریاضی
از همان فونت استفاده می‌کنند. انتخاب لاتین پیش‌فرض این قالب‌ها Times New Roman در صورت
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
برای پیشنهاد قابلیت جدید، [روند توسعهٔ قطعه](docs/EXTENDING_THE_KIT.md) را ببینید.

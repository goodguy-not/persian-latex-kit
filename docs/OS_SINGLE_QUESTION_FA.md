# افزودن قالب تک‌سؤال سیستم‌عامل به کتابخانهٔ مرکزی

این قالب یک قابلیت افزوده به **همین** `persian-latex-kit` است، نه یک ریپوی مستقل.
قالب‌های عمومی `assignment` و گزارش آزمایشگاه دست‌نخورده می‌مانند. فایل‌های
اصلی قالب جدید، `tex/persian-os.sty` و `templates/os-single-question/main.tex` هستند؛
فایل‌های Markdown فقط راهنمای مخزن‌اند، نه محتوای قابل تحویل.

## حفظ نمای Word

قالب با XeLaTeX و XePersian، فونت **Noto Sans Arabic** و استایل مستقل، سربرگ، پابرگ،
عنوان، جدول دو دانشجو و فاصله‌های سند Word را بازسازی می‌کند. یکسانی کاملاً پیکسلی
بین خروجی Word و PDF لاتک تضمین نمی‌شود. این استایل عمداً فونت Vazirmatn
قالب عمومی را تغییر نمی‌دهد. مشخصات واقعی دانشجویان فقط در پروژهٔ شخصی قرار بگیرند.

## ساخت پروژه با ریپوی مرکزی (حالت پیش‌فرض)

ابتدا این تغییرات باید در مخزن اصلی commit و push شوند. سپس، از ریشهٔ کتابخانه:

```powershell
.\scripts\new-os-homework.ps1 -Destination "E:\uni\os\HW2_Q1" -QuestionNumber "۱" -AssignmentNumber "۲"
```

اسکریپت به Git، Python 3 و دسترسی به remote ریپو نیاز دارد؛ آدرس
`origin` خودِ کتابخانه را پیدا می‌کند و نسخهٔ منتشرشده را به‌صورت **Git Submodule**
در پروژهٔ سؤال ثبت می‌کند. در صورت تمایل می‌توان آن را با `-RepositoryUrl` تعیین کرد.
برای به‌روزرسانی کنترل‌شدهٔ کتابخانه در پروژهٔ درسی:

```powershell
git -C vendor/persian-latex-kit fetch origin
git -C vendor/persian-latex-kit checkout main
git -C vendor/persian-latex-kit pull --ff-only origin main
git add vendor/persian-latex-kit
git commit -m "Update shared Persian LaTeX Kit"
```

## حالت بدون اینترنت (آگاهانه و اختیاری)

```powershell
.\scripts\new-os-homework.ps1 -Destination "E:\uni\os\HW2_Q1" -QuestionNumber "۱" -Offline
```

این حالت فقط `persian-os.sty` را در پوشهٔ `vendor/` کپی می‌کند و با آپدیت
ریپوی مرکزی خودکار تغییر نمی‌کند. در صورت امکان، حالت Submodule ترجیح دارد.
برای Linux/macOS: `python3 scripts/new-os-homework.py --destination /tmp/HW2_Q1 --offline`.

## ویرایش و کامپایل لاتک

- `config/metadata.tex` اطلاعات درس، تمرین، دانشجو و شمارهٔ سؤال را تعیین می‌کند.
- فایل `questions/questionNN.tex` فقط پاسخ **یک سؤال** را در خود دارد؛ `main.tex`
  همان یک فایل را وارد می‌کند و یک PDF تک‌سؤال می‌سازد.
- برای سؤال بعدی، پروژه‌ای دیگر از همین قالب بساز. منابع همه در قالب مرکزی‌اند.
- در ریشهٔ پروژه با XeLaTeX دو بار `main.tex` را کامپایل کن. نمونه:

```sh
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
```

## راست‌به‌چپ و نشانه‌گذاری فارسی

- نثر فارسی را مستقیم بنویس و از «گیومه»، «ویرگول،»، «نقطه‌ویرگول؛» و «علامت سؤال؟»
  فارسی استفاده کن؛ نوشتن جملهٔ انگلیسی برای پاسخ تمرین مجاز نیست.
- عبارت‌های لاتین را با `\OSLatin{fork()}` یا `\lr{waitpid()}` مستقل کن؛ کد C
  را در محیط `latin` + `lstlisting` قرار بده. پرانتزهای **درون عبارت لاتین**
  باید داخل همان `\OSLatin{...}` باشند.
- برای پرانتز **دور متن فارسی** از `\OSParen{آ}`، برای کروشه از
  `\OSBracketed{متن}` و برای خطِ جداکننده از `\OSDash` استفاده کن.
  دلیل وجود این دستورها این است که نسخهٔ فونت Noto Sans Arabic مرجع، بعضی
  گلیف‌های ASCII و `–/—` را ندارد. این دستورات آن‌ها را با فونت نماد مکمل
  می‌کشند و با توجه به چیدمان راست‌به‌چپ، گلیف ابتدا و انتها را درست آینه می‌کنند،
  **بدون تغییر فونت فارسی اصلی**. نوشتن مستقیم `(` یا `[` در متن فارسی
  با این خانوادهٔ فونت می‌تواند گلیف مفقود یا علامت معکوس تولید کند.
- برای بازهٔ سال از `\OSDateRange{۱۴۰۵}{۱۴۰۶}` و برای تیتر جزء سؤال از
  `\OSPart{آ}[عنوان]` استفاده کن. `\OSTechnicalTerm{فراخوانی}{waitpid()}`
  اصطلاح فارسی و معادل لاتین را با پرانتز درست نشان می‌دهد.
- متن جای‌نگهدار داخل کروشه را قبل از تحویل پاک کن. با بازبینی PDF، جهت پرانتزها،
  اعداد، جدول، فرمول، خط‌شکنی و شماره صفحه را بررسی کن.

## تحویل

صورت HW2 پوشه/فایل فشرده با نام `HW2_StudentID1_StudentID2` و PDF بخش تئوری
را خواسته است. می‌توان فایل‌های TeX هر سؤال و PDFهای مستقل را نگه داشت و برای
تحویل، در صورت نیاز یک PDF تجمیعی تئوری هم تهیه کرد. هر دو عضو گروه باید همان
نسخهٔ نهایی را تحویل بدهند. پاسخ‌ها باید فارسی و علمی بررسی‌شده باشند.

## آزمون‌های کتابخانه

```sh
python3 tests/test-new-os-homework.py
xelatex -interaction=nonstopmode -halt-on-error tests/os-layout.tex
xelatex -interaction=nonstopmode -halt-on-error tests/os-rtl.tex
```

تست‌ها باید همراه بازبینی تصویر خروجی PDF انجام شوند. فایل‌های شخصی، خروجی
تکلیف، فونت‌ها و فایل‌های موقت XeLaTeX را به مخزن کتابخانه کامیت نکن.

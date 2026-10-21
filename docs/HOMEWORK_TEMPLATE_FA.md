# روش ثابت تهیهٔ هر تمرین

## یک‌بار برای همیشه

قالب/کامپوننت‌های اصلی در `tex/persian-kit.sty` ذخیره می‌شوند. فونت اصلی `Vazirmatn` است و در نبود آن کامپایل با خطای واضح متوقف می‌شود؛ جایگزینی خودکار نداریم. خروجی با **XeLaTeX** ساخته می‌شود. هیچ فونت تجاری در GitHub ذخیره نشود.

## برای هر تکلیف جدید

از پوشهٔ محلیِ ریپوی کتابخانه، در PowerShell:

```powershell
.\scripts\new-assignment.ps1 -Destination "E:\uni\assignments\example-course-hw1" -RepositoryUrl "https://github.com/goodguy-not/persian-latex-kit.git"
```

در پروژه جدید `config/metadata.tex` و `questions/question01.tex` را پر کن. سؤال‌های جدید را به صورت فایل جدا بساز و به `main.tex` اضافه کن. هر بار `main.tex` را با XeLaTeX بساز. در پروژه اولیه فقط پاسخ‌های نمونه را پاک کن.

**نکته:** این دستور به آخرین نسخه‌ای از کتابخانه دسترسی دارد که در GitHub `push` شده؛ بنابراین تغییرات جدید را اول در ریپوی کتابخانه ثبت و ارسال کن.

## تغییر یک مؤلفه برای همیشه

۱. فایل `tex/persian-kit.sty` در **ریپوی کتابخانه** را تغییر بده (نه فایل نسخهٔ submodule در تکلیف). ۲. نمونه‌ای در `examples` و شرح در `docs` اضافه کن. ۳. `git add .`، `git commit` و `git push` کن. ۴. برای تمرین‌های جدید نسخه نو استفاده می‌شود؛ برای قدیمی‌ها به دلخواه به‌روزرسانی کن:

```powershell
git -C vendor/persian-latex-kit pull --ff-only origin main
git add vendor/persian-latex-kit
git commit -m "Update shared LaTeX styles"
```

## قطعات فعلی

- `\HWActivateAssignmentLayout`: فعال‌سازی صفحه‌بندی یکدست و شماره صفحهٔ فارسی در پابرگ
- `\MakeHomeworkTitle`: عنوان و مشخصات
- `\HWQuestion` / `\HWQuestion[عنوان]`: شروع سؤال با شماره‌گذاری خودکار
- `\HWPart{الف}` / `\HWPart{الف}[عنوان]`: شروع زیربخش
- `\HWSubpart{عنوان}`: زیرعنوان ریزتر
- `\Term{موجودیت}{Entity}`: نمایش معادل لاتین با جهت درست
- `HWTable`: جدول نواری و سربرگ رنگی
- `HWTip`, `HWWarning`: کادرهای قابل استفاده
- `\HWFigure[0.7]{assets/img.png}{عنوان شکل}`: افزودن تصویر
- محیط‌های استاندارد `\[...\]` و `equation`: فرمول ریاضی

کدبلاک syntax-highlighted یا جدول چندصفحه‌ای هنوز به این کتابخانه اضافه نشده؛ آن‌ها را هنگام نیاز، با نمونهٔ آزمایشی، اضافه می‌کنیم.

# قالب تک‌سؤال با ظاهر تاریخی OS

`templates/os-single-question/` برای **یک سؤال در هر پروژه و PDF** است.
سربرگ، پابرگ، جدول دو نفر، عنوان سؤال و کد C از
`tex/persian-os.sty` می‌آیند. این طراحی از قالب تکلیف چندسؤالی جداست.

## ساخت پروژهٔ مستقل

Windows:
```powershell
.\scripts\new-os-homework.ps1 -Destination "C:\Documents\question-2" -QuestionNumber "۲"
```
Ubuntu/Linux:
```sh
python3 scripts/new-os-homework.py --destination "$HOME/Documents/question-2" --question-number ۲
```

`-AssignmentNumber` / `--assignment-number` اختیاری است و فقط عنوان
تمرین سری مربوط را در metadata قرار می‌دهد. `-Offline` / `--offline`
برای سازگاری با فرمان‌های قدیمی باقی مانده و اکنون با حالت پیش‌فرض مستقل
یکسان است. برای حالت Git اختیاری `-Git -RepositoryUrl URL` یا
`--git --repository-url URL` را انتخاب کنید. پروژهٔ مستقل شامل استایل
لازم در `vendor/` است، Git یا اینترنت نمی‌خواهد و خودکار به‌روز نمی‌شود.

## ویرایش و کامپایل

مشخصات عمومی، شمارهٔ سؤال و دو نام/شناسه را در
`config/metadata.tex` وارد کنید. فونت اختیاری در `config/fonts.tex`
تعریف می‌شود. پاسخ همان یک سؤال در `questions/questionNN.tex` است و
`main.tex` فقط همان فایل را وارد می‌کند. برای سؤال دیگری پروژهٔ تازه
بسازید. اطلاعات واقعی را در کتابخانهٔ عمومی قرار ندهید.

`main.tex` را از ریشهٔ پروژه با XeLaTeX در TeXstudio اجرا کنید؛ یا:
```sh
latexmk -xelatex -outdir=build main.tex
```
در نبود `latexmk`، دو بار `xelatex -interaction=nonstopmode -halt-on-error
main.tex` اجرا کنید. توزیع محلی لاتک، XePersian و فونت نصب‌شده لازم‌اند.

## فونت و RTL

فونت پیش‌فرض کنونی **Vazirmatn** با مقیاس `1.05` است؛ Noto Sans Arabic
فقط با انتخاب صریح در `config/fonts.tex` و پس از نصب قابل استفاده است.
انتخاب `\PLKLatinFont` مستقل است. فونت انتخاب‌شده اگر موجود نباشد،
کامپایل متوقف می‌شود. مسیر محلیِ قدیمی Vazirmatn نیز پشتیبانی می‌شود:
دو فایل `Vazirmatn-Regular.ttf` و `Vazirmatn-Bold.ttf` را در
`fonts/` پروژه قرار دهید و در `config/fonts.tex` بنویسید:
```latex
\newcommand{\OSVazirmatnPath}{fonts}
```
این گزینه را هم‌زمان با `\PLKPersianFont` فعال نکنید. فونت‌ها در مخزن
کتابخانه نگهداری نمی‌شوند.

نثر فارسی و `، ؛ ؟ « »` را راست‌به‌چپ نگه دارید. نام فنی لاتین را با
`\OSLatin{fork()}` جدا کنید. برای پرانتز و کروشهٔ دور نثر فارسی از
`\OSParen{متن}` و `\OSBracketed{متن}`، و برای بازه از
`\OSDateRange{۱۴۰۵}{۱۴۰۶}` استفاده کنید؛ در نثر فارسی نشانه‌های
ASCII کروشه را مستقیم ننویسید. `\OSPart{آ}[عنوان]` تیتر زیربخش است.
کد C را در `latin` + `lstlisting` با `style=OSCode` قرار دهید؛
جدول‌ها، فرمول‌ها و `\OSFigure` نیز در استایل فعلی پشتیبانی می‌شوند.

پس از کامپایل، PDF را از نظر RTL، علائم، فونت، حاشیه، کد، جدول، شکل و
سربرگ/پابرگ بازبینی کنید. آزمون‌های مخزن:
```sh
python3 tests/test-new-os-homework.py
xelatex -interaction=nonstopmode -halt-on-error tests/os-layout.tex
xelatex -interaction=nonstopmode -halt-on-error tests/os-rtl.tex
```

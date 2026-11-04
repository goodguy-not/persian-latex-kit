# نصب و کامپایل در ویندوز

- Python 3 برای ساخت پروژه و TeX Live یا MiKTeX با XeLaTeX و XePersian برای
  کامپایل لازم‌اند. TeXstudio برای ویرایش راحت اختیاری است.
- در TeXstudio: `Options > Configure TeXstudio > Build > Default Compiler > XeLaTeX`.
- فونت پیش‌فرض `Vazirmatn` را در وزن‌های Regular و Bold نصب کن. برای TeX Live بهتر است گزینهٔ `Install for all users` را به‌کار ببری. این ریپو فایل فونت ندارد. فونت جایگزینِ نصب‌شده را می‌توان در `config/fonts.tex` پروژه انتخاب کرد.
- برای بررسی، `gallery.tex` را باز و Compile کن.
- اگر خطای `Required Persian font ... not found` دیدی، نصب شدن فونت انتخاب‌شده و نام آن در `config/fonts.tex` را بررسی کن؛ به‌جای تغییر موردی فایل `sty`، بعد از نصب یک بار ویرایشگر را باز و بسته کن.
- اگر `xepersian.sty not found` دیدی، TeX Live مجموعهٔ Arabic/Persian یا XePersian را ندارد و باید با TeX Live Manager اضافه شود.
- در صورت خطای مسیر روی ویندوز، همیشه پروژه را از ریشهٔ خودش اجرا کن. مولد مسیرهای دارای فاصله و Unicode را پشتیبانی می‌کند.

ساخت مستقل و بدون Git از ریشهٔ کتابخانه:

```powershell
.\scripts\new-assignment.ps1 -Destination "C:\Documents\assignment-1"
```

مسیرهای دارای فاصله و Unicode نیز پشتیبانی می‌شوند. فرمان اختیاری
`latexmk -xelatex -outdir=build main.tex` فقط وقتی کار می‌کند که توزیع
لاتک و latexmk نصب باشند؛ از ریشهٔ پروژهٔ ساخته‌شده اجرا شود.

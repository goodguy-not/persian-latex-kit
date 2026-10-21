# نصب و کامپایل در ویندوز

- TeX Live و TeXstudio باید نصب شده باشند.
- در TeXstudio: `Options > Configure TeXstudio > Build > Default Compiler > XeLaTeX`.
- فونت `Vazirmatn` را از نسخهٔ رسمی در وزن‌های Regular و Bold نصب کن. برای TeX Live بهتر است گزینهٔ `Install for all users` را به‌کار ببری. این ریپو فایل فونت ندارد.
- برای بررسی، `gallery.tex` را باز و Compile کن.
- اگر `Required font Vazirmatn not found` دیدی، نصب شدن فونت و تشخیص آن توسط XeLaTeX را بررسی کن؛ به‌جای تغییر موردی فایل `sty`، بعد از نصب یک بار ویرایشگر را باز و بسته کن.
- اگر `xepersian.sty not found` دیدی، TeX Live مجموعهٔ Arabic/Persian یا XePersian را ندارد و باید با TeX Live Manager اضافه شود.
- در صورت خطای مسیر روی ویندوز، همیشه پروژه را از ریشهٔ خودش اجرا کن و از مسیرهای سادهٔ انگلیسی استفاده کن.

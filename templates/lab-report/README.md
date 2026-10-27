# قالب گزارش آزمایشگاه — دو مرحله در یک پروژه

ابتدا `config/metadata.tex` را تکمیل کنید و `\LabFinalfalse` باقی بماند.
بخش‌های ۱ تا ۴ را بر اساس دستور کار هر آزمایش پر کنید؛
`sections/05-evaluation-plan.tex` برنامهٔ شبیه‌سازی یا اجرا را شرح می‌دهد.
در مرحلهٔ دوم، تصویرهای واقعی و مقادیر مشاهده‌شده را در `assets/` بگذارید،
`sections/05-results.tex` را کامل کنید و تنظیم را به `\LabFinaltrue` تغییر دهید.
پیش‌گزارش و گزارش نهایی باید نسخه‌بندی و جداگانه خروجی گرفته شوند.

## شروع

قالب را با `scripts/new-lab-report.ps1` از کتابخانه بسازید. این اسکریپت نسخهٔ منتشرشده در GitHub
را از طریق submodule اضافه می‌کند؛ ابتدا تغییرات کتابخانه را commit و push کنید.

اگر پروژه به‌صورت دستی ساخته شد، در ریشهٔ پروژه اجرا کنید:

```powershell
git init -b main
git submodule add https://github.com/YOUR_USERNAME/persian-latex-kit.git vendor/persian-latex-kit
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

فونت Vazirmatn و XeLaTeX لازم است. تصاویر و پاسخ‌های اختصاصی را وارد ریپوی عمومی قالب نکنید.
برای جدول شماره‌دار، `LabTable` و برای شکل شماره‌دار، `\LabFigure` را به‌کار ببرید.
عنوان جدول بالا و عنوان شکل پایین است؛ هر دو دارای `\label` و قابلیت `\ref` هستند.

> این پوشه عمداً فقط ساختار گزارش را دارد؛ هیچ پاسخ آماده یا متن فرضی در خروجی PDF چاپ نمی‌شود.

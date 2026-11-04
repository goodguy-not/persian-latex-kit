# قالب گزارش آزمایشگاه

این قالب از `persian-kit.sty` و افزونهٔ `persian-lab.sty` استفاده می‌کند.
اطلاعات آزمایش و شواهد واقعی در پروژهٔ ساخته‌شده نگه داشته می‌شوند.

## ساخت

Windows:
```powershell
.\scripts\new-lab-report.ps1 -Destination "C:\Documents\lab-1"
```
Ubuntu/Linux:
```sh
python3 scripts/new-project.py --template lab-report --destination "$HOME/Documents/lab-1"
```

این پروژه به‌صورت پیش‌فرض مستقل است و استایل‌های لازم را در `vendor/`
دارد. Git اختیاری است؛ [راهنمای Git](GIT_WORKFLOW_FA.md) را ببینید.

## ساختار و وضعیت

- `config/metadata.tex`: مشخصات و `\LabFinalfalse` / `\LabFinaltrue`.
- `config/fonts.tex`: انتخاب اختیاری فونت پیش از بارگذاری استایل.
- `sections/01..04`: هدف، مشخصات، طراحی و آزمون‌ها.
- `sections/05-evaluation-plan.tex`: برنامهٔ ارزیابی برای پیش‌گزارش.
- `sections/05-results.tex`: نتایج واقعی برای گزارش نهایی.
- `sections/06-conclusion.tex`: نتیجه‌گیری متناسب با وضعیت.
- `assets/`: شکل‌ها و داده‌های همان آزمایش.

قبل از نتیجهٔ واقعی `\LabFinalfalse` بماند؛ پس از ثبت شواهد و تحلیل،
`\LabFinaltrue` را انتخاب کنید. عکس یا اندازه‌گیری ساختگی را نتیجهٔ واقعی
معرفی نکنید.

`\LabFigure[0.75]{assets/schematic.png}{عنوان}{fig:design}` شکل شماره‌دار
و `LabTable` جدول شماره‌دار با `\label` و `\ref` فراهم می‌کنند.
نمونهٔ کامل در `examples/snippets/lab-figure-table.tex` است.

`main.tex` را از ریشهٔ پروژه با XeLaTeX در TeXstudio یا با
`latexmk -xelatex -outdir=build main.tex` بسازید. فونت پیش‌فرض Vazirmatn
است؛ برای تغییر آن [راهنمای قطعات](COMPONENTS_FA.md) را ببینید. PDF و
ارجاع‌ها را بازبینی کنید.

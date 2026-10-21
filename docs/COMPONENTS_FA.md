# کاتالوگ دستورهای قابل استفادهٔ مجدد

## اصطلاح لاتین در متن راست‌به‌چپ

```latex
\Term{موجودیت}{Entity}
\EN{FIFO}
```

`\Term` عبارت فارسی را با معادل لاتین داخل پرانتز قرار می‌دهد و جهت را حفظ می‌کند.

## جدول رنگی

```latex
\begin{HWTable}{>{\centering\arraybackslash}p{2cm}Y C}
\rowcolor{HWNavy}
\HWTableHead{ردیف} & \HWTableHead{توضیحات} & \HWTableHead{وضعیت}\\
۱ & نمونهٔ متن & آماده\\
\end{HWTable}
```

- برای تغییر کل رنگ‌ها فقط `HWNavy`, `HWStripe`, `HWLine` در فایل قالب را تغییر بده.
- `Y` برای متن بلندِ راست‌چین و `C` برای ستون وسط‌چین است.
- برای جدول‌های خیلی بلند بعداً الگوی longtable مستقل می‌سازیم.

## جعبه‌های نکته و هشدار

```latex
\begin{HWTip}
نکتهٔ مهم.
\end{HWTip}

\begin{HWWarning}
توضیح تکمیلی یا هشدار.
\end{HWWarning}
```

## افزودن شکلِ تبلت

```latex
\HWFigure[0.7]{assets/figure1.png}{توضیح شکل}
```

## عنوان تمرین و فرمول

```latex
\MakeHomeworkTitle
\[
\overline{W}=\frac{\sum_{i=1}^{n} W_i}{n}
\]
```

برای اجرای قطعات آماده، `gallery.tex` را کامپایل کن. برای ذخیرهٔ هر قطعهٔ جدید: کد در کتابخانه، مثال در `examples/snippets`، راهنما در همین فایل و ثبت تغییر در CHANGELOG.


## قالب مادر تمرین

```latex
\HWActivateAssignmentLayout
\MakeHomeworkTitle
\HWQuestion[عنوان اختیاری]
\HWPart{الف}
متن پاسخ...
\HWPart{ب}
متن پاسخ...
```

اطلاعات درس فقط در `config/metadata.tex` و متن سؤال‌ها در `questions/` قرار می‌گیرند. راهنما: [قالب تکلیف](HOMEWORK_TEMPLATE_FA.md).

## فونت پیش‌فرض و اعداد فارسی

کتابخانه به‌طور سراسری از **Vazirmatn (وزیرمتن)** برای متن، اعداد متن و اعداد ریاضی استفاده می‌کند. پیش از اجرای XeLaTeX باید نسخه‌های Regular و Bold را از [انتشار رسمی فونت](https://github.com/rastikerdar/vazirmatn/releases) روی سیستم نصب کرده باشی. در نبود فونت، کامپایل با خطا متوقف می‌شود و فونت دیگری بی‌خبر جایگزین نمی‌شود.

در فایل‌های `questions/*.tex` فونت را تنظیم نکن. برای آزمایش فونت و علائم فارسی، از ریشهٔ ریپو فایل `tests/font-vazirmatn.tex` را با XeLaTeX کامپایل کن.

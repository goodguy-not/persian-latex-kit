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

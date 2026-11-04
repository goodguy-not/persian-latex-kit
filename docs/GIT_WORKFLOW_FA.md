# استفادهٔ اختیاری از Git

ساخت پروژهٔ معمولی به Git، GitHub یا اینترنت نیاز ندارد. مولد به‌صورت
پیش‌فرض یک نسخهٔ مستقل از قالب و استایل‌های لازم می‌سازد. اطلاعات شخصی و
پاسخ‌های تمرین را در مخزن عمومی کتابخانه قرار ندهید.

اگر عمداً می‌خواهید پروژهٔ **جدید** با submodule ساخته شود، از ریشهٔ
کتابخانه اجرا کنید:
```sh
python3 scripts/new-project.py --template assignment --destination ./my-project --git --repository-url https://github.com/goodguy-not/persian-latex-kit.git
```

در PowerShell، `-Git -RepositoryUrl URL` را به wrapper قالب بدهید. برای
سازگاری با فراخوانی قدیمی، `-RepositoryUrl` به‌تنهایی هم حالت Git را
انتخاب می‌کند. این حالت `git init` و `git submodule add` اجرا می‌کند،
به Git و دسترسی به مخزن نیاز دارد، و نسخهٔ مشخصی از کتابخانه را ثبت می‌کند.

برای گرفتن پروژهٔ Gitدار روی دستگاه دیگر:
```sh
git clone --recurse-submodules URL
```

برای به‌روزرسانی **دستی** کتابخانه در پروژهٔ خود، ابتدا وضعیت Git و
سازگاری استایل را بررسی کنید، سپس submodule را به نسخهٔ موردنظر ببرید،
`main.tex` را دوباره کامپایل و PDF را بازبینی کنید و pointer را commit
کنید. هیچ پروژه‌ای خودکار به‌روز نمی‌شود. پروژهٔ مستقل را نیز می‌توانید
بعداً به‌صورت یک مخزن معمولی ثبت کنید؛ برای کامپایل نیازی به این کار نیست.

نمونهٔ به‌روزرسانی دستی در ریشهٔ یک پروژهٔ Gitدار (اگر شاخهٔ مخزن شما
`main` است):

```sh
git status
git -C vendor/persian-latex-kit fetch origin
git -C vendor/persian-latex-kit checkout main
git -C vendor/persian-latex-kit pull --ff-only origin main
git add vendor/persian-latex-kit
git commit -m "Update shared Persian LaTeX Kit"
```

قبل از commit، تفاوت PDF جدید را بررسی کنید. این فرمان‌ها برای پروژهٔ
مستقل لازم نیستند و روی آن اجرا نمی‌شوند.

این مخزن کتابخانه از قبل Git دارد. راه‌اندازی دوبارهٔ آن با `git init`
یا تغییر visibility مخزن جزو استفادهٔ معمول از قالب نیست.

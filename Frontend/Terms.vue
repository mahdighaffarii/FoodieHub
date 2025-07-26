<template>
  <div class="terms-page">
    <h2>قوانین و مقررات سایت فودی‌هاب</h2>

    <section>
      <h3>1. شرایط استفاده از خدمات</h3>
      <p>
        کاربران با ثبت‌نام و استفاده از خدمات فودی‌هاب، موافقت می‌کنند که قوانین سایت را رعایت کنند و اطلاعات صحیح وارد نمایند.
      </p>
    </section>

    <section>
      <h3>2. سفارش غذا و پرداخت</h3>
      <p>
        سفارش‌ها از طریق رستوران‌های همکار ثبت می‌شوند. مسئولیت کیفیت و زمان تحویل غذا بر عهده رستوران است. پرداخت از طریق کیف پول مجازی سایت انجام می‌شود.
      </p>
    </section>

    <section>
      <h3>3. حساب کاربری و امنیت</h3>
      <p>
        کاربران مسئول حفظ امنیت حساب کاربری خود هستند. هرگونه استفاده غیرمجاز از حساب به عهده کاربر است.
      </p>
    </section>

    <section>
      <h3>4. حریم خصوصی</h3>
      <p>
        اطلاعات کاربران محفوظ است و فقط برای ارائه خدمات به کار می‌رود. فودی‌هاب متعهد به حفظ حریم خصوصی کاربران است.
      </p>
    </section>

    <section>
      <h3>5. محدودیت مسئولیت</h3>
      <p>
        فودی‌هاب مسئول خسارات ناشی از سفارشات، تأخیر در تحویل یا مشکلات کیفیت غذا نیست.
      </p>
    </section>

    <section>
      <h3>6. تغییرات قوانین</h3>
      <p>
        فودی‌هاب حق تغییر قوانین را در هر زمان دارد. تغییرات بلافاصله پس از اعلام در سایت اعمال می‌شود.
      </p>
    </section>
  </div>
</template>

<script>
export default {
  name: "Terms"
}
</script>

<style scoped>
.terms-page {
  max-width: 700px;
  margin: 2rem auto;
  padding: 1.5rem 2rem;
  background-color: #fafafa;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgb(0 0 0 / 0.1);
  font-family: "Vazir", sans-serif;
  direction: rtl;
  color: #333;
}

.terms-page h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  font-weight: 700;
  color: #2c3e50;
}

.terms-page section {
  margin-bottom: 1.5rem;
}

.terms-page h3 {
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #34495e;
}

.terms-page p {
  line-height: 1.7;
  font-size: 1rem;
  color: #555;
}
</style>

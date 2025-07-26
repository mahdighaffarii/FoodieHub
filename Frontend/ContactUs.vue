<template>
  <div class="contact-page">
    <h2>تماس با ما</h2>

    <div class="contact-info">
      <p><strong>📍 آدرس:</strong> تهران، خیابان مثال، پلاک ۱۲۳</p>
      <p><strong>📞 تلفن ۱:</strong> ۰۲۱-۱۲۳۴۵۶۷۸</p>
      <p><strong>📞 تلفن ۲:</strong> ۰۲۱-۸۷۶۵۴۳۲۱</p>
      <p>
        <strong>📷 اینستاگرام:</strong>
        <a href="https://instagram.com/yourpage" target="_blank">instagram.com/yourpage</a>
      </p>
      <p>
        <strong>📺 یوتیوب:</strong>
        <a href="https://youtube.com/yourchannel" target="_blank">youtube.com/yourchannel</a>
      </p>
    </div>

    <hr />

    <p>می‌توانید از طریق فرم زیر برای ما پیام بفرستید:</p>

    <form @submit.prevent="handleSubmit">
      <input type="text" v-model="name" placeholder="نام شما" required />
      <input type="email" v-model="email" placeholder="ایمیل شما" required />
      <textarea v-model="message" placeholder="پیام شما" required></textarea>
      <button type="submit">ارسال پیام</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      email: '',
      message: ''
    }
  },
  methods: {
    handleSubmit() {
      alert(`پیام شما ارسال شد. ممنون، ${this.name}! (شبیه‌سازی)`)
      this.name = ''
      this.email = ''
      this.message = ''
    }
  }
}
</script>

<style scoped>
.contact-page {
  max-width: 600px;
  margin: auto;
  padding: 2rem;
  border: 1px solid #ccc;
  border-radius: 10px;
  direction: rtl;
  font-family: sans-serif;
}

.contact-info p {
  margin-bottom: 0.8rem;
}

input,
textarea {
  display: block;
  width: 100%;
  margin-bottom: 1rem;
  padding: 0.6rem;
  border: 1px solid #aaa;
  border-radius: 5px;
}

textarea {
  min-height: 120px;
}

button {
  padding: 0.6rem 1.2rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #339966;
}
</style>

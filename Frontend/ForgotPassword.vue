<template>
  <div class="forgot-password-page">
    <h2>فراموشی رمز عبور</h2>
    <form @submit.prevent="handleReset">
      <input type="email" v-model="email" placeholder="ایمیل خود را وارد کنید" required />
      <button type="submit">ارسال لینک بازیابی</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "ForgotPassword",
  data() {
    return {
      email: ''
    }
  },
  methods: {
    handleReset() {
      alert(`لینک بازیابی به ایمیل ${this.email} ارسال شد (شبیه‌سازی).`)
      this.email = ''
    }
  }
}
</script>

<style scoped>
.forgot-password-page {
  max-width: 400px;
  margin: auto;
  padding: 2rem;
  direction: rtl;
  font-family: "Vazir", sans-serif;
  text-align: right;
  border: 1px solid #ccc;
  border-radius: 10px;
}

input {
  display: block;
  width: 100%;
  margin-bottom: 1rem;
  padding: 0.5rem;
  text-align: right;
}

button {
  padding: 0.5rem 1rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #369f6e;
}
</style>

<template>
  <div class="login-page">
    <h2>ورود به حساب</h2>
    <form @submit.prevent="handleLogin">
      <input type="text" v-model="username" placeholder="نام کاربری" />
      <input type="password" v-model="password" placeholder="رمز عبور" />
      <button type="submit">ورود</button>
    </form>
    <p>
      <router-link to="/forgot-password">رمز عبور را فراموش کرده‌اید؟</router-link>
    </p>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    handleLogin() {
      console.log('نام کاربری:', this.username)
      console.log('رمز عبور:', this.password)
      alert("ورود انجام شد (فعلاً شبیه‌سازی)")
    }
  }
}
</script>

<style scoped>
.login-page {
  max-width: 400px;
  margin: auto;
  padding: 2rem;
  border: 1px solid #ccc;
  border-radius: 10px;
  direction: rtl; /* مهم برای راست‌چین شدن */
  text-align: right;
  font-family: sans-serif; /* در صورت استفاده از فونت فارسی، اینجا تغییر بده */
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
  cursor: pointer;
}

p {
  margin-top: 0.5rem;
}
</style>

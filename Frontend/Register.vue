<template>
  <div class="register-page">
    <h2>ثبت‌نام</h2>
    <form @submit.prevent="handleRegister">
      <input type="text" v-model="username" placeholder="نام کاربری" />
      <input type="email" v-model="email" placeholder="ایمیل" />
      <input type="password" v-model="password" placeholder="رمز عبور" />
      <button type="submit">ثبت‌نام</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      username: '',
      email: '',
      password: ''
    }
  },
  methods: {
    handleRegister() {
      console.log('ثبت‌نام با اطلاعات زیر انجام شد:')
      console.log('نام کاربری:', this.username)
      console.log('ایمیل:', this.email)
      console.log('رمز عبور:', this.password)
      alert("ثبت‌نام انجام شد (فعلاً شبیه‌سازی)")
    }
  }
}
</script>

<style scoped>
.register-page {
  max-width: 400px;
  margin: auto;
  padding: 2rem;
  border: 1px solid #ccc;
  border-radius: 10px;
  direction: rtl;
  font-family: "Tahoma", "Vazirmatn", sans-serif;
  text-align: right;
}
input {
  display: block;
  width: 100%;
  margin-bottom: 1rem;
  padding: 0.5rem;
}
button {
  padding: 0.5rem 1rem;
  cursor: pointer;
}
</style>

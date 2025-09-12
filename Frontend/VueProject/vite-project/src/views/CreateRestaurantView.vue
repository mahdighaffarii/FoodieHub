<template>
  <div class="create-restaurant-container">
    <h2>ثبت رستوران جدید</h2>
    <p>شما هنوز رستورانی در سیستم ثبت نکرده‌اید. لطفاً اطلاعات رستوران خود را وارد کنید.</p>
    
    <form @submit.prevent="handleCreateRestaurant" class="card">
      <div class="form-group">
        <label for="name">نام رستوران</label>
        <input type="text" id="name" v-model="formData.name" required>
      </div>
      <div class="form-group">
        <label for="address">آدرس</label>
        <textarea id="address" v-model="formData.address" required></textarea>
      </div>
      <div class="form-group">
        <label for="phone_number">شماره تلفن</label>
        <input type="text" id="phone_number" v-model="formData.phone_number" required>
      </div>
      <button type="submit">ثبت رستوران</button>
    </form>
  </div>
</template>

<script setup>
import { reactive } from 'vue';
import managerService from '../services/managerService';
import { useAuthStore } from '../stores/authStore';
import { useRouter } from 'vue-router';

const authStore = useAuthStore();
const router = useRouter();

const formData = reactive({
  name: '',
  address: '',
  phone_number: ''
});

const handleCreateRestaurant = async () => {
  try {
    await managerService.createRestaurant({ ...formData });
    alert('رستوران شما با موفقیت ثبت شد.');
    // اطلاعات کاربر را رفرش می‌کنیم تا اطلاعات رستوران جدید را شامل شود
    await authStore.fetchUserProfile();
    // کاربر را به داشبورد اصلی مدیریت هدایت می‌کنیم
    router.push('/manager/dashboard');
  } catch (error) {
    console.error("Failed to create restaurant:", error.response?.data);
    alert(`خطا در ثبت رستوران: ${JSON.stringify(error.response?.data)}`);
  }
};
</script>

<style scoped>
.create-restaurant-container { max-width: 600px; margin: 30px auto; text-align: center; }
.card { background: #fff; border: 1px solid #e0e0e0; padding: 20px; border-radius: 8px; margin-top: 20px; text-align: right; }
.form-group { margin-bottom: 15px; }
label { display: block; margin-bottom: 5px; }
input, textarea { width: 100%; padding: 10px; box-sizing: border-box; }
button { width: 100%; padding: 12px; font-size: 1.1em; }
</style>
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { getRestaurants } from '@/api/restaurants.api';

const loading = ref(true);
const error = ref('');
const items = ref<any[]>([]);

onMounted(async () => {
  try {
    const { data } = await getRestaurants();
    items.value = data.results ?? data;
  } catch (e: any) {
    error.value = e?.response?.data?.detail ?? 'خطا در دریافت رستوران‌ها';
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <div>
    <h1>رستوران‌ها</h1>
    <div v-if="loading">در حال بارگذاری…</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
      <div v-for="r in items" :key="r.id">{{ r.name }}</div>
    </div>
  </div>
</template>
                
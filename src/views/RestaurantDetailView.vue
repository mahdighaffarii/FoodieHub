<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { getRestaurant, searchFoods } from '@/api/restaurants.api';
import { useCartStore } from '@/store/cart.store';

const route = useRoute();
const id = Number(route.params.id);
const restaurant = ref<any>(null);
const foods = ref<any[]>([]);
const loading = ref(true); const error = ref('');
const cart = useCartStore();

onMounted(async () => {
  try {
    const [r, f] = await Promise.all([getRestaurant(id), searchFoods(id)]);
    restaurant.value = r.data;
    foods.value = f.data.results ?? f.data;
  } catch (e: any) {
    error.value = e?.response?.data?.detail ?? 'خطا در دریافت منو';
  } finally { loading.value = false; }
});

function add(food: any) {
  cart.addItem({ foodId: food.id, name: food.name, price: food.price, restaurantId: id, quantity: 1 });
}
</script>

<template>
  <div>
    <div v-if="loading">در حال بارگذاری…</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
      <h2>{{ restaurant.name }}</h2>
      <ul>
        <li v-for="f in foods" :key="f.id">
          {{ f.name }} - {{ f.price }}
          <button @click="add(f)">افزودن</button>
        </li>
      </ul>
    </div>
  </div>
</template>
                
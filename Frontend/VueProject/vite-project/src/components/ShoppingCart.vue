<!-- src/components/ShoppingCart.vue -->
<template>
  <div class="shopping-cart">
    <h3>سبد خرید شما</h3>
    <div v-if="cartStore.items.length === 0">سبد خرید خالی است.</div>
    <div v-else>
      <ul>
        <li v-for="item in cartStore.items" :key="item.id">
          <span>{{ item.name }} ({{ item.quantity }} عدد)</span>
          <span>{{ item.price * item.quantity }} تومان</span>
          <button @click="cartStore.removeItem(item.id)">❌</button>
        </li>
      </ul>
      <hr />
      <div class="cart-total">
        <strong>مجموع:</strong>
        <span>{{ cartStore.cartTotalPrice }} تومان</span>
      </div>
      <button class="checkout-btn" @click="cartStore.checkout()">ثبت نهایی و پرداخت</button>
      <button class="clear-btn" @click="cartStore.clearCart()">خالی کردن سبد</button>
    </div>
  </div>
</template>

<script setup>
import { useCartStore } from '../stores/cartStore';
const cartStore = useCartStore();
</script>

<style scoped>
.shopping-cart {
  position: fixed;
  top: 60px;
  right: 20px;
  width: 300px;
  background: white;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 15px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  z-index: 1000;
}
ul { list-style: none; padding: 0; }
li { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
.cart-total { display: flex; justify-content: space-between; font-size: 1.1em; margin-top: 10px; }
.checkout-btn, .clear-btn { width: 100%; margin-top: 10px; padding: 10px; border-radius: 5px; border: none; cursor: pointer; color: white; }
.checkout-btn { background-color: #4CAF50; }
.clear-btn { background-color: #f44336; }
</style>
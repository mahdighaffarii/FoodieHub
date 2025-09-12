<!-- src/components/EditFoodItemModal.vue -->
<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2>ویرایش آیتم: {{ itemToEdit.name }}</h2>
      <form @submit.prevent="submitForm">
        <input type="text" v-model="editableItem.name" placeholder="نام غذا" required>
        <textarea v-model="editableItem.description" placeholder="توضیحات"></textarea>
        <input type="number" v-model="editableItem.price" placeholder="قیمت" required>
        <select v-model="editableItem.category" required>
          <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
        </select>
        <label>
          <input type="checkbox" v-model="editableItem.is_available">
          موجود است
        </label>
        <div class="modal-actions">
          <button type="submit">ذخیره تغییرات</button>
          <button type="button" @click="$emit('close')">انصراف</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  itemToEdit: Object,
  categories: Array,
});

const emit = defineEmits(['close', 'item-updated']);

const editableItem = ref({ ...props.itemToEdit });

// اگر آیتم ورودی تغییر کرد، فرم را آپدیت کن
watch(() => props.itemToEdit, (newItem) => {
  editableItem.value = { ...newItem };
});

const submitForm = () => {
  // TODO: فراخوانی API ویرایش
  console.log("Submitting updated item:", editableItem.value);
  emit('item-updated', editableItem.value);
};
</script>

<style scoped>
.modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); display: flex; justify-content: center; align-items: center; z-index: 1001; }
.modal-content { background: white; padding: 20px; border-radius: 8px; width: 400px; }
form { display: flex; flex-direction: column; gap: 15px; }
.modal-actions { display: flex; justify-content: flex-end; gap: 10px; margin-top: 20px; }
</style>
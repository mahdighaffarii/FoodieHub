import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

import './style.css'

const app = createApp(App)

// Pinia و Router را به اپلیکیشن اضافه می‌کنیم
app.use(createPinia())
app.use(router)

// اپلیکیشن را به DOM متصل می‌کنیم
app.mount('#app')


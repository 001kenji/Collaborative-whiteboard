import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createNotivue } from 'notivue'
import App from './App.vue'
import router from './router'
import './style.css'

import 'notivue/notification.css'
import 'notivue/animations.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)
const notivue = createNotivue(/* Options */)
app.use(notivue)
app.mount('#app')
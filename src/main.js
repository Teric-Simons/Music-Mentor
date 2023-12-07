import { createApp } from 'vue'
import App from './App.vue'
import mitt from 'mitt';
import router from './router'

import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
const emitter = mitt();
const app = createApp(App);
app.component('VueDatePicker', VueDatePicker);
app.use(router)
app.config.globalProperties.emitter = emitter;

app.mount('#app');

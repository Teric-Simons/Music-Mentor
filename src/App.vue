
<!-- App.vue -->
<template>
  <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@300&display=swap" rel="stylesheet">
<navbar />

<main>
  <RouterView />
</main>

<footer></footer>

</template>

<script>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from "@/components/Navbar.vue";
import UploadBar from "@/components/Uploadbar.vue";


export default {
  components: {
    Navbar,
    UploadBar,
  
  },
  // Your app logic goes here
};

</script>

<style>

/* Add your global styles here */
body {
  
  margin: 0;

    font-family: 'Figtree', 'Figtree-fallback', 'Figtree-fallback-android', 'Noto Sans', 'NotoSans-fallback', 'NotoSans-fallback-android', sans-serif;
}
</style>



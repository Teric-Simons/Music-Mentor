<template>
    <button @click="becomeTutor" >Become tutor</button>
</template>


<script setup >
 import { ref, onMounted } from "vue";
 let result = ref([])
onMounted(() => {
 getCsrfToken();
});
function becomeTutor() {
    fetch('/api/becomeTutor', {
    method: 'GET',
    headers: {
 'X-CSRFToken': csrf_token.value
 }
 
})
 
    .then(function (data) {
        console.log("om here")
    // display a success message
    
    console.log(data.json().tutors)
    })
    .catch(function (error) {
        console.log(JSON.stringify(error))
    });
}





let csrf_token = ref("");
    function getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
    console.log(data);
    csrf_token.value = data.csrf_token;
 })
 }

</script>
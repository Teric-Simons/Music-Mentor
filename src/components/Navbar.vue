<!-- Navbar.vue -->
<template>
  <nav class="nnavbar">
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
    <div class="logo ">
      <router-link to="/">Music Mentor</router-link>
      
    </div>
 
      <form @submit.prevent="search" action="search" class="f104noyw">
        <div class = "searchimg">
          
          <input v-model="searchTerm" placeholder="Search any song" type="search" class="s7ugfhf icefewr" style="--s7ugfhf-0:transparent" >
         <button class = "imgbut">
          <img src="src\assets\search.png" alt="">
         </button>
        </div>
        </form>
    
    <div class = "containerr">
          <uploadButton>
           
          </uploadButton>
        </div>
  
    <ul class="nav-links">
      <li><router-link to="/">Discover</router-link></li>
      <li><router-link to="/tutors">Find tutors</router-link></li>
 
      
          
        </ul>

        <nav class = "sign">
          <li v-if="!token" >
            <registerButton  class="nav-button">
              
            </registerButton> 
            
          </li>
          <div v-else class="bo">
              <div class = "navimg"  @click="openModal">
                
                <p><img height="38" width="38" src="src\assets\profile.png" alt="">{{fname}}</p>
              </div>
            </div>
        </nav>
        
  </nav>
  <div v-if="isModalVisible">
    <div class = "beek" @click="closeModal">

   

<div class = "loginoptions">


  <div v-if="tut == 'True'" class = 'sup'>
        <router-link  to="/dashboard" class ="dash">Dashboard</router-link>
      </div>
      <div class = 'sup' >

        <div class ="dash" @click="logout">
Logout
        </div>
        
    </div>
</div>
</div>

      
            </div>
 
</template>

<script setup>
 import { ref, onMounted } from "vue";
 const fname = localStorage.getItem("fname")
 const token = localStorage.getItem("token")
 const tut = localStorage.getItem("tutor")
 console.log(tut)
onMounted(() => {

 getCsrfToken();
});

const logout = () => {
  localStorage.removeItem("token")
  window.location.reload()
}
</script>

<script>


let csrf_token = ref("");
    function getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
    
    csrf_token.value = data.csrf_token;
    console.log(csrf_token.value)
    return csrf_token.value
 })
  
}

import uploadButton from "@/components/uploadButton.vue";
import registerButton from "@/components/Registerbutton.vue";
import becomeTutor from "./becomeTutor.vue";
export default {
  data() {
    return {
      searchTerm: '',
      isModalVisible: false,
    };
  },
  methods: {
    openModal() {
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    },
    search() {
      let cook = {"search" : this.searchTerm}
  cook = JSON.stringify(cook)
  fetch('/api/search', {
    method: 'POST',
    body: cook,
    headers: {
 'X-CSRFToken': csrf_token.value, 'content-type': 'application/json'
 }
 
    })
    .then(res => res.json())
        .then(data => {
          console.log(data)
          this.$router.push({
            path: '/about',
            query: { searchTerm: this.searchTerm, results: JSON.stringify(data.upload)}
            
         

          });
          
      
        })
      }
 
  },
  components: {
    uploadButton,
    registerButton,

    becomeTutor
},
};
</script>



<style scoped>
.beek{
  position: absolute;
  background-color: transparent;
  width: 89%;
  height: 680px;
}

a
{
  text-decoration: none;
  color: white;
}
.searchimg img{
  margin-top: -80px;
}
.loginoptions{
  box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
  padding: 5px;
  letter-spacing: 0.5px;
  font-size: 15px;
  display: block;
  align-items: center;
  border-radius: 4px;
  justify-content: center;
  position: absolute;
  background-color: white;
  margin-left: 1289px;
  width: 150px;
}


.searchimg input{
      height: inherit;
    appearance: none;
    background-color: #fff;
    border: none;
    border-radius: inherit;
    color: #333;
    font-family: TheSans,Arial,sans-serif;
    font-size: 16px;
    line-height: calc(24px - 2px);
    outline: 0;
    width: 100%;
}

input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration,
input[type="search"]::-webkit-search-results-button,
input[type="search"]::-webkit-search-results-decoration {
    display: none;
}
.sign{
  float: right;
 position: absolute;
 right: 0;
 margin-right: 40px;
 list-style: none;

}
.nav-button{
  width: 100%;
}

.bo{
  position: sticky;
}
.navimg{

  width: 100px;
  display: flex;
  align-items: center;
  text-align: center;
  cursor: pointer;

}

.navimg :hover{
  opacity: 0.5;
}
.navimg p{
  padding-top: 16px;
  font-size: 19px;
  margin-left: 5px;
  font-family: "Times New Roman", Times, serif;
}
.containerr{
  display: flex;
    align-items: center;
    vertical-align: middle;
    height: 100%;

    padding-left: 20px;
  padding-right: 20px;
 width:156px;
}
.imgbut{
  background-color: transparent;

  height: 37.5px;
  margin-left: 240px;
  border-color: transparent;
  border-radius: 4px;
  width: 1px;
}
.imgbut img
.icon{
    font-family: icons!important;
    font-style: normal;
    font-weight: 400!important;
    font-variant: normal;
    text-transform: none;
    line-height: 1;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
.icon {
    color: var(--i18g1tu5-0);
    display: inline-block;
    font-size: var(--i18g1tu5-1);
    font-style: normal;
    font-weight: inherit;
    -webkit-text-decoration: none;
    text-decoration: none;
    vertical-align: middle;
}
.searchimg{

  height: 100%;
  width: 60%;

}

form{
  height: 75%;
  width:500px;


}
input[type="search" i] {
    appearance: auto;
    box-sizing: border-box;
 
    padding-block: 1px;
    padding-inline: 2px;
    width: 100%;
}
/* Add your navigation bar styles here */

input{
  border-color: transparent;
    font-size: 14px;
    margin: 0;
    padding: 4px 32px 4px 8px;
    border: 1px solid transparent;
    border-radius: 4px;
    color: #333;
    height: 100%;
    text-overflow: ellipsis;
    line-height: calc(24px - 2px);
    width: 400px;




 
}
.nnavbar {
display: flex;
vertical-align: middle;
text-align: center;
background-color: #278dc0;
color: #FFFFFF;

height: 50px;
align-items: center;
}

.logwrapper{
  background-color: aqua;
}
.logo{
  font-size: 35px;
  padding-left: 20px;
  padding-right: 20px;

}





.nav-links {
  list-style: none;
  display: flex;
  gap: 23px;
  height: inherit;
  align-items: center;
  margin-top: 14px;
  margin-left: -220px;
  
}

.nav-links li {
  padding: 5px;
  vertical-align: middle;
  align-items: center;
  font-weight: bolder;

  font-size: 15px;
  
}
li:after {
  display:block;
  content: '';
  border-bottom: solid 3px white;  
  transform: scaleX(0);  
  transition: transform 250ms ease-in-out;
}
li:hover:after { transform: scaleX(1); }
li.fromRight:after{ transform-origin:100% 50%; }
li.fromLeft:after{  transform-origin:  0% 50%; }

.nav-links a {
  text-decoration: none;
  color: white;
}





.logo li{
  list-style: none;
  color: #FFFFFF;
  text-decoration: none;
  outline: none;

}
.sup{
  padding: 5px;
  width: 100%;
  cursor: pointer;
  border-bottom: 0.5px solid rgb(209, 195, 177) 
}

.dash{

  color: rgb(20, 20, 20);
 
  margin-left: 35px;



}

.sup:hover{
  background-color: lightblue;
}
</style>



<template>
<div class = "first">

        <div className="first2">
          <h1 className="first3">
            Think of the song and we'll find the materials!
          </h1>
          <h1 className="first3">
            Find the best tutor for you!
          </h1>
          <h1 class = 'ff'>
            Search our 23 million+ songs
          </h1>
          <form @submit.prevent="search" class = "first4">
            <div class = "bee"> 
              <input v-model="searchTerm" type="text" id="search" className="first5" placeholder="Search for any song" />
            </div>
            
            <button type="submit" className="first6">
              <span>Search</span>
              <img src="src\assets\search.ico" alt="">
            </button>
        
        </form>
        </div>
    


</div>
<footer className="first7">
        <div className="first8">
          <div className="first9">
            <div>
              <h2 className="first10">ABOUT</h2>
              <ul>
                <li><a href="/about">About Music Mentors</a></li>
                <li><a href="/privacy">Privacy Policy</a></li>
                <li><a href="/terms">Terms & Conditions</a></li>
              </ul>
            </div>
            <div>
              <h2 className="first10">FOR TUTORS</h2>
              <ul>
                <li><a href="/tutors/benefits">Benefits</a></li>
                <li><a href="/tutors/apply">Apply Now</a></li>
                <li><a href="/tutors/faq">FAQ</a></li>
              </ul>
            </div>
            <div>
              <h2 className="first10">FOR STUDENTS</h2>
              <ul>
                <li><a href="/students/find-tutor">Find a Tutor</a></li>
                <li><a href="/students/success-stories">Success Stories</a></li>
                <li><a href="/students/resources">Resources</a></li>
              </ul>
            </div>
            <div>
              <h2 className="first10">CONTACT</h2>
              <ul>
                <li><a href="/support/help-desk">Help Desk</a></li>
                <li><a href="/support/community">Our Community</a></li>
                <li><a href="/support/contact">Support</a></li>
              </ul>
            </div>
          </div>
        </div>
      </footer>



</template>

<style scoped>
.first10{
  margin-bottom: 0.75rem; 
font-size: 1.125rem;
line-height: 1.75rem; 
font-weight: 700; 
}

.first11{
  margin-bottom: 0.75rem; 
font-size: 1.125rem;
line-height: 1.75rem; 
font-weight: 700; 

}
.first6 span{
  padding-right:  20px;
  padding-left:  20px;
}

.first6 img{
  padding-right:  20px;
}
.ff{
  margin-top: 125px;
  color: #ffffff; 
font-size: 36px;
    text-align: center;
    text-shadow: 0 1px 1px rgba(0,0,0,.5), 0 2px 4px rgba(0,0,0,.3);
    font-family: "Times New Roman", Times, serif;
    font-weight: bolder;
}
.first{
  
  display: flex;
 
  justify-content: center;
  background-image: url('src\\assets\\home.jpg');
  background-size: cover;
  background-repeat: inherit;
  height: 94vh;
  width: 100%;

 

  
}

.first2{
  text-align: center;
  width: 100%;
  margin-top: 160px;
  
}

.first3{
  margin-bottom: 1.5rem; 
font-size: 2.25rem;
line-height: 2.5rem; 
font-weight: bolder;
color: #ffffff; 
font-size: 60px;
    text-align: center;
    text-shadow: 0 1px 1px rgba(0,0,0,.5), 0 2px 4px rgba(0,0,0,.3);
    font-family: "Times New Roman", Times, serif;
    
  
}

.first4{
  display: flex; 
justify-content: center; 
align-items: center; 
height: 50px;
font-size: 18px;



}

.bee{
  align-items: center;
    background-color: #fff;
    border: 1px solid #dfdfdf;
    border-radius: 4px;
    display: flex;
    padding: 8px 16px;
    width: 768px;
}

.first4 input{
 
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



input[type="search" i] {
    appearance: auto;
    box-sizing: border-box;
    writing-mode: horizontal-tb !important;
    padding-block: 1px;
    padding-inline: 2px;
}
.first5{
  padding-top: 0.5rem;
padding-bottom: 0.5rem; 
padding-left: 1rem;
padding-right: 1rem; 
border-top-left-radius: 0.25rem;
border-bottom-left-radius: 0.25rem; 
width: 50%; 
height: 80px;

}

.first5:focus{
  -webkit-transition: all 0.30s ease-in-out;
  -moz-transition: all 0.30s ease-in-out;
  -ms-transition: all 0.30s ease-in-out;
  -o-transition: all 0.30s ease-in-out;
  box-shadow: 0 0 5px rgba(81, 203, 238, 1);
  padding: 3px 0px 3px 3px;
  margin: 5px 1px 3px 0px;
  border: 1px solid rgba(81, 203, 238, 1);
}

.first6{

background-color: #2898d1;
height: 50px;
    color: #fff;
    font-size: 24px;
    padding-top: 8px;
    font-weight: 700;
    padding: 12px 24px;
    border: 1px solid transparent;
    border-radius: 8px;
    cursor: pointer;
    font-family: TheSans,Arial,sans-serif;
    margin: 0;
    outline: 0;
    padding: 0;
    position: relative;
    white-space: nowrap;
    margin-left: 10px;

}

.first7{
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 1.5rem;
padding-bottom: 1.5rem; 
color: #ffffff; 
background-color: #1F2937; 

}

.first8{
  padding-left: 1rem;
padding-right: 1rem; 
width: 100%;
}



.first9{
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr)); 
gap: 1rem; 


}

</style>



<style>
/* Add any component specific styles here */
</style>

<script setup>
 import { ref, onMounted } from "vue";
 
 let message = ref("Hello World! This is a VueJS and Flask Starter Template.")
 let result = ref([])
onMounted(() => {
 getCsrfToken();
});





</script>




<script>
onMounted(() => {
 getCsrfToken();
});
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
                    
export default {
  data() {
    return {
      searchTerm: '',
    };
  },
  methods: {
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
};
</script>
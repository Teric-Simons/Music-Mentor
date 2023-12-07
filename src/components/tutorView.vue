<template  >
  <div v-if="renderComponent">

 
     <div class="flex-table-row" v-for="(data, index) in tutors" :key="tutors.email" >
      <button @click="() => openModal(index)" class="">Send Message</button>
      <button @click="() => openModal2(index)" class="">Book</button>
    </div>
      <teleport to ="body">
    <div v-if="isModalVisible" class ="wrapper">
      <div class = "messagewrapper">
        <div class="xbut">
          <button @click="closeModal" class="close-button"><span id = "xee">x</span></button>
          <!-- Your content goes here -->
        </div>

        <div class="imgwrapper">
         <img class = "pimg" src="https://avatars.preply.com/i/logos/i/logos/avatar_qvozq1nkgm.jpg" alt="">
          <!-- Your content goes here -->
        </div>
        <div id = "heading">
         <h3 id = "needs" class="namewrapper">{{name}}</h3>
          <!-- Your content goes here -->
          <p>
            Introduce yourself to the tutor, share your learning goals and ask any questions
          </p>
          
        </div>
        
        <form class ="" action="POST"  @submit.prevent="sendMessage" id = "uploadForm" enctype="multipart/form-data">
          <div v-if="result.errors">
                <ul class="alert alert-danger">
                    <li v-for="error in result.errors">{{ error }}</li>
                </ul>
            </div>
          <div class="mmesswrapper">
            <textarea name = "message" class="messwrapper" placeholder="Write your message here…"></textarea>
       
        </div>

        <div class="buttonwrapper">
            <button id = "submit" type="submit">Send message</button>

        </div>
        
      </form>

        
     
        <section ref = "uploadedArea" class="uploaded-area"></section>

     
  
      </div>
    </div>

       <div  v-if="isModalVisible2" class ="wrapper">
    <div class = "mmessagewrapper">
        <div class = headingwrapper>
            <div class = "headingp">
                <img class = "ppimg" src="https://avatars.preply.com/i/logos/i/logos/avatar_qvozq1nkgm.jpg" alt="">
            <h3>Book a trial lesson</h3>
            </div>
            
            <button @click="closeModal2" class="close-button"><span id = "xee">x</span></button>
        </div>
        <form class ="" action="POST"  @submit.prevent="book" id = "bookForm" enctype="multipart/form-data">
          <div class = "bodywrapper">
        <div class="to">
            <p>From:</p>
            <Datepicker  v-model="picked" />
        </div>

        <div class="to">
            <p>To  :</p>
            <Datepicker  v-model="pickedd" />
        </div>

        <div class="bbuttonwrapper">
            <button id = "ssubmit" type="submit">Book date</button>

        </div>
      </div>
        </form>
      
     
        
        
        

  
  
      </div>

   </div>
    
    </teleport>
    
    
      
    
  </div>
</template>
<script>




let current = ""

let tutors  = []
let result = ref([])

export default {
  components: {
 
  },

  setup() {
    const date = ref(new Date());

    return {
      date,
    };
  },
  
data() {
  return {
    isModalVisible: false,
    isModalVisible2: false,
    name:null,
   
  };
},
methods: {
 
  closeModal() {
    this.isModalVisible = false;
    result = ref([])
  },
  closeModal2() {
    this.isModalVisible2 = false;
    result = ref([])
  },
   openModal(index) {
   
    Object.entries(tutors).forEach((entry) => {
  const [key, value] = entry;
  console.log(value);
  if(key == index){
    current = value.email
    this.name = "Contact "+value.fname + " " + value.lname
  }
});
this.isModalVisible = true;
    console.log(index)
    
  },
  openModal2(index) {
    Object.entries(tutors).forEach((entry) => {
  const [key, value] = entry;
  console.log(value);
  if(key == index){
    current = value.email
    this.name = "Contact "+value.fname + " " + value.lname
  }
});
this.isModalVisible2 = true;
    console.log(index)
   
 },



},
};
</script>



<script setup>

import Datepicker from 'vue3-datepicker'

import Book from './Book.vue'

 import { objectToString } from "@vue/shared";
import { ref, onMounted, nextTick } from "vue";
 let posts= ref([])

 const picked = ref(new Date())
 const pickedd = ref(new Date())
const renderComponent = ref(true)
const forceRender = async () => {
        renderComponent.value = false;
        await nextTick();
        renderComponent.value = true;
    };

    
onMounted(() => {
 getCsrfToken();

 getTutors();
//or in f
 
});
function getem(hi)
{
  console.log(hi)
}

function sendMessage()
{
  console.log(current)
  let movieForm = document.getElementById('uploadForm');
    let form_data = new FormData(movieForm);
    form_data.append("to", current)
    console.log(form_data)

  fetch('/api/sendMessage', {
    method: 'POST',
    body: form_data,
    headers: {
 'X-CSRFToken': csrf_token.value
 }
 
})
 
.then((response) => response.json())
  .then((data) => {
    result.value = data
    console.log(result.value)

})
    .catch(function (error) {
        console.log(JSON.stringify(error))
    });
}


function getTutors() {
    fetch('/api/getTutors', {
    method: 'GET',
    headers: {
 'X-CSRFToken': csrf_token.value
 }
 
})
 
.then((response) => response.json())
  .then((data) => {
    tutors = data.tutors
    forceRender()

  console.log(tutors)
})
    .catch(function (error) {
        console.log(JSON.stringify(error))
    });
}

function book()
{
  let date1 = picked.value.toString().substring(0, 15)
  let date2 = pickedd.value.toString().substring(0, 15)
  let cook = {"from" : date1, "to" : date2, "booker" : current}
  cook = JSON.stringify(cook)
  fetch('/api/book', {
    
    method: 'POST',
    body: cook,
    headers: {
 'X-CSRFToken': csrf_token.value, 'content-type': 'application/json'
 }
 
})
 
.then((response) => response.json())
  .then((data) => {
 

  console.log(tutors)
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


<style scoped>

.alert{
    list-style: none;
    text-align: center;
    font-weight: bold;
}
#ssubmit{
    width: 100%;
    height: 50px;
    border-radius: 7px;
    font-weight: bold;
    font-size: 18px;
    border-color: black;
    background-color: aqua;
    margin-top: 10px;
    color:#121117;
    
}

.to p{
  font-weight: bold;
  font-size: 18px;
}
.bbuttonwrapper{
    display: flex;
    align-items: center;
    justify-content: center;

}
.bodywrapper{
    margin-top: 20px;
}
.to{
    display: flex;
    width: 100%;
    justify-content: space-between;
}
.line{
    background-color: gray;
    height: 1px;
    margin-top: 25px;
}
.headingwrapper button{
    background-color: transparent;
    border: none;
}
.headingp h3{
    font-size: 18px;
    font-weight: bolder;
    margin-left: 18px;
    
}

#xee :hover{
  background-color: white;
}
.ppimg{
    height: 60px;
    width: 60px;
    border-radius: 4px;
}
.headingp{
    display: flex;
    align-items: center;
    justify-content: space-between;

}
.headingwrapper{
    vertical-align: baseline;
    padding-bottom: 23px;
    display: flex;
    width: 100%;
    justify-content: space-between;
    border-bottom: rgb(187, 186, 186) 1px solid;
    
}
.mmessagewrapper{
    text-align: center;
width: 330px;
height: auto;
background: #fff;
border-radius: 6px;
padding: 30px;
box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
float: left;
animation: 0.5s ease-out 0s 1 normal forwards running eowJkx;
}

.wrapper{
position: absolute;
top:0;
left:0;
background-color: rgba(0, 0, 0, 0.1);
width: 100%;
height: 100%;
display: flex;
justify-content: center;
letter-spacing: 0.025em;
    line-height: 32px;
    padding: 4px;
align-items: center;

}

.xbut{
    float: right;
    background-color: transparent;;
}

.close-button{
float: right;
margin-top: -20px;
font-size: 40px;
width:1px; /* or whatever width you want. */
 max-width:1px; /* or whatever width you want. */
 height:1px; /* or whatever width you want. */
 max-height:1px; /* or whatever width you want. */
 border: none;
}
#submit{
    width: 100%;
    height: 50px;
    border-radius: 7px;
    font-weight: bold;
    font-size: 18px;
    border-color: black;
    background-color: aqua;
    margin-top: 10px;
    color:#121117;
    
}
#heading p {
    font-size: 16px;
    font-style: normal;
    font-variation-settings: normal;
    font-weight: 400;
    line-height: 24px;
    color:#121117;

}

form{
    margin-top: 30px;
}


.pimg{
    height: 96px;
    width: 96px;
    border-radius: 4px;
}
h3{
    font-size: 24px;
    font-weight:600;
    letter-spacing: 0.016em;
    line-height: 32px;
    padding-bottom: 4px;
}
.buttonwrapper{
    display: flex;
    align-items: center;
    justify-content: center;

}
.messwrapper{
    border-radius: 8px;
    width: 100%;
    height: 80px;
    
}
.namewrapper{
    display: flex;
    align-items: center;
    width: 100%;
    flex-wrap: no-wrap;
    justify-content: center;
    margin-bottom: -3px;
  
}

.imgwrapper{
    display: flex;
    align-items: center;
    width: 100%;
    flex-wrap: no-wrap;
    justify-content: center;
    margin-bottom: 18px;
}
.wrapper{
position: absolute;
top:0;
left:0;
background-color: rgba(0, 0, 0, 0.1);
width: 100%;
height: 100%;
display: flex;
justify-content: center;
letter-spacing: 0.025em;
    line-height: 32px;
    padding: 4px;
align-items: center;

}

.messagewrapper{
    text-align: center;
width: 450px;
height: auto;
background: #fff;
border-radius: 6px;
padding: 30px;
box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
float: left;
animation: 0.5s ease-out 0s 1 normal forwards running eowJkx;
}</style>
<template>
    <div  class="teacherbody" >
        <teleport to ="body">
    <div v-if="isModalVisible" class ="wrapper">
      <div id = "oof2" class = "messagewrapper">
        <div class="xbut">
          <button @click="closeModal" class="close-button"><span id = "xee">x</span></button>
          <!-- Your content goes here -->
        </div>

        <div class="imgwrapper">
         <img id = "dumbimg" class = "pimg" :src="imgsrc" alt="">
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
            <button @click="sentMessage" id = "submit" type="submit">Send message</button>

        </div>
        
      </form>

        
     
        <section ref = "uploadedArea" class="uploaded-area"></section>

     
  
      </div>




      <div id = "oof" class = "sent messagewrapper">
        <div class="xbut">
          <button @click="closeModal" class="close-button"><span id = "xee">x</span></button>
          <!-- Your content goes here -->
        </div>

        <div class="imgwrapper">
         <img id = "dumbimg" class = "pimg" :src="imgsrc" alt="">
          <!-- Your content goes here -->
        </div>
        <div id = "heading2">
         <h3 id = "needs" class="namewrapper">Message Sent!</h3>
          <!-- Your content goes here -->
          <p id="suchi">
            Excited to start your learning journey?Book a lesson now.
          </p>
          
        </div>
        <div class="buttonwrapper">
            <button @click = "openModal2(currindex);closeModal()" id = "submit" type="submit">Book lesson</button>

        </div>

        <div class="buttonwrapper">
            <button @click="closeModal()" id = "submit2" type="submit">Close</button>

        </div>
        
       

        
     
        <section ref = "uploadedArea" class="uploaded-area"></section>

     
  
      </div>
    </div>

       <div  v-if="isModalVisible2" class ="wrapper">
    <div id = "nooof" class = "mmessagewrapper">
        <div class = headingwrapper>
            <div class = "headingp">
                <img class = "ppimg" :src="imgsrc" alt="">
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

      <div id = "nooof2" class = "mmessagewrapper sent">
        <div class = headingwrapper>
            <div class = "headingp">
                <img class = "ppimg" :src="imgsrc" alt="">
            <h3>Book a trial lesson</h3>
            </div>
            
            <button @click="closeModal2" class="close-button"><span id = "xee">x</span></button>
        </div>
        <div class = "bodywrapper">
        <div>
            <p id="lite">
                Tutor successfully booked! Please check your email.
          </p>
        </div>

        <div class="bbuttonwrapper">
            <button @click="closeModal2()" id = "ssubmit" type="submit">Close</button>

        </div>
      </div>
      
     
        
        
        

  
  
      </div>

   </div>
    
    </teleport>
        
        <div class = "filterwrap" >
            <div class="row1">
                <div class = "filter">
                    <div class="filterh">
                        <span>I want to learn</span>
                        <button class = "superclear" @click="clear2">X</button>

                    </div>
                    
                    <label for="">
                        <div  class = "inputss"  >
                            <select v-model="selected" name="cars" id="cars">
                                <option disabled selected value>Guitar</option>
                                <option value="Guitar">Guitar</option>
                                <option value="Piano">Piano</option>
                                <option value="Ukele">Ukele</option>
                                <option value="Drum">Drum</option>
                                <option value="Bass">Bass</option>
                                <option value="Violin">Violin</option>
                            </select>
                       
                        </div>
                    </label>

                </div>

                <div class = "filter">
                    <div class="filterh">
                        <span>Super Tutor</span>
                        <button class = "superclear" @click="clear1">X</button>

                    </div>
                    <label for="">
                        <div class="inputss">
                            <select v-model="selected4"  name="cars" id="cars">
                                <option disabled selected value>Yes</option>
                                <option value="Yes">Yes</option>
                                <option value="No">No</option>
                             
                            </select>

                       
                        </div>
                    </label>

                </div>


                <div class = "filter">
                    <div class="filterh">
                        <span>Country of Birth</span>
                        <button ></button>

                    </div>
                    <label for="">
                        <div id = "beet" class="inputss">
                            <img height ="25" src="src\assets\greysearch.ico" alt="">
                            <input v-model="selected2" id = "nat" type="text" placeholder="Jamaica">
                            
                       
                        </div>
                    </label>

                </div>

            </div>

            <div class="row2">
                <div>
                    <img height ="25" src="src\assets\greysearch.ico" alt="">
                    <input  v-model="selected3" type="text" class="filter" placeholder="Search by Name">
                </div>
                
            </div>
        </div>



        <div class = "avheading">
            <p>{{numtut}} Music teachers available</p>
        </div>

        <div v-if="componentLoaded" class = "tutorcard" v-for="(data, index) in filteredItems" :key="data.email">

            <div class="tutorwrap">
                <div class = "tutorinfo">
                <div class="img">
                <img height ='160' width="160" :src=  "data.imglink" alt="">
            </div>
            <div class ='info'>
                <div class = "name"><h2>{{ data.name }}</h2>
                    <svg aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M15.291 4.055 12 2 8.709 4.055l-3.78.874-.874 3.78L2 12l2.055 3.291.874 3.78 3.78.874L12 22l3.291-2.055 3.78-.874.874-3.78L22 12l-2.055-3.291-.874-3.78-3.78-.874ZM9.793 15.707l.707.707.707-.707 6-6-1.414-1.414-5.293 5.293-2.293-2.293-1.414 1.414 3 3Z" clip-rule="evenodd"></path></svg>
                    <img src="src\assets\jam.png" height ='20' width="20" alt="">
                    <span v-if="data.isSuper">
                  Super tutor
                </span>
                <span id="telse" v-else>Tutor
                </span>
                 
                </div>
              
                <div class = "add">
                    <p><img src="src\assets\music-note.png" alt=""> {{ data.instrument }}</p>
                    <p><img height="16" width="16" src="src\assets\student.jpg" alt=""> {{ data.numbook }} active students</p>
                    <p><img height="16" width="16" src="src\assets\lang.jpg" alt=""> Speaks {{ data.language }}</p>
                </div>

                <div class = "desc">
                    <p>{{ data.description }}</p> 
                </div>

            </div>
            <div class = 'controls'>
                <div class = 'revs'>
                    <div class = "review">
                    <img width="20" height="20" src="src\assets\star.png" alt="">
                    <span>5</span>
                </div>

                <div class = "price">
                    <p>${{ data.price }} JMD</p>
                </div>
                </div>
            

                <div class = 'buttons'>
                    <div class = 'book'>
                        <button @click="() => openModal2(index)">Book Lesson</button>
                    </div>

                    <div class = 'message'>
                        <button @click="() => openModal(index)">Send Message</button>
                    </div>
                </div>
        
                </div>



             

                

                

                
                <div>

               
            </div>
            </div>
            </div>
     

            <div id = "vid" class="tutorvidwrap">
                <div class = "tutorvid">
                    <iframe width="" height=""
:src= "data.video">
</iframe>
                </div>
                
             
            </div>
        </div>

    
    </div>
    

</template>


<script>




let current = ""

let tutors  = []
let  letgo = false
let result = ref([])
let numtut =""

let csrf_token = ref("");
export default {
   
  components: {
 
  },

  setup() {
    const date = ref(new Date());
    

    return {
      date,
    };
  },

 
  mounted()
  {
    
    this.getCsrfToken();
    this.getTutors();
    
    console.log("loaded")
  },

  
data() {
  return {
    isModalVisible: false,
    isModalVisible2: false,
    isModalVisible5: false,
    name:null,
    imgsrc:null,
    selected: '',
    selected2:'',
    selected3:'',
    selected4:'',
    componentLoaded: false,
    currindex:null,
    
   
  };
},

methods: {
     clear1()
{
  this.selected4 = '';
  console.log("hi")
},
getTutors() {
    console.log("Getut")
    fetch('/api/getTutors', {
    method: 'GET',
    headers: {
 'X-CSRFToken': csrf_token.value
 }
 
})
 
.then((response) => response.json())
  .then((data) => {
    tutors = data.tutors
    numtut = tutors.length
    console.log(numtut)
    this.componentLoaded = true;
    
 

  console.log(tutors)
})
    .catch(function (error) {
        console.log(JSON.stringify(error))
    });
},

     getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
    console.log(data);
    csrf_token.value = data.csrf_token;
 })
 },

clear2()
{
  this.selected = '';
  console.log("hi")
},
clear3()
{
  this.selected2 = '';
  console.log("hi")
},

 
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
    this.currindex = index;
    current = value.email
    this.name = "Contact "+value.fname + " " + value.lname
    this.imgsrc = value.imglink
    console.log(this.imgsrc)

    
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
    this.imgsrc = value.imglink
    console.log(this.imgsrc)
  }
});
this.isModalVisible2 = true;
    console.log(index)
   
 },



},
computed: {
   
    

    filteredItems() {
       
        
     console.log("filter")

      
        return tutors
        .filter(item => {
         return item.instrument.toLowerCase().includes(this.selected.toLowerCase());
      })
      .filter(item => {
         return item.nationality.toLowerCase().includes(this.selected2.toLowerCase());
      })
      .filter(item => {
         return item.name.toLowerCase().includes(this.selected3.toLowerCase());
      })
      .filter(item => {
    
        return item.isrlly.toLowerCase().includes(this.selected4.toLowerCase());
      })
    
    
    }
    
  }
};
</script>



<script setup>

import Datepicker from 'vue3-datepicker'

import Book from './Book.vue'

 import { objectToString } from "@vue/shared";
import { ref ,onBeforeMount, onMounted, nextTick, defineExpose } from "vue";
 let posts= ref([])

 const picked = ref(new Date())
 const pickedd = ref(new Date())
const renderComponent = ref(true)
const forceRender = async () => {
        renderComponent.value = false;
        await nextTick();
        renderComponent.value = true;
    };

    



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
    if (!data['errors']){
        console.log("sent")
var  sent = document.getElementById("oof")
var  sent2 = document.getElementById("oof2")
sent.classList.add("sentshow");
sent2.classList.add("sent")
    }
    

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
  var  sen = document.getElementById("nooof")
var  sen2 = document.getElementById("nooof2")
sen.classList.add("sent");
sen2.classList.add("sentshow")
})
    .catch(function (error) {
        console.log(JSON.stringify(error))
    });
}





</script>




<style scoped>
#submit{
    width: 100%;
    height: 50px;
    border-radius: 7px;
    font-weight: bold;
    font-size: 18px;
    border-color: black;
    background-color: #3db0e9;
    margin-top: 10px;
    color:#121117;
    
}

#submit2{
    width: 100%;
    height: 50px;
    border-radius: 7px;
    font-weight: bold;
    font-size: 18px;
    border-color: black;
    margin-top: 10px;
    color:#121117;
    
}

.messwrapper{
    border-radius: 8px;
    width: 100%;
    height: 80px;
    
}
.alert{
    list-style: none;
    text-align: center;
    font-weight: bold;
}
#heading p {
    font-size: 16px;
    font-style: normal;
    font-variation-settings: normal;
    font-weight: 400;
    line-height: 24px;
    color:#121117;

}

#heading2 p {
    
    font-size: 16px;
    font-style: normal;
    font-variation-settings: normal;
    width: 290px;
    font-weight: 700;
    line-height: 24px;
    color:#121117;
    text-align: center;
    align-items: center;
    margin-left: 40px;
    justify-content: center;

}


.pimg{
    height: 96px;
    width: 96px;
    border-radius: 4px;
}


.imgwrapper{
    display: flex;
    align-items: center;
    width: 100%;
    flex-wrap: no-wrap;
    justify-content: center;
    margin-bottom: 18px;
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

.filter{
    background-color: #fff;
    border: 2px #dcdce5 solid;
    border-radius: 8px;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 8px 16px;
    width: 25%;
}



.filter span{
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    font-size: 17px;
}

.inputss{


}
.buttonwrapper{
    display: flex;
    align-items: center;
    justify-content: center;

}
#needs{
    font-weight: 700;
}
.namewrapper{
    display: flex;
    align-items: center;
    width: 100%;
    flex-wrap: no-wrap;
    justify-content: center;
    margin-bottom: 5px;
  
}

.inputss select{
    font-weight: 700;
    border-radius: 4px;
    width: 100%;
    border: none;
}

.filterh{
    display: flex;
    justify-content: space-between;
}

.filterh button{
    background-color: transparent;
    border: none;
    font-size: 13px;
}

.filterh button:hover{
    background-color: transparent;
    border: none;
    font-size: 16px;
}

.inputss option{
    font-size: 18px;
    font-family: 'Figtree', 'Figtree-fallback', 'Figtree-fallback-android', 'Noto Sans', 'NotoSans-fallback', 'NotoSans-fallback-android', sans-serif;
    font-weight: 100;
}
.avheading{
    margin-bottom: 23px;
    margin-top: 23px;
}
#beet{
    display: flex;
    justify-content: space-between;
  
}

.xbut{
    float: right;
    background-color: transparent;;
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
}

#beet input{
    margin-left: 15px;
}
.tutorvidwrap{

    
    border: 2px solid black;
    border-radius: 4px;
    opacity: 0;
    transition: 0.5s;
    margin-left: 10px;
}

.tutorvid{
    height: 238px;
    aspect-ratio: 16/9;
    width: 420px;
 
}

.tutorvid iframe{
    height: 100%;
    width: 100%;
    
    
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
.sent{
    display: none;
}

.sentshow{
    display: block;
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

.row2{
    display: flex;
    justify-content: right;
}

.row2 div{
  
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 25%;
    border: #2898d1;;
    border: 2px solid #dcdce5;
    border-radius: 8px;
    height: 50px;
    padding: 16px;

}

.row2 input{
    width: 100%;
    border: none;
    border: none;
    height: 27px;
    margin-left: 5px;
    font-weight: bold;
}

.row2 input:focus{
    
}

.row2 input:hover{
    cursor: text;
}

#nat{
    border: none;
    width: 100%;
   
    border-radius: 8px;
    font-weight: 700;
    letter-spacing: 0.5px;
}
.teacherbody{
   
  margin-left: 80px;
  margin-right: 80px;
    
}
.filter{
    margin-top: 25px;
    margin-bottom: 25px;
  
}
.row1{
    display: flex;
    justify-content:space-between;
}
.tutorcard{
   
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-bottom: 10px;
}

.tutorcard:hover .tutorvidwrap{
    opacity: 1;

}
.img{
    background: #f8f8f8;
    border-radius: 4px;
    text-decoration: none;
    transition: all .3s;
   
}
#telse{
    padding-left: 10px;
    padding-right: 10px;
    background-color: #2898d1;
}

.img img{
    border: 0.5px solid rgba(18,17,23,.06);
    border-radius: 4px;
   
}

.avheading p{
    font-size: 18px;
    font-weight: 700;
    line-height: 1.42857143;
}

.info{
   margin-left: 13px;
   margin-right: 13px;
width: 400px;
}
.tutorinfo{
  
    display: flex;
    flex-direction: row;
    width: 100%;
}


.controls{
    display: flex;
  flex-direction: column;
   


width: 225px;
  
}

.revs{
  

    display: flex;
    justify-content: space-between;
    margin-bottom: auto;

}

.price{
   
}
.buttons{
    
}

.book button{
    width: 100%;
  
}


.message button{
    width: 100%;
   
}

.tutorwrap{
   

    padding: 25px;
    border: 2px solid black;
    border-radius: 4px;
    line-height: 1.42857143;
}

.name{
    display: flex;
   align-items: center;
    width: auto;
   
}

.name svg{
    width: 20px;
    height: 20px;
    margin-right: 10px;
}

.name h2{
    margin-top: 5px;
    font-size: 1.5rem;
line-height: 2rem; 
font-weight: 700; 
color: #000000; 
margin-right: 10px;
white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
;
}



.name span{
    display: inline-block; 
padding-top: 0.31rem;
padding-bottom: 0.25rem; 
padding-left: 0.5rem;
padding-right: 0.5rem; 
margin-left: 0.5rem; 
border-radius: 9999px; 
font-size: 0.75rem;
line-height: 1rem; 
line-height: 1; 
color: #ffffff; 
background-color: #d7672f;; 
margin-top: 6px;
height: 25px;
font-weight: 900;
letter-spacing: 0.4px;

}
.add{
    margin-top: 4px;
    margin-bottom: 15px;
}

.add img{
    margin-top: -7px;
}
.add p{
    font-family :'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin-bottom: 0.5rem; 
font-size: 1rem;
font-weight: 400;
line-height: 1.25rem; 
color: #4d4c5c;
}

.desc p{
    font-family:Arial, Helvetica, sans-serif;
    margin-bottom: 0.5rem; 
font-size: 1rem;
line-height: 1.25rem; 
color: black; 
    font-size: 16px;
    font-weight: lighter;
    letter-spacing: 0.5px;
    
}


.review img{
    margin-top: -10px;
}

.review span{
    margin-left: 0.25rem; 
font-size: 0.875rem;
line-height: 1.25rem; 
font-size: 1.5rem;
    font-weight: 700;
color: black 
}

.price p{
    margin-left: 0.25rem; 
    font-size: 1.5rem;
    font-weight: 700;
line-height: 1.25rem; 
color: black; 
    
}

.book button{
    padding-top: 0.5rem;
padding-bottom: 0.5rem; 
padding-left: 1rem;
padding-right: 1rem; 
border-radius: 8px; 
border-width: 1px; 
border-color: #000000; 
width: 100%; 
font-size: 18px;
line-height: 1.25rem; 
font-weight: 700; 
color: black; 
background-color: #3db0e9;; 
margin-bottom: 9px;
min-height: 48px;
letter-spacing: 0.005em;
border: 2px solid black;
}


.message button{
    padding-top: 0.5rem;
padding-bottom: 0.5rem; 
padding-left: 1rem;
padding-right: 1rem; 
border-radius: 8px; 
border-width: 1px;
font-weight: 700;  
width: 100%; 
font-size: 18px;
line-height: 1.25rem; 
font-weight: 700; 
margin-bottom: 0px;
min-height: 48px;
letter-spacing: 0.005em;
background-color: transparent;
    border-color: #dcdce5;
    color: black;
    border: 2px solid rgb(168, 163, 163);

}
.close-button :hover{
  font-size: 30px;
}

.headingwrapper{
    vertical-align: baseline;
    padding-bottom: 23px;
    display: flex;
    width: 100%;
    justify-content: space-between;
    border-bottom: rgb(187, 186, 186) 1px solid;
    
}
.headingp h3{
    font-size: 18px;
    font-weight:bolder;
    margin-left: 18px;
    
}
.headingp{
    display: flex;
    align-items: center;
    justify-content: space-between;

}
.bodywrapper{
    margin-top: 20px;
}

.bbuttonwrapper{
    display: flex;
    align-items: center;
    justify-content: center;

}

#ssubmit{
    width: 100%;
    height: 50px;
    border-radius: 7px;
    font-weight: bold;
    font-size: 18px;
    border-color: black;
    background-color: #3db0e9;
    margin-top: 10px;
    color:#121117;
    
}
.ppimg{
    height: 60px;
    width: 60px;
    border-radius: 4px;
}
.to p{
  font-weight: bold;
  font-size: 18px;
}

.to{
    display: flex;
    width: 100%;
    justify-content: space-between;
}

#suchi{
    font-size: 200px;
    font-style: normal;
    font-variation-settings: normal;
    font-weight: 400;
    line-height: 24px;
    color:#121117;
}

#lite{
    font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    width: 250px;
    margin-left: 5px;
    font-weight: 700;
}
</style>
<template>
  <div class = "containerr">
    <button @click="openModal" class="nav-button">
      <img width="18"  height="18" src="src\assets\upload.ico" alt="">
      <div id = "up">
        <p >Upload Song</p>
      </div>
    </button>
    <!-- Modal -->

    <teleport to ="body">
    <div v-if="isModalVisible" class ="upload">
      <div class = "aupload">
        <div class="container">
          <button @click="closeModal" class="close-button"><span id = "xee">x</span></button>
          <!-- Your content goes here -->
        </div>
        
        <form class ="cf" action="POST"  @submit.prevent="saveSheet" id = "uploadForm" enctype="multipart/form-data">
          
          <div class="half left cf">
            <div v-if="result.errors">
            <ul class="alert alert-danger">
                <li >{{ result.errors[0] }}</li>
            </ul>
        </div>

     
            <header>Upload Sheet Music</header>
          <input type="text" id="input-name" placeholder="Sheet Title" name ="title">
          <input type="text" id="input-email" placeholder="Composer" name ="composer">
          <select class="input-subject" name="genre">
            <option value="" disabled selected>Select a Genre</option>
            <option value="Hip Hop">Hip Hop</option>
            <option value="Reggae">Reggae</option>
            <option value="Classical">Classical</option>
            <option value="Dancehall">Dancehall</option>
          </select>

          <select class="input-subject" name="instrument">
            <option value="" disabled selected>Select an Instrument</option>
            <option value="Piano">Piano</option>
            <option value="Guitar">Guitar</option>
            <option value="Violin">Violin</option>
            <option value="Drum">Drum</option>
          </select>

          <input id = "sheet-file" class="file-input" type="file" name="file">
          <input type="submit" value="Submit" id="input-submit">
  
        </div>
          
        <div v-if="result.message">
        <div class = "su">
          <p>Upload Successful</p>
          <img src="src\assets\check.png" alt="" height="25" width="29">
        </div>
      
        </div>

        
      </form>
        
     
     

      </div>
       
  
      </div>
    </teleport>
  </div>

</template>


<script setup>
import { ref, onMounted } from "vue";

onMounted(() => {
getCsrfToken();
});

function succ(){
  
  if(result.errors)
  {
    console.log("noo")
  }
}

function saveSheet() {
  let movieForm = document.getElementById('uploadForm');
  let form_data = new FormData(movieForm);


  fetch('/api/bee', {
  method: 'POST',
  body: form_data,
  headers: {
'X-CSRFToken': csrf_token.value
}


  })

  .then(res => res.json())
        .then(data => {
            result.value = data
            console.log(data)
        })
        .catch(err => result.value = err)
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



<script>
let result = ref([])








export default {
data() {
  return {
    isModalVisible: false,
  };
},
methods: {
  
  openModal() {
    result = ref([])
    this.isModalVisible = true;
    console.log("gg")
  },
  closeModal() {
    this.isModalVisible = false;
  },
  



},
};
</script>




<style scoped>
@import url(https://fonts.googleapis.com/css?family=Merriweather);
.nav-button:hover { background:#19a8ba }

#up{
  display: flex;
  height: 100%;
  align-items: center;
  justify-content: center;
  font-weight: bolder;
}
#up p{
  display: flex;
  align-items: center;
  font-size: 13px;
 height: 100%;
 margin-top: 14px;
 margin-left: 5px;
  
}
.half {
float: left;
width: 300px;
margin-bottom: 1em;
}


.left {
   margin-right: 2%; 
}


@media (max-width: 480px) {
.half {
   width: 100%; 
   float: none;
   margin-bottom: 0; 
}
}





/* Clearfix */
.cf:before,
.cf:after {
  content: " "; /* 1 */
  display: table; /* 2 */
}

#xee :hover{
  background-color: white;
}
.cf:after {
  clear: both;
}
form input, textarea, select {
border:0; outline:0;
   padding: 1em;
   border-radius: 8px;
   display: block;
   width: 100%;
   background-color:  #f1f1f1;;
   margin-top: 1em;
   font-family: 'Merriweather', sans-serif;

   box-shadow: 1px 1px #888888;
   resize: none;

}

.containerr{
  margin-left: -220px;
}
 


#input-submit {
   color: white; 
   background-color: #2898d1;
   cursor: pointer;
   width: 50%;
   margin-left: 70px;
   margin-top: 20px;
  

}

.upload{
position: absolute;
top:0;
left:0;
background-color: rgba(0, 0, 0, 0.1);
width: 100%;
height: 100%;
display: flex;
justify-content: center;
align-items: center;
}

.aupload{
width: auto;
height: auto;
background: #fff;
border-radius: 5px;
padding: 30px;
box-shadow: 7px 7px 12px rgba(0,0,0,0.05);
}

.alert{
  list-style: none;
}

.su{
  margin-top: -11px;
  display: flex;
  align-items: center;
  vertical-align: middle;
  background-color: #78d995;
  text-align: center;
  height: 40px;
  justify-content: space-between;
  padding: 10px;
  border-radius: 40px;
  padding-left: 23px;
  padding-right: 23px;
}

.su p{
  margin-top: 14px;
  color: #207239;
  font-weight: bold;
  height: auto;
  font-size: 25px;
}

.alert-danger{
  margin-top: 9px;
}
.aupload header{
color: #6990F2;
font-size: 27px;
font-weight: 600;
text-align: center;

}
form{
width: auto;
 text-align: center;
 margin: 20px auto;

}
.purple{
border: 2px dashed #6990F2;
height: 167px;
display: flex;
cursor: pointer;
margin: 30px 0;
align-items: center;
justify-content: center;
flex-direction: column;
border-radius: 5px;
}
.purple :where(i, p){
color: #6990F2;

}
form i{
font-size: 50px;
}
form p{
margin-top: 15px;
font-size: 16px;
}
section .row{
margin-bottom: 10px;
background: #E9F0FF;
list-style: none;
padding: 15px 20px;
border-radius: 5px;
display: flex;
align-items: center;
justify-content: space-between;
}
section .row i{
color: #6990F2;
font-size: 30px;
}
section .details span{
font-size: 14px;
}
.progress-area .row .content{
width: 100%;
margin-left: 15px;
}
.progress-area .details{
display: flex;
align-items: center;
margin-bottom: 7px;
justify-content: space-between;
}
.progress-area .content .progress-bar{
height: 6px;
width: 100%;
margin-bottom: 4px;
background: #fff;
border-radius: 30px;
}
.content .progress-bar .progress{
height: 100%;
width: 0%;
background: #6990F2;
border-radius: inherit;
}
.uploaded-area{
max-height: 232px;
overflow-y: scroll;
}
.uploaded-area.onprogress{
max-height: 150px;
}
.uploaded-area::-webkit-scrollbar{
width: 0px;
}
.uploaded-area .row .content{
display: flex;
align-items: center;
}
.uploaded-area .row .details{
display: flex;
margin-left: 15px;
flex-direction: column;
}
.uploaded-area .row .details .size{
color: #404040;
font-size: 11px;
}
.uploaded-area i.fa-check{
font-size: 16px;
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



.nav-button {
  align-items: center;
  display: flex;
  background-color: #1b6286;
color: white;
font-size: 15px;
border: none;
border-radius: 4px;
cursor: pointer;
width: 1050px;
height: 80%;

}

</style>
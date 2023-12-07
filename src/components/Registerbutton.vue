<template>
    <button @click="openModal" class="nav-button"><span class="">Sign up<!-- --> | <!-- -->Log in</span></button>
    <teleport to ="body">
        <div v-if="isModalVisible" class ="logcontainer">
            <div class = "s7hxpvl d16v9yx2 svzlj66" style="--svzlj66-0: 8px; --svzlj66-1: 0 16px 32px -16px rgba(0,0,0, .25); --s7hxpvl-0: 540px;">
                <div class = "modalheader">
                    <h2 id="modal-title" class ="t7ooqdc h3w46bu">Log in to Music Mentor</h2>
                    <button @click="closeModal" id = "closebut">
                        <img src="src\assets\close.png" height="18" width="18" alt="">
                    </button>
                </div>
                <div class="cjhg8mv">
                    <h3 class="t17ttet6 h1n234tp"></h3>
                    <p></p>
                    <div id = "s1" class="fwj7npu n1ft9k01" style="--n1ft9k01-0: block;">
                        <button id = "redbut" class="f18bz2u9 bzq1snp b9568gz" style="--bzq1snp-0: 4px; --bzq1snp-1: 12px; --bzq1snp-2: 4px 8px;">
                            <img height="20" width="20" src="src\assets\goog.png" alt="">
                            Continue with Google</button><div class="h9qtbd2">Or</div>
                        </div>
                        <form id = "login" action="POST"  @submit.prevent="loginUser" enctype="multipart/form-data">
                            <div v-if="result.errors">
                <ul class="alert alert-danger">
                    <li v-for="error in result.errors">{{ error }}</li>
                </ul>
            </div>
                            
                            <label class = "lkx9euj" for="email">Email Address</label>
                            <div class="MuiInput-root ip1pa97"><input required="" autocomplete="email" name="email" height="40" placeholder="musicmentor@gmail.com" type="email" class="MuiInput-input icefewr" value=""></div>
                            <label class = "lkx9euj" for="pass">Password</label>
                            <div pattern=".{6,}" class="MuiInput-root ip1pa97"><input required="" autocomplete="current-password" name="password" placeholder="At least 6 characters" type="password" class="MuiInput-input icefewr" value=""></div>
                            <div id = "lanc" class="l1nbac25"><a class="l1amswbe" style="--l1amswbe-0: inherit; --l1amswbe-1: underline;">Forgot password?</a></div>
                            <div  class="b1ix7qfq"><button @click="openSignup" type="button" class="b1rgdfc0 bzq1snp b9568gz" style="--bzq1snp-0: 4px; --bzq1snp-1: 14px; --bzq1snp-2: 8px 16px;"><span class="c19mc1wo"><span id = "loginButton">Create account</span></span></button><button type="submit" class="bwifbmu bzq1snp b9568gz" style="--bzq1snp-0: 4px; --bzq1snp-1: 14px; --bzq1snp-2: 8px 16px;"><span class="c19mc1wo"><span id = "signBut">Log in</span></span></button></div>
                        </form>
                        <form id = "signup" action="POST"  @submit.prevent="registerUser" enctype="multipart/form-data">
                            <div v-if="result.errors">
                <ul class="alert alert-danger">
                    <li v-for="error in result.errors">{{ error }}</li>
                </ul>
            </div>
                            
                            <label class = "lkx9euj" for="first">First Name</label>
                            <div class="MuiInput-root ip1pa97"><input required="" autocomplete="email" name="firstname" height="40" placeholder="Music" type="text" class="MuiInput-input icefewr" value=""></div>
                            <label class = "lkx9euj" for="last">Last Name</label>
                            <div class="MuiInput-root ip1pa97"><input required="" autocomplete="email" name="lastname" height="40" placeholder="Mentor" type="text" class="MuiInput-input icefewr" value=""></div>
                            <label class = "lkx9euj" for="email">Email Address</label>
                            <div class="MuiInput-root ip1pa97"><input required="" autocomplete="email" name="email" height="40" placeholder="musicmentor@gmail.com" type="email" class="MuiInput-input icefewr" value=""></div>
                            <label class = "lkx9euj" for="pass">Password</label>
                            <div pattern=".{6,}" class="MuiInput-root ip1pa97"><input required="" autocomplete="current-password" name="password" placeholder="At least 6 characters" type="password" class="MuiInput-input icefewr" value=""></div>
                            <div id = "lanc" class="l1nbac25"><a class="l1amswbe" style="--l1amswbe-0: inherit; --l1amswbe-1: underline;">Forgot password?</a></div>
                            <div  class="b1ix7qfq"><button @click="openSignup" type="button" class="b1rgdfc0 bzq1snp b9568gz" style="--bzq1snp-0: 4px; --bzq1snp-1: 14px; --bzq1snp-2: 8px 16px;"><span class="c19mc1wo"><span id = "loginButton">Log in instead</span></span></button><button  type="submit" class="bwifbmu bzq1snp b9568gz" style="--bzq1snp-0: 4px; --bzq1snp-1: 14px; --bzq1snp-2: 8px 16px;"><span class="c19mc1wo"><span id = "signBut">Create account</span></span></button></div>
                        </form>
                        
                </div>
                
            </div>
        </div>
    </teleport>
</template>





<script setup >
 import { ref, onMounted } from "vue";
 let result = ref([])

onMounted(() => {
 getCsrfToken();
});
function registerUser() {
    
    let movieForm = document.getElementById('signup');
    let form_data = new FormData(movieForm);
  
  
    fetch('/api/register', {
    method: 'POST',
    body: form_data,
    headers: {
 'X-CSRFToken': csrf_token.value
 }
 

    })
 
    .then(res => res.json())
        .then(data => {
            result.value = data
            if(data["errors"])
            {
              
            }
            else{
                console.log(data)
                localStorage.setItem("token", data.token)
                localStorage.setItem("fname", data.fname)
                localStorage.setItem("email", data.email)
                localStorage.setItem("tutor", data.tutor)
                 window.location.reload()
            }
        })
        .catch(err => result.value = err)




    

        
}



function loginUser() {
    
    console.log("login")
    let movieForm = document.getElementById('login');
    let form_data = new FormData(movieForm);
  
  
    fetch('/api/login', {
    method: 'POST',
    body: form_data,
    headers: {
 'X-CSRFToken': csrf_token.value
 }
 

    })
 
     .then(res => res.json())
        .then(data => {
            console.log(result.value)
            result.value = data
            if(data["errors"])
            {
              
            }
            else{
                localStorage.setItem("token", data.token)
                localStorage.setItem("email", data.email)
                localStorage.setItem("fname", data.fname)
                localStorage.setItem("tutor", data.tutor)
                localStorage.setItem("price", data.price)
                 window.location.reload()
            }
            
        })
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


function openSignup() {

      let login = document.getElementById('login')
      let signup = document.getElementById('signup')
      let logBut = document.getElementById('loginButton')
      let signBut = document.getElementById('signBut')
      if (login.style.display != 'none')
      {
        login.style.display = "none";
        signup.style.display = "block";
        logBut.innerText = "Log in instead"
        signBut.innerText = "Create Account"

      }
      else{
        login.style.display = "block";
        signup.style.display = "none";
        logBut.innerText = "Create Account"
        signBut.innerText = "Log in"
      }
      
 
    }
</script>


<script>
 
export default {
  data() {
    return {
      isModalVisible: false,
    };
  },
  methods: {
    openModal() {
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

.nav-button{
    background-color: transparent;
    color: white;
    outline: none;
    border: none;
    font-weight: bolder;
    font-size: 15px;
}

form{
    width: 100%;
}
#login{
    display: none;
    display:block;
}

#signup{
    
    display: none;
}

.inheight{

}

.alert{
    list-style: none;
    text-align: center;
    font-weight: bold;
}

.icefewr {
    border-radius: 4px;
    color: #333;
    font-family: TheSans,Arial,sans-serif;
    font-size: 16px;
    line-height: calc(24px - 2px);
    outline: 0;
    width: 100%;
    height: 42px;
}
.lkx9euj {
    margin-bottom: 4px;
    color: #000;
    font: 11pt thesans,Arial,sans-serif;
    font-size: 16px;
}
#closebut{
    background-color: Transparent;
    background-repeat:no-repeat;
    border: none;
    cursor:pointer;
    overflow: hidden;  
    width: auto;   

}

#closebut :hover{
    background-color: #dfdfdf;    
    border-radius: 4px;
}
#modal-title{
    font-size: 24px;
}
.t7ooqdc {
    font-size: 24px;
}
.t7ooqdc {
    -webkit-align-self: center;
    -ms-flex-item-align: center;
    align-self: center;
    font-size: 20px;
}

.h3w46bu {
    font-size: 20px;
}
.h3w46bu {
    color: inherit;
    font-weight: 400;
    margin: 0;
    font-size: 18px;
    font-weight: 700;
}
.bwifbmu.bzq1snp.b9568gz {
    background-color: #2898d1;
    color: #fff;
}
.bzq1snp.b9568gz {
    border: 1px solid transparent;
    border-radius: var(--bzq1snp-0);
    font-size: var(--bzq1snp-1);
    font-weight: 700;
    padding: var(--bzq1snp-2);
}
.b1ix7qfq button+button {
    margin-left: 8px;
}
.b9568gz {
    background-color: transparent;
    border: none;
    color: inherit;
    cursor: pointer;
    font-family: TheSans,Arial,sans-serif;
    margin: 0;
    outline: 0;
    padding: 0;
    position: relative;
    white-space: nowrap;
}
.b1ix7qfq {
    padding: 4px 0;
    text-align: right;
}
.b1rgdfc0.bzq1snp.b9568gz {
    background-color: #fff;
    border-color: #333;
    color: #333;
}

.bzq1snp.b9568gz {
    border: 1px solid transparent;
    border-radius: var(--bzq1snp-0);
    font-size: var(--bzq1snp-1);
    font-weight: 700;
    padding: var(--bzq1snp-2);
}
.b9568gz {
    background-color: transparent;
    border: none;
    color: inherit;
    cursor: pointer;
    font-family: TheSans,Arial,sans-serif;
    margin: 0;
    outline: 0;
    padding: 0;
    position: relative;
    white-space: nowrap;
}
.l1amswbe {
    color: var(--l1amswbe-0);
    -webkit-text-decoration: var(--l1amswbe-1);
    text-decoration: underline;
}
.l1nbac25 {
    margin: 16px 0;
    text-align: left;
}
#lanc{
    margin-top: 35px;
}

input {
 
  border: 1px solid #ccc;
  border-radius: .1875rem;
  box-sizing: border-box;
  display: block;
  font-size: .875rem;
  margin-bottom: 1rem;
  padding: 20px;
  width: 100%;
  opacity: 0.7;
}



input[type="password"] {
  margin-bottom: .5rem;
}

input[type="submit"] {
  background-color: #015294;
  border: none;
  color: #fff;
  font-size: 1rem;
  padding: .5rem 1rem;
}

label {
  color: #666;
  font-size: .875rem;
}
.h9qtbd2::before {
    -webkit-transform: translateX(calc(-5px - 100%));
    -ms-transform: translateX(calc(-5px - 100%));
    transform: translateX(calc(-5px - 100%));
}
.h9qtbd2::before, .h9qtbd2::after {
    border-bottom: 1px solid;
    border-color: inherit;
    content: "";
    height: 1px;
    opacity: .75;
    position: absolute;
    top: calc(50% - 1px);
    width: 60px;
}
.h9qtbd2::after {
    margin-left: 5px;
}
.h9qtbd2::before, .h9qtbd2::after {
    border-bottom: 1px solid;
    border-color: inherit;
    content: "";
    height: 1px;
    opacity: .75;
    position: absolute;
    top: calc(50% - 1px);
    width: 60px;
}
.h9qtbd2 {
    color: inherit;
    font-weight: 700;
    margin: 10px 0;
    position: relative;
    text-align: center;
    text-transform: uppercase;
}
.fwj7npu {
    margin-top: 20px;
    text-align: center;
}
.n1ft9k01 {
    display: var(--n1ft9k01-0);
}
user agent stylesheet
div {
    display: block;
}
#s1{
    display: block;
}
#s3{
    font-size: 30px;
}
*[class^=icon-], *[class*=" icon-"] {
    font-family: icons!important;
    font-style: normal;
    font-weight: 400!important;
    font-variant: normal;
    text-transform: none;
    line-height: 1;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
.c15raq77 {
    float: left;
    font-weight: 400;
    margin-right: 5px;
}
.i18g1tu5 {
    color: white;
    color: var(--i18g1tu5-0);
    display: inline-block;
    font-size: var(--i18g1tu5-1);
    font-style: normal;
    font-weight: inherit;
    -webkit-text-decoration: none;
    text-decoration: none;
    vertical-align: middle;
}
#redbut{
    background: black;
 
    color: white;
}
.bzq1snp.b9568gz {
    border: 1px solid transparent;
    border-radius: var(--bzq1snp-0);
    font-size: var(--bzq1snp-1);
    font-weight: 700;
    padding: var(--bzq1snp-2);
}
.f18bz2u9 {
    background-color: #395b93;
    color: #fff;
    line-height: 30px;
    padding: 5px 20px 5px 15px;
    text-align: left;
}
.b9568gz {
    background-color: transparent;
    border: none;
    color: inherit;
    cursor: pointer;
    font-family: TheSans,Arial,sans-serif;
    margin: 0;
    outline: 0;
    padding: 0;
    position: relative;
    white-space: nowrap;
}
.cjhg8mv {
    overflow: auto;
}
.t17ttet6 {
    margin: 10px 0;
    text-align: center;
}
.h1n234tp {
    color: inherit;
    font-weight: 400;
    margin: 0;
}

h3 {
    display: block;
    font-size: 1.17em;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-weight: bold;
}
div {
    display: block;
}
element.style {
    --svzlj66-0: 8px;
    --svzlj66-1: 0 16px 32px -16px rgba(0,0,0, .25);
    --s7hxpvl-0: 540px;
}
.s7hxpvl {
    max-height: calc(100vh - 16px);
    max-width: var(--s7hxpvl-0);
    width: calc(100vw - 16px);
}
.d16v9yx2 {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    overflow: auto;
    padding: 16px;
}

.svzlj66 {
    background-color: #fff;
    border: 1px solid #dfdfdf;
    border-radius: var(--svzlj66-0);
    box-shadow: var(--svzlj66-1);
}

.modalheader{
    display: flex;
    flex-flow: nowrap;
    justify-content: space-between;
    margin-bottom: 4px;
    min-width: 0;

}


.logcontainer{
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

.loginbar{
  width: auto;
  height: 470px;
  background: #fff;
  border-radius: 5px;
  padding: 30px;
  box-shadow: 7px 7px 12px rgba(0,0,0,0.05);
}
</style>
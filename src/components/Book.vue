<template>

</template>


<script setup>
import Datepicker from 'vue3-datepicker'

</script>

<style scoped>

#submit{
    width: 100%;
    height: 50px;
    border-radius: 7px;
    font-weight: 400;
    font-size: 18px;
    border-color: black;
    background-color: aqua;
    margin-top: 10px;
    color:#121117;
    
}
.buttonwrapper{
    display: flex;
    align-items: center;
    justify-content: center;

}
.bodywrapper{
    margin-top: 20px;
}
.to{
    display: flex;
    width: 70%;
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
    font-size: 20px;
    font-weight: bolder;
    margin-left: 15px;
    
}
.pimg{
    height: 66px;
    width: 66px;
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
.messagewrapper{
    text-align: center;
width: 370px;
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
</style>
<template>
  <!DOCTYPE html>
<html lang="en" v-if="renderComponent">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">

	<!-- Boxicons -->
	<link href='https://unpkg.com/boxicons@2.0.9/css/boxicons.min.css' rel='stylesheet'>
	<!-- My CSS -->
	<link rel="stylesheet" href="style.css">

	<title>AdminHub</title>
</head>
<body>


	<!-- SIDEBAR -->
	
	<!-- SIDEBAR -->



	<!-- CONTENT -->
	<section id="content">
		<!-- NAVBAR -->
		<!-- NAVBAR -->

		<!-- MAIN -->
		<main>
			<div class="head-title">
				<div class="left ey diffblu unhhead">
					<h1 >Dashboard</h1>
				
				</div>
				
			</div>

			<ul class="box-info">
				<div class="ey">
					<li>
					<i class='bx bxs-calendar-check' ></i>
					<span class="text blu">
						<h3 class = "blu">{{ students.length }}</h3>
						<p class = "blu">Registered Students</p>
					</span>
				</li>
				</div>
			<div class = "ey">
				<li>
					<i class='bx bxs-group' ></i>
					<span class="text blu">
						<h3>2834</h3>
						<p>Views</p>
					</span>
				</li>

			</div>
			<div class = 'ey'>
				<li>
					<i class='bx bxs-dollar-circle' ></i>
					<span class="text blu">
						<h3>${{ price * students.length }}</h3>
						<p>Account balance</p>
					</span>
				</li>

			</div>
			
			</ul>


			<div class="table-data ey">
				<div class="order">
					<div class="head">
						<h3 class="diffblu">Registered Students</h3>
						<i class='bx bx-search' ></i>
						<i class='bx bx-filter' ></i>
					</div>
					<table>
						<thead>
							<tr>
								<th class="pad">First Name</th>
								<th>Last Name</th>
								<th>Email</th>
								<th>Start</th>
								<th>End</th>
							</tr>
						</thead>
						<tbody>
							<tr v-for="(data, index) in students">
								<td>
									<p>{{ data.fname }}</p>
								</td>
								<td>{{ data.lname }}</td>
								<td>{{ data.email }}</td>
								<td>{{ data.start }}</td>
								<td>{{ data.end }}</td>
							</tr>
							
						</tbody>
					</table>
				</div>
				
			</div>







			<div class="table-data ey">
				<div class="order">
					<div class="head">
						<h3 class="diffblu">Messages</h3>
						<i class='bx bx-search' ></i>
						<i class='bx bx-filter' ></i>
					</div>
					<table>
						<thead>
							<tr>
								<th class="pad">First Name</th>
								<th>Last Name</th>
								<th>Email</th>
								<th>Message</th>
								<th>Date Sent</th>
							</tr>
						</thead>
						<tbody>
							<tr v-for="(data, index) in messages" :key="data.id">
								<td>
									<p>{{ data.fname }}</p>
								</td>
								<td>{{ data.lname }}</td>
								<td>{{ data.email }}</td>
								<td> <button class = 'view'  @click="openModal(index)">View</button> </td>
								<td>{{ data.date }}</td>
							</tr>
							
						</tbody>
					</table>

				</div>
				
			</div>
			<div v-if="isModalVisible" class ="logcontainer">
				<div class = "messagewrapper">
					<div class = "heading">
						<h3>Message</h3>
					</div>

					<div class = "viewtab">
						<p >{{message}}</p>
					</div>
					<div class = "buttonwrap">
						<button class = 'view' @click="closeModal">Close</button>
					</div>
					
				</div>
					</div>

			
		</main>
		<!-- MAIN -->
	</section>
	<!-- CONTENT -->
	

	
</body>
</html>

</template>

<script>
let students  = []
let messages  = []
let price = localStorage.getItem("price")*145
 
export default {
  data() {
    return {
      isModalVisible: false,
	  message: null,
    };
  },
  methods: {
    openModal(index) {
      this.isModalVisible = true;
      console.log("gg")
	  Object.entries(messages).forEach((entry) => {
  const [key, value] = entry;
 
  if(key == index){
   console.log(value.messsage)
    this.message = value.messsage
  }
});
      
    },
    
    closeModal() {
      
      this.isModalVisible = false;
    },
  },
};
</script>


<script setup>

import Datepicker from 'vue3-datepicker'

import Book from './Book.vue'

 import { objectToString } from "@vue/shared";
import { ref, onMounted, nextTick } from "vue";


const renderComponent = ref(true)
const forceRender = async () => {
        renderComponent.value = false;
        await nextTick();
        renderComponent.value = true;
    };
    
onMounted(() => {
 getCsrfToken();
 getStudents();
 getMessages();

//or in f
 
});




function getStudents() {
    fetch('/api/getStudents', {
    method: 'GET',
    headers: {
 'X-CSRFToken': csrf_token.value
 }
 
})
 
.then((response) => response.json())
  .then((data) => {
    students = data.tutors
	forceRender()


  console.log(students)
})
    .catch(function (error) {
        console.log(JSON.stringify(error))
    });
}



function getMessages() {
    fetch('/api/getMessages', {
    method: 'GET',
    headers: {
 'X-CSRFToken': csrf_token.value
 }
 
})
 
.then((response) => response.json())
  .then((data) => {
    messages = data.tutors
	forceRender()


  console.log(messages)
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
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Poppins:wght@400;500;600;700&display=swap');

* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

a {
	text-decoration: none;
}

li {
	list-style: none;
}

.buttonwrap{
	width: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
	margin-top: 20px;
	

}
.viewtab{
	font-family: "Times New Roman", Times, serif;
	letter-spacing: 1px;
	width: 100%;
	color: black;
	font-size: 18px;
	text-align: left;
	height: auto;
	background-color: #f4f4ff;
	border-radius: 4px;
	padding: 10px;
}

.viewtab p{
	background: rgba(0, 114, 135, .1);
	border: 2px solid rgba(0, 114, 135, .1);
	color: #6c6c6c;
	border-radius: 6px 0 6px 0;
}

h3{
    font-size: 24px;
    font-weight:600;
    letter-spacing: 0.016em;
    line-height: 32px;
    padding-bottom: 4px;
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
letter-spacing: 0.025em;
    line-height: 32px;
    padding: 4px;
align-items: center;

}

.ey{
	background-color: white;
	box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
	border-radius: 8px;
}

:root {
	--poppins: 'Poppins', sans-serif;
	--lato: 'Lato', sans-serif;

	--light: #F9F9F9;
	--blue: #3C91E6;
	--light-blue: #CFE8FF;
	--grey: #eee;
	--dark-grey: #AAAAAA;
	--dark: #342E37;
	--red: #DB504A;
	--yellow: #FFCE26;
	--light-yellow: #FFF2C6;
	--orange: #FD7238;
	--light-orange: #FFE0D3;
}


html {
	overflow-x: hidden;
}

body.dark {
	--light: #0C0C1E;
	--grey: #060714;
	--dark: #FBFBFB;
}

body {
	background: var(--grey);
	overflow-x: hidden;
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

.view{
	color: white; 
   background-color: #2898d1;
   cursor: pointer;
   border-radius: 4px;
   width: 70%;
   height: 30px;
}

.buttonwrap button{
width: 25%;
height: 40px;
}

/* SIDEBAR */
#sidebar {
	position: fixed;
	top: 0;
	left: 0;
	width: 280px;
	height: 100%;
	background: var(--light);
	z-index: 2000;
	font-family: var(--lato);
	transition: .3s ease;
	overflow-x: hidden;
	scrollbar-width: none;
}
#sidebar::--webkit-scrollbar {
	display: none;
}
#sidebar.hide {
	width: 60px;
}
#sidebar .brand {
	font-size: 24px;
	font-weight: 700;
	height: 56px;
	display: flex;
	align-items: center;
	color: var(--blue);
	position: sticky;
	top: 0;
	left: 0;
	background: var(--light);
	z-index: 500;
	padding-bottom: 20px;
	box-sizing: content-box;
}
#sidebar .brand .bx {
	min-width: 60px;
	display: flex;
	justify-content: center;
}
#sidebar .side-menu {
	width: 100%;
	margin-top: 48px;
}
#sidebar .side-menu li {
	height: 48px;
	background: transparent;
	margin-left: 6px;
	border-radius: 48px 0 0 48px;
	padding: 4px;
}
#sidebar .side-menu li.active {
	background: var(--grey);
	position: relative;
}
#sidebar .side-menu li.active::before {
	content: '';
	position: absolute;
	width: 40px;
	height: 40px;
	border-radius: 50%;
	top: -40px;
	right: 0;
	box-shadow: 20px 20px 0 var(--grey);
	z-index: -1;
}
#sidebar .side-menu li.active::after {
	content: '';
	position: absolute;
	width: 40px;
	height: 40px;
	border-radius: 50%;
	bottom: -40px;
	right: 0;
	box-shadow: 20px -20px 0 var(--grey);
	z-index: -1;
}
#sidebar .side-menu li a {
	width: 100%;
	height: 100%;
	background: var(--light);
	display: flex;
	align-items: center;
	border-radius: 48px;
	font-size: 16px;
	color: var(--dark);
	white-space: nowrap;
	overflow-x: hidden;
}
#sidebar .side-menu.top li.active a {
	color: var(--blue);
}
#sidebar.hide .side-menu li a {
	width: calc(48px - (4px * 2));
	transition: width .3s ease;
}
#sidebar .side-menu li a.logout {
	color: var(--red);
}
#sidebar .side-menu.top li a:hover {
	color: var(--blue);
}
#sidebar .side-menu li a .bx {
	min-width: calc(60px  - ((4px + 6px) * 2));
	display: flex;
	justify-content: center;
}
/* SIDEBAR */





/* CONTENT */
#content {
	position: relative;
	width: 100%;
    padding-left:150px;
    padding-right: 150px;
	height: 200vh;
	
	transition: .3s ease;
}
#sidebar.hide ~ #content {
	width: calc(100% - 60px);
	left: 60px;
}


.diffblu{
	color: #41a6d8;
	font-weight: bolder;
	letter-spacing: 1px;
}


/* NAVBAR */
#content nav {
	height: 56px;
	background: var(--light);
	padding: 0 24px;
	display: flex;
	align-items: center;
	grid-gap: 24px;
	font-family: var(--lato);
	position: sticky;
	top: 0;
	left: 0;
	z-index: 1000;
}
#content nav::before {
	content: '';
	position: absolute;
	width: 40px;
	height: 40px;
	bottom: -40px;
	left: 0;
	border-radius: 50%;
	box-shadow: -20px -20px 0 var(--light);
}
#content nav a {
	color: var(--dark);
}
#content nav .bx.bx-menu {
	cursor: pointer;
	color: var(--dark);
}
#content nav .nav-link {
	font-size: 16px;
	transition: .3s ease;
}
#content nav .nav-link:hover {
	color: var(--blue);
}
#content nav form {
	max-width: 400px;
	width: 100%;
	margin-right: auto;
}
#content nav form .form-input {
	display: flex;
	align-items: center;
	height: 36px;
}
#content nav form .form-input input {
	flex-grow: 1;
	padding: 0 16px;
	height: 100%;
	border: none;
	background: var(--grey);
	border-radius: 36px 0 0 36px;
	outline: none;
	width: 100%;
	color: var(--dark);
}
#content nav form .form-input button {
	width: 36px;
	height: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	background: var(--blue);
	color: var(--light);
	font-size: 18px;
	border: none;
	outline: none;
	border-radius: 0 36px 36px 0;
	cursor: pointer;
}
#content nav .notification {
	font-size: 20px;
	position: relative;
}
#content nav .notification .num {
	position: absolute;
	top: -6px;
	right: -6px;
	width: 20px;
	height: 20px;
	border-radius: 50%;
	border: 2px solid var(--light);
	background: var(--red);
	color: var(--light);
	font-weight: 700;
	font-size: 12px;
	display: flex;
	justify-content: center;
	align-items: center;
}
#content nav .profile img {
	width: 36px;
	height: 36px;
	object-fit: cover;
	border-radius: 50%;
}
#content nav .switch-mode {
	display: block;
	min-width: 50px;
	height: 25px;
	border-radius: 25px;
	background: var(--grey);
	cursor: pointer;
	position: relative;
}
#content nav .switch-mode::before {
	content: '';
	position: absolute;
	top: 2px;
	left: 2px;
	bottom: 2px;
	width: calc(25px - 4px);
	background: var(--blue);
	border-radius: 50%;
	transition: all .3s ease;
}
#content nav #switch-mode:checked + .switch-mode::before {
	left: calc(100% - (25px - 4px) - 2px);
}
/* NAVBAR */





/* MAIN */
#content main {
	width: 100%;
	padding: 36px 24px;
	font-family: var(--poppins);
	max-height: calc(100vh - 56px);
	
}
#content main .head-title {
	display: flex;
	align-items: center;
	justify-content: space-between;
	grid-gap: 16px;
	flex-wrap: wrap;
}
#content main .head-title .left h1 {
	font-size: 36px;
	font-weight: 600;
	margin-bottom: 10px;
	color: var(--dark);
}


#content main .head-title .left .breadcrumb {
	display: flex;
	align-items: center;
	grid-gap: 16px;
}
#content main .head-title .left .breadcrumb li {
	color: var(--dark);
}
#content main .head-title .left .breadcrumb li a {
	color: var(--dark-grey);
	pointer-events: none;
}
#content main .head-title .left .breadcrumb li a.active {
	color: var(--blue);
	pointer-events: unset;
}
#content main .head-title .btn-download {
	height: 36px;
	padding: 0 16px;
	border-radius: 36px;
	background: var(--blue);
	color: var(--light);
	display: flex;
	justify-content: center;
	align-items: center;
	grid-gap: 10px;
	font-weight: 500;
}




#content main .box-info {
	display: grid;
	grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
	grid-gap: 24px;
	margin-top: 36px;
}
#content main .box-info li {
	padding: 24px;
	background: var(--light);
	border-radius: 20px;
	display: flex;
	align-items: center;
	grid-gap: 24px;
}
#content main .box-info li .bx {
	width: 80px;
	height: 80px;
	border-radius: 10px;
	font-size: 36px;
	display: flex;
	justify-content: center;
	align-items: center;
}
#content main .box-info li:nth-child(1) .bx {
	background: var(--light-blue);
	color: var(--blue);
}
#content main .box-info li:nth-child(2) .bx {
	background: var(--light-yellow);
	color: var(--yellow);
}
#content main .box-info li:nth-child(3) .bx {
	background: var(--light-orange);
	color: var(--orange);
}
#content main .box-info li .text h3 {
	font-size: 24px;
	font-weight: 600;
	color: var(--dark);
}
#content main .box-info li .text p {
	color: var(--dark);	
}





#content main .table-data {
	display: flex;
	flex-wrap: wrap;
	grid-gap: 24px;
	margin-top: 24px;
	width: 100%;
	color: var(--dark);
}
#content main .table-data > div {
	border-radius: 20px;
	background: var(--light);
	padding: 24px;
	overflow-x: auto;
}
#content main .table-data .head {
	display: flex;
	align-items: center;
	grid-gap: 16px;
	margin-bottom: 24px;
}
#content main .table-data .head h3 {
	margin-right: auto;
	font-size: 24px;
	font-weight: 600;
}
#content main .table-data .head .bx {
	cursor: pointer;
}

#content main .table-data .order {
	flex-grow: 1;
	flex-basis: 500px;
}
#content main .table-data .order table {
	width: 100%;
	border-collapse: collapse;
}
#content main .table-data .order table th {
	padding-bottom: 12px;
	font-size: 13px;
	text-align: left;
	border-bottom: 1px solid var(--grey);
	background-color: #41a6d8;
	vertical-align: middle;

	align-items: center;
	height: 55px;
	font-size: 18px;
	color: white;
	padding-top: 11px;
	
}

thead{
	border-radius: 4px;
}


thead tr{
	font-size: 50px;
	vertical-align: middle;
	text-align: center;
	align-items: center;
	border-radius: 4px;
	}

.pad{
	padding-left: 15px;
}
#content main .table-data .order table td {
	padding: 16px 0;
}
#content main .table-data .order table tr td:first-child {
	display: flex;
	align-items: center;
	grid-gap: 12px;
	padding-left: 6px;
}
#content main .table-data .order table td img {
	width: 36px;
	height: 36px;
	border-radius: 50%;
	object-fit: cover;
}
#content main .table-data .order table tbody tr:hover {
	background: var(--grey);
}
#content main .table-data .order table tr td .status {
	font-size: 10px;
	padding: 6px 16px;
	color: var(--light);
	border-radius: 20px;
	font-weight: 700;
}
#content main .table-data .order table tr td .status.completed {
	background: var(--blue);
}
#content main .table-data .order table tr td .status.process {
	background: var(--yellow);
}
#content main .table-data .order table tr td .status.pending {
	background: var(--orange);
}


#content main .table-data .todo {
	flex-grow: 1;
	flex-basis: 300px;
}
#content main .table-data .todo .todo-list {
	width: 100%;
}
#content main .table-data .todo .todo-list li {
	width: 100%;
	margin-bottom: 16px;
	background: var(--grey);
	border-radius: 10px;
	padding: 14px 20px;
	display: flex;
	justify-content: space-between;
	align-items: center;
}
#content main .table-data .todo .todo-list li .bx {
	cursor: pointer;
}
#content main .table-data .todo .todo-list li.completed {
	border-left: 10px solid var(--blue);
}
#content main .table-data .todo .todo-list li.not-completed {
	border-left: 10px solid var(--orange);
}
#content main .table-data .todo .todo-list li:last-child {
	margin-bottom: 0;
}
/* MAIN */
/* CONTENT */







.left{
	width: 100%;
	padding: 20px;


}

.blu{
	font-weight: bolder;
}

@media screen and (max-width: 768px) {
	#sidebar {
		width: 200px;
	}

	#content {
		width: calc(100% - 60px);
		left: 200px;
	}

	#content nav .nav-link {
		display: none;
	}
}



section{

	background-color: #e9ecef;
}

template{
	background-color: #5092cf !important;
}


@media screen and (max-width: 576px) {
	#content nav form .form-input input {
		display: none;
	}

	#content nav form .form-input button {
		width: auto;
		height: auto;
		background: transparent;
		border-radius: none;
		color: var(--dark);
	}

	#content nav form.show .form-input input {
		display: block;
		width: 100%;
	}
	#content nav form.show .form-input button {
		width: 36px;
		height: 100%;
		border-radius: 0 36px 36px 0;
		color: var(--light);
		background: var(--red);
	}

	#content nav form.show ~ .notification,
	#content nav form.show ~ .profile {
		display: none;
	}

	#content main .box-info {
		grid-template-columns: 1fr;
	}

	#content main .table-data .head {
		min-width: 420px;
	}
	#content main .table-data .order table {
		min-width: 420px;
	}
	#content main .table-data .todo .todo-list {
		min-width: 420px;
	}

	
}
</style>
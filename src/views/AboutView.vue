<template>
    <body :key="$route.path">
       
      <div  class ="d-flex flex-column page-container">
        <div class = "container search-page">
          <div class ="row">
            <div class = "col-xs-12">
              <h1 class = "page-title mb18 pb0 hidden-xs">results for "{{ searchResult }}"
                <button class = "pull-right btn btn-sm btn-blue show-filter" @click="showPopup">
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="17px" height="13px" viewBox="0 0 17 13" version="1.1" id="" class="svg ico-with-text mr8 processed replaced-svg"><g id="Search" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-1108.000000, -110.000000)" id="sub-header" fill="#FFFFFF"><g transform="translate(207.000000, 99.000000)"><g id="btn/search-filters" transform="translate(885.000000, 2.000000)"><g id="btn/small-primary"><g id="filters-icon" transform="translate(16.000000, 9.000000)"><rect id="Rectangle" x="0" y="1" width="17" height="1"></rect><circle id="Oval" cx="2.5" cy="1.5" r="1.5"></circle><rect id="Rectangle" x="0" y="6" width="17" height="1"></rect><circle id="Oval" cx="12.5" cy="6.5" r="1.5"></circle><rect id="Rectangle" x="0" y="11" width="17" height="1"></rect><circle id="Oval" cx="7.5" cy="11.5" r="1.5"></circle></g></g></g></g></g></g></svg>
                   
                Show filters
                </button>
            
                
              </h1>
              <div id = "ful" class = "filterwrap">
                    <div class="filter">
                      
                        <div class = "frow">
                            <label class = "filterlabl" for="instrument">Instrument</label>
                            <select v-model="selected2" class="input-subject" name="instrument">
            <option value="" disabled selected >Select an Instrument</option>
            <option value="Piano">Piano</option>
            <option value="Guitar">Guitar</option>
            <option value="Violin">Violin</option>
            <option value="Drum">Drum</option>
          </select>
                        </div>
                        <div class = "frow">
                            <label class = "filterlabl" for="genre">Genre</label>
                            <select  v-model="selected" class="input-subject" name="genre">
            <option value="" disabled selected>Select a Genre</option>
            <option value="Hip Hop">Hip Hop</option>
            <option value="Reggae">Reggae</option>
            <option value="Classical">Classical</option>
            <option value="Dancehall">Dancehall</option>
          </select>
                        </div>
                        <div class = "buttonwrap">
                            <button  v-on:click="clearFilters">Clear filters</button>
                            <button  v-on:click="closePopup">Close</button>
                        </div>
                    </div>
              </div>
            </div>
          </div>
    
          <div @click="closePopup" class="flex-table mb70">
            <div class ="flex-table-title">
                <div class = "downloads"> </div>
              <div class = "title">Title</div>
            <div class = "composer">Composer</div>
            <div class = "form">Genre</div>
            <div class = "instruments">Instruments</div>
    
            </div>
    
            <div class="flex-table-row" v-for="data in filteredItems" :key="searchResults.id">
                <button  @click="download(data.sheet)" class="downloads"><img src="src\assets\download.ico" alt=""></button>
                <div class="title"><a href="/music/35452-aveja-para-labrar/">{{data.title}}</a></div>
                <div class="composer"><a href="/music/composer/miguel-matheo-dallo-y-lana/">{{data.composer}}</a>
              </div>
              <div class="form"><a href="/music/form/christmas-carols/">{{data.genre}}</a></div>
              <div class="instruments"><a href="/music/instrument/choir-and-instrument/">{{data.instrument}}</a></div>
            </div>
    
          
        </div>
    </div>
      </div>
        
    
    </body>
    </template>
    
    <style scoped>
    .buttonwrap{
        display: flex;
        float: right;

        width: 250px;
        justify-content: space-between;
    }

    .buttonwrap button{
        border: 1px solid transparent;
    border-radius: 2px;
    display: inline-block;
    font-size: 13px;
    font-weight: 600;
    line-height: 18px;
    padding: 4px 20px 5px;
    transition: .3s;
    color: #fff;
    background-color: #2898d1;
    }
    .filterwrap{
        position: absolute;
        display: none;
        justify-content: right;
        height: auto;
        right: 0;
        margin-right: 20px;
        margin-top: -25px;
        
       
      
    
    }
  
    .filter{
        border: 1px solid rgba(44,48,51,0.16);
        width:400px;
        padding: 25px;
        font-weight: bold;
        letter-spacing: 0.5px;
        background-color: #f8f8f8;
    }
   
    .frow{
height: 15px;
margin-bottom: 40px;
    }
    .input-subject{
        width: 70%;
        height: 40px;
    }
    .filterlabl{
        font-size: 15px;
        width: 28%;
        height: 40px;
        color: #41474c;

    }
    .svg.replaced-svg, svg.replaced-svg {
        overflow: visible;
    }
    .svg.replaced-svg, svg.replaced-svg {
        overflow: visible;
    }
    svg:not(:root) {
        overflow: hidden;
    }
    svg:not(:root) {
        overflow: hidden;
    }
    .svg, svg {
        vertical-align: middle;
    }
    .mr8 {
        margin-right: 8px;
    }
    .d-flex {
        display: flex!important
    }
    
    .pull-right {
        float: right;
    }
    .btn-blue {
        background-color: #d12860;
        color: #fff;
    }
    .btn {
        border: 1px solid transparent;
        border-radius: 2px;
        display: inline-block;
        font-size: 16px;
        font-weight: 600;
        line-height: 18px;
        padding: 4px 20px 5px;
        transition: .3s;
    }
    .btn {
        
        display: inline-block;
        margin-bottom: 0;
        font-weight: 400;
        text-align: center;
        vertical-align: middle;
        touch-action: manipulation;
        cursor: pointer;
        background-image: none;
        border: 1px solid transparent;
        white-space: nowrap;
        padding: 6px 12px;
        line-height: 1.5;
        border-radius: 4px;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }
    
    .page-container {
        min-height: 100vh!important;
    }
    
    
    
    .flex-column {
        flex-direction: column!important
    }
    
    .align-items-baseline {
        align-items: baseline!important
    }
    
    .justify-content-between {
        justify-content: space-between!important
    }
    
    .h-100 {
        height: 100%
    }
    
    .mb-3 {
        margin-bottom: 1rem!important
    }
    
    .mt-auto {
        margin-top: auto!important
    }
    
    .position-relative {
        position: relative
    }
    
    .w-50 {
        width: 50%!important
    }
    
    .w-100 {
        width: 100%!important
    }
    
    @media(min-width: 576px) {
        .d-sm-flex {
            display:flex!important
        }
    }
    
    .navbar {
        box-shadow: 0 0 6px rgba(65,71,76,.2)
    }
    
    .container {
        margin-right: auto;
        margin-left: auto;
        padding-left: 15px;
        padding-right: 15px;
    }
    
    .container {
        width: 750px;
    }
    @media (min-width: 768px){
    .container, .container-md, .container-sm {
        max-width: 720px;
    }
    }
    @media (min-width: 576px){
    .container, .container-sm {
        max-width: 1150px;
    }
    }
    .container, .container-fluid, .container-lg, .container-md, .container-sm, .container-xl, .container-xxl {
        --bs-gutter-x: 1.5rem;
        --bs-gutter-y: 0;
        width: 100%;
        padding-right: calc(var(--bs-gutter-x) * .5);
        padding-left: calc(var(--bs-gutter-x) * .5);
        margin-right: auto;
        margin-left: auto;
    }
    
    .navbar .container {
        display: flex;
        flex-wrap: wrap;
        min-height: 73px;
        padding-top: 10px;
        position: relative
    }
    
    .navbar .menu {
        display: flex;
        flex-basis: 100%;
        list-style: none;
        margin: 0;
        padding: 0;
        text-transform: uppercase;
        white-space: nowrap
    }
    
    .navbar .menu>li {
        flex: 0 1 25%;
        padding: 10px 0;
        text-align: center
    }
    
    .navbar .menu>li.active a {
        color: #2898d1;
        text-decoration: none
    }
    
    .navbar .menu a {
        color: #41474c
    }
    
    .navbar .menu a:hover {
        color: #2898d1;
        text-decoration: none
    }
    
    .navbar .user-pic {
        padding-left: 10px;
        position: static
    }
    
    .navbar .user-pic .icon {
        height: 32px;
        width: 32px
    }
    
    .navbar .user-pic .avatar {
        border-radius: 50%
    }
    
    .navbar .dropdown-menu {
        border: 0;
        border-radius: 0;
        box-shadow: none;
        left: 0;
        margin: 0;
        padding: 0;
        top: 42px;
        width: 100%
    }
    
    .navbar .dropdown-menu .login a {
        margin-top: 6px
    }
    
    .navbar .dropdown-menu .signup a {
        margin-bottom: 6px
    }
    
    .navbar .dropdown-menu .login a,.navbar .dropdown-menu .signup a {
        padding-bottom: 6px;
        padding-top: 6px
    }
    
    .navbar .dropdown-menu .login p,.navbar .dropdown-menu .signup p {
        margin-bottom: 0
    }
    
    .navbar .dropdown-menu:after,.navbar .dropdown-menu:before {
        display: none
    }
    
    .navbar .dropdown-menu:after {
        border-bottom-color: #fff;
        border-width: 10px
    }
    
    .navbar .dropdown-menu:before {
        border-bottom-color: #e0e0e0;
        margin-right: -1px
    }
    
    .navbar .dropdown-menu li a {
        align-items: center;
        border: 1px solid transparent;
        border-left-width: 4px;
        display: flex;
        padding: 12px 40px 12px 15px
    }
    
    .navbar .dropdown-menu li a:hover {
        background-color: #f6fafc;
        border-bottom-color: #e0e0e0;
        border-left-color: #2898d1;
        border-top-color: #e0e0e0
    }
    
    .navbar .dropdown-menu li a .icon,.navbar .dropdown-menu li a .svg,.navbar .dropdown-menu li a .image {
        height: 29px;
        margin-right: 15px;
        width: 29px
    }
    
    .navbar .dropdown-menu li a .list-group-item-heading {
        font-weight: 600;
        margin-bottom: 8px
    }
    
    .navbar .dropdown-menu li a .list-group-item-text {
        color: #999;
        line-height: 1.3;
        margin-bottom: 0
    }
    
    .navbar .dropdown-menu li:last-child:not(.signup) a {
        border-bottom-right-radius: 4px;
        border-bottom-left-radius: 4px
    }
    
    .navbar .dropdown-menu li:last-child:not(.signup) a p {
        margin: 0
    }
    
    .navbar .dropdown-menu .divider {
        margin: 0
    }
    
    .navbar .search-icon {
        fill: #999;
        height: 28px;
        width: 28px
    }
    
    #logo {
        flex-grow: 1
    }
    
    #search {
        visibility: hidden
    }
    
    #search input {
        background-color: #fff;
        border: 0;
        border-bottom: 1px solid #e0e0e0;
        height: 42px;
        top: 0;
        right: 0;
        padding: 1em;
        position: absolute;
        transition: width .3s;
        width: 0
    }
    
    #search .x-icon {
        height: 12px;
        position: absolute;
        right: 15px;
        stroke: silver;
        top: 15px;
        width: 12px
    }
    
    #search.active {
        visibility: visible
    }
    
    #search.active input {
        font-size: 16px;
        width: 100%
    }
    
    @media(min-width: 768px) {
        #logo {
            flex-grow:0
        }
    
        .navbar {
            padding-top: 0
        }
    
        .navbar .container {
            align-items: center;
            flex-wrap: nowrap;
            padding-top: 0
        }
    
        .navbar .user-pic {
            order: 4;
            position: relative
        }
    
        .navbar .dropdown-menu {
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,.16);
            left: auto;
            right: 0;
            width: auto
        }
    
        .navbar .dropdown-menu:after,.navbar .dropdown-menu:before {
            border: 11px solid transparent;
            bottom: 100%;
            content: "";
            display: block;
            height: 0;
            pointer-events: none;
            position: absolute;
            right: 5px;
            width: 0
        }
    
        .navbar .menu {
            flex-basis: auto;
            font-weight: 600;
            order: 3
        }
    
        .navbar .menu li {
            padding-left: 5px;
            padding-right: 5px
        }
    
        #search {
            flex-grow: 1;
            order: 2;
            padding: 0 10px 0 30px;
            position: relative;
            text-align: right;
            visibility: visible
        }
    
        #search input {
            background-color: #f7f7f7;
            border: 0;
            border-radius: 4px;
            display: inline-block;
            font-weight: 600;
            height: 40px;
            padding: 5px 10px 5px 40px;
            position: relative;
            width: 100%
        }
    
        #search .x-icon {
            display: none
        }
    
        #search:after {
            background-image: url(../img/search-grey.ac65a07a229c.svg);
            background-image: url(data:image/svg+xml;charset=UTF-8;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZpZXdib3g9JzAgMCAxNSAxNSc+PGNpcmNsZSBjeD0nNicgY3k9JzYnIHI9JzUuNScgc3Ryb2tlPScjOTk5JyBmaWxsPSd0cmFuc3BhcmVudCcvPjxsaW5lIHgxPScxMCcgeTE9JzEwJyB4Mj0nMTQuNScgeTI9JzE0LjUnIHN0cm9rZT0nIzk5OScgc3Ryb2tlLWxpbmVjYXA9J3JvdW5kJy8+PC9zdmc+);
            background-repeat: no-repeat;
            content: '';
            left: 42px;
            height: 28px;
            position: absolute;
            top: 13px;
            width: 28px
        }
    }
    
    @media(min-width: 1200px) {
        .navbar .menu li {
            padding-left:12px;
            padding-right: 12px
        }
    
        .navbar #search {
            padding-left: 100px
        }
    
        .navbar #search:after {
            left: 115px
        }
    }
    
    .mb0 {
        margin-bottom: 0
    }
    
    .mb6 {
        margin-bottom: 6px
    }
    
    .mb10 {
        margin-bottom: 10px
    }
    
    .mb13 {
        margin-bottom: 13px
    }
    
    .mb15 {
        margin-bottom: 15px
    }
    
    .mb16 {
        margin-bottom: 16px
    }
    
    .mb18 {
        margin-bottom: 18px
    }
    
    .mb20 {
        margin-bottom: 20px
    }
    
    .mb24 {
        margin-bottom: 24px
    }
    
    .mb28 {
        margin-bottom: 28px
    }
    
    .mb30 {
        margin-bottom: 30px
    }
    
    .mb35 {
        margin-bottom: 35px
    }
    
    .mb38 {
        margin-bottom: 38px
    }
    
    .mb42 {
        margin-bottom: 42px
    }
    
    .mb48 {
        margin-bottom: 48px
    }
    
    .mb50 {
        margin-bottom: 50px
    }
    
    .mb55 {
        margin-bottom: 55px
    }
    
    .mb62 {
        margin-bottom: 62px
    }
    
    .mb70 {
        margin-bottom: 70px
    }
    
    .mb82 {
        margin-bottom: 82px
    }
    
    .mb95 {
        margin-bottom: 95px
    }
    
    .mb98 {
        margin-bottom: 98px
    }
    
    .mr8 {
        margin-right: 8px
    }
    
    .mr15 {
        margin-right: 15px
    }
    
    .mt0 {
        margin-top: 0
    }
    
    .mt10 {
        margin-top: 10px
    }
    
    .mt15 {
        margin-top: 15px
    }
    
    .mt18 {
        margin-top: 18px
    }
    
    .mt24 {
        margin-top: 24px
    }
    
    .mt28 {
        margin-top: 28px
    }
    
    .mt32 {
        margin-top: 32px
    }
    
    .mt40 {
        margin-top: 40px
    }
    
    .mt50 {
        margin-top: 50px
    }
    
    .mt58 {
        margin-top: 58px
    }
    
    .pb0 {
        padding-bottom: 0
    }
    
    .pb8 {
        padding-bottom: 8px
    }
    
    .pb13 {
        padding-bottom: 13px
    }
    
    .pb15 {
        padding-bottom: 15px
    }
    
    .pb19 {
        padding-bottom: 19px
    }
    
    .pb24 {
        padding-bottom: 24px
    }
    
    .pt0 {
        padding-top: 0
    }
    
    .pt18 {
        padding-top: 18px
    }
    
    .text-dark-blue {
        color: #273550
    }
    
    .bg-white {
        background: #fff
    }
    
    .bg-dark-blue {
        background-color: #273550
    }
    
    
    
    .btn:active,.btn:hover {
        border: 1px solid transparent
    }
    
    .btn:focus,.btn.focus,.btn:active.focus,.btn.active.focus,.btn:active:focus,.btn.active:focus {
        border-color: transparent;
        outline: 0
    }
    
    .btn-md {
        padding: 11px 34px 12px
    }
    
    .btn-transparent {
        background-color: transparent;
        border: 1px solid #2898d1;
        color: #2898d1
    }
    
    .btn-transparent:hover,.btn-transparent:focus,.btn-transparent:active {
        background-color: rgba(40,152,209,.12);
        border: 1px solid #2898d1;
        color: #2898d1
    }
    
    .btn-blue {
        background-color: #2898d1;
        color: #fff
    }
    
    .btn-blue:hover,.btn-blue:focus,.btn-blue:active {
        background-color: #0f75a8;
        color: #fff
    }
    
    .btn-white {
        background-color: #fff;
        color: #2898d1
    }
    
    .btn-white:hover,.btn-white:focus,.btn-white:active {
        background-color: rgba(255,255,255,.8);
        color: #2898d1
    }
    
    .btn-gray {
        background-color: #41474c;
        color: #fff
    }
    
    .btn-gray:hover,.btn-gray:focus,.btn-gray:active {
        background-color: #262c31;
        color: #fff
    }
    
    .btn-ok {
        color: #30ab98
    }
    
    .btn-ok:hover {
        color: #50cbb8
    }
    
    .btn-outlined {
        border: 1px solid;
        background-color: transparent
    }
    
    .btn-outlined:hover {
        border: 1px solid;
        opacity: .8
    }
    
    button svg path {
        transition: .3s
    }
    
    button svg .heart-ico path#Path {
        fill: transparent;
        transition: .3s
    }
    
    .btn-change-password span {
        padding-left: 5px;
        background-image: url(../images/sprite.0704336c42e4.svg);
        background-position: -727px center;
        background-repeat: no-repeat;
        width: 12px;
        height: 32px;
        display: block;
        margin-right: 8px;
        float: left
    }
    
    .btn-show-profile {
        text-decoration: none
    }
    
    .btn-show-profile span {
        padding-left: 5px;
        background-image: url(../images/sprite.0704336c42e4.svg);
        background-position: -642px center;
        background-repeat: no-repeat;
        width: 16px;
        height: 10px;
        display: inline-block;
        margin-right: 8px
    }
    
    .btn-cancel {
        background-color: transparent;
        border: 1px solid #e13838;
        color: #e13838
    }
    
    .btn-cancel:hover,.btn-cancel:active,.btn-cancel:focus {
        background-color: transparent;
        border: 1px solid #e13838;
        color: #e13838
    }
    
    .form-control {
        border: 1px solid #c2c2c2;
        border-radius: 2px;
        box-shadow: none;
        color: #41474c;
        font-size: 13px;
        height: 40px;
        padding: 10px 16px
    }
    
    span.select2-container--default .select2-selection--single {
        border: 1px solid rgba(0,0,0,.24);
        border-radius: 0;
        height: 40px
    }
    
    span.select2-container--default .select2-selection--single .select2-selection__rendered {
        line-height: 40px;
        padding: 0 16px
    }
    
    span.select2-container--default .select2-selection--single .select2-selection__arrow {
        display: none
    }
    
    .select2-results {
        padding-left: 16px
    }
    
    span.select2-search--dropdown {
        padding: 4px 16px
    }
    
    .help-block-hidden .help-block {
        display: none
    }
    
    .question-form textarea {
        height: 100px
    }
    
    .question-form .control-label {
        padding-top: 10px;
        text-align: left
    }
    
    .question-form .asteriskField {
        display: none
    }
    
    ul.token-input-list-facebook {
        border-color: #c2c2c2!important
    }
    
    li.token-input-token-facebook {
        border-color: #c2c2c2!important
    }
    
    .close-modal {
        position: absolute;
        top: -16px;
        right: -16px;
        width: 32px;
        height: 32px;
        background-image: url(../images/close.1fb22688d264.png);
        background-position: center center;
        background-repeat: no-repeat;
        z-index: 10
    }
    
    .close-modal svg {
        stroke: #41474c
    }
    
    .modal-content {
        border-radius: 3px
    }
    
    .modal-content h4 {
        color: #383838
    }
    
    .modal-content .modal-footer {
        border-bottom-right-radius: 3px;
        border-bottom-left-radius: 3px
    }
    
    .modal-backdrop.in {
        opacity: .8
    }
    
    .pagination {
        align-items: center;
        display: flex;
        justify-content: space-between;
        margin: 0 auto 100px;
        max-width: 420px
    }
    
    .pagination .pages p {
        margin-bottom: 5px
    }
    
    .pagination .pages p.pagination-description {
        color: #999;
        font-size: 85%;
        line-height: inherit;
        margin-bottom: 0
    }
    
    .footer {
        border-top: 1px solid #e0e0e0;
        line-height: 48px;
        padding: 40px 0;
        white-space: nowrap
    }
    
    
    
    * {
        box-sizing: border-box
    }
    
    input[type=search] {
        box-sizing: border-box
    }
    
    body,button,input,select,textarea {
        color: #41474c;
        font-size: 13px;
        font-family: open sans,helvetica neue,Helvetica,Arial,sans-serif;
        line-height: 1.5
    }
    
    a {
        color: #2898d1;
        text-decoration: none
    }
    
    a:focus,*:focus {
        outline: 0
    }
    
    hr {
        border-color: #e0e0e0
    }
    
    input[type=submit],label,legend {
        text-transform: capitalize
    }
    
    body.modal-open {
        margin-right: 0
    }
    
    .image .avatar {
        background: #e0e0e0;
        color: #e0e0e0;
        display: block;
        overflow: hidden;
        text-decoration: none;
        text-transform: none
    }
    
    .content-body {
        padding: 45px 0
    }
    
    .static-page {
        margin: 40px 0
    }
    
    .static-page h2:first-child {
        margin-top: 0
    }
    
    .static-page p {
        text-align: justify;
        color: #666
    }
    
    .slide-out-div {
        width: 500px;
        background: #fff;
        border: 1px solid #000;
        position: fixed
    }
    
    .slide-out-div a {
        width: 150px;
        height: 30px;
        display: block
    }
    
    .breadcrumb {
        white-space: nowrap;
        background: 0 0;
        max-width: 100%;
        overflow: hidden;
        padding-left: 0;
        padding-right: 0;
        text-overflow: ellipsis
    }
    
    .breadcrumb>li {
        display: inline-block
    }
    
    .breadcrumb>li.active {
        color: #41474c
    }
    
    .breadcrumb>li+li:before {
        display: none
    }
    
    .breadcrumb>li .icon {
        height: 11px;
        opacity: .4;
        width: 18px
    }
    
    .bordered {
        border-bottom: 1px solid #e0e0e0
    }
    
    .bordered .breadcrumb {
        margin-bottom: 6px
    }
    
    .bordered-top {
        border-top: 1px solid #e0e0e0
    }
    
    .font-regular {
        font-weight: 400!important
    }
    
    .invert {
        color: #41474c
    }
    
    .invert:hover,.invert:active,.invert:focus {
        color: #2898d1
    }
    
    .link {
        color: #2898d1
    }
    
    .page-title {
        font-size: 2em;
        line-height: 1.19;
        margin-top: 10px;
        padding: 16px 0 18px
    }
    
    .table thead tr th {
        border-bottom: 1px solid #e0e0e0;
        color: #999;
        font-weight: 400;
        padding: 16px 8px
    }
    
    .table tbody tr td {
        border-top: 1px solid #e0e0e0;
        padding: 16px 8px
    }
    
    .svg,svg {
        vertical-align: middle
    }
    
    .svg.replaced-svg,svg.replaced-svg {
        overflow: visible
    }
    
    .flfr {
        align-items: baseline;
        display: flex;
        justify-content: space-between
    }
    
    .flfr>*:first-child {
        margin-right: auto
    }
    
    .flfr>*:last-child {
        margin-left: auto
    }
    
    .is-flex {
        display: -webkit-box;
        display: -webkit-flex;
        display: -ms-flexbox;
        display: flex;
        -webkit-flex-wrap: wrap;
        -ms-flex-wrap: wrap;
        flex-wrap: wrap
    }
    
    .is-flex:before,.is-flex:after {
        display: none
    }
    
    .is-flex.space-around {
        justify-content: space-around
    }
    
    .is-flex.space-between {
        justify-content: space-between
    }
    
    .is-flex>[class*=col-] {
        display: -webkit-box;
        display: -webkit-flex;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-orient: vertical;
        -webkit-box-direction: normal;
        -webkit-flex-direction: column;
        -ms-flex-direction: column;
        flex-direction: column
    }
    
    .flex-table .title {
        font-weight: 600;
        width: 30%;
    }
    .flex-table .composer {
        width: 20%;
    }
    .flex-table .form {
        width: 15%;
    }
    .flex-table .instruments {
        width: 15%;
    }
    
    .flex-table .downloads {
        width: 5%;
        background-color: transparent;
        border: none;
    }


    .flex-table .flex-table-title {
        border-bottom: 1px solid #e0e0e0;
        color: #999;
        display: flex;
        justify-content: space-between
    }
    
    .flex-table .flex-table-title>* {
        padding: 0 8px 16px
    }
    
    .flex-table .flex-table-row {
        align-items: baseline;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between
    }
    
    .flex-table .flex-table-row:not(:last-child) {
        border-bottom: 1px solid #e0e0e0
    }
    
    .flex-table .flex-table-row>* {
        padding: 15px 8px
    }
    
    .flex-table .flex-table-row a {
        color: inherit
    }
    
    .gray {
        color: #555
    }
    
    .gray_light {
        color: #999
    }
    
    .color-blue {
        color: #2898d1
    }
    
    .list-unstyled li {
        margin-bottom: 5px
    }
    
    .alert {
        border-radius: 2px
    }
    
    .font-semibold {
        font-weight: 600
    }
    
    @keyframes waiting {
        from {
            opacity: 1
        }
    
        to {
            opacity: .2
        }
    }
    
    @media(max-width: 767px) {
        body {
            font-size:15px
        }
    
        p {
            line-height: 24px
        }
    
        .page-title {
            font-size: 1.467em
        }
    
        h2 {
            font-size: 1.2em
        }
    
        h3 {
            font-size: 1.067em
        }
    
        h4 {
            font-size: 1em
        }
    
        .flex-table .flex-table-row:nth-child(2) {
            border-top: 1px solid #e0e0e0
        }
    
        .flex-table .flex-table-row:last-child {
            border-bottom: 1px solid #e0e0e0
        }
    }
    
    @media(max-width: 767px) {
        .modal .modal-dialog {
            margin:10px auto
        }
    }
    
    .modal .modal-dialog .modal-header .close {
        background: 0;
        margin-top: 0;
        opacity: .9;
        right: 25px;
        top: 25px
    }
    
    .modal .modal-dialog .modal-header .close img,.modal .modal-dialog .modal-header .close svg {
        height: 11px;
        width: 11px
    }
    
    .modal .modal-dialog .modal-header .close img path,.modal .modal-dialog .modal-header .close svg path {
        fill: #41474c
    }
    
    .login-modal .modal-dialog {
        max-width: 444px
    }
    
    .login-modal .modal-dialog .modal-header {
        border: 0;
        padding-bottom: 0
    }
    
    .login-modal .modal-dialog .modal-header .close img {
        height: 11px;
        visibility: visible;
        width: 11px
    }
    
    .login-modal .modal-dialog .modal-footer {
        background-color: #f6f8f9;
        text-align: center
    }
    
    .header.bordered {
        margin-bottom: 19px;
        margin-top: 0;
        padding-bottom: 18px
    }
    
    h3.header.bordered {
        margin-bottom: 16px;
        margin-top: 16px
    }
    
    h4.header.bordered,h5.header.bordered,h6.header.bordered {
        margin-bottom: 14px;
        margin-top: 14px
    }
    
    section {
        margin-bottom: 50px
    }
    
    .page-container {
        min-height: 100vh!important
    }
    
    .fold-state,.fold-wrap {
        display: none
    }
    
    .fold-state:checked~.fold-wrap {
        display: initial
    }
    
    .fold-trigger {
        cursor: pointer;
        font-weight: 400
    }
    
    .fold-state:checked~.fold-trigger {
        display: none
    }
    
    .icon {
        height: 16px;
        width: 16px
    }
    
    .stroke-white {
        stroke: #fff
    }
    
    .svg-inject {
        height: 0;
        left: -9999px;
        position: absolute;
        width: 0
    }
    
    .top-banner {
        border: 0;
        margin: 0;
        text-align: center
    }
    
    .rot90 {
        transform: rotate(90deg)
    }
    
    .rot270 {
        transform: rotate(270deg)
    }
    
    .cc {
        font-size: 16px!important;
        color: rgba(40,152,209,.75);
        padding: 0 1px;
        vertical-align: middle
    }
    
    .h280 {
        height: calc(100vw/1.2)
    }
    
    @media(min-width: 480px) {
        .h280 {
            height:280px
        }
    }
    
    .awesomplete [hidden] {
        display: none
    }
    
    .awesomplete .visually-hidden {
        display: none
    }
    
    .awesomplete {
        color: #41474c;
        display: inline-block;
        width: 100%
    }
    
    .awesomplete>input {
        display: block
    }
    
    .awesomplete>ul {
        background: #fff;
        border: 0;
        border-radius: 4px;
        box-shadow: 0 4px 8px rgba(0,0,0,.16);
        font-size: 14px;
        left: 0;
        line-height: 1.5;
        list-style: none;
        margin: 0;
        min-height: 100vh;
        min-width: calc(70%);
        padding: 0;
        position: absolute;
        right: 0;
        text-align: left;
        top: 42px;
        z-index: 1000;
        width: 100%
    }
    
    .awesomplete>ul:empty {
        display: none
    }
    
    .awesomplete>ul>li {
        align-items: center;
        cursor: pointer;
        display: flex;
        min-height: 62px;
        padding: 10px 12px;
        position: relative
    }
    
    .awesomplete>ul>li:not(:first-child) {
        border-top: 1px solid #e0e0e0
    }
    
    .awesomplete>ul>li:hover {
        background: #ebebeb
    }
    
    .awesomplete>ul>li[aria-selected=true] {
        background: #3d6d8f;
        color: #fff
    }
    
    .awesomplete>ul>li>a {
        color: inherit
    }
    
    .awesomplete>ul>li>a:hover {
        text-decoration: none
    }
    
    .awesomplete>ul>li .result_description {
        color: #999;
        font-size: 11px
    }
    
    @media(min-width: 768px) {
        .awesomplete {
            position:relative
        }
    
        .awesomplete>ul {
            border: 1px solid #e0e0e0;
            margin: .4em auto 0;
            min-height: auto;
            min-width: 100%
        }
    
        .awesomplete>ul:before {
            content: "";
            position: absolute;
            top: -.43em;
            left: 1em;
            width: 0;
            height: 0;
            padding: .4em;
            background: #fff;
            border: inherit;
            border-right: 0;
            border-bottom: 0;
            -webkit-transform: rotate(45deg);
            transform: rotate(45deg)
        }
    }
    
    h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6 {
        font-family: source sans pro,Georgia,times new roman,Times,serif;
        font-weight: 700;
        line-height: 1.2;
        color: inherit;
    }
    
    </style>
    
    <script >
    export default {
      data() {
        return {
          searchResult: '',
          searchResults: [],
          selected: '',
          selected2: '',
        };
      },
      methods: {
        clearFilters:  function()
{
    this.selected = ''
    this.selected2 = ''
}
  },
    
      created() {
        this.searchResult = this.$route.query.searchTerm || '';
        console.log(this.searchResult)
        this.searchResults = this.$route.query.results;
        this.searchResults = JSON.parse(this.searchResults)
        console.log(this.searchResults)
     
       
      },
      beforeUpdate() {
        this.searchResult = this.$route.query.searchTerm || '';
        console.log(this.searchResult)
        this.searchResults = this.$route.query.results;
        this.searchResults = JSON.parse(this.searchResults)
        console.log(this.searchResults)
     
       
      },
      computed: {
    filteredItems() {
        console.log(typeof(this.searchResults))
      return this.searchResults
      .filter(item => {
         return item.genre.toLowerCase().includes(this.selected.toLowerCase());
      })
      .filter(item => {
         return item.instrument.toLowerCase().includes(this.selected2.toLowerCase());
      })
    }
  }
    };
    </script>

    <script setup>
 
function showPopup() {
    let popup = document.getElementById("ful")
    if (popup.style.display != "flex")
    {
        popup.style.display = "flex"
    }

   

}



function download(link){
        window.open(link)

    }
function closePopup() {
  console.log("ddads")
  let popup = document.getElementById("ful")
    if (popup.style.display == "flex")
    {
        popup.style.display = "none"
    }
}
</script>
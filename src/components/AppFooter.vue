<template>
      <footer className="bg-gray-800 text-white py-6">
        <div className="max-w-6xl mx-auto px-4">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div>
              <h2 className="font-bold text-lg mb-3">ABOUT</h2>
              <ul>
                <li><a href="/about">About Music Mentors</a></li>
                <li><a href="/privacy">Privacy Policy</a></li>
                <li><a href="/terms">Terms & Conditions</a></li>
              </ul>
            </div>
            <div>
              <h2 className="font-bold text-lg mb-3">FOR TUTORS</h2>
              <ul>
                <li><a href="/tutors/benefits">Benefits</a></li>
                <li><a href="/tutors/apply">Apply Now</a></li>
                <li><a href="/tutors/faq">FAQ</a></li>
              </ul>
            </div>
            <div>
              <h2 className="font-bold text-lg mb-3">FOR STUDENTS</h2>
              <ul>
                <li><a href="/students/find-tutor">Find a Tutor</a></li>
                <li><a href="/students/success-stories">Success Stories</a></li>
                <li><a href="/students/resources">Resources</a></li>
              </ul>
            </div>
            <div>
              <h2 className="font-bold text-lg mb-3">CONTACT</h2>
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

<script setup>
import { ref } from "vue";

const year = (new Date).getFullYear();
</script>

<style>
/* Add any component specific styles here */
</style>
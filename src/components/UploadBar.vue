<!-- Modal.vue -->
<template>
  <div v-if="isModalVisible" class="modal">
    <!-- Modal content -->
    <p>This is the modal content!</p>
    <button @click="closeModal">Close</button>
  </div>
</template>

<script>


export default {
  data() {
    return {
      isModalVisible: false,
    };
  },
  created() {
    console.log("Created")
    // Listen for the 'open-modal' event
    this.emitter.on('open-modal', this.openModal);
    console.log("Created")
  },
  methods: {
    openModal() {
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    },
  },
};
</script>

<style scoped>
/* Add your modal styles here */
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  width: 5555555555px;
}
</style>
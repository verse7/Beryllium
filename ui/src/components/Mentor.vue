<template>
  <div>
    <button class="accordian" v-on:click="toggleAccordian">Button</button>
    <div class="panel">
      <h3 id="name">{{ mentor.fname }} {{ mentor.lname }}</h3>
      <p>ID: {{ mentor.id }}</p>
      <p>Status: Contract {{ mentor.contract }}</p>
      <p>Email: {{ mentor.email }}</p>
      <p>Telephone #: {{ mentor.telnum }}</p>
      <p v-for="(mentee, index) in mentor.mentees" v-bind:key="index">Mentees: {{ mentor.mentees }}</p>
      <p>Maximum Assignment: {{ mentor.met_max }}</p>
    </div>
  </div>
</template>

<script>
export default {
    props: ["mentor"],
    data() {
        return {
            acc: null,
        }
    },
    methods: {
        toggleAccordian: function () {
            console.log(this);
            this.classList.toggle("active");
            let panel = this.nextElementSibling;
            if (panel.style.display === "block") {
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }
        }   
    },
    mounted() {
        // this.acc = document.getElementsByClassName("accordian");
        // console.log(this.acc)        
    }
};
</script>

<style scoped>
.accordian {
  background-color: darkgrey;
  color: forestgreen;
  cursor: pointer;
  padding: 20px;
  width: 100%;
  text-align: left;
  border: none;
  outline: none;
  transition: 0.5s;
}

.active, .accordian:hover {
  background-color: darkslategrey;
}

.panel {
  padding: 0 18px;
  background-color: white;
  display: none;
  overflow: hidden;
}
</style>
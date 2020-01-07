<template>
    <div>
        <Mentor 
            v-for="mentor in mentors"
            v-bind:key="mentor.id"
            v-bind:mentor="mentor"
        ></Mentor>
    </div>
</template>

<script>
import api from '../api'
import Mentor from '../components/Mentor'

export default {
    components: {
        Mentor
    },
    data() {
        return {
            mentors: []
        }
    },
    mounted() {
        api.endpoints.mentors.getAll()
        .then(response => {
            this.mentors = response.data;
        });
    }
}
</script>

<style scoped>

</style>
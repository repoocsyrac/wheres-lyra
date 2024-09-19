<template>
    <div>
        <h2>Recent Sightings</h2>
        <ul class="list-unstyled">
            <li v-for="sighting in sightings" :key="sighting.id">
                {{ sighting.location }} - {{ new Date(sighting.timestamp).toLocaleString() }}
            </li>
        </ul>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                sightings: []
            };
        },

        mounted() {
            this.getSightings();
        },

        methods: {
            async getSightings() {
                const response = await axios.get('http://127.0.0.1:5000/api/sightings');
                this.sightings = response.data;
            }
        }
    };
</script>
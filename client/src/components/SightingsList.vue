<template>
    <div>
        <h2>Recent Sightings</h2>
        <ul class="list-unstyled">
            <li v-for="sighting in sightings.slice(0,10)" :key="sighting.id">
                {{ sighting.location }} - {{ new Date(sighting.timestamp).toLocaleString() }}
            </li>
        </ul>
    </div>
</template>

<script>
    import axios from 'axios';
    import { io } from "socket.io-client";

    export default {
        data() {
            return {
                sightings: []
            };
        },

        mounted() {
            // Connect to websocket 
            const socket = io("http://127.0.0.1:5000");
            
            // Listen for new_sighting events
            socket.on('new_sighting', (sighting) => {
                console.log("New sighting received: ", sighting);
                this.sightings.unshift(sighting); // Adds new sighting to the top of the list
            });

            // Fetch initial list of sightings
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
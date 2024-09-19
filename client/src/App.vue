<template>
  <div id="app">
    <h1>Where's Lyra?</h1>
    <img src="./assets/lyra.jpeg" alt="Lyra the cat" class="img-rounded">
    <ReportSighting />
    <SightingsList :sightings-data="sightings" />
    <SightingsChart :sightings-data="sightings" />
    
  </div>
</template>

<script>
  import axios from 'axios';
  import { io } from "socket.io-client";
  import ReportSighting from './components/ReportSighting.vue';
  import SightingsList from './components/SightingsList.vue';
  import SightingsChart from './components/SightingsChart.vue';

  export default {
    data() {
      return {
        sightings: []
      };
    },
    components: {
      ReportSighting, SightingsList, SightingsChart
    },
    async mounted() {
      // Connect to websocket 
      const socket = io("http://127.0.0.1:5000");
            
      // Listen for new_sighting events
      socket.on('new_sighting', (sighting) => {
          console.log("New sighting received: ", sighting);
          this.sightings.unshift(sighting); // Adds new sighting to the top of the list
      });

      // Fetch sightings from backend
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

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #faf3e4;
  /*color: #2c3e50;
  margin-top: 60px;*/
}

html {
  background-color: #faf3e4;
}
</style>

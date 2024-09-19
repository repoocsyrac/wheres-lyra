<template>
  <div id="app">
    <h1>Where's Lyra?</h1>
    <img src="./assets/lyra.jpeg" alt="Lyra the cat" class="img-rounded">
    <ReportSighting />
    <SightingsList />
    <SightingsChart :sightings-data="sightings" />
    
  </div>
</template>

<script>
  import axios from 'axios';
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
  background-color: #fefaf1;
  /*color: #2c3e50;
  margin-top: 60px;*/
}

html {
  background-color: #fefaf1;
}
</style>

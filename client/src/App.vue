<template>
  <div id="app">
    <h1>Where's Lyra?</h1>
    <img src="./assets/lyra.jpeg" alt="Lyra the cat" class="img-rounded">
    <ReportSighting />
    <SightingsList />
  </div>
</template>

<script>
  import ReportSighting from './components/ReportSighting.vue';
  import SightingsList from './components/SightingsList.vue';

  export default {
    components: {
      ReportSighting, SightingsList
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

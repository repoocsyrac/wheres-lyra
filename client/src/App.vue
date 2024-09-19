<template>
  <div id="app">
    <h1>Where's Lyra?</h1>
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
  color: #2c3e50;
  margin-top: 60px;
}
</style>

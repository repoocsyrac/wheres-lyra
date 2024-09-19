<template>
    <div>
        <h2>Report a Sighting</h2>
        <button @click="reportSighting('Lodge')">Lodge</button>
        <button @click="reportSighting('Main Quad')">Main Quad</button>
        <button @click="reportSighting('Hall')">Hall</button>
        <button @click="reportSighting('Old Library')">Old Library</button>
        <button @click="reportSighting('Fellows Garden')">Fellows Garden</button>
        <button @click="reportSighting('Radcliffe Quad')">Rad Quad</button>
        <button @click="reportSighting('Masters Garden')">Masters Garden</button>
        <button @click="reportSighting('Logic Lane')">Logic Lane</button>
        <button @click="reportSighting('Goodhart Lawn')">Goodhart Lawn</button>
        <button @click="reportSighting('Cecily Court')">Cecily Court</button>
        <button @click="reportSighting('New Library')">New Library</button>
        <button @click="reportSighting('Merton Street')">Merton Street</button>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        methods: {
            async reportSighting(loc) {
                await axios.post('http://127.0.0.1:5000/api/sightings', { location: loc }, {headers: {'Content-Type': 'application/json'}});
                alert('Lyra sighting reported!');
            }
        }
    };
</script>
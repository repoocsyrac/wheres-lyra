<template>
    <div>
        <h2>Report a Sighting</h2>
        <button @click="reportSighting('Lodge')" class="btn btn-default">Lodge</button>
        <button @click="reportSighting('Main Quad')" class="btn btn-default">Main Quad</button>
        <button @click="reportSighting('Hall')" class="btn btn-default">Hall</button>
        <button @click="reportSighting('Old Library')" class="btn btn-default">Old Library</button>
        <button @click="reportSighting('Fellows Garden')" class="btn btn-default">Fellows Garden</button>
        <button @click="reportSighting('Radcliffe Quad')" class="btn btn-default">Rad Quad</button>
        <button @click="reportSighting('Masters Garden')" class="btn btn-default">Masters Garden</button>
        <button @click="reportSighting('Logic Lane')" class="btn btn-default">Logic Lane</button>
        <button @click="reportSighting('Goodhart Lawn')" class="btn btn-default">Goodhart Lawn</button>
        <button @click="reportSighting('Cecily Court')" class="btn btn-default">Cecily Court</button>
        <button @click="reportSighting('New Library')" class="btn btn-default">New Library</button>
        <button @click="reportSighting('Merton Street')" class="btn btn-default">Merton Street</button>
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
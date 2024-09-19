<template>
    <div>
        <h2>Recent Sightings</h2>
        <ul class="list-unstyled">
            <li v-for="sighting in sightingsData.slice(0,10)" :key="sighting.id">
                {{ sighting.location }} - {{ new Date(sighting.timestamp).toLocaleString() }}
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        props: {
            sightingsData: Array
        },

        data() {
            return {
                sightings: []
            };
        }
    };
</script>
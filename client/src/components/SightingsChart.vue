<template>
    <div class="chart-container">
        <BarChart :data="chartData" :options="chartOptions"></BarChart>
    </div>
</template>

<script>
    import { Bar } from 'vue-chartjs';
    import { Chart, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';

    Chart.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

    export default {
        name: 'SightingsChart',
        components: {
            BarChart: Bar
        },
        props: {
            sightingsData: Array
        },
        computed: {
            chartData() {
                const locationCounts = this.sightingsData.reduce((acc, sighting) => {
                    acc[sighting.location] = (acc[sighting.location] || 0) + 1;
                    return acc;
                }, {});

                return {
                    labels: Object.keys(locationCounts),
                    datasets: [
                        {
                            label: 'Sightings',
                            backgroundColor: 'rgba(75,192,192,0.6)',
                            borderColor: 'rgba(75,192,192,1)',
                            borderWidth: 1,
                            data: Object.values(locationCounts)
                        }
                    ]
                };
            },

            chartOptions() {
                return {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                precision: 0 // Show only whole numbers
                            }
                        }
                    }
                };
            }
        }
    };
</script>

<style>
    .chart-container {
        width:40%;
        height:auto;
        margin: auto;
    }
</style>
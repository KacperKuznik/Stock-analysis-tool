<template>
  <div>
    <VueApexCharts :options="chartOptions" :series="series" type="candlestick" height="350" width="800" />
  </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue';
import axios from "axios"
import VueApexCharts from 'vue3-apexcharts';
import { predicted } from './data';
const candlestickData = ref([])
const macd = ref([])
//const predicted = ref([])

onMounted(() => {
  axios.get("http://localhost:8000/stocks/BTCUSDT/")
  .then(res => candlestickData.value = res.data.data)
})

const series = ref([
  {
    name: "candlestick",
    type: "candlestick",
    data: candlestickData
  },
  {
    name: "predictions",
    type: "line",
    color: '#FFFF00',
    data: predicted
  },
  {
    name: "macd",
    type: "line",
    color: '#FF0000',
    data: macd
  },
]);

const chartOptions = ref({
  title: {
    text: 'CandleStick Chart',
    align: 'left',
  },
  xaxis: {
    type: 'datetime',
  },
  yaxis: {
    tooltip: {
      enabled: true,
    },
  },
});
</script>

<template>
    <div class="border max-w-8">
        <div @click="selectedInterval = '1d'">1d</div>
        <div @click="selectedInterval = '1h'">1h</div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
const selectedInterval = ref("1d")
</script>


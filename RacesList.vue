<!-- QUESTÃO 5 - Axios, fetchRaces(), v-for e integração com a API -->

<template>
  <div>
    <h2>Lista de Corridas</h2>

    <div v-for="race in races" :key="race.id">
      <strong>{{ race.nome }}</strong>
      <span> - {{ race.data }} - {{ race.local }}</span>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";

const races = ref([]);

async function fetchRaces() {
  const response = await axios.get("http://127.0.0.1:8000/races");
  races.value = response.data;
}

onMounted(() => {
  fetchRaces();
});
</script>

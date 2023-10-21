<template>
  <router-view />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

console.log(localStorage.getItem('token'))

</script>
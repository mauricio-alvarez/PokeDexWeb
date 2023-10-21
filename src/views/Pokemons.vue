<template>
    <div>
        <h1>Pokemons</h1>
        <ul>
        <li v-for="pokemon in pokemons" :key="pokemon.name">
            <router-link :to="{ name: 'pokemon', params: { name: pokemon.name } }">
            {{ pokemon.name }}
            </router-link>
        </li>
        </ul>
        <router-view />
    </div>
</template>

<script setup>

</script>
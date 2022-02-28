<template>
    <span class="py-1">
        {{ user }} is typing...
    </span>
</template>

<script lang="ts">
export default {
    props: {
        user: String
    }
}
</script>

<style scoped>

</style>
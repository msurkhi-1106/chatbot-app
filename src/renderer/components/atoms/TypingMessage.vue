<template>
    <span class="py-1">
        {{ user.name }} is typing...
    </span>
</template>

<script lang="ts">
import { User } from 'renderer/models/user'
export default {
    props: {
        user: User
    }
}
</script>

<style scoped>

</style>
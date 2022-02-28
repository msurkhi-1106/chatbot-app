<template>
    <chat-container class="chat-container"></chat-container>
</template>

<script lang="ts">
import ChatContainer from "./components/organisms/ChatContainer.vue"

export default {
    components: {
        ChatContainer
    }
}
</script>

<style scoped>
.chat-container {
    width: 100vw;
    height: 100vh;
}
</style>
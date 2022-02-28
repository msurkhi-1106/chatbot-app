<template>
    <div class="chat-container d-flex flex-column">
        <ChatHeader v-if="$chatService.state.recipient" :name="$chatService.state.recipient.name"></ChatHeader>
        <ChatBox class="flex-grow-1 overflow-auto"></ChatBox>
        <ChatBar></ChatBar>
    </div>
</template>

<script lang="ts">
import ChatBar from "~/components/molecules/ChatBar.vue"
import ChatBox from "~/components/molecules/ChatBox.vue"
import ChatHeader from "~/components/molecules/ChatHeader.vue"

export default {
    components: {
        ChatBar,
        ChatBox,
        ChatHeader
    },
}
</script>

<style scoped>
.chat-container {
    background-color: rgb(240,240,240);
    overflow: none;
}
</style>

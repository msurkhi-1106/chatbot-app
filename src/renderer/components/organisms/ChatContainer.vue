<template>
<<<<<<< HEAD
    <div class="d-flex flex-column vh-100 vw-100" style="background-color: rgb(240,240,240)">
        <ChatHeader v-if="$chatService.state.recipient" :name="$chatService.state.recipient.name"></ChatHeader>
        <ChatBox class="flex-grow-1"></ChatBox>
=======
    <div class="chat-container d-flex flex-column">
        <ChatHeader v-if="$chatService.state.recipient" :name="$chatService.state.recipient.name"></ChatHeader>
        <ChatBox class="flex-grow-1 overflow-auto"></ChatBox>
>>>>>>> e0b123c4b486e3f43930b944097308cfa072bd5d
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

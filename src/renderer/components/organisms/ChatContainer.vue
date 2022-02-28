<template>
    <div class="d-flex flex-column vh-100 vw-100">
        <chat-box class="flex-grow-1"></chat-box>
        <chat-bar></chat-bar>
    </div>
</template>

<script lang="ts">
import ChatBar from "~/components/molecules/ChatBar.vue"
import ChatBox from "~/components/molecules/ChatBox.vue"

export default {
    components: {
        ChatBar,
        ChatBox
    }
}
</script>

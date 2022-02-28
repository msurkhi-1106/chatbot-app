<template>
    <div class="d-flex flex-column vh-100 vw-100" style="background-color: rgb(240,240,240)">
        <ChatHeader name="Doctor Phil (MD)"></ChatHeader>
        <ChatBox class="flex-grow-1"></ChatBox>
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
    }
}
</script>

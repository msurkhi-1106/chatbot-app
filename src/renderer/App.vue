<template>
    <div>
        hello
        <chat-bar></chat-bar>
    </div>
</template>

<script lang="ts">
import ChatBar from "./components/ChatBar.vue"

export default {
    created() {
        console.log("hey")
    },
    components: {
        ChatBar
    }
}
</script>
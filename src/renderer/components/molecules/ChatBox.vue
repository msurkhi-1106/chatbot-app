<template>
    <div class="p-2">
        <chat-message v-for="(message, index) in $chatService.messages" :message="message" :key="index"></chat-message>
    </div>
</template>

<script lang="ts">
import ChatMessage from "~/components/atoms/ChatMessage.vue"
import { mapGetters } from 'vuex'

export default {
    mounted() {
        
    },
    data() {
        return {}
    },
    computed: {
        ...mapGetters({
            messages: 'getMessages'
        })
    },
    components: {
        ChatMessage
    }
}
</script>
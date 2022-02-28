<template>
    <div class="p-2">
        <ChatMessage v-for="(message, index) in $chatService.messages" :message="message" :key="index"></ChatMessage>
        <TypingMessage v-if="$chatService.state.recipient.typing" :user="$chatService.state.recipient"></TypingMessage>
    </div>
</template>

<script lang="ts">
import ChatMessage from "~/components/atoms/ChatMessage.vue"
import TypingMessage from "~/components/atoms/TypingMessage.vue"

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
        ChatMessage,
        TypingMessage
    }
}
</script>
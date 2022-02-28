<template>
    <div>
        <div class="p-2">
            <ChatMessage v-for="(message, index) in messages" :message="message" :key="index"></ChatMessage>
            <TypingMessage v-if="$chatService.state.recipient.typing" :user="$chatService.state.recipient"></TypingMessage>
        </div>
        <div ref="bottom"></div>
    </div>
</template>

<script lang="ts">
import ChatMessage from "~/components/atoms/ChatMessage.vue"
import TypingMessage from "~/components/atoms/TypingMessage.vue"

export default {
    mounted() {
        
    },
    data() {
        return {}
    },
    computed: {
        messages() {
            return this.$chatService.messages
        }
    },
    methods: {
        scrollToBottom() {
            const el: HTMLElement = this.$refs['bottom'] as any
            el.scrollIntoView()
        }
    },
    components: {
        ChatMessage,
        TypingMessage
    },
    watch: {
        messages: {
            handler() {
                this.$nextTick(() => (this as any).scrollToBottom())
            },
            deep: true
        }
    }
}
</script>
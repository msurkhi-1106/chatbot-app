<template>
    <div class="p-2">
        <chat-message v-for="(message, index) in messages" :message="message" :key="index"></chat-message>
    </div>
</template>

<script lang="ts">
import ChatMessage from "~/components/atoms/ChatMessage.vue"
import { mapGetters } from 'vuex'

export default {
    mounted() {
        console.log(this.messages)
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
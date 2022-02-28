<template>
    <div class="d-flex flex-row">
        <input type="text" class="flex-grow-1" v-model="messageBody" @keypress.enter="sendMessage" />
        <button class="btn btn-primary" @click="sendMessage" :disabled="sendDisabled">Send</button>
    </div>
</template>

<script lang="ts">
export default {
    data() {
        return {
            messageBody: "",
        }
    },
    methods: {
        sendMessage() {
            if(!this.messageBody) return;
            this.$chatService.sendMessage(this.messageBody)
            this.messageBody = ""
        }
    },
    computed: {
        sendDisabled(): boolean {
            return this.messageBody == ""
        }
    }
}
</script>

<style scoped>

</style>
<template>
    <div class="py-1">
        <span class="pe-2 message-time">
            [{{ messageTime }}]
        </span>
        <span class="message-sender">
            {{ message.name }}: 
        </span>
        <span>
            {{ message.message }}
        </span>
    </div>
</template>

<script>
import Message from "~/models/message"

export default {
    props: {
        message: Message
    },
    computed: {
        messageTime() {
            const hours24 = this.message.date.getHours()
            const hours12 = hours24 % 12
            const minutes = this.message.date.getMinutes()
            const seconds = this.message.date.getSeconds()
            const am = hours24 / 12 < 1

            const minutes_str = String(minutes).padStart(2, '0')
            const seconds_str = String(seconds).padStart(2, '0')

            return `${hours12}:${minutes_str}:${seconds_str} ${am?'AM':'PM'}` 
        }
    }
}
</script>

<style scoped>

</style>

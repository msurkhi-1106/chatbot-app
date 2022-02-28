<template>
    <div class="d-flex flex-row bg-white bottom-rounded">
        <img :src="doctorImage" class="avatar m-2" />
        <div class="p-2 d-flex flex-column align-items-stretch justify-content-center">
            <span>{{ name }}</span>
            <span><small>Active Now</small><span class="ps-2" :style="statusClass">●</span></span>
        </div>
    </div>
</template>

<script lang="ts">
import doctorImage from "assets/doctor.jpg"
export default {
    mounted() {
        
    },
    data() {
        return {
            doctorImage,
            loggedIn: true
        }
    },
    computed: {
        statusClass() {
            return {
                color: 'green'
            }
        }
    },
    props: {
        name: String
    }
}
</script>

<style scoped>
.avatar {
    object-fit: cover;
    width: 75px;
    height: 75px;
    border-radius: 50%;
}

.bottom-rounded {
    border-radius: 0 0 15px 15px;
}
</style>
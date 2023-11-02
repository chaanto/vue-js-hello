<template>
    <div class="container">
        <button type="button" class="btn btn-primary">{{ msg }}</button>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'members', 
        data() {
            return {
                msg: "",
            };
        },
        methods : {
            getMessage() {
                const path = 'http://127.0.0.1:5000/members';
                axios.get(path).then((res) => {
                    this.msg = res.data;
                }).catch((error) => {
                    console.log(error);
                });
            },
        },
        created() {
            this.getMessage();
        }
    };
</script>
<template>
    <div class="login-box center-align">
        <h4>Confirm Signup</h4>
        <div class="card-panel red darken-2" v-if="error != null"><span class="white-text">{{ error.message }}</span></div>
        <p>Enter the verification code you should have recieved via email</p>
         
        <v-form ref="confirmForm" lazy-validation>
            <v-text-field v-model="email" label="e-mail" required></v-text-field>
            <v-text-field v-model="confirmcode" label="confirmation code" required></v-text-field>
            <v-btn class="error mt4" @click="confirm()" > Verify Now </v-btn>

        </v-form>
    </div>
</template>

<script>
export default {
    name: 'Confirm',
    data () {
        return {
            email: '',
            confirmcode: '',
            error: null
        }
    },
    methods: {
        confirm () {
            /*eslint no-unused-vars: "off"*/
            this.$cognitoAuth.confirmRegistration(this.email, this.confirmcode, (err, result) => {
                if (err) {
                    this.error = err
                } else {
                    this.$router.push('/profile')
                }
            });
        }
    }
}
//confirmcode
</script>

<style scoped>
h4 {
    text-align: center;
    margin: 0;
    padding: 0;
    font-weight: 800;
    font-size: 18px;
}
p {
    text-align: center;
    font-size: 14px;
    padding-bottom: 10px;
}
.login-box {
    width: 400px;
    height: auto;
    background-color: white;
    border-radius: 5px;
    padding: 40px;
    margin: auto;
    margin-top: 60px;
    border: 1px solid #E4E6E7;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.4);
}
button {
    margin: auto;
    background-color: #FA3254;
    margin: 0;
    padding: 0px 40px;
}
button i {
    font-size: 18px;
}
</style>
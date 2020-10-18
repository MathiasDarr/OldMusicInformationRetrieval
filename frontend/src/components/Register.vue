<template>
    <div class="login-box">
        <h4>Register</h4>
        <hr/>
        <div class="alert alert-warning" v-if="error != null"><span class="white-text">{{ error.message }}</span></div>
        <p>Don't have an account? Register for one now</p>
         <v-form ref="registerForm" v-model="valid" lazy-validation>
            <v-text-field v-model="firstname" label="First Name" required></v-text-field>
            <v-text-field v-model="lastname"  label="Last Name" required></v-text-field>
            <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>
            <v-text-field v-model="password" :rules="[rules.required, rules.min]" label="Password" required></v-text-field>
            <v-text-field v-model="verify" :rules="[rules.required, passwordMatch]" label="Verify Password" required></v-text-field>
            <v-btn class="error mt4" @click="authenticate()" > Register </v-btn>
            <p>Already have an account? - <router-link to="Login">Login Now</router-link></p> 
         </v-form>
        
    </div>
</template>

<script>
export default {
  name: 'Register',
  computed:{
    passwordMatch() {
      return () => this.password === this.verify || "Password must match";
    }
  },
  data() {
      return {
            firstname: '',
            lastname: '',
            email: '',
            password: '',
            verify:'',
            error: null,
            valid: true,
            emailRules: [
              v => !!v || "Required",
              v => /.+@.+\..+/.test(v) || "E-mail must be valid"
            ],
            loginEmailRules: [
              v => !!v || "Required",
              v => /.+@.+\..+/.test(v) || "E-mail must be valid"
            ],
            rules: {
              required: value => !!value || "Required.",
              min: v => (v && v.length >= 8) || "Min 8 characters"
        }
      }
  },
  methods: {
    authenticate () {
        /*eslint no-unused-vars: "off"*/
        this.$cognitoAuth.signup(this.email,this.firstname, this.lastname, this.password, (err, result) => {
            if (err) {
                this.error = err
            } else {
                this.$router.push({path: '/confirm'})
            }
        })
    }
  }
}
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
    margin-top: 60px;
    border-radius: 5px;
    padding: 40px;
    margin: auto;
    margin-top: 60px;
    border: 1px solid #E4E6E7;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.4);
}
</style>
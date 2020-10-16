<template>
  <v-container>
      
    <v-layout>
        <div>

            <v-tabs v-model="tab" show-arrows background-color="deep-purple accent-4" icons-and-text dark grow>
                    <v-tabs-slider color="purple darken-4"></v-tabs-slider>
                    <v-tab v-for="i in tabs" :key="i.id">
                        <v-icon large>{{ i.icon }}</v-icon>
                        <div class="caption py-1">{{ i.name }}</div>
                    </v-tab>
                    <v-tab-item>
                        <v-card class="px-4">
                            <v-card-text>
                                <v-form ref="loginForm" v-model="valid" lazy-validation>
                                    <v-row>
                                        <v-col cols="12">
                                            <v-text-field v-model="loginEmail" :rules="loginEmailRules" label="E-mail" required></v-text-field>
                                        </v-col>
                                        <v-col cols="12">
                                            <v-text-field v-model="loginPassword" :append-icon="show1?'eye':'eye-off'" :rules="[rules.required, rules.min]" :type="show1 ? 'text' : 'password'" name="input-10-1" label="Password" hint="At least 8 characters" counter @click:append="show1 = !show1"></v-text-field>
                                        </v-col>
                                        <v-col class="d-flex" cols="12" sm="6" xsm="12">
                                        </v-col>
                                        <v-spacer></v-spacer>
                                        <v-col class="d-flex" cols="12" sm="3" xsm="12" align-end>
                                            <v-btn x-large block :disabled="!valid" color="success" @click="login"> Login </v-btn>
                                        </v-col>
                                    </v-row>
                                </v-form>
                            </v-card-text>
                        </v-card>
                    </v-tab-item>
                    <v-tab-item>
                        <v-card class="px-4">
                            <v-card-text>
                                <v-form ref="registerForm" v-model="valid" lazy-validation>
                                    <v-row>
                                        <v-col cols="12" sm="6" md="6">
                                            <v-text-field v-model="firstName" :rules="[rules.required]" label="First Name" maxlength="20" required></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="6">
                                            <v-text-field v-model="lastName" :rules="[rules.required]" label="Last Name" maxlength="20" required></v-text-field>
                                        </v-col>
                                        <v-col cols="12">
                                            <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>
                                        </v-col>
                                        <v-col cols="12">
                                            <v-text-field v-model="password" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" :rules="[rules.required, rules.min]" :type="show1 ? 'text' : 'password'" name="input-10-1" label="Password" hint="At least 8 characters" counter @click:append="show1 = !show1"></v-text-field>
                                        </v-col>
                                        <v-col cols="12">
                                            <v-text-field block v-model="verify" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" :rules="[rules.required, passwordMatch]" :type="show1 ? 'text' : 'password'" name="input-10-1" label="Confirm Password" counter @click:append="show1 = !show1"></v-text-field>
                                        </v-col>
                                        <v-spacer></v-spacer>
                                        <v-col class="d-flex ml-auto" cols="12" sm="3" xsm="12">
                                            <v-btn x-large block :disabled="!valid" color="success" @click="register">Register</v-btn>
                                        </v-col>
                                    </v-row>
                                </v-form>
                            </v-card-text>
                        </v-card>
                    </v-tab-item>
                </v-tabs>
            </div>

    </v-layout>
  </v-container>
</template>

<script>
import * as  AmazonCognitoIdentity from "amazon-cognito-identity-js";
import { mapGetters, mapActions } from "vuex";
import router from '../../router'
// import axios from 'axios';

export default {
    mounted() {

    },
    methods: {
         ...mapActions(["setJWT"]),
         ...mapActions(["setEmail"]),
        login(){
            // console.log("jesus " + process.env.VUE_APP_COGNITO_APP_DOMAIN)
            let registerObj = this
            var poolData = {
                UserPoolId : process.env.VUE_APP_COGNITO_USERPOOL_ID,
                ClientId : process.env.VUE_APP_COGNITO_CLIENT_ID
            };
            var userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);

            var userData = {
                Username : this.loginEmail, // your username here
                Pool : userPool
            };
            var authenticationData = {
                Username : this.loginEmail, 
                Password : this.loginPassword, 
            };
            var authenticationDetails = new AmazonCognitoIdentity.AuthenticationDetails(authenticationData);

            var cognitoUser = new AmazonCognitoIdentity.CognitoUser(userData);
            cognitoUser.authenticateUser(authenticationDetails, {

                onSuccess: function (result) {
                    // console.log('access token + ' + result.getAccessToken().getJwtToken());
                    // console.log("ID TOKEN SDFDF " + result.getIdToken().getJwtToken())
                    // console.log("ID ACCESS SDFDF " + result.getAccessToken().getJwtToken())
                    registerObj.setJWT({access:result.getAccessToken().getJwtToken(),id: result.getIdToken().getJwtToken()})
                    registerObj.setEmail(registerObj.loginEmail)
                    router.go(-1)
                // router.push('/')
                },
            
                onFailure: function(err) {
                    alert(err);
                },
            
            });

     },
     register(){
     
            var poolData = {
            UserPoolId : this.cognitoUserPoolId,
            ClientId : this.cognitoUserPoolClientId
            };
            var userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);
            // console.log(userPool)
            var attributeList = [];

            var email = this.email 
            var pw =  this.password 
            var verifyPw = this.verify 
            var dataEmail = {
                Name : 'email',
                Value : email
            };

            var attributeEmail = new AmazonCognitoIdentity.CognitoUserAttribute(dataEmail);
            attributeList.push(attributeEmail);
            if (pw === verifyPw) {
            userPool.signUp(email, pw, attributeList, null, function(err, result){
                if (err) {
                    alert(err.message);
                    return;
                }
                var cognitoUser = result.user;
                console.log(cognitoUser);
                localStorage.setItem('email', email);
                window.location.replace('confirm.html');
            });
            } else {
            alert('Passwords do not match.')
            }
  
    },

    validate() {
      if (this.$refs.loginForm.validate()) {
        console.log("The user ID is " + this.loginEmail)
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    }
  },
  computed: {
    ...mapGetters(["getJwtAccessToken"]),
    passwordMatch() {
      return () => this.password === this.verify || "Password must match";
    }
  },
  data: () => ({
    envvar: process.env.DRUGS,
    cognitoUserPoolId:'us-west-2_rrVhZsufQ',
    cognitoUserPoolClientId:'633b35gtorn2odi25dotujndob',

    tab: 0,
    tabs: [
        {id:1, name:"Login", icon:"mdi-account"},
        {id:2,name:"Register", icon:"mdi-account-outline"}
    ],
    valid: true,
    
    token:String,
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    verify: "",
    loginPassword: "",
    loginEmail: "",
    loginEmailRules: [
      v => !!v || "Required",
      v => /.+@.+\..+/.test(v) || "E-mail must be valid"
    ],
    emailRules: [
      v => !!v || "Required",
      v => /.+@.+\..+/.test(v) || "E-mail must be valid"
    ],

    show1: false,
    rules: {
      required: value => !!value || "Required.",
      min: v => (v && v.length >= 8) || "Min 8 characters"
    }
  })
}
</script>
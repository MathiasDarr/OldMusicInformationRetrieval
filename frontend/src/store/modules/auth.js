/* eslint-disable */

// import axios from 'axios';
import * as  AmazonCognitoIdentity from "amazon-cognito-identity-js";
import axios from 'axios';


const state = {
    loggedIn: false,
    cognitoInfo:{},
    loadingState:true,
    errorLoadingState:false,
    access_token: false,
    idToken: false,
    email: false

};

const getters = {
    getJwtAccessToken: state => state.access_token,
    getLoggedIn: state => state.loggedIn,
    getIdToken: state => state.idToken,
    getEmail: state => state.email

};

const actions = {

    async setJWT({commit}, tokens){
        console.log("Token " + tokens.access)
        console.log("id token " + tokens.id)
        commit('setAccessToken', tokens)
    },


    async setEmail({commit}, email){
        console.log("The incoming emai lis " + email)
        commit('setEmail', email)
    },

    async authentication({commit}, email, password){
        
        var poolData = {
            UserPoolId : 'us-west-2_rrVhZsufQ',
            ClientId : '633b35gtorn2odi25dotujndob'
            };
        var userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);

        var userData = {
            Username : email, 
            Pool : userPool
        };

        var authenticationData = {
            Username : email, 
            Password : password, 
        };
        var authenticationDetails = new AmazonCognitoIdentity.AuthenticationDetails(authenticationData);

        var cognitoUser = new AmazonCognitoIdentity.CognitoUser(userData);
        cognitoUser.authenticateUser(authenticationDetails, {
            onSuccess: function (result) {
                console.log("ID TOKEN " +result.getIdToken().getJwtToken())
                commit('setAccessToken', {access:result.getAccessToken().getJwtToken(),id: result.getIdToken().getJwtToken()})
            },

            onFailure: function(err) {
                alert(err);
            },

        });
      },


    async registration({commit}){

    
        const api_url = window.__runtime_configuration.load_balancer_dns+'guitarset'
        axios.get(api_url).then((response) => {
    
            var response_string = JSON.stringify(response.data)
            var data = JSON.parse(response_string)
            console.log(data)
            commit('setGuitarSetData', data)
    
          }, (error) => {
            console.log(error);
          });
      },
};



const mutations = {
    setLoggedIn: (state, newValue) => { state.loggedIn = newValue;},
    setEmail:(state, email) => (state.email= email),
    setLoggedOut:(state) => {
        state.loggedIn=False; state.cognitoInfo = {}},
    setCognitoInfo:(state, newValue) => (state.cognitoInfo= newValue),
    setAccessToken:(state, tokens) => {//token, idToken) => {

        state.loggedIn = true;
        state.access_token = tokens.acces;
        state.idToken = tokens.id
    }
};

export default {
  state,
  getters,
  actions,
  mutations
};

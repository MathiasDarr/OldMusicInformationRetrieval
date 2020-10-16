<template>
    <v-container>

      <v-layout>
        <v-flex md2>
        <BaseNavBar v-bind:items=items />
        </v-flex>
        <v-flex md10>

          <v-layout row>
            <v-flex md8>
              <v-card  tile flat>
                <v-card-text>
                  <v-card-title>
                    Music Information Retrieval
                  </v-card-title>
                  <v-divider></v-divider>
                  <Paragraph v-bind:title = "''" v-bind:text = introduction />
                  <Paragraph v-bind:title = motivation_title v-bind:text = motivation />
                  <Paragraph v-bind:title = methods_title v-bind:text = methods />
                  <Paragraph v-bind:title = results_title v-bind:text = results />
                  <Paragraph v-bind:title = "'Future Work'" v-bind:text = future />


                </v-card-text>
              </v-card>
            </v-flex>
            
            <v-flex md4>
              <v-card  tile flat >
                <ImageComponent :image_src="audio_image" v-bind:caption="' Raw Audio'" v-bind:height="'100px'" v-bind:width="'500px'" />
                <ImageComponent :image_src="transform_image" v-bind:caption="'Spectogram generated with Librosa'" v-bind:height="'400px'" v-bind:width="'500px'" />
                <ImageComponent :image_src="cnn_image" v-bind:caption="'Convolutional Neural Network Architecture'" v-bind:height="'300px'" v-bind:width="'500px'" />

              </v-card>
            </v-flex>
          </v-layout>

          <v-layout row>
            <v-flex md3>
              <v-card  tile flat>
                <v-card-text>
                  <Paragraph v-bind:title = architecture_title v-bind:text = architecture />
                </v-card-text>
              </v-card>
            </v-flex>
            
            <v-flex md9>
              <v-card  tile flat >
                <ImageComponent :image_src="architecture_image" v-bind:caption="'Serverless Application Architecture'" v-bind:height="'700px'" v-bind:width="'1000px'" />
              </v-card>
            </v-flex>
          </v-layout>

          <v-layout row>
            <TechnologiesList v-bind:technologies=technologies />
            </v-layout>
          <v-layout row>
            <GithubFooter v-bind:link = link v-bind:link_title = link_title />
          </v-layout>

        </v-flex>
  
      </v-layout> 
    </v-container>
    
</template>

<script>


import BaseNavBar from  '../BaseNavBar'
import GithubFooter from '../shared/GithubFooter'
import Paragraph from '../shared/Paragraph'
import TechnologiesList from '../shared/TechnologiesList'
import ImageComponent from '../shared/ImageComponenet'


export default {
  components:{
    BaseNavBar,
    GithubFooter,
    Paragraph,
    TechnologiesList,
    ImageComponent
  },
  
  data () {
    return {
      link: 'https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-mir',
      link_title: 'Music Information Retrieval',
      introduct_title: 'Project Description',
      introduction:`In this project I attempt to perform automatic music transcription, the process of taking raw audio of a musician playing '\
                'and instrumentand outputting guitar tab or piano sheet music depending on the instrument.  This problem falls under the subfield' \
                of data science known as MIR (Music Information Retrieval). `,
      motivation_title:'Motivation',
      motivation: `As an musician I am frequently faced with wanting to know how a particular piece of music is played.  This often occurs
                  when I watch people perform covers of songs I want to learn on Youtube.  Woulden't it be great if I could get a transcription
                  of what they are playing?`,
      methods_title: 'Methods',
      methods: `I attempt to reproduce the neural
                network archticture described by Manuel Minguez Carretero in his thesis. He proposes several neural network architectures for 
                solving this problem, which he trained on the MusicNet database, an MIR dataset of piano recordings and sheet music.  In this 
                project I instead train models using the GuitarSet & the Maestro datasets for performing guitar and piano transcription.  `,
      architecture_title: 'Serverless Application Architecture',
      architecture: `I used the AWS Serverless Application Model SAM to deploy several lambda functions as well as an API Gateway API defined with Swagger.   
      An authenticated user uploads an audio file from the front end Vue application to a serverless Lambda function, which starts an EC2 instance which 
      processess the audio using librosa to be input to the Keras model.  Additional processing involving Librosa is done to produce a transcription from
      the array of probabilities that the output of the model.   
      `,
      future: `Improve the model.  Clean up the tab rendering code.`,
      
      results: `The model shows signs of overfitting (training loss decreases while validation loss increases/fluctuates)`,
      results_title: 'Results',

      architecture_image: 'https://dakobedbard.s3-us-west-2.amazonaws.com/mir_arhcitecture.png',

      items: [
        { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/musiclanding' },
        { title: 'GuitarSet', icon: 'mdi-image', route:'/guitarset' },
        // { title: 'Transcriber', icon: 'mdi-help-box', route:'/transcriber' },
        // { title: 'Transcriptions', route:'/transcriptions' }
      ],
      technologies: [
        "Keras deep learning library on AWS EC2 GPU instance",
        "Librosa audio processing library",
        "AWS Serverless Application modle deploys Lambda functions API Gateway",
        "AWS SQS as a messaging queue",
        "Swagger to define the API & enable CORS",
        "AWS CloudFront to serve audio files from S3.",
        "AWS EC2 instance with keras & librosa isntalled.",
        "AWS cognito for user aser authentication",
        "VexFlow javascript library for rendering music notation"
      ],
      transform_image: 'https://dakobed-style.s3-us-west-2.amazonaws.com/screenshot.png',
      audio_image: 'https://dakobed-style.s3-us-west-2.amazonaws.com/audio.png',
      cnn_image: 'https://dakobed-style.s3-us-west-2.amazonaws.com/cnn.png'
      

    }
  },
}
</script>
# Dakobed Vue Frontend
Front end web application developed using Vue, Vuex  & Vuetify

Run locally
npm install 
npm run serve



Host the SPA in an S3 bucket.  

npm run build
serve ./dist

aws s3 sync ./dist s3://dakobed-bard.com



https://s3-us-west-2.amazonaws.com/dalinar-mir.com/profile.jpg


#### ECR 


aws cloudformation create-stack --template-body file://templates/instance-and-route53.yml --stack-name route53 \
--parameters ParameterKey=KeyName,ParameterValue=tutorial ParameterKey=InstanceType,ParameterValue=t2.micro \
 ParameterKey=HostedZoneName,ParameterValue=example.local. ParameterKey=Subdomain,ParameterValue=testsubdomain


aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 710339184759.dkr.ecr.us-west-2.amazonaws.com

docker build -t dakobed-vue-repository .
docker run -it -p 8080:8080 --rm --name dockerize-vuejs-app-1 dakobed/dakobed-vuejs-app

docker tag dakobed-vue-repository:latest 710339184759.dkr.ecr.us-west-2.amazonaws.com/dakobed-vue-repository:latest

docker push 710339184759.dkr.ecr.us-west-2.amazonaws.com/dakobed-vue-repository:latest



### Build for staging, running npm run serve like normal doesn't seem to bundle the environment variables the way that I needed ..

./node_modules/.bin/vue-cli-service build --mode staging


### Serve the distribution

serve ./dist
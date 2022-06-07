# CI / CD Pipline
 
We are applying a CI/CD pipline to a node project using github actions.


<img src="https://miro.medium.com/max/1400/0*TH1nBsXNDB5Njynk.PNG" height="300">

### Plan:
The Plan phase often combines practices from Scrum and Agile to enable frequent microincremental releases.

### Code:
The Code phase focuses on core development tasks from within IDEs and appropriate sandboxing and frameworks.

### Build:
The Build phase rapidly and incrementally merges code commits with some testing and security validation.

### Test:
The Test phase focuses on automated verification of enhancements, often incorporating test-driven deployment practices. Testing is sometimes incorporated as part of the Build phase, and generally extends in some way to all phases of the CI/CD process to ensure continuous feedback and improvement.

### Release:
The Release phase is centered around repository commits and adequate documentation of the changes.

### Deploy:
The Deploy phase is the actual update to the codebase, with special thought given to issue and error avoidance.

### Operate:
The Operate phase occurs once the code is made live, and consists of monitoring and orchestration.

### Monitor:
The Monitor phase takes place parallel to the Operate phase and consists of data collection, analysis, and feedback to the start of the pipeline and to other phases as needed. In the most sophisticated environments, optimization is automated as continuous optimization (CO), an extension of CI/CD that leverages machine learning to eliminate risks and waste associated with manual infrastructure selection.

## Work done:
We have planned to create a posts manager server with these features:
- Check all posts
- Add a like to a post
- Remove a like from a post

Then we started coding these features with express.js and we have implemented some test cases in the code using the testing package  ____Jest____. 
 
### Github actions workflow
So to create the pipeline we have used github actions. So we have to define the jobs with the theirs steps in workflow file. 

### When ?
We have chosen to trigger our github action pipline when we push the code to the github repository. 

```yml
name: DevOps pipline
on: [push]
```

### Job 1 : Test
The role of this job is to perform ___Jest___ tests on our code on a ubuntu environement. With this job we make sure that our server is working as expected.

```yml
jobs:
   Test:
     runs-on: ubuntu-latest
     steps:
       - name: Check out repository code
         uses: actions/checkout@v3
       - uses: actions/setup-node@v3
         with:
           node-version: '14'
       - run: npm install
       - run: npm test
```

### Job 2 : Build
This job triggers after the Test job is completed successfuly. In this job we are going to build our project into a docker image based on a Dockerfile and then the image is released in the dockerhub repo [postsmanager](https://hub.docker.com/repository/docker/marouenmahou/postsmanager) after logging to my dockerhub account
via login secretes ( ___DOCKER_HUB_USERNAME____ and  ___DOCKER_HUB_ACCESS_TOKEN___). We have used the github sha of the commits to know which commits are related to whichs releases.

```yml
   Build:
     needs: Test
     runs-on: ubuntu-latest
     steps: 
       - name: Checkout
         uses: actions/checkout@v2
       - name: Login to Docker Hub
         uses: docker/login-action@v1
         with:
           username: ${{ secrets.DOCKER_HUB_USERNAME }}
           password: ${{ secrets.DOCKER_HUB_ACCESS_TOKEN }}
       - name: Build and push
         uses: docker/build-push-action@v2
         with: 
           context: .
           file: ./Dockerfile
           push: true
           tags: ${{ secrets.DOCKER_HUB_USERNAME }}/postsmanager:${{ github.sha }}
```

### Job 3: Deploy
This job depends on the build job. It triggers when the build job finishs with success. In this job we are going to deploy our server as service into an ECS cluster of AWS. 
First, we have created an ECS cluster in AWS called marouenmahou: 

![Cluster image](images/cluster.PNG?raw=true)

Then created a service called posts-manager-app-devops with a replication factor of 2 tasks and with the task definition called marouen-task-def-postsmanagerapp-pipeline:
```json
{
    "family": "marouen-task-def-postsmanagerapp-pipeline",
    "containerDefinitions": [
        {
            "name": "marouen-devops-app",
            "image": "marouenmahou/postsmanager",
            "portMappings": [
                {
                    "containerPort": 3000,
                    "hostPort": 3000,
                    "protocol": "tcp"
                }
            ]
        }
    ],
    "requiresCompatibilities": [
        "FARGATE"
    ],
    "networkMode": "awsvpc",
    "memory": "1024",
    "cpu": "512"
}
```

![Service image](images/cluster.PNG?raw=true)

The service is associated with a load balancer exposing the port 3000 because we are using a nodejs server. 

![Service image](images/service.PNG?raw=true)

Then in our job we configure the AWS credentials first with login secrets added to github then we fille the new image and then we deploy the task definition.

```yml
env:
  AWS_REGION: us-east-1
  ECS_SERVICE: posts-manager-app-devops            
  ECS_CLUSTER: marouenmahou                 
  ECS_TASK_DEFINITION: .aws/task-definition.json
  CONTAINER_NAME: marouen-devops-app

...

   Deploy:
       name: Deploy
       runs-on: ubuntu-latest
       needs: 
         - Build
       steps:
         - name: Checkout
           uses: actions/checkout@v3

         - name: Configure AWS credentials
           uses: aws-actions/configure-aws-credentials@13d241b293754004c80624b5567555c4a39ffbe3
           with:
             aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
             aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
             aws-region: ${{ env.AWS_REGION }}
         - name: Fill in the new image ID in the Amazon ECS task definition
           id: task-def
           uses: aws-actions/amazon-ecs-render-task-definition@97587c9d45a4930bf0e3da8dd2feb2a463cf4a3a
           with:
             task-definition: ${{ env.ECS_TASK_DEFINITION }}
             container-name: ${{ env.CONTAINER_NAME }}
             image: ${{ secrets.DOCKER_HUB_USERNAME }}/postsmanager:${{ github.sha }}

         - name: Deploy Amazon ECS task definition
           uses: aws-actions/amazon-ecs-deploy-task-definition@de0132cf8cdedb79975c6d42b77eb7ea193cf28e
           with:
             task-definition: ${{ steps.task-def.outputs.task-definition }}
             service: ${{ env.ECS_SERVICE }}
             cluster: ${{ env.ECS_CLUSTER }}
             wait-for-service-stability: true
```


At the end we have two tasks of our server are running:

![Service image](images/service2.PNG?raw=true)


## Final pipline
Here is our final pipline execution.
![Service image](images/finalePipline.png?raw=true)



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

Then created a service called posts-manager-app-devops 



## Plan
The Plan phase often combines practices from Scrum and Agile to enable frequent microincremental releases.

So the first step is to plan what to code. In our case it a posts management server where we are going to implement these features :
- Check all posts
- Add a like to a post
- Remove a like from a post

## Code
The Code phase focuses on core development tasks from within IDEs and appropriate sandboxing and frameworks.

We have coded our application with node.js (Express server).

## Build



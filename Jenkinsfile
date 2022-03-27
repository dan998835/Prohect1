pipeline {
  agent {
      dockerfile true
      label 'zip-job-docker'
  }
  tools{
    maven "3.8.5"
  }
  stages{
     stage('Server'){
        steps{
          rtServer {
            id: "my-artifactory-server"
            url: 'http://localhost:8082/artifactory'
            username: 'super-user'
            password: 'Qw12856!'
            bypassProxy: true
            timeout: 300
          }
     }
     stage('Build){
        steps{
          execute the zip job
        }
     }
     stage('Publish){
        stages{
          upload zip files to artifactory
        }
     }
     stage('Report'){
        stages{
          send email with job status to some email
        }
     }
     stage('Cleanup'){
        stages{
          delete the workspace
        } 
     }
  }
}

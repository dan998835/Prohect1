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
            id: "my-artifactory-server" ,
            url: 'http://localhost:8082/artifactory' ,
            username: 'super-user' ,
            password: 'Qw12856!' ,
            bypassProxy: true ,
            timeout: 300 ,
          }
     }
     stage('Build){
        steps{
          sh 'zip_job.py'
        }
     }
     stage('Publish){
        steps { 
          rtUpload {
             buildName:  JOB_NAME,
             buildNumber:   BUILD_NUMBER,
             serverId:  SERVER_ID,
               spec:  '''{
                  "files":{
                      "pattern": "$WORKSPACE/*.zip"
                      "target": "repository/"
                      "recursive": "false"
                  }
               
               }'''
          }
          
        }
     }
     stage('Report'){
        steps{
            post{
                always{
                  emailext attachLog: true, body: 'This is the job status', subject:"Jenkins Build ${currentBuild.currentResult} , to: 'dan998835@gmail.com'
                }
            }
        }
     }
     stage('Cleanup'){
        steps{
            sh 'rm -rf $WORKSPACE/*'
        } 
     }
  }
}

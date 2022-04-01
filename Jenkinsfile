  pipeline {
    agent {
      dockerfile {
        filename 'DockerFile'
        args '--privileged'
        args '-u root:sudo -v /var/lib/jenkins/workspace/artifactory-declerative-pipeline@tmp:/tmp'
      }
    }
    tools{
      maven "maven"
    }
    stages{
         stage('Server'){
              steps{
                  rtServer (
                    id: 'My_Artifactory' ,
                    url: 'http://localhost:8082/artifactory' ,
                    username: 'super-user' ,
                    password: 'Qw12856!' ,
                    bypassProxy: true ,
                    timeout: 300 ,
                  )
              }
         }
         stage('Build'){
              steps{
                  script{
                      try {
                          sh '''
                          /tmp/zip_job.py
                          '''
                        }
                        catch (Exception e) {
                          currentBuild.result = 'FAILURE'
                          stageResultMap.didBuildSucceeded = false
                        }
                    }
                }
           }
       ```stage('Publish'){
             when {
                 expression {
                   return stageResultMap.find( it.key == "didBuildSucceeded" )?.value
                 }
             }
             steps {
                  rtUpload (
                       serverId: 'My_Artifactory' , 
                       spec: '''{
                              "files": [
                                        {
                                          "pattern": "$WORKSPACE/*.zip",
                                          "target": "repository/"
                                        }
                              ]
                       }'''
                  )
              }
       }
       stage('Report'){
            steps {
                echo 'Send Mail'
                emailext body: 'This is job status', subject: "Jenkins Build ${currentBuild.currentResult}", to: 'dan998835@gmail.com'
            }
        }
       stage('Cleanup'){
            steps{
                sh 'rm -rf $WORKSPACE/*'
            } 
       }
    }
    post { 
           always { 
                     mail to: 'dan998835@gmail.com',
                     body: "This is the job status", 
                     subject:"Jenkins Build ${currentBuild.currentResult}" ,
                     from: 'Jenkins Update'
           }
     }
}

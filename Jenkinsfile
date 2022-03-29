  pipeline {
    agent {
      dockerfile {
        filename 'DockerFile'   
      }
    }
    tools{
      maven "maven"
    }
    stages{
         stage('Server'){
              steps{
                  rtServer (
                    id: "my-artifactory-server" ,
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
                      python3 '''
                      cd /tmp
                      'zip_job.py'
                      '''
                    }
                    catch (Exception e) {
                      currentBuild.result = 'FAILURE'
                      stageResultMap.didBuildSucceeded = false
                    }
                }
            }
       }
       stage('Publish'){
             when {
                 expression {
                   return stageResultMap.find( it.key == "didBuildSucceeded" )?.value
                 }
             }
             steps {
                  rtUpload (
                       serverId: 'my-artifactory-server', 
                       spec:  '''{
                              "files": [
                                        {
                                          "pattern": "$WORKSPACE/*.zip"
                                          "target": "repository/"
                                          "recursive": "false"
                                        }
                              ]
                       }'''
                  )
              }
       }
       stage('Report'){
            steps{
                post{
                    always{
                      emailext body: 'This is the job status', subject:'Jenkins Build ${currentBuild.currentResult}' , to: 'dan998835@gmail.com'
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

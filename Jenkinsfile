  pipeline {
    agent {
      dockerfile {
        filename 'DockerFile'
        args '--privileged'
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
                      python3 ./zip_job.py
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
             steps {
                  rtUpload (
                       serverId: 'My_Artifactory' , 
                       spec: '''{
                              "files": [
                                        {
                                          "pattern": "./*.zip",
                                          "target": "repository/${VERSION env variable}/"
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
}

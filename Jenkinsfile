pipeline{
    agent any
    stages{
        stage ('Image creation from GitHub repo'){
            steps{
                build job: 'Sample_Flask_Manual_Build_Docker_Image'
            }
        }
        stage ('Testing the Image'){
            steps{
                build job: 'Test_curl', parameters:[
                    string (name:'Check_Docker_Image',value:'Test_Full')
                    ], wait: true
            }
        }
        stage ('Push to Nexus'){
            steps{
                build job : 'Sample_Flask_Upload_Nexus', wait: true
            }
        }
    }
}

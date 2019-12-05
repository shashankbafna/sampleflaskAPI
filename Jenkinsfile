node{
	stage('Push Docker Images to Nexus Registry'){
		sh 'docker login -u deploy -p deploy http://ilutdto353.corp.amdocs.com:8081/'
		sh 'docker push ilutdto353.corp.amdocs.com/sbafna/flasksampleapi'
		sh 'docker logout ilutdto353.corp.amdocs.com'
	}
}

node{
	stage('Push Docker Images to Nexus Registry'){
		sh 'docker login -u user -p password ilutdto353.corp.amdocs.com'
		sh 'docker push ilutdto353.corp.amdocs.com/sbafna/flasksampleapi'
		sh 'docker logout ilutdto353.corp.amdocs.com'
	}
}

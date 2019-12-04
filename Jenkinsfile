stage('Push Docker Images to Nexus Registry'){
sh 'docker login -u user -p password NexusDockerRegistryUrl'
sh 'docker push NexusDockerRegistryUrl/Imagename}'
sh 'docker rmi $(docker images --filter=reference="NexusDockerRegistryUrl/ImageName*" -q)'
sh 'docker logout NexusDockerRegistryUrl'
}
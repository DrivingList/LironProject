pipeline {

    agent {label "ec2"}

    stages{
	    stage ('Workspace Cleanup') {
		steps {    
	    cleanWs()
          }	
	}
	    stage('Git Checkout') {
            steps {
		    git branch: 'master', url: 'https://github.com/DrivingList/LironProject.git'
            }
        }
        stage('build') {
            steps{
                sh "docker build -t liron7833project:$BUILD_NUMBER ."
                }
            }

        stage('push') {
            steps {
                sh "aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 054789182582.dkr.ecr.eu-central-1.amazonaws.com"
                sh "docker tag liron7833project:$BUILD_NUMBER 054789182582.dkr.ecr.eu-central-1.amazonaws.com/liron7833project:$BUILD_NUMBER"
                sh "docker push 054789182582.dkr.ecr.eu-central-1.amazonaws.com/liron7833project:$BUILD_NUMBER"
            }
        }

    }
}

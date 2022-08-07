pipeline {

    agent {label "ec2"}

    stages{
        stage("Build") {
            steps{
                sh "docker build -t liron7833project:$BUILD_NUMBER ."
                }
            }

        stage("Push") {

            steps {
                sh "aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 054789182582.dkr.ecr.eu-central-1.amazonaws.com"
                sh "docker tag liron7833project:$BUILD_NUMBER 054789182582.dkr.ecr.eu-central-1.amazonaws.com/liron7833project:$BUILD_NUMBER"
                sh "docker push 054789182582.dkr.ecr.eu-central-1.amazonaws.com/liron7833project:$BUILD_NUMBER"
            }
        }

    }
}

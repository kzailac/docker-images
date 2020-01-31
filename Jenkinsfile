pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Build...'
                sh './build.sh $env.BRANCH_NAME'
            }
        }
    }
}

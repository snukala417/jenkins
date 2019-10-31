pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python maths.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python Testmath.py'
            }
        }
    }
}

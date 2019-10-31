pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                python maths.py
            }
        }
        stage('Test') {
            steps {
                python Testmath.py
            }
        }
    }
}

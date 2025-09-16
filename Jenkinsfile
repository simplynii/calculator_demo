pipeline {
    agent any
 
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/simplynii/calculator_demo.git'
            }
        }
 
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
            }
        }
 
        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && python3 -m unittest discover -s tests -p "*_test.py"'
            }
        }
 
        stage('Deploy') {
            steps {
                echo 'Deploying Calculator App...'
                sh 'mkdir -p /var/lib/jenkins/deploy && cp calculator.py /var/lib/jenkins/deploy/'  // or wherever you want to deploy
            }
        }
    }
}
 

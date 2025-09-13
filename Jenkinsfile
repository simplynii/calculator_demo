pipeline {

    agent any
 
    stages {

        stage('Clone Repository') {

            steps {

                git branch: 'main', url: 'https://github.com/simplynii/calculator_demo.git'

            }

        }
 
        stage('Setup Python Environment') {

            steps {

                sh '''

                    sudo apt-get update

                    sudo apt-get install -y python3-venv python3-pip

                '''

            }

        }
 
        stage('Install Dependencies') {

            steps {

                sh '''

                    python3 -m venv venv

                    . venv/bin/activate

                    pip install --upgrade pip

                    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

                '''

            }

        }
 
        stage('Run Tests') {

            steps {

                sh '''

                    . venv/bin/activate

                    python3 -m unittest discover -s tests

                '''

            }

        }
 
        stage('Deploy') {

            steps {

                echo 'Deploying Calculator App...'

                sh 'cp calculator.py /var/www/html/'  // adjust path as needed

            }

        }

    }

}

 

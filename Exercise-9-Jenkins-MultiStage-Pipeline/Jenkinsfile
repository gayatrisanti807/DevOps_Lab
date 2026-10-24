pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Python Flask Application'
                sh 'python3 --version'
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Unit Tests'
                sh 'venv/bin/python -m unittest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Python Application'
            }
        }

        stage('Run Application') {
            steps {
                echo 'Starting Flask Application'
                sh 'nohup venv/bin/python app.py > app.log 2>&1 &'
            }
        }

        stage('Test Application') {
            steps {
                echo 'Testing Flask Application'
                sh 'sleep 3'
                sh 'python3 -c "import urllib.request; print(urllib.request.urlopen(\'http://127.0.0.1:5000/\').read().decode())"'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
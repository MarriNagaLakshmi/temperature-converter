pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'temp-converter'
        DOCKER_TAG = "v${BUILD_NUMBER}"
    }

    stages {
        stage('Source Code & Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com'
            }
        }

        stage('Continuous Integration (Tests)') {
            steps {
                bat '''
                if not exist venv (
                    "C:\\Program Files\\Python310\\python.exe" -m venv venv
                )
                call .\\venv\\Scripts\\activate.bat
                pip install -r requirements.txt
                pytest test_app.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
            }
        }

        stage('Deployment to Kubernetes') {
            steps {
                bat '''
                kubectl apply -f k8s/deployment.yml
                kubectl apply -f k8s/service.yml
                kubectl rollout status deployment/temp-converter
                '''
            }
        }
    }
}
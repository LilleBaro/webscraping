pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "lillebaro/webscraper:v1"
    }

    stages {
        stage('Cloner le dépôt') {
            steps {
                git 'https://github.com/LilleBaro/webscraping.git'
            }
        }

        stage('Construire l’image Docker') {
            steps {
                script {
                    sh "docker build -t -f MyScrapper\Dockerfile ."
                }
            }
        }

        stage('Se connecter à Docker Hub') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'docker-hub-password', variable: 'DOCKER_PASSWORD')]) {
                        sh "echo $DOCKER_PASSWORD | docker login -u lillebaro --password-stdin"
                    }
                }
            }
        }

        stage('Pousser l’image sur Docker Hub') {
            steps {
                script {
                    sh "docker push $DOCKER_IMAGE"
                }
            }
        }

        stage('Déployer le conteneur') {
            steps {
                script {
                    sh "docker stop webscraping_app || true"
                    sh "docker rm webscraping_app || true"
                    sh "docker pull $DOCKER_IMAGE"
                    sh "docker run -d -p 8501:8501 --name webscraping_app $DOCKER_IMAGE"
                }
            }
        }
    }

    post {
        success {
            echo '✅ Déploiement réussi !'
        }
        failure {
            echo '❌ Erreur dans le pipeline.'
        }
    }
}

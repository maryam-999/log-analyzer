pipeline {
    agent any

    stages {
        stage('Start') {
            steps {
                echo 'Début de l\'analyse des logs'
            }
        }

        stage('Exécution du script') {
            steps {
                bat 'python log_analyzer.py'
            }
        }

        stage('End') {
            steps {
                echo 'Fin du pipeline'
            }
        }
    }
}

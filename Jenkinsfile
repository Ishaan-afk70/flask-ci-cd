pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install selenium pytest'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'pytest tests/ui_tests.py'
            }
        }
    }
}

pipeline {
    agent any

    environment {
        // Define URL for the Flask app if it's not set dynamically in your pipeline
        FLASK_APP_URL = "http://localhost:5000"
    }

    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                // Checkout the Git repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install necessary dependencies for Flask, Selenium, and other tools
                bat 'pip install selenium pytest webdriver-manager flask'
            }
        }

        stage('Start Flask Application') {
            steps {
                // Run the Flask app in the background
                bat 'start /b python app.py'

                // Wait for the app to be fully up and running before proceeding with tests
                bat 'ping -n 6 127.0.0.1 1>nul'  // Wait for a few seconds to ensure the app is available
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Run Selenium-based tests using pytest
                bat 'python -m pytest test.py -v'
            }
        }

        stage('Shutdown Application') {
            steps {
                // Add any necessary shutdown steps here (if Flask needs to be killed manually)
                echo 'Flask application is shutting down after tests'
                // Optional: If the Flask app is running in the background and needs to be stopped:
                // bat 'taskkill /F /IM python.exe'
            }
        }

        stage('Declarative: Post Actions') {
            steps {
                echo 'Cleaning up...'
                echo 'Tests failed. Please check the logs.'
            }
        }
    }

    post {
        always {
            // Clean up and close any processes if needed
            echo 'Pipeline finished. Cleaning up.'
        }

        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Please check the logs for more details.'
        }
    }
}

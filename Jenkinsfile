pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                // Install required Python packages
                bat 'pip install selenium pytest webdriver-manager flask'
            }
        }

        stage('Start Flask Application') {
            steps {
                // Start Flask application in the background
                bat 'start /b python app.py'
                // Wait for the application to start using ping instead of timeout
                bat 'ping -n 6 127.0.0.1 > nul'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Run the tests using pytest with the test.py file in the root directory
                bat 'python -m pytest test.py -v'
            }
        }

        stage('Shutdown Application') {
            steps {
                // Find and kill the Flask process running on port 5000
                bat '''
                for /f "tokens=5" %%a in ('netstat -ano ^| find ":5000" ^| find "LISTENING"') do (
                    taskkill /F /PID %%a
                )
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }

        success {
            echo 'Tests passed successfully!'
        }

        failure {
            echo 'Tests failed. Please check the logs.'
        }
    }
}
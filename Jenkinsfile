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
                // Allow time for the application to start
                bat 'timeout /t 5'
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
                // Shut down the Flask application (find and kill the process)
                bat 'for /f "tokens=5" %%a in (\'netstat -aon ^| find ":5000" ^| find "LISTENING"\') do taskkill /F /PID %%a'
                // Note: In batch files within Jenkinsfile, use %%a instead of %a
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
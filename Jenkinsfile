pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.13.0-slim'
    }

    stages {

        stage('Run Tests in Docker') {
            steps {
                script {
                    // Run the tests inside the Docker container
                    sh """
                        docker run --rm \
                        -v ${WORKSPACE}:/workspace \
                        -w /workspace \
                        ${DOCKER_IMAGE} \
                        /bin/bash -c 'pip install -r requirements.txt && pytest --alluredir=allure-results playwright_module/tests/'
                    """
                }
            }
        }
    }

    post {
        always {
            script {
                // Publish the Allure report regardless of success or failure
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}

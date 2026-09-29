pipeline {
    agent any
    environment {
        POLARIS__TOKEN = credentials('POLARIS_TOKEN')
    }
 
    stages {
 
        stage('Create coverity.yaml') {
            steps {
                writeFile file: 'coverity.yaml', text: '''capture:
analyze:
  cov-analyze-args:
    - '--aggressiveness-level'
    - 'high'
    - '--all'
    - '--rule'
    - '--security'
    - '--webapp-security'
    - '--webapp-security-aggressiveness-level'
    - 'high'
    - '--distrust-all'
    - '--enable-audit-mode'
'''
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://gitlab.com/bridgenext1/proftpd'
            }
        }
 
        stage('Build') {
            steps {
                echo 'Building GitLab project...'
            }
        }
 
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
 
        stage('Security Scan') {
            steps {
                echo 'Running Black Duck Polaris security scan...'
            }
        }
        stage('Polaris Black Duck Security Scan') {
            steps {
                security_scan(
                    product: 'polaris',
                    polaris_server_url: POLARIS_URL,
                    polaris_access_token: POLARIS__TOKEN,
                    polaris_application_name: 'Cop Testing application',
                    polaris_project_name: 'ProFTPd',
                    polaris_branch_name: 'master',
                    polaris_assessment_types: 'SAST,SCA'
                )
            }
        }
    }
 
    post {
        success {
            echo 'Pipeline completed successfully'
        }
 
        failure {
            echo 'Pipeline failed'
        }
    }
}
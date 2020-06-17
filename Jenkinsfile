pipeline {
    agent any

    stages {
        stage('Pull latest code') {
            steps {
                sh 'git pull origin testing'
            }
        }
        stage('Checkout to SCM') {
            steps {
                sh 'git checkout testing'
                sh 'git pull'
            }
        }
        stage('Testing') {
            steps {
                sh 'robot --outputdir RegressionTestingSuites/logs RegressionTestingSuites/TestSuites/AllTagsTestCases.robot'
            }
        }
        stage('Deploy to Production') {
            steps {
                sh 'git checkout master'
                sh 'git merge testing'
                sleep 5
            }
        }
    }
}

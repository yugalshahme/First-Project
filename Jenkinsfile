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
            }
        }
        stage('Testing Started') {
            steps {
                sh 'robot --outputdir RegressionTestingSuites/logs RegressionTestingSuites/TestSuites/AllTagsTestCases.robot'
            }
        }
        stage('Deploy to Production') {
            steps {
                sh 'git checkout master'
                sh 'git merge testing'
            }
        }
    }
}

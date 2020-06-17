pipeline {
    agent any

    stages {
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
                sh 'git merge master'
            }
        }
    }
}

node {
    stage "Create build output"

    // Make the output directory.
    sh "mkdir -p output"

    // Write an useful file, which is needed to be archived.
    writeFile file: "output/usefulfile.txt", text: "This file is useful, need to archive it."

    stage "build docker image "

    //sh "sudo docker build  -t cloud-overview .
    checkout([
        $class: 'GitSCM', branches: [[name: '*/master']],
  userRemoteConfigs: [[url: 'git@github.com:pearsontechnology/cloud-overview.git',credentialsId:'jenkinsmaster']]
])
    sh "ls -al  "
    sh "pwd "
    sh "chmod 700 dockercommand.sh "
    sh "sudo ./dockercommand.sh  "

    // Archive the build output artifacts.
    archiveArtifacts artifacts: 'output/*.txt', excludes: 'output/*.md'
}


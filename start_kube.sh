#!/bin/bash




ignor(){


export project_name='cloudoverview'

apt-get -y install openssh-server


chmod 700 /etc/apt/sources.list

wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
wget -q -O - https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo sh -c 'echo deb http://apt.kubernetes.io/ kubernetes-xenial main > /etc/apt/sources.list.d/kubernetes.list'

chmod 644 /etc/apt/sources.list
 apt-get -y update
 apt-get install -y kubelet kubeadm kubectl kubernetes-cni

 apt-get -y install jenkins

cat /etc/default/jenkins |  sed -e "s/HTTP_PORT=8080/HTTP_PORT=666/" > /tmp/jenkins
 cp -f /tmp/jenkins /etc/default/jenkins
 /etc/init.d/jenkins restart

 apt-get -y install git
mkdir -p $project_name/cloudoverview
mkdir -p $project_name/cloudworm
cd $project_name
apt-get -y install unzip

rm master.zip*

#wget . https://github.com/oui/pingponggo/archive/master.zip

 `pwd`

unzip -o master.zip

#cp pingponggo-master/requirements.txt ping/.
#cp pingponggo-master/ping.py ping/.
#cp pingponggo-master/restserver.go  revel/.
#cd ping
 apt install -y docker.io

echo " killing all running docker containers .... "
 docker kill $(sudo docker ps -q)

}
 # ignor()
rm -rf cloudoverview
git clone https://github.com/configm/cloudoverview.git

cd cloudoverview
alias kk="kubectl "
alias ka="kubeadm "
swapoff -a
mkdir -p /etc/systemd/system/docker.service.d

# Restart docker.
systemctl daemon-reload
systemctl restart docker

ka init

modprobe overlay
modprobe br_netfilter


apt-get install -y openjdk-8-jdk openjdk-8-jre
# Install prerequisites
apt-get update
apt-get -y install software-properties-common

add-apt-repository ppa:projectatomic/ppa
apt-get update

# Install CRI-O
apt-get  install -y  curl
apt-get install -y cri-o-1.11



kubeadm init


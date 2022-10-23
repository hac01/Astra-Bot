#!/bin/bash

o=$(cat /etc/os-release | grep PRETTY_NAME)
RED="\e[31m"
ENDCOLOR="\e[0m"
#echo $o
#declare -a packages=("sudo apt update" "sudo apt upgrade")
if [ "$o" == 'PRETTY_NAME="Ubuntu 22.04 LTS"' ]
then 
	echo "it's ok"
       #for i in "${packages[@]}"; do `$i`; done
	echo "installing"
	echo "It may take some time to complete"
	sudo apt-get update
	sudo apt-get install -y nmap
	sudo apt-get install -y golang-go	
	sudo apt-get install python3 python3-pip
	go install -v github.com/OWASP/Amass/v3/...@master
	sudo cp ~/go/bin/amass /usr/bin
	go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
	sudo cp ~/go/bin/subfinder /usr/bin
	pip install -r requirements.txt

else
	echo -e "${RED} This script is tested on Ubuntu 22.04 LTS . You may face problem in other distro's . If U want to continue type y .  ${ENDCOLOR}"
 	read a
fi

if [ "$a" == "y" ]
then 
	echo "installing"
	echo "It may take some time to complete"
	sudo apt update
	sudo apt install -y nmap
	sudo apt install -y golang-go	
	sudo apt install python3 python3-pip
	go install -v github.com/OWASP/Amass/v3/...@master
	sudo cp ~/go/bin/amass /usr/bin
	go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
	sudo cp ~/go/bin/subfinder /usr/bin
	pip install -r requirements.txt
fi

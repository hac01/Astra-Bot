#!/bin/bash
# $1 is host and $2 is URL of target
echo $1> domains.txt
amass enum -passive -norecursive -noalts -df domains.txt -o subdomains.txt
cat subdomains.txt | httpx -o httpx.txt
waybackurls $1 > waybackurls.txt
wget https://raw.githubusercontent.com/shriyanss/hackers-one-command/main/utils/ipResolve.py
python3 ipResolve.py > ip.txt
mkdir httpselfie 
cp httpx.txt httpselfie/httpx.txt
cd httpselfie
wget https://raw.githubusercontent.com/shriyanss/HTTPSelfie/main/httpselfie.py
python3 httpselfie.py httpx.txt url
cd ../ 
wget https://raw.githubusercontent.com/shriyanss/hackers-one-command/main/utils/replace.py
python3 replace.py > hosts.txt
nmap -v -iL hosts.txt -oN nmap.txt
#nikto -url $2 -ask no -Cgidirs all -o nikto.txt -Tuning 1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,x -timeout 30

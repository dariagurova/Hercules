#!/bin/bash

apt-get update && apt-get install openssh-server
cat /etc/ssh/sshd_config | sed 's/.*Port.*/Port 8100/' > ./asd
mv -f ./asd /etc/ssh/sshd_config
systemctl restart sshd

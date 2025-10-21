#!/bin/bash

HW=250425-ptm/Sergii

	for i in {1..10}
	do
		date +"%H:%M:%S"
		ps -ef
#		sleep 5
	done

 
cat /proc/cpuinfo > greg.txt


cat /etc/os-release | grep NAME= | head -1 >> greg.txt

cat /etc/os-release | grep NAME= | head -1 | awk -F "=" '{print$2}' >> greg.txt

	for i in {50-100}
	do
		touch $i.txt
	done



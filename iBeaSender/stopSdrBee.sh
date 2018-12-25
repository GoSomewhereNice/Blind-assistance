#!/bin/bash

NAME=FinalBee.py
echo $NAME
ID=`ps -ef | grep "$NAME" | grep -v "grep" | awk '{print $2}'`
echo $ID
echo "-------------"
for id in $ID
do
sudo kill -9 $id
echo "killed $id"
done
echo "-------------"

#!/bin/ksh
List=pinglist1.txt

cat $List | while read ip
do

  ping -c 2 $ip
  rc=$?
 
  if [[ "$rc" = "0" ]]
  then
    echo "$ip PINGS">>pingresults.txt
  else
    echo "$ip DOESN'T PING">>pingresults.txt
  fi
done
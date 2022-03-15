#!/bin/bash

# Define variables
states=('Texas' 'Arizona' 'Colorado' 'Kentucky' 'Nevada' )
nums=$(echo {0..9})
ls_out=$(ls -l | awk '{print $1, $9}')
execs=$(find /home -type f -perm 777 2> /dev/null)

# Define lists to use later
files=(
   '/etc/shadow'
  '/etc/passwd'
  '/etc/hosts'
)

commands=(
   'date'
   'uname -a'
   'hostname -s'
)

# Iterate through list states and find Arizona
for state in ${states[@]};
do
  if [ $state == 'Arizona' ];
    then
      echo "Arizona is the best!"
  else
      echo "Im not fond of Hawaii!"
  fi
done

# Create a loop that prints 3 5 7
for num in ${nums[@]};
do
  if [ $num = 3 ] || [ $num = 5 ] || [ $num= 7 ]
  then
    echo $num
  fi
done


# Create a for loop that prints out each item in variable holds output of the ls command
for x in ${ls_out[@]};
do
  echo $x
done


#
for exec in ${execs[@]};
do
  echo $exec
done

# Lists permissions for files in /etc/shadow & /etc/passwd
for perm in ${shapass[@]};
do
  echo "$ls_out"
done

#!/bin/bash
for var in ./irudia/* ;
do
  irudi=$(md5sum $var)
  md5="e5ed313192776744b9b93b1320b5e268"
  if [[ $irudi =~ $md5 ]]; then
    echo "EUREKA!!!! Artxiboa arkitu duzu!!!!!!!!!"
    echo "$var"
  fi
done

#!/bin/bash

input_file="example.json"

jq -r '.data[] | "\(.name), \(.link)"' "$input_file" |
while IFS= read -r employee_info; do

    name=$(echo "$employee_info" | cut -d ',' -f1)
    link=$(echo "$employee_info" | cut -d ',' -f2)

    echo "App Name: $name"
    echo "App link: $link"
    echo "--------------------------------"


b="nativefier '"$link"' -n "$name" --disable-dev-tools --darwin-dark-mode-support true --background-color '#000'"
c=$(echo $b)
for i in  1
do

    a=`expr $a + 1`

      $c
    echo "--------------------------------"
done
done

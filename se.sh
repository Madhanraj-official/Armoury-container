number=$(echo "hai hai" | awk -F ' ' '{ print $2 }')
print $number

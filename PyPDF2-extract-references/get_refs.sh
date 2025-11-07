#!/usr/bin/bash

output=$1
a=$(egrep -i -n "references" $output | cut -d ':' -f 1)
let a++
sed -n -i "$a,$ p" $output

#!/bin/bash
tempfile=`tempfile 2>/dev/null` || tempfile=/tmp/test$$
trap "rm -f $tempfile" 0 1 2 5 15

if [ $1 == "-c" ] 
    then
    
    dialog --clear --title "Choose Quality:" --menu "Choose one:" 10 30 4 "hq" "720p" "std" "480p" "wifi" "320p" "3g" "240p" 2> $tempfile
    choice=`cat $tempfile`
    shift    
    else
    choice="hq"
fi



output=$(curl -s -A "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5" $1)

url=$(echo $output | grep -o -P '(?<=<video src=\").*?(?=\")' | sed s/wifi/$choice/ )

#echo $url
#title=$(curl -s $1 | grep -o -P '\<div\ class="title"\>.*\<\/div\>')
#date=$(curl -s $1 | grep -o -P '(<div class="datum">).*(</div>)')
title=$(curl -s $1 | grep -o -m1 -P '(?<=<div\ class=\"title\">).*(?=</div>)' | sed "s/\ /\_/g")
date=$(curl -s $1 | grep -o -i -m1 -P '(?<=<div class=\"datum\">)\d\d/\d\d/\d\d\d\d(?=</div>)' | sed "s/\//\_/g")


#echo $date"_"$title".mp4"

echo "Downloading $url to `echo $date"_"$title".mp4"`"
curl $url -o `echo $date"_"$title".mp4"`


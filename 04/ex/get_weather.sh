#!/bin/bath

mkdir -p weather
cd weather
for y in 2013 2014 2015 2016; do 
  for m in $(seq -w 1 12); do 
    for d in $(seq -w 1 31); do 
      echo ${y}${m}${d}
      curl https://www.wunderground.com/history/airport/KMDW/${y}/${m}/${d}/DailyHistory.html?format=0 -s -o ${y}${m}${d}
    done
  done
done

cd ..
cat weather/2* | sed "s/<br \/>//" | sort | uniq | sort -k 14 -t"," > weather_2013-2016
rm -rf weather


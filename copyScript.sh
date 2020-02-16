i=0
F=a
while [ $i -le 50 ]
do
  cp -vf leetcode刷题_01两数之和.md leetcode刷题_$i.md 
  let i+=1
done

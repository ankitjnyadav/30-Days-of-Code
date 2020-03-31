#Problem Statement - https://www.hackerrank.com/challenges/bash-tutorials---comparing-numbers/problem
read x
read y
if [ $x -gt $y ]; then
  echo X is greater than Y
elif [ $x -lt $y ]; then
  echo X is less than Y
elif [ $x == $y ]; then
  echo X is equal to Y
fi
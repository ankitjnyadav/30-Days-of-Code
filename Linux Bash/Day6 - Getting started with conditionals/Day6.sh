#Problem Statement - https://www.hackerrank.com/challenges/bash-tutorials---getting-started-with-conditionals/problem
read option
if [ $option == 'Y' ] || [ $option == 'y' ]; then
  echo 'YES'
elif [ $option == 'N' ] || [ $option == 'n' ]; then
  echo 'NO'
fi
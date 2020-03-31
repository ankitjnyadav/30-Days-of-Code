#Probleme Statement - https://www.hackerrank.com/challenges/bash-tutorials---arithmetic-operations/problem
read expr
printf "%.3f\n" $(awk "BEGIN {printf $expr}")
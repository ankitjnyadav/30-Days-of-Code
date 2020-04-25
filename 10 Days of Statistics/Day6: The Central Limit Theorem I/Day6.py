'''
Problem Statement - https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem
'''

'''
The central limit theorem (CLT) states that, for a large enough sample (), 
the distribution of the sample mean will approach normal distribution. 
This holds for a sample of independent random variables from any distribution with a finite standard deviation. 
'''
import math

def cumulative_distribution(x,mean,sd):
    return float((0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5))))))

if __name__=='__main__':
    max_weight = 9800
    no_of_boxes = 49
    mean_cargo_weight=205
    sd=15
    mean1 = no_of_boxes*mean_cargo_weight
    sd1 = math.sqrt(no_of_boxes)*sd
    print('{:.4f}'.format(cumulative_distribution(max_weight,mean1,sd1)))
import numpy as np
from scipy.stats import norm, poisson, uniform, expon
import matplotlib.pyplot as plt

AVG = 80
STD_DEVIATION = 12
TEST_SCORE = norm(80, 12)


def part1():
    prob = 90/100
    min_score = TEST_SCORE.ppf(prob)
    print("His/Her minimum score is: ", min_score)


def part2():
    prob_start_range = 0.5
    prob_end_range = 0.75
    score_start_range = TEST_SCORE.ppf(prob_start_range)
    score_end_range = TEST_SCORE.ppf(prob_end_range)
    print(f"The range of scores inbetween quartile 2 and 3 is: [{score_start_range}, {score_end_range}]")


def part3():
    score_start_range = 80
    score_end_range = 90
    prob_start_range = TEST_SCORE.cdf(score_start_range)
    prob_end_range = TEST_SCORE.cdf(score_end_range)
    prob = prob_end_range - prob_start_range
    print(f'The probability of scores being between 80 and 90 is:  {prob}')


def part4():
    size = 50000
    physics = np.random.uniform(40, 80, size=size)
    ap = np.random.exponential(1/60, size=size)
    dm = np.random.poisson(60, size=size)
    sum_random_variable = physics + ap + dm

    # calculate the average and the standard deviation
    exp = np.mean(sum_random_variable)
    var = np.var(sum_random_variable, ddof=1)
    std_dev = np.std(sum_random_variable, ddof=1)
    norm_approximated_samples = np.linspace(80, 180, size)
    print(f'variance: {var}',  f'expectation: {exp}', f'standard deviation: {std_dev}', sep='\n')

    # make figure
    plt.figure()
    plt.hist(sum_random_variable, density=True, bins=30, color='g', label='Sum of Random Variables')
    plt.plot(norm_approximated_samples, norm.pdf(norm_approximated_samples, exp, std_dev), color='r', label='normal approximated')
    plt.xlabel('numbers')
    plt.ylabel('density')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    part1()
    part2()
    part3()
    part4()

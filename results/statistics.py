#!/usr/bin/env python3
import sys
import numpy

# Minimum
# Median
# Mean
# Maximum
# Standard Deviation

def main():

    V = numpy.loadtxt("results/V.txt")
    N = numpy.loadtxt("results/N.txt")
    d = numpy.loadtxt("results/d.txt")
    b = numpy.loadtxt("results/b.txt")

    all = [V, N, d, b]

    for i in range(len(all)):
        if i == 0:
            print("____ Statistics for V ____")
        elif i == 1:
            print("____ Statistics for N ____")
        elif i == 2:
            print("____ Statistics for d ____")
        elif i == 3:
            print("____ Statistics for b ____")

        print("MIN.: ", numpy.min(all[i]))
        print("MEDIAN: ", numpy.median(all[i]))
        print("MEAN: ", numpy.mean(all[i]))
        print("MAX: ", numpy.max(all[i]))
        print("STD. DEV.: ", numpy.std(all[i]))


if __name__ == '__main__':
    main()
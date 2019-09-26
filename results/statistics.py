#!/usr/bin/env python3
import sys
import numpy

# Minimum
# Median
# Mean
# Maximum
# Standard Deviation

def main():

    for h in range(4):

        V = numpy.loadtxt("V_h"+str(h)+".txt")
        N = numpy.loadtxt("N_h"+str(h)+".txt")
        d = numpy.loadtxt("d_h"+str(h)+".txt")
        b = numpy.loadtxt("b_h"+str(h)+".txt")

        print("\n\n\n\n____Statistics for heuristic: ",h,"____\n")
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
from matplotlib import pyplot
data = [(0.05, 8), (0.1, 9), (0.15000000000000002, 10), (0.2, 12), (0.25, 13), (0.3, 14), (0.35, 16), (0.39999999999999997, 17), (0.44999999999999996, 19), (0.49999999999999994, 21), (0.5499999999999999, 24), (0.6, 27), (0.65, 32), (0.7000000000000001, 37), (0.7500000000000001, 45), (0.8000000000000002, 56), (0.8500000000000002, 75), (0.9000000000000002, 112), (0.9500000000000003, 219)]
scalefreegraph = [(0.05, 12), (0.1, 14), (0.15000000000000002, 16), (0.2, 17), (0.25, 20), (0.3, 22), (0.35, 24), (0.39999999999999997, 27), (0.44999999999999996, 31), (0.49999999999999994, 34), (0.5499999999999999, 39), (0.6, 43), (0.65, 51), (0.7000000000000001, 59), (0.7500000000000001, 74), (0.8000000000000002, 91), (0.8500000000000002, 119), (0.9000000000000002, 183), (0.9500000000000003, 364)]
dampingfactor = []
iterations = []
scalefreeiteration = []
for d in data:
    dampingfactor.append(d[0])
    iterations.append(d[1])
for d in scalefreegraph:
    scalefreeiteration.append(d[1])
pyplot.plot(dampingfactor,iterations)
pyplot.plot(dampingfactor,scalefreeiteration)
pyplot.legend(['Airline Data','Scale Free Graph'])
pyplot.xticks(dampingfactor[0::2])
pyplot.yticks(range(0,250,25))
pyplot.xlabel("Damping factor")
pyplot.ylabel("Number of iterations")
pyplot.suptitle("Effect of damping factor on number of iterations to converge with threshold value 0.000000001")
pyplot.show()
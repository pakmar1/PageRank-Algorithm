scalefreeaccuracy = [[75.0, 87.5, 75.0, 68.75, 60.0], [75.0, 87.5, 83.33333333333334, 68.75, 60.0], [75.0, 87.5, 83.33333333333334, 68.75, 60.0], [75.0, 87.5, 91.66666666666666, 68.75, 65.0], [75.0, 87.5, 91.66666666666666, 75.0, 65.0], [75.0, 87.5, 91.66666666666666, 75.0, 70.0], [100.0, 87.5, 91.66666666666666, 75.0, 80.0], [100.0, 87.5, 91.66666666666666, 81.25, 80.0], [100.0, 87.5, 91.66666666666666, 81.25, 80.0], [100.0, 87.5, 91.66666666666666, 87.5, 80.0], [100.0, 87.5, 91.66666666666666, 87.5, 85.0], [100.0, 100.0, 91.66666666666666, 87.5, 90.0], [100.0, 100.0, 100.0, 93.75, 95.0], [100.0, 100.0, 100.0, 93.75, 95.0], [100.0, 100.0, 100.0, 93.75, 100.0], [100.0, 100.0, 100.0, 93.75, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 87.5, 100.0, 100.0, 95.0], [100.0, 87.5, 100.0, 100.0, 90.0]]
airlinesaccuracy = [[45.45454545454545, 62.68656716417911, 73.26732673267327, 74.07407407407408, 74.55621301775149], [45.45454545454545, 62.68656716417911, 75.24752475247524, 75.55555555555556, 75.14792899408283], [45.45454545454545, 64.17910447761194, 76.23762376237624, 76.29629629629629, 76.92307692307693], [51.515151515151516, 65.67164179104478, 78.21782178217822, 76.29629629629629, 79.88165680473372], [51.515151515151516, 70.1492537313433, 79.20792079207921, 78.51851851851852, 79.88165680473372], [51.515151515151516, 73.13432835820896, 82.17821782178217, 80.74074074074075, 81.06508875739645], [60.60606060606061, 74.6268656716418, 83.16831683168317, 82.96296296296296, 82.84023668639054], [66.66666666666666, 77.61194029850746, 85.14851485148515, 84.44444444444444, 82.84023668639054], [72.72727272727273, 77.61194029850746, 86.13861386138613, 85.18518518518519, 83.4319526627219], [75.75757575757575, 79.1044776119403, 87.12871287128714, 85.92592592592592, 84.61538461538461], [81.81818181818183, 80.59701492537313, 87.12871287128714, 87.4074074074074, 86.98224852071006], [81.81818181818183, 85.07462686567165, 90.0990099009901, 88.88888888888889, 89.3491124260355], [84.84848484848484, 86.56716417910447, 92.07920792079209, 89.62962962962962, 91.12426035502959], [84.84848484848484, 88.05970149253731, 92.07920792079209, 91.85185185185185, 92.89940828402366], [87.87878787878788, 91.04477611940298, 94.05940594059405, 94.07407407407408, 95.26627218934911], [90.9090909090909, 94.02985074626866, 96.03960396039604, 96.29629629629629, 97.63313609467455], [100.0, 100.0, 100.0, 100.0, 100.0], [90.9090909090909, 95.52238805970148, 95.04950495049505, 95.55555555555556, 96.44970414201184], [84.84848484848484, 89.55223880597015, 91.0891089108911, 91.11111111111111, 89.94082840236686]]
top4scalefree = []
for acc in scalefreeaccuracy:
    top4scalefree.append(acc[3])

scalefreeiterations = [(0.05, 12), (0.1, 14), (0.15000000000000002, 16), (0.2, 17), (0.25, 20), (0.3, 22), (0.35, 24), (0.39999999999999997, 27), (0.44999999999999996, 31), (0.49999999999999994, 34), (0.5499999999999999, 39), (0.6, 43), (0.65, 51), (0.7000000000000001, 59), (0.7500000000000001, 74), (0.8000000000000002, 91), (0.8500000000000002, 119), (0.9000000000000002, 183), (0.9500000000000003, 364)]
dampingfactor = []
scalefreeperf = []
for cur in scalefreeiterations:
    dampingfactor.append(cur[0])
    scalefreeperf.append(119/cur[1] * 100)

from matplotlib import pyplot
pyplot.plot(dampingfactor, scalefreeperf)
pyplot.plot(dampingfactor, top4scalefree)
pyplot.xticks(dampingfactor[0::2])
#pyplot.yticks(range(50,100,3))
pyplot.xlabel("Damping factor")
pyplot.ylabel("Percentage")
pyplot.legend(["Performance Scale Free Graph","Accuracy Scale Free Graph"])
pyplot.show()


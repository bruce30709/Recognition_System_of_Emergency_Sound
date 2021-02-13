from pyAudioAnalysis import audioTrainTest as aT
from pyAudioAnalysis import audioSegmentation as aS
#aT.featureAndTrain(["/home/bruce/Desktop/siren","/home/bruce/Desktop/nsiren"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm_rbf", "/home/bruce/Desktop/b", False)
a=aT.fileClassification("/home/bruce/Desktop/s/jj.wav", "/home/bruce/Desktop/b", "svm_rbf")
#[flagsInd, classesAll, acc, CM]=aS.mtFileClassification("/home/bruce/Desktop/s/jj.wav", "/home/bruce/Desktop/b", "svm", True, 'data/scottish.segments')
print("jj ["+str(int(a[1][0]*100))+".]")


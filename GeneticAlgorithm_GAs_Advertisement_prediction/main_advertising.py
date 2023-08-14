from ClassGeneticAlgorithm import GeneticAlgorithm
import numpy as np
import matplotlib.pyplot as plt


#__________________________________INITIALIZE_INPUT_________________________________________________________________________________


def getData(data_path_, number_of_chromosome_):
    data_           =   np.genfromtxt(data_path_,delimiter=',',skip_header=1).astype(float)
    feature_X_      =   data_[0:number_of_chromosome_,0:(data_.shape[1]-1)]
    feature_b_      =   np.ones((number_of_chromosome_,1)).astype(float)
    feature_Xb_     =   np.hstack((feature_b_,feature_X_))
    label_Y_        =   data_[0:number_of_chromosome_,-1]
    return data_ ,feature_Xb_,label_Y_



data_path               =   'GeneticAlgorithm_GAs_Advertisement_prediction/advertising.csv'
number_of_gene          =   4
number_of_chromosome    =   150
number_of_generation    =   300
etilism                 =   2
cross_value             =   0.5
mutation_rate           =   0.05
bound                   =   10
feature_Xb     = getData(data_path, number_of_chromosome)[1]
label_Y        = getData(data_path, number_of_chromosome)[2]

GA_data         =   GeneticAlgorithm(feature_Xb,label_Y,number_of_gene, number_of_chromosome,number_of_generation, etilism, cross_value, mutation_rate, bound)
GA_data.visualizingTrainingResult()

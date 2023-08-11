import numpy as np
import matplotlib.pyplot as plt
import random



class GeneticAlgorithm():
    def __init__(self,feature_Xb_,label_Y_,number_of_gene_,number_of_chromosome_,number_of_generation_,etilism_,cross_value_,mutation_rate_,bound_):
        self.feature_Xb_                =   feature_Xb_            
        self.label_Y_                   =   label_Y_                  
        self.number_of_gene_            =   number_of_gene_
        self.number_of_chromosome_      =   number_of_chromosome_
        self.number_of_generation_      =   number_of_generation_
        self.etilism_                   =   etilism_
        self.cross_value_               =   cross_value_
        self.mutation_rate_             =   mutation_rate_
        self.bound_                     =   bound_

   
    def computeLoss(self, individual_):
        Y_hat_          =   np.dot(individual_, self.feature_Xb_.T)
        loss_           =   np.multiply((Y_hat_ - self.label_Y_),(Y_hat_ - self.label_Y_)).mean()
        return loss_
    
    def computeFitness(self, individual_):
        fitness_        =   1/(self.computeLoss(individual_)+1e-6)
        return fitness_
    
    def createIndividual(self):
        individual_     =   []
        for _ in range(self.number_of_gene_):
            individual_.append(random.uniform(-0.5*self.bound_,0.5*self.bound_))
        return individual_
    
    def createPopulation(self):
        population_     =   []
        for _ in range(self.number_of_chromosome_):
            population_.append(self.createIndividual())
        return population_ 
    
    def selectBetterIndividual(self,population_):
        index_individual_1_         =   random.randint(0,self.number_of_chromosome_-1)
        index_individual_2_         =   random.randint(0,self.number_of_chromosome_-1)
        while index_individual_2_   ==  index_individual_1_:
            index_individual_2_     =   random.randint(0,self.number_of_chromosome_-1)
        selected_individual_        =   population_[index_individual_1_]
        if index_individual_2_ > index_individual_1_:
            selected_individual_    =   population_[index_individual_2_]
        return selected_individual_
    
    def crossOverExploiting(self,individual_1_,individual_2_):
        new_individual_1_c_     =   individual_1_.copy()
        new_individual_2_c_     =   individual_2_.copy()
        for i_ in range(self.number_of_gene_):
            if random.uniform(0,1)<self.cross_value_:
                new_individual_1_c_[i_]     =   individual_2_[i_]
                new_individual_2_c_[i_]     =   individual_1_[i_]
        return  new_individual_1_c_, new_individual_2_c_
    
    def mutationExploring(self,individual_):
        for i_ in range(self.number_of_gene_):
            if random.uniform(0,1)<self.mutation_rate_:
                individual_[i_]   =   random.uniform(-0.5*self.bound_,0.5*self.bound_)
        return individual_
    
    def createNewSortedPopulation(self, population_):
        new_population_      =   population_[-self.etilism_:]
        while len(new_population_) < self.number_of_chromosome_:
            individual_1_           =   self.selectBetterIndividual(population_)
            individual_2_           =   self.selectBetterIndividual(population_)
            new_individual_1_c_, new_individual_2_c_        =   self.crossOverExploiting(individual_1_,individual_2_)
            new_individual_1_cm_, new_individual_2_cm_      =   self.mutationExploring(new_individual_1_c_), self.mutationExploring(new_individual_2_c_)
            new_population_.append(new_individual_1_cm_)
            new_population_.append(new_individual_2_cm_)
        new_population_     =   sorted(new_population_,key=self.computeFitness)
        return new_population_

    def processingEvolutionary(self):
        population_                 =   sorted(self.createPopulation(),key=self.computeFitness)
        lst_best_fitness_           =   [self.computeFitness(population_[-1])]
        lst_best_loss_              =   [self.computeLoss(population_[-1])]
        lst_number_of_generation_   =   [_ for _ in range(self.number_of_generation_+1)]
        lst_number_of_chromosome_   =   [_ for _ in range(self.number_of_chromosome_)]
        for p_ in range(self.number_of_generation_):
            print("\rProcessing .. %d%%  complete" % ((p_/self.number_of_generation_)*100) ,end="",flush=True)
            population_         =   self.createNewSortedPopulation(population_)
            lst_best_fitness_.append(self.computeFitness(population_[-1]))
            lst_best_loss_.append(self.computeLoss(population_[-1]))
        best_individual_        =   population_[-1]
        return lst_best_fitness_, lst_best_loss_,lst_number_of_generation_, lst_number_of_chromosome_, best_individual_
    
    def visualizingTrainingResult(self):
        lst_best_fitness_, lst_best_loss_,lst_number_of_generation_, lst_number_of_chromosome_, best_individual_  =   self.processingEvolutionary()
        
        print(f'The best fitness    =   {lst_best_fitness_[-1]}')
        print(f'The best loss       =   {lst_best_loss_[-1]}')
        print(f'The best chromosome =   {best_individual_}')
        plt.xlabel('Generation No.')
        plt.ylabel('Best Fitness(R) and Best Loss(B)')
        plt.plot(lst_number_of_generation_,lst_best_fitness_,color='red')
        plt.plot(lst_number_of_generation_,lst_best_loss_,color='blue')
        plt.show()
        
        print(f'Training result @ No.{self.number_of_generation_} of Evolutionary progress')
        lst_predict_sale_Y_              =   list(np.dot(np.array(best_individual_),self.feature_Xb_.T))#self.getData()[0].T))
        lst_sale_Y_                      =   list(self.label_Y_)#self.getData()[1])
        plt.xlabel('Individual No.')
        plt.ylabel('Sale_value')
        plt.plot(lst_number_of_chromosome_,lst_predict_sale_Y_,color='red')
        plt.plot(lst_number_of_chromosome_,lst_sale_Y_,color='blue')
        plt.show()
        return
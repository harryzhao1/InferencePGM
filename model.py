import numpy as np
import loadData

class model:
  def __init__(self,  num_class = 14):
    self.num_class = num_class;

    # data
    self.data = loadData.loadData().getDataArray()

    # model parameters
    # for each pixel in each class, there are: 
      # 1. pi representing probability of the class
      # 2. alpha representing probability of being foreground
      # 3. mu and sigma representing gaussian of observation vs fg/bg data
    self.param_pi = np.array([1.0/self.num_class] * self.num_class)
    self.param_alpha = np.ones((self.num_class, len(self.data[0])))  * 0.5
    self.param_mu = np.random.random((self.num_class, len(self.data[0]))) 
    self.param_sigma = np.ones((self.num_class, len(self.data[0]))) * 1.0

  def gaussian(self, x, mu, sig):
      return 1.0/(pow(2*np.pi, .5) * sig) * np.exp(-(x-mu)*(x-mu) / (2 * sig * sig ))

  def step_E(self):
      raise NotImplemented

  def step_M(self): 
      raise NotImplemented
    
  def do_EM(self, n_iteration = 10):
    for i in range(n_iteration):
      print "iteration:", i
      self.step_E()
      self.step_M()

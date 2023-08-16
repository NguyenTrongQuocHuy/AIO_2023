import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

url         =   'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
pure_data   =   pd.read_csv(url,delimiter='\t')

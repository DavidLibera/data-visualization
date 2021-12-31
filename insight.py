### Setting up environment
# python -m virtualenv myenv
# source myenv/bin/activate
# pip freeze > requirements.txt
### Running after cloning 
# python -m virtualenv myenv
# python -m pip install -r requirements.txt
# python -m idlelib.idle
### Extract dataset from
# soccer-spi: https://data.fivethirtyeight.com/

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

myfile1 = './dataset/soccer-spi/spi_global_rankings.csv'
df1 = pd.read_csv(myfile1, index_col=0)

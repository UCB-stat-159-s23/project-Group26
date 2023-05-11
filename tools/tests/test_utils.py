from tools import utils as ul
import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

evict = pd.read_csv("data/Eviction_Notices.csv", engine='python', on_bad_lines='skip')
bad_reasons = evict[['Eviction ID', 'Address','File Date', 'Non Payment', 'Nuisance', 'Illegal Use', 
                     'Unapproved Subtenant', 'Demolition', 'Ellis Act WithDrawal', 'Late Payments', 
                     'Failure to Sign Renewal', 'Neighborhoods - Analysis Boundaries']].dropna()

sample = bad_reasons.sample(5000).rename({'Neighborhoods - Analysis Boundaries': 'Neighborhoods'}, axis=1)

sample['File Date'] = pd.to_datetime(sample['File Date'])
sample['year'] = pd.DatetimeIndex(sample['File Date']).year
sample['month'] = pd.DatetimeIndex(sample['File Date']).month

df = sample

# test for get_count_plot()
def test_get_count_plot():
    assert type(df) == pd.core.frame.DataFrame
    
# test for create_map()
def test_create_map():
    assert type(df) == pd.core.frame.DataFrame
    
    
test_get_count_plot()
test_create_map()
# -*- coding: utf-8 -*-
"""
Script to create a pairplot using a standard seaborn dataset.
Find the available datasets on https://github.com/mwaskom/seaborn-data.

Created on Tue Mar 26 15:54:47 2024

@author: Lina Blijleven <selina.blijleven@code-cafe.nl>
"""

import seaborn as sns

data = sns.load_dataset("penguins")
sns.pairplot(data)
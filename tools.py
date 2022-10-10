from use import *
import os
with open('word','r') as f:
    data=f.read()


data=remove_item(data)
data=remove_and_percent(data)
data=remove_ref_cite_textbf(data)
data=remove_n_t(data)
data=remove_redundant_blank(data)

print(data)
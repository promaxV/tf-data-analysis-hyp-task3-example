import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, boxcox

chat_id = 664256606  # Ваш chat ID, не меняйте название переменной
alpha = 0.04

def solution(x, y) -> bool:
    new_x, lm = boxcox(x)
    statistic, p_value = ttest_ind(new_x, boxcox(y, lmbda=lm), alternative="greater")
    return p_value < alpha

import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 664256606  # Ваш chat ID, не меняйте название переменной
alpha = 0.04

def solution(x, y) -> bool:
    statistic, p_value = ttest_ind(x, y, alternative="greater")
    return p_value < alpha

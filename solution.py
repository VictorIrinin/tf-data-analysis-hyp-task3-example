import pandas as pd
import numpy as np


chat_id = 5780444792 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    res = False
    s = np.mean(x)
    if s >= 500:
        res = True
    else:
        res = False
    return res # Ваш ответ, True или False

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def mse(actual, predicted):
    n = len(actual)
    loss = sum([(y_i - y_p) ** 2 for y_i, y_p in zip(actual, predicted)]) / n
    return loss

# def 

if __name__=='__main__':
    # Open the dataset
    df = pd.read_csv('data_for_lr.csv')
    actual_y = df['y']
    n = len(actual_y)
    
    m = 0
    b = 0
    alpha = 0.00001 # Learning rate

    # Before Loss
    predicted_y = m * df['x'] + b
    loss = mse(actual_y, predicted_y)
    print('before loss:', loss)
    
    iter = 100
    for _ in range(iter):   
        
        sum_m = 0
        sum_b = 0
        for i in range(n):
            sum_m += (df['y'][i] - (m * df['x'][i] + b)) * df['x'][i]
            sum_b += (df['y'][i] - (m * df['x'][i] + b))
            
        dL_dm = (2 / n) * sum_m 
        dL_db = (2 / n) * sum_b
        
        print('dL_dm, dl_db', dL_dm, dL_db)
        
        m = m - dL_dm * alpha
        b = b - dL_db * alpha
        
        print('m, b', m, b)

    # After loss
    predicted_y = m * df['x'] + b
    loss = mse(actual_y, predicted_y)
    print('After loss:', loss)
    


    # Plot the dataset
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.scatter(df['x'], df['y'])
    # plt.show()


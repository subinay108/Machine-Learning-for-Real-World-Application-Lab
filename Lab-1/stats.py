import statistics

def mean(vector):
    return sum(vector) / len(vector)

def median(vector):
    n = len(vector)
    if n % 2 == 1: # length is odd
        return sorted(vector)[(n + 1) // 2]
    else: # length is even
        s_vector = sorted(vector)
        return (s_vector[n // 2] + s_vector[n // 2 - 1]) / 2

def mode(vector):
    freq = {}
    for i in vector:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1 
    
    max_val = 0
    for i in freq:
        if freq[i] > max_val:
            max_val = freq[i]

    modes = []
    for i in freq:
        if freq[i] == max_val:
            modes.append(i)
    
    return modes

def variance(vector):
    m = mean(vector)
    s = 0
    for i in vector:
        s += (i - m) ** 2
    
    return s / (len(vector) - 1)

def standard_deviation(vector):
    return variance(vector) ** 0.5

if __name__ == '__main__':
    arr = [40, 32, 65, 75, 58, 68, 65, 72, 70, 55]
    print('mean: ', mean(arr))
    print('median: ', median(arr))
    print('mode(s): ', mode(arr))
    print('variance: ', variance(arr))
    print('standard deviation: ', standard_deviation(arr))

    # using statistics library
    print('\nUsing statistics library')
    print('mean: ', statistics.mean(arr))
    print('median: ', statistics.median(arr))
    print('mode(s): ', statistics.mode(arr))
    print('variance: ', statistics.variance(arr))
    print('standard deviation: ', statistics.stdev(arr))

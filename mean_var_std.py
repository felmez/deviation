import numpy as np

def calculate(line):
    mean = []
    variance = []
    standard = []
    maximum = []
    minimum = []
    summary = []
    array = np.array(line)
    try:
        array = np.reshape(array, (3, 3))
    except:
        raise ValueError('List must contain nine numbers.')
    mean.append(np.mean(array, axis=0).tolist())
    mean.append(np.mean(array, axis=1).tolist())
    mean.append(np.mean(array).tolist())
    variance.append(np.var(array, axis=0).tolist())
    variance.append(np.var(array, axis=1).tolist())
    variance.append(np.var(array).tolist())
    standard.append(np.std(array, axis=0).tolist())
    standard.append(np.std(array, axis=1).tolist())
    standard.append(np.std(array).tolist())
    maximum.append(np.amax(array, axis=0).tolist())
    maximum.append(np.amax(array, axis=1).tolist())
    maximum.append(np.amax(array).tolist())
    minimum.append(np.amin(array, axis=0).tolist())
    minimum.append(np.amin(array, axis=1).tolist())
    minimum.append(np.amin(array).tolist())
    summary.append(np.sum(array, axis=0).tolist())
    summary.append(np.sum(array, axis=1).tolist())
    summary.append(np.sum(array).tolist())
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard,
        'max': maximum,
        'min': minimum,
        'sum': summary
    }
    return calculations
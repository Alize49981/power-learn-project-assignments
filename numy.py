import numpy as np
def days_until_april():
    """calculate number of days until first day april."""
    today = date.today()
    april = date(today.april + 1, 1, 1)
    return(april - today).days
print(f"days until april: {days_until_april}")
#array manipulation
def manipulate_array(arr):
    """perform some basic array manipulations.""" 
    np.arr = np.array(arr)
    return {'original' : np.arr, 'mean':np.mean(np.arr), 'std_dev': np.std(np.arr), 'squared': np.square(np.arr)}
print(manipulate_array([1, 2, 3, 4, 5]))


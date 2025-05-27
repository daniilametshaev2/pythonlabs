import numpy as np

def run_length_encoding(x):

    diff = np.diff(x)
    change_indices = np.where(diff != 0)[0] + 1

   
    segment_starts = np.concatenate(([0], change_indices))
  
    segment_ends = np.concatenate((change_indices, [len(x)]))

    
    values = x[segment_starts]
    counts = segment_ends - segment_starts

    return values, counts

# Пример использования
x = np.array([2, 2, 2, 3, 3, 3, 5])
values, counts = run_length_encoding(x)

print("Значения:", values)
print("Повторения:", counts)

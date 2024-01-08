import pandas as pd
import numpy as np

# simple array
data = [1, 2, 3, 4]

ser = pd.Series(data)
print(ser)

print("* "*15)

# simple array
data = np.array(['g', 'e', 'e', 'k', 's'])
# print(data)
ser = pd.Series(data)
print(ser)


print("* "*15)
# initialise data of lists.
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18],
        'marks': [56, None, 89, 74]
        }
# Create DataFrame
df = pd.DataFrame(data)
# Print the output.
print(df)
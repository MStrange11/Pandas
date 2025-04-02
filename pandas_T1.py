import pandas as pd
import numpy as np
#
# # simple array
# data = [1, 2, 3, 4]
#
# ser = pd.Series(data)
# print(ser)
#
# print("* "*15)
#
# # simple array
# data = np.array(['g', 'e', 'e', 'k', 's'])
# # print(data)
# ser = pd.Series(data)
# print(ser)
#
#
# print("* "*15)

#
# # creating simple array
# data = np.array(['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's'])
# ser = pd.Series(data, index=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
#
# # accessing a element using index element
# print(ser[16])
#
# print("* "*15)


# # initialise data of lists.
# data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
#         'Age': [20, 21, 19, 18],
#         'marks': [56, None, 89, 74]
#         }
# # Create DataFrame
# df = pd.DataFrame(data)
# # Print the output.
# print(df)
# print("* "*15)

df = pd.read_csv("Project_title-FSD-1.csv")
ser = pd.Series(df['Project Title'])
# print(ser)

print("* "*15)

data = ser.loc[90:100]
print(data)

print("* "*15)

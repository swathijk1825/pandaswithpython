import pandas as pd



# 1:List all data from csv

data=pd.read_csv('employee_data.csv')

data2=pd.read_csv('new_data_no_dup.csv')



merged_data = pd.merge(data, data2, on='emp_id', how='right')  # or 'right' or 'outer'


print("Merged data frame:")

print(merged_data)



# Read the first file
data1 = pd.read_csv('employee_data.csv')

# Read the second file
data2 = pd.read_csv('new_data_no_dup.csv')

# Concatenate the two DataFrames vertically (along rows)
combined_data = pd.concat([data1, data2], ignore_index=True)

# Write the combined DataFrame to a new CSV file
combined_data.to_csv('combined_data.csv', index=False)

print("Combined data frame:")
print(combined_data)

# print(data)


# # 2: Get the highest salary employee

# high_salary_emp=data[data['salary']>9000]

# print("The highest salary emp")

# print(high_salary_emp)

# manager_id=data.loc[data['emp_name']=='swetha','emp_id'].iloc[0]


# # 3: find the employees reporting to swetha

# rep_emps=data[data['managerId']==manager_id]

# count=len(rep_emps)

# print(f'the no of employees reporting to swetha is {count}')


# 4: get and delete all duplicate records

# no_duplicate_data=data.drop_duplicates(subset=['emp_id'])


# no_duplicate_data.to_csv('new_data_no_dup.csv',index=False)









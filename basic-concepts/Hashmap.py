import pandas as pd

emp_details = {'Employee': {'Dave': {'ID': '001',
                                     'Salary': 2000,
                                     'Designation': 'Python Developer'},
                            'Ava': {'ID': '002',
                                    'Salary': 2300,
                                    'Designation': 'Java Developer'},
                            'Joe': {'ID': '003',
                                    'Salary': 1843,
                                    'Designation': 'Hadoop Developer',
                                    'Age': 55}}}
df = pd.DataFrame(emp_details['Employee'])
print(df)

total_salary = 0
for p_type,p_name in emp_details.items():
    for p_info in p_name:
        total_salary = int(emp_details[p_type][p_info]['Salary'])+ sum
print(total_salary)



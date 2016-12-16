import pandas as pd
import numpy as np

def print_three(d):
  count = 0  
  print 'Here are up to three items from the dictionary:'
  for k, v in d.items():  
    print k, v  
    count += 1  
    if count == 3:  
      break

df = pd.read_csv('faculty.csv')
df.columns = [n.strip() for n in list(df)]
df.title = df.title.replace(' is ', ' of ', regex = True)
df.degree = df.degree.replace('0', np.nan)
df.degree = df.degree.str.strip()

# Split full name into firstname and lastname
df['firstname'] = df.name.str.extract('(.+(?= ))')
df['lastname'] = df.name.str.extract('(\w+$)')

#Q6
# Create faculty_dict
faculty_dict = dict()
cols = ['degree', 'title', 'email']
for i in range(len(df)):
    faculty_dict.setdefault(df.loc[i, 'lastname'], []).append(df.loc[i, cols].tolist())

      
print_three(faculty_dict)
print '\n'

#Q7
# Create professor_dict
professor_dict = dict()
for i in range(len(df)):
    professor_dict.setdefault((df.loc[i, 'firstname'], df.loc[i, 'lastname']), \
                            []).extend(df.loc[i, cols].tolist())

print_three(professor_dict)
print '\n'

#Q8
def dict_sort_last(d):
  return sorted(d, key = lambda x: x[1])

print 'Here is the dictionary sorted by last name:', dict_sort_last(professor_dict)

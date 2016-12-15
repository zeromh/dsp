import pandas as pd

df = pd.read_csv('faculty.csv')
df.columns = [n.strip() for n in list(df)]

total_degree_list = []
for item in df.degree:
    total_degree_list.extend(item.strip().replace('.', '').split())
total_degree_list.remove('0')
degree_freq = pd.Series(total_degree_list).value_counts() 

print 'Number of different degrees:', len(degree_freq)
print 'Frequencies of each degree:\n', degree_freq, '\n'
    
df.title = df.title.apply(lambda s: s.replace(' is ', ' of '))
print 'Number of different titles:', len(df.title.value_counts())
print 'Frequencies of each title:\n', df.title.value_counts(), '\n'

pattern = r'[\w.-]+@([\w+.-]+)'
valid_emails = df.email[df.email.str.contains(pattern)]
print 'List of email addresses:'
print valid_emails, '\n'

domain_freq = valid_emails.str.extract(pattern).value_counts()
print 'Number of different email domains:', len(domain_freq)
print 'List of different domains:\n', domain_freq, '\n'

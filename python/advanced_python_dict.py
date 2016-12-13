#Q6
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}

def print_three(d):
  count = 0  
  print 'Here are up to three items from the dictionary:'
  for k, v in d.items():  
    print k, v  
    count += 1  
    if count == 3:  
      break
      
print_three(faculty_dict)
print '\n'

#Q7
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
print_three(professor_dict)
print '\n'

#Q8
def dict_sort_last(d):
  t = []
  res = []
  for key in d.keys():
      t.append((key[-1], key))
  t.sort()
  for x, y in t:
      res.append(y)
  return res

print 'Here is the dictionary sorted by last name:', dict_sort_last(professor_dict)

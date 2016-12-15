# Hint:  use Google to find python function
import datetime

def print_date_diff(date_start, date_stop, format):
  '''
  Prints the difference (in days) between two date strings in a given format.
  '''
  date_start = datetime.datetime.strptime(date_start, format)
  date_stop = datetime.datetime.strptime(date_stop, format)
  print 'Days between %s and %s:' % \
      (date_start.strftime('%m-%d-%Y'), date_stop.strftime('%m-%d-%Y')), \
      (date_stop - date_start).days

if __name__ == '__main__':
  ####a) 
  date_start = '01-02-2013'  
  date_stop = '07-28-2015'   

  print_date_diff(date_start, date_stop, '%m-%d-%Y')


  ####b)  
  date_start = '12312013'  
  date_stop = '05282015'  

  print_date_diff(date_start, date_stop, '%m%d%Y')

  ####c)  
  date_start = '15-Jan-1994'  
  date_stop = '14-Jul-2015'  

  print_date_diff(date_start, date_stop, '%d-%b-%Y')

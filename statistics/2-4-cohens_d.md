[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

```python
import thinkstats2
from nsfg import *

df = ReadFemPreg()

df['birthord_bin'] = df.birthord.apply(lambda x: \
                        'first' if x == 1 else 'other')

print 'The average weight of first and non-first babies is:'
print df.groupby('birthord_bin').totalwgt_lb.mean()
  # Result
  # first: 7.20
  # other: 7.33

first = df[df.birthord_bin == 'first'].totalwgt_lb
other = df[df.birthord_bin == 'other'].totalwgt_lb

print "Cohen's d for this difference is:", \
    thinkstats2.CohenEffectSize(first, other)
    # Result
    # Cohen's d: -.09
```
>>This is a very small difference.  
Additionally, this effect shows that first babies weigh slightly LESS than other babies, even though we learned in the book chapter that first babies are slightly LATE. This is odd.

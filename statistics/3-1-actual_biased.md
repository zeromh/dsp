[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```python
%matplotlib inline

import chap01soln
resp = chap01soln.ReadFemResp()
```

Make a PMF of <tt>numkdhh</tt>, the number of children under 18 in the respondent's household.


```python
import thinkstats2
pmf = thinkstats2.Pmf(resp.numkdhh, 'actual')
```

Display the PMF.


```python
print pmf
```

    Pmf({0: 0.46617820227659301, 1: 0.21405207379301322, 2: 0.19625801386889966, 3: 0.087138558157791451, 4: 0.025644380478869556, 5: 0.010728771424833181})


Define <tt>BiasPmf</tt>.


```python
def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
```

Make a the biased Pmf of children in the household, as observed if you surveyed the children instead of the respondents.


```python
b_pmf = BiasPmf(pmf, 'biased')
print 'Actual pmf:'
print pmf
print 'Biased pmf:'
print b_pmf
```

    Actual pmf:
    Pmf({0: 0.46617820227659301, 1: 0.21405207379301322, 2: 0.19625801386889966, 3: 0.087138558157791451, 4: 0.025644380478869556, 5: 0.010728771424833181})
    Biased pmf:
    Pmf({0: 0.0, 1: 0.20899335717935616, 2: 0.38323965252938175, 3: 0.25523760858456823, 4: 0.10015329586101177, 5: 0.052376085845682166})


Display the actual Pmf and the biased Pmf on the same axes.


```python
import thinkplot
#thinkplot.Hist(pmf, label='actual')
#thinkplot.Hist(b_pmf, label='biased')
thinkplot.Pmfs([pmf, b_pmf])
thinkplot.Show(xlabel = 'number of children in household', ylabel='pmf')
```

Compute the means of the two Pmfs.


```python
print 'Actual mean:', pmf.Mean()
print 'Biased mean:', b_pmf.Mean()
```

    Actual mean: 1.02420515504
    Biased mean: 2.40367910066


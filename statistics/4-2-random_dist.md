[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)


Generate 1000 random values using <tt>random.random()</tt> and plot their PMF.


```python
import random, thinkstats2, thinkplot
vals = [random.random() for x in range(1000)]
vals_pmf = thinkstats2.Pmf(vals)
thinkplot.Pmf(vals_pmf, linewidth=0.1)
```

Assuming that the PMF doesn't work very well, try plotting the CDF instead.


```python
vals_cdf = thinkstats2.Cdf(vals)
thinkplot.Cdf(vals_cdf)
thinkplot.Show(xlabel = 'random value', ylabel = 'CDF')
```


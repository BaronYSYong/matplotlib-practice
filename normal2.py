import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

# generate log-normal distributed set of samples
np.random.seed(42)
samples   = np.random.lognormal( mean=1, sigma=.4, size=10000 )

# make a fit to the samples
shape, loc, scale = scipy.stats.lognorm.fit( samples, floc=0 )
x_fit       = np.linspace( samples.min(), samples.max(), 100 )
samples_fit = scipy.stats.lognorm.pdf( x_fit, shape, loc=loc, scale=scale )

# plot a histrogram with linear x-axis
plt.subplot( 1, 2, 1 )
N_bins = 50
counts, bin_edges, ignored = plt.hist( samples, N_bins, histtype='stepfilled', label='histogram' )
# calculate area of histogram (area under PDF should be 1)
area_hist = .0
for ii in range( counts.size):
    area_hist += (bin_edges[ii+1]-bin_edges[ii]) * counts[ii]
# oplot fit into histogram
plt.plot( x_fit, samples_fit*area_hist, label='fitted and area-scaled PDF', linewidth=2)
plt.legend()

# make a histrogram with a log10 x-axis
plt.subplot( 1, 2, 2 )
# equally sized bins (in log10-scale)
bins_log10 = np.logspace( np.log10( samples.min()  ), np.log10( samples.max() ), N_bins )
counts, bin_edges, ignored = plt.hist( samples, bins_log10, histtype='stepfilled', label='histogram' )
# calculate area of histogram
area_hist_log = .0
for ii in range( counts.size):
    area_hist_log += (bin_edges[ii+1]-bin_edges[ii]) * counts[ii]
# get pdf-values for log10 - spaced intervals
x_fit_log       = np.logspace( np.log10( samples.min()), np.log10( samples.max()), 100 )
samples_fit_log = scipy.stats.lognorm.pdf( x_fit_log, shape, loc=loc, scale=scale )
# oplot fit into histogram
plt.plot( x_fit_log, samples_fit_log*area_hist_log, label='fitted and area-scaled PDF', linewidth=2 )

plt.xscale( 'log' )
plt.xlim( bin_edges.min(), bin_edges.max() )
plt.legend()
plt.show()

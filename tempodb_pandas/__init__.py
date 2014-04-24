from pandas import Series
from numpy import negative
from tempodb import DataPoint


# fromTempo :: [DataPoint] -> Series
def fromTempo(series):

    splitDatapoint = lambda x: (x.ts, x.value)
    index, values = zip(*map(splitDatapoint, series))

    return Series(values, index)


# Convenience function to output back to a DataSet object.
#
# fromPandas :: Series -> [DataPoint]
def fromPandas(series):
    # I'm missing Haskell's zipWith here...
    return [DataPoint(x[0], x[1]) for x in zip(series.index, series)]


# Convenience function for flipping the sign on all the data points in
# a series (this happens often with negative input values and pandas +
# numpy is *much* faster than mapping a (*-1) over the value list).
#
# flipDatumSign :: Series -> String -> Series
def flipDatumSign(series, interval):
    return series.resample(interval, how=negative)

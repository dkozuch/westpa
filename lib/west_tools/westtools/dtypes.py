
'''Numpy/HDF5 data types shared among several WESTPA tools'''

import numpy

# Pick up a few data types from the WEST core if possible
try:
    from west.data_manager import n_iter_dtype, seg_id_dtype, weight_dtype
except ImportError:
    n_iter_dtype = numpy.uint32
    seg_id_dtype = numpy.int64
    weight_dtype = numpy.float64

# A quantity averaged over iterations
iter_block_ci_dtype = numpy.dtype([('iter_start', n_iter_dtype),
                                   ('iter_stop', n_iter_dtype),
                                   ('expected', numpy.float64),
                                   ('ci_lbound', numpy.float64),
                                   ('ci_ubound', numpy.float64),
                                   ('sterr', numpy.float64),
                                   ('corr_len', n_iter_dtype)])

# A quantity to store event duration distribution stuff.
# Comes from the old w_kinetics.

ed_list_dtype       = numpy.dtype([('istate', numpy.uint16), 
                                   ('fstate', numpy.uint16), 
                                   ('duration', numpy.float64),
                                   ('weight', numpy.float64), 
                                   ('seg_id', seg_id_dtype)])

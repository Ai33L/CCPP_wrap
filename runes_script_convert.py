import numpy as np
from cffi import FFI

class runes (object):
    def __init__(self, precision = 'double'):
        self._ffi = FFI()
        self.precision = precision

    def convert_to_from_cffi(self, c_or_numpy_array, num_bytes = None, type='none'):
        
        if type=='integer':
            self._numpy_type = np.intc
            self._ffi_type = 'int'
        else:
            if self.precision == 'single':
                self._numpy_type = np.float32
                self._ffi_type = 'float'
            elif self.precision == 'double':
                self._numpy_type = np.float64
                self._ffi_type = 'double'
            else:
                raise ValueError(
                    'Uknown precision type {}'.format(self.precision))

        if isinstance(c_or_numpy_array, np.ndarray):
            if c_or_numpy_array.ndim > 1:
                out_buffer = self._ffi.cast('{} **'.format(self._ffi_type),
                                        c_or_numpy_array.ctypes.data)
            else:
                out_buffer = self._ffi.cast('{} *'.format(self._ffi_type),
                                        c_or_numpy_array.ctypes.data)
                # print("In pointer: {}".format(c_or_numpy_array.ctypes.data))

        elif isinstance(c_or_numpy_array, self._ffi.CData):
            out_buffer = np.frombuffer(self._ffi.buffer(
                c_or_numpy_array, num_bytes), dtype=self._numpy_type)
            # print("Out pointer: {}".format(out_buffer.ctypes.data))

        else:
            raise ValueError(
                'Buffer must be either numpy.ndarray or ffi CData,\
                not {}'.format(type(c_or_numpy_array)))

        return out_buffer
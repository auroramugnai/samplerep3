"""
"""
import numpy as np

from samplerep.utils import square

def test_square():
	"""Unit test for the square() function.
	"""
	assert square(2.) == 4.# the reason this works is some magic of pytest (non dovresti mai eguagliare floating point)
	assert square(-2.) == 4.
	assert square(0.) == 0.
	assert square(2) == 4.
	assert square(-2) == 4.
	assert square(0) == 0
	# assert square(np.ones(100)) == np.ones(100)
	assert np.allclose(square(np.ones(100)), np.ones(100))# close enough given errore di arrotondam della macchina
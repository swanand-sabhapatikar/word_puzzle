#This class defines all the custom Exceptions for this project.

class ValueNotStringError(Exception):
	def __init__(self,a=""):	
		a="ERROR:String entered should contain only letters "
		Exception.__init__(self,a)

class ValueExceedsLimitError(Exception):
	def __init__(self,a=""):	
		a="ERROR:Length of the required word should be less then count of letters given as input"
		Exception.__init__(self,a)

from Components.Converter.Converter import Converter
from Components.Element import cached
from enigma import eServiceCenter, iServiceInformation, eServiceReference

class NowaHDRefToString(Converter, object):
	SERVICEREFERENCE_TO_STRING = 0
	PICON_REFERENCE = 1
	def __init__(self, type):
		Converter.__init__(self, type)
		if type == "PiconRef":
			self.type = self.PICON_REFERENCE
		else:
			self.type = self.SERVICEREFERENCE_TO_STRING
	@cached
	def getText(self):
		ref = self.source.service
		if ref is not None:
			if self.type == self.SERVICEREFERENCE_TO_STRING:
				return ref.toString()
			elif self.type == self.PICON_REFERENCE:
				if ref.getPath():
					info = eServiceCenter.getInstance().info(ref)
					if info:
						return info.getInfoString(ref, iServiceInformation.sServiceref)
				else:
					return ref.toString()				
		return ""
		
	text = property(getText)

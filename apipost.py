



from pmfs import DistribucionDeProbabilidadFactory

class DistribucionesC(object):	
	def __init__(self):
		pass

	def getDistribucion(self, tipo, args):
		#parsear args a un diccionario de acuerdo al tipo
		if(tipo=="Poisson"):
			dict={'l': int (args['l']) }
		elif tipo == "Binomial" or tipo == "BinomialNegativa":
			dict={'p':  float(args['p']), 'n': int(args['n']) }	
		elif tipo == "Normal":
			dict={'loc': int (args['loc']), 'scale': int(args['scale']) }
		elif tipo == "Exponencial":
			dict={'scale': int (args['scale'])}
		else:
			#si ocurre un error devolver error
			return "ocurrio un error"

		#caso contrario continuar con el factory
		factory=DistribucionDeProbabilidadFactory()
		f=factory.getDistribucion(tipo, dict)
		#results=f.getProbability(3)
		results=f.getSample( int(args['cardinality']) )
		return results
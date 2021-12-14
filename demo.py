from pmfs import DistribucionDeProbabilidadFactory#PoissonDistribution,  BinomialDistribucion, BinomialDistribucionNegativa

#poisson=PoissonDistribution(l=5)
#print(poisson.getProbability(3))
#s=poisson.getSample(100)
#print(s)

#binomial=BinomialDistribucion(0.9, 10)
#print(binomial.getProbability(3))
#s=binomial.getSample(100)
#print(s)


#binomialN=BinomialDistribucionNegativa(0.9, 20)
#print(binomialN.getProbability(11))
#s=binomialN.getSample(100)
#print(s)

#Usar una fábrica de Figuras
factory=DistribucionDeProbabilidadFactory()
#f=factory.getFigura("Triangulo", dict)
#print ("El area de la figura es ", f.area())
#print("Tipo de Figura:", type(f))
dict={'l':10}
f=factory.getDistribucion("Poisson", dict)
#print(f)

s=f.getSample(100)
print(s)
print("")

#binomial
dict={'p':0.9, 'n':10}
f=factory.getDistribucion("Binomial", dict)
print(f)
s=f.getSample(100)
print(s)
print("")

#BinomialNegativa
dict={'p':0.9, 'n':5}
f=factory.getDistribucion("BinomialNegativa", dict)
print(f)
s=f.getSample(100)
print(s)
print("")

#Normal
dict={'loc':1, 'scale':2}
f=factory.getDistribucion("Normal", dict)
print(f)
s=f.getSample(1000)
print(s)
print("")

#Exponencial
dict={'scale':10}
f=factory.getDistribucion("Exponencial", dict)
print(f)
s=f.getSample(1000)
print(s)
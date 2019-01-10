m = int (input ('\nDigite uma medida: '))

km = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
cm = m * 100
mm = m * 1000
	
print ('\n{}m corresponde a\n{:.3f}km\n{:.2f}hm\n{:.1f}dam\n{}dm\n{}cm\n{}mm'.format(m,km,hm,dam,dm,cm,mm))

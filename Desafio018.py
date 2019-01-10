import math
ang = float (input  ('\nDigite um ângulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {}° tem o SENO de {:.2f}'.format(ang,sen))
print('O ângulo de {}° tem o COSSENO de {:.2f}'.format(ang,cos))
print('O ângulo de {}° tem a TANGENTE de {:.2f}'.format(ang,tan))

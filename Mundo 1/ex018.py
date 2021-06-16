ang = float(input('Digite o ângulo que você deseja: '))

from math import sin, cos, tan, radians

a = radians(ang)

print('O ângulo de {} tem SENO de {:.2f}'.format(ang, sin(a)))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(ang, cos(a)))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(ang, tan(a)))

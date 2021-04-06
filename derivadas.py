from sympy import diff, Symbol
from sympy.parsing.sympy_parser import parse_expr
import sympy
def derivar(pregunta): #funcion para hallar la respuesta del juego de matematicas, retorna la respuesta
    p = pregunta
    p = p.replace('=(', '=')
    z = len(p)
    n = p.find('f(x)') #encuentra el inicio de la funcion
    user_str = p[n+5: z]
    user_str = user_str.replace('sen', 'sin') #reemplaza sen por sin para su implementacion en el codigo
    user_str = user_str.replace('(c', 'c')
    user_str = user_str.replace('(t', 't')
    user_str = user_str.replace('5)', '5')
    
    user_str = user_str.replace('))', ')')
    my_symbols = {'x': Symbol('x', real=True)}
    my_func = parse_expr(user_str, my_symbols) 
    derivada = diff(my_func, my_symbols['x']) #deriva la expresion
    n = p.find('pi') #busca pi en el string p
    if p[n+3].isnumeric:
        evaluar = (p[n: n+4]) #Buscamos el valor a evaluar
    else:
        evaluar = 'pi'
    evaluar = evaluar.replace('pi', '3.14') #cambiamos pi por su valor numerico
    evaluar = eval(evaluar)
    derivada = str(derivada)
    x,y,z = sympy.symbols('x y z')
    respuesta = (sympy.sympify(derivada).subs(x,evaluar)) #evalua la funcion con respecto a evaluar
    return respuesta

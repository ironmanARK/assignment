import scipy.optimize as opt
def f(vars):
    x,y=vars
    return 2*(x-y-3)**2+4*(x+2*y+1)**4
def constraint1(vars):
    x,y=vars
    return x-y+3
def constraint2(vars):
    x,y=vars
    return 5-(x+2)**2-(y+1)**2
initial_guess=[1,1]
constraints = [{'type': 'ineq', 'fun': constraint1},{'type': 'ineq', 'fun': constraint2}]
result = opt.minimize(f,initial_guess, constraints=constraints)
print(result)
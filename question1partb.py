def F(d : dict):
    t={}
    for key in sorted(d):
        t[d[key][0]]=[key,d[key][1]]
    for key in sorted(t,reverse=True):
        print(t[key][0],key,t[key][1]) 
F({1 : (1, 2), 2 : (-1, 4), 5 : (-4, 3), 4 : (2, 3)})
F({-8 : (4, 2), 6 : (-3, 4), 7 : (2, 1), 5 : (9, -10)})
# similarly it can be done for ascending y we just have to make reverse false and change the position of key in the print.
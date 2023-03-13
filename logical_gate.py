def and_gate(w1,w2,theta,x1,x2):
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    else:
        return 1

def or_gate(w1,w2,theta):
    tmp = x1*w1 + x2*w2
    if tmp < theta:
        return 0
    else:
        return 1

and_value = and_gate(1,1,1,0,0)
print(and_value)
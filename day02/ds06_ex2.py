# 함수 선언 부분

def printPoly(t_x, p_x) :
    polyStr = 'P(x) = '

    for i in range(len(p_x)):
        term = t_x[i] # 항의 차수
        coef = p_x[i] # 계수

        if(coef >=  0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "

    return printPoly

def calcPoly(xVal, t_x, p_x) :
    retValue = 0

    for i in range(len(px)) :
        term = t_x[i] # 항의 차수
        coef = p_x[i]
        retValue += coef * xValue ** term

    re
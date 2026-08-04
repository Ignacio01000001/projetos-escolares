import turtle as t
print("Digite a figura que quer (quadrado/circulo/retangulo)")
forma=str(input())
print("Digite a cor que quer em inglês(ex: red, blue, black)")
cor=str(input())
if forma=="quadrado":
    print("Digite o tamanho em Unidades de Comprimento (UC)")
    print("(Recomendavél que o valor inserido seja >100)")
    front = int(input())
    def quadrado(cor, veloc, front, direita):
        for angulo in range(0, 100, 15):
            t.Turtle()
            t.color(cor)
            t.speed(veloc)
            t.forward(front)
            t.right(direita)
    t.reset()
    t.shape("turtle")
    quadrado(cor,2,front,90)
    t.done()
elif forma=="circulo":
    def circulo(cor,x,y,veloc,raio):
        for angulo in range (0,1,1):
            t.goto(x,y)
            t.color(cor)
            t.speed(veloc)
            t.seth(angulo)
            t.circle(raio)
    t.reset()
    t.shape("turtle")
    circulo(cor,0,0,100,100)
    t.done()
else:
    print("Algum dado inserido não está correto")

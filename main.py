from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index1.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    mayedad = 18
    mayyedad = 30
    resultado = ''
    desc = 0.25
    desc2 = 0.30
    precio = 9000

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantpin = int(request.form['cantpin'])

        total = cantpin * precio
        desctotal = total * desc
        totalpaga = total - desctotal
        desctotall = total * desc2
        totalpagaa = total - desctotall
        descu = desc * 100
        descuu = desc2 * 100

        if mayedad <= edad <= mayyedad:
            resultado = f'Hola {nombre}, tu edad es {edad}. Has comprado {cantpin} tarro(s) de pintura. Por tu mayoría de edad tienes un descuento del {descu}%.' \
                         f' Precio normal del producto es ${total}, el descuento que tienes es ${desctotal} y el total de tu compra es ${totalpaga}.'
        elif edad > mayyedad:
            resultado = f'Hola {nombre}, tu edad es {edad}. Has comprado {cantpin} tarro(s) de pintura. Por tu mayoría de edad tienes un descuento del {descuu}%.' \
                         f' Precio normal del producto es ${total}, el descuento que tienes es ${desctotall} y el total de tu compra es ${totalpagaa}.'
        else:
            resultado = f'Hola {nombre}, tu edad es {edad}. Has comprado {cantpin} tarro(s) de pintura. Por tu edad no cuentas con un descuento. Precio normal del producto es ${total} y el total de tu compra es ${total}.'

    return render_template('ejercicio1.html', resultado=resultado)



@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():

    usuarios = {"juan": "admin", "pepe": "user"}
    mensaje = ""

    if request.method == 'POST':

        usuario = request.form.get('usuario')
        contraseña = request.form.get('contraseña')

        if usuario in usuarios and contraseña == usuarios[usuario]:
            if usuario == "juan":
                mensaje = "Bienvenido administrador juan"
            elif usuario == "pepe":
                mensaje = "Bienvenido usuario pepe"
            else:
                mensaje = "Bienvenido {}".format(usuario)
        else:
            mensaje = "Credenciales incorrectas"

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
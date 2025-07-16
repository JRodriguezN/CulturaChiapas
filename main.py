# main.py
from flask import Flask, render_template
from controller.eventosController import eventos_bp

app = Flask(__name__)
app.register_blueprint(eventos_bp)



# Ruta principal "/"
@app.route('/')
def inicio():
    estados_info = {
        'chiapas': {
            'nombre': 'Chiapas',
            'capital': 'Tuxtla Gutiérrez',
            'descripcion': 'Hogar de impresionantes ruinas mayas, el Cañón del Sumidero y las comunidades indígenas tzotziles y tzeltales con sus coloridas tradiciones textiles.',
            'poblacion': '5.5 millones',
            'clima': 'Tropical',
            'etiqueta': ['Palenque', 'San Cristóbal', 'Textiles'],
            'region': 'Sur',
            'color': 'orange'
        },
        'jalisco': {
            'nombre': 'Jalisco',
            'capital': 'Guadalajara',
            'descripcion': 'Tierra del tequila, mariachi y charrería. Guadalajara, su capital, es conocida como la Perla de Occidente y es cuna de muchas tradiciones mexicanas.',
            'poblacion': '8.3 millones',
            'clima': 'Templado',
            'etiqueta': ['Tequila', 'Mariachi', 'Charrería'],
            'region': 'Occidente',
            'color': 'gray'
        }
    }

    return render_template('index.html', estados=estados_info)

# Ruta individual de Chiapas
@app.route('/chiapas')
def chiapas():
    return render_template('chiapas.html')

if __name__ == "__main__":
    app.run(debug=True)

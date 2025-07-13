from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('index.html', person=name)


@app.route("/estados")
def estados():
    estados_info={
        'chiapas':{
            'nombre':'Chiapas',
            'capital': 'Tuxtla Gutiérrez',
            'descripcion': 'Hogar de impresionantes ruinas mayas, el Cañón del Sumidero y las comunidades indígenas tzotziles y tzeltales con sus coloridas tradiciones textiles.',
            'poblacion':'5.5 millones',
            'clima':'Tropical',
            'etiqueta':['Palenque', 'San cristobal','Textiles'],
            'region':'Sur',
            'atracciones': ['Palenque', 'San Cristóbal de las Casas', 'Cañón del Sumidero', 'Cascadas de Agua Azul'],
            'gastronomia': ['Cochito', 'Tamales de chipilín', 'Pozol', 'Tascalate'],
            'color': 'gold-accent'
        },
        'Jalisco':{
            'nombre':'Jalisco',
            'capital': 'Guadalajara',
            'descripcion': 'Tierra del tequila, mariachi y charrería. Guadalajara, su capital, es conocida como la Perla de Occidente y es cuna de muchas tradiciones mexicanas.',
            'poblacion':'5.5 millones',
            'clima':'Tropical',
            'etiqueta':['Palenque', 'San cristobal','Textiles'],
            'region':'Sur',
            'atracciones': ['Palenque', 'San Cristóbal de las Casas', 'Cañón del Sumidero', 'Cascadas de Agua Azul'],
            'gastronomia': ['Cochito', 'Tamales de chipilín', 'Pozol', 'Tascalate'],
            'color': 'gold-accent'
        }
    }

    return render_template('index.html',estados=estados_info)

@app.route('/chiapas')
def chiapas():
    return render_template('chiapas.html')


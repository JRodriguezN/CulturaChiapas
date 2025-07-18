# main.py
from flask import Flask, render_template
import requests
from controller.eventosController import eventos_bp
from controller.recetasController import recetas_api


app = Flask(__name__)
app.register_blueprint(eventos_bp)
app.register_blueprint(recetas_api)

# Diccionario global de estados
estados_info = {
    'chiapas':{
        'nombre':'Chiapas',
        'capital': 'Tuxtla Gutiérrez',
        'descripcion': 'Hogar de impresionantes ruinas mayas, el Cañón del Sumidero y las comunidades indígenas tzotziles y tzeltales con sus coloridas tradiciones textiles.',
        'poblacion':'5.5 millones',
        'clima':'Tropical',
        'etiqueta':['Palenque', 'San Cristóbal','Textiles'],
        'region':'Sur',
        'atracciones': ['Palenque', 'San Cristóbal de las Casas', 'Cañón del Sumidero', 'Cascadas de Agua Azul'],
        'gastronomia': ['Cochito', 'Tamales de chipilín', 'Pozol', 'Tascalate'],
        'color': '#8B4513',
        'color_light': '#D2691E',
        'imagen': 'https://static.wixstatic.com/media/fd3de2_bb0edc60f6d946bda23a3a94625f2595~mv2.jpg/v1/fill/w_1000,h_608,al_c,q_85,usm_0.66_1.00_0.01/fd3de2_bb0edc60f6d946bda23a3a94625f2595~mv2.jpg'
    },
    'oaxaca':{
        'nombre':'Oaxaca',
        'capital': 'Oaxaca de Juárez',
        'descripcion': 'Famoso por su rica gastronomía, mezcal, y las celebraciones del Día de Muertos. Cuna de la cultura zapoteca y mixteca con su impresionante sitio arqueológico de Monte Albán.',
        'poblacion':'4.1 millones',
        'clima':'Templado',
        'etiqueta':['Mezcal', 'Alebrijes', 'Mole'],
        'region':'Sur',
        'atracciones': ['Monte Albán', 'Hierve el Agua', 'Mercado Benito Juárez', 'Templo de Santo Domingo'],
        'gastronomia': ['Mole Negro', 'Tlayudas', 'Chapulines', 'Mezcal'],
        'color': '#D4AF37',
        'color_light': '#FFD700',
        'imagen': 'https://one.cdnmega.com/images/viajes/covers/40316-oaxaca-clasico-1024x575_667db28d0a5d4.webp'
    },
    'jalisco':{
        'nombre':'Jalisco',
        'capital': 'Guadalajara',
        'descripcion': 'Tierra del tequila, mariachi y charrería. Guadalajara, su capital, es conocida como la Perla de Occidente y es cuna de muchas tradiciones mexicanas.',
        'poblacion':'8.3 millones',
        'clima':'Templado',
        'etiqueta':['Tequila', 'Mariachi', 'Charrería'],
        'region':'Occidente',
        'atracciones': ['Tequila', 'Lago de Chapala', 'Tlaquepaque', 'Zapopan'],
        'gastronomia': ['Tequila', 'Birria', 'Tortas Ahogadas', 'Carne en su Jugo'],
        'color': '#C0C0C0',
        'color_light': '#E5E4E2',
        'imagen': 'https://media.istockphoto.com/id/1313685202/es/foto/catedral-de-guadalajara-al-anochecer-en-el-centro-de-guadalajara-jalisco-m%C3%A9xico.jpg?s=612x612&w=0&k=20&c=5Etw-uEtYKX49pDT7VUAsgrzdn573eBjAVp40mraEu0='
    },
    'yucatan':{
        'nombre':'Yucatán',
        'capital': 'Mérida',
        'descripcion': 'Tierra de los mayas, con impresionantes cenotes, Chichén Itzá y una rica cultura gastronómica que combina tradiciones mayas y españolas.',
        'poblacion':'2.3 millones',
        'clima':'Tropical',
        'etiqueta':['Chichén Itzá', 'Cenotes', 'Cochinita'],
        'region':'Sureste',
        'atracciones': ['Chichén Itzá', 'Cenotes', 'Uxmal', 'Mérida Colonial'],
        'gastronomia': ['Cochinita Pibil', 'Sopa de Lima', 'Queso Relleno', 'Poc Chuc'],
        'color': '#FF6B35',
        'color_light': '#FF8C42',
        'imagen': 'https://upload.wikimedia.org/wikipedia/commons/7/7e/Yucatan_collage.png'
    },
    'puebla':{
        'nombre':'Puebla',
        'capital': 'Puebla de Zaragoza',
        'descripcion': 'Cuna del mole poblano y la talavera, con una rica historia colonial y arquitectura barroca que la hace Patrimonio de la Humanidad.',
        'poblacion':'6.5 millones',
        'clima':'Templado',
        'etiqueta':['Mole Poblano', 'Talavera', 'Chiles en Nogada'],
        'region':'Centro',
        'atracciones': ['Catedral de Puebla', 'Talavera', 'Cholula', 'Amparo'],
        'gastronomia': ['Mole Poblano', 'Chiles en Nogada', 'Cemitas', 'Chalupas'],
        'color': '#4A90E2',
        'color_light': '#6BA5E8',
        'imagen': 'https://upload.wikimedia.org/wikipedia/commons/1/1e/Puebla_collage.png'
    },
    'michoacan':{
        'nombre':'Michoacán',
        'capital': 'Morelia',
        'descripcion': 'Tierra de la mariposa monarca, el Día de Muertos y una rica tradición artesanal. Morelia, su capital, es Patrimonio de la Humanidad.',
        'poblacion':'4.7 millones',
        'clima':'Templado',
        'etiqueta':['Mariposa Monarca', 'Día de Muertos', 'Carnitas'],
        'region':'Occidente',
        'atracciones': ['Mariposa Monarca', 'Morelia Colonial', 'Pátzcuaro', 'Lago de Pátzcuaro'],
        'gastronomia': ['Carnitas', 'Uchepos', 'Corundas', 'Enchiladas Placeras'],
        'color': '#FFD700',
        'color_light': '#FFE55C',
        'imagen': 'https://upload.wikimedia.org/wikipedia/commons/2/2d/Michoacan_collage.png'
    },
    'guerrero':{
        'nombre':'Guerrero',
        'capital': 'Chilpancingo',
        'descripcion': 'Tierra de playas paradisíacas como Acapulco, Ixtapa y Zihuatanejo, con una rica cultura indígena y tradiciones ancestrales.',
        'poblacion':'3.5 millones',
        'clima':'Tropical',
        'etiqueta':['Acapulco', 'Taxco', 'Plata'],
        'region':'Sur',
        'atracciones': ['Acapulco', 'Taxco', 'Ixtapa', 'Zihuatanejo'],
        'gastronomia': ['Pozole Verde', 'Tinga', 'Chilate', 'Tamales de Iguana'],
        'color': '#32CD32',
        'color_light': '#90EE90',
        'imagen': 'https://upload.wikimedia.org/wikipedia/commons/5/5e/Guerrero_collage.png'
    },
    'nuevo_leon':{
        'nombre':'Nuevo León',
        'capital': 'Monterrey',
        'descripcion': 'Estado industrial y moderno, hogar de las majestuosas montañas de la Sierra Madre Oriental y una gastronomía única con influencias norteñas.',
        'poblacion':'5.8 millones',
        'clima':'Seco',
        'etiqueta':['Monterrey', 'Carne Asada', 'Sierra'],
        'region':'Norte',
        'atracciones': ['Chipinque', 'Cola de Caballo', 'Museo de Historia Mexicana', 'Macroplaza'],
        'gastronomia': ['Carne Asada', 'Cabrito', 'Machacado', 'Queso Asadero'],
        'color': '#8B0000',
        'color_light': '#DC143C',
        'imagen': 'https://upload.wikimedia.org/wikipedia/commons/7/7e/NuevoLeon_collage.png'
    }
}

# Ruta principal "/"
@app.route('/')
def index():
    return render_template('index.html', estados=estados_info)



@app.route('/estado/<nombre_estado>')
def estado_detalle(nombre_estado):
    estado = estados_info.get(nombre_estado)
    if not estado:
        return "Estado no encontrado", 404
    return render_template('estado_info.html', estado=estado)

# Ruta individual de Chiapas
@app.route('/chiapas')
def chiapas():
    return render_template('chiapas.html')

if __name__ == "__main__":
    app.run(debug=True)

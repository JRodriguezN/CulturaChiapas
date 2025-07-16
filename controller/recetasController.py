from flask import Blueprint, jsonify

recetas_api = Blueprint('recetas_api', __name__)

RECETAS = {
    'chiapas': [
        {
            'nombre': 'Tamales de Chipilín',
            'descripcion': 'Tamales tradicionales rellenos de chipilín, una hierba local que le da un sabor único y característico de la región.',
            'ingredientes': [
                '2 tazas de masa de maíz',
                '1 manojo de chipilín fresco',
                '1/2 taza de manteca de cerdo',
                'Hojas de plátano para envolver',
                'Sal al gusto'
            ],
            'etiquetas': ['Chipilín', 'Maíz', 'Tradicional'],
            'icono': '🌽',
            'procedimiento': [
                'Lavar y picar finamente el chipilín, reservar.',
                'Batir la masa con la manteca hasta que esté esponjosa.',
                'Incorporar el chipilín picado y la sal, mezclar bien.',
                'Formar bolitas de masa y envolver en hojas de plátano.',
                'Cocinar al vapor por 45-60 minutos hasta que estén firmes.'
            ],
            'nutricion': {
                'tiempo': '1 hora 30 min',
                'porciones': '8-10 tamales',
                'dificultad': 'Media',
                'origen': 'Chiapas'
            }
        },
        {
            'nombre': 'Chocolate Artesanal',
            'descripcion': 'Chocolate tradicional preparado con cacao local, canela y azúcar, servido caliente o frío según la tradición.',
            'ingredientes': [
                'Cacao',
                'Canela',
                'Azúcar',
                'Leche o agua'
            ],
            'etiquetas': ['Cacao', 'Canela', 'Artesanal'],
            'icono': '🍫',
            'procedimiento': [
                'Moler el cacao y la canela.',
                'Mezclar con azúcar.',
                'Disolver en leche o agua caliente y batir hasta espumar.'
            ],
            'nutricion': {
                'tiempo': '20 min',
                'porciones': '4 tazas',
                'dificultad': 'Fácil',
                'origen': 'Chiapas'
            }
        },
        {
            'nombre': 'Pozol Blanco',
            'descripcion': 'Bebida tradicional de maíz fermentado, refrescante y nutritiva, perfecta para el clima cálido de Chiapas.',
            'ingredientes': [
                'Maíz',
                'Agua',
                'Sal'
            ],
            'etiquetas': ['Maíz', 'Fermentado', 'Refrescante'],
            'icono': '🥘',
            'procedimiento': [
                'Cocer el maíz y molerlo.',
                'Fermentar la masa en agua.',
                'Servir frío y endulzar al gusto.'
            ],
            'nutricion': {
                'tiempo': '12 horas (fermentación)',
                'porciones': '6 vasos',
                'dificultad': 'Fácil',
                'origen': 'Chiapas'
            }
        },
    ],
    'oaxaca': [
        {
            'nombre': 'Mole Negro',
            'descripcion': 'El mole negro es uno de los platillos más emblemáticos de Oaxaca, hecho con chiles, chocolate y especias.',
            'ingredientes': ['Chiles', 'Chocolate', 'Especias', 'Pollo'],
            'etiquetas': ['Mole', 'Chocolate', 'Tradicional'],
            'icono': '🍗',
            'procedimiento': [
                'Tostar los chiles y especias.',
                'Moler junto con chocolate.',
                'Cocinar con pollo hasta espesar.'
            ],
            'nutricion': {
                'tiempo': '2 horas',
                'porciones': '6',
                'dificultad': 'Alta',
                'origen': 'Oaxaca'
            }
        },
        {
            'nombre': 'Tlayudas',
            'descripcion': 'Tortilla grande y crujiente cubierta de frijoles, carne, queso y vegetales.',
            'ingredientes': ['Tortilla', 'Frijoles', 'Queso', 'Carne', 'Vegetales'],
            'etiquetas': ['Tlayuda', 'Frijoles', 'Queso'],
            'icono': '🌮',
            'procedimiento': [
                'Untar frijoles sobre la tlayuda.',
                'Agregar carne, queso y vegetales.',
                'Hornear o asar hasta crujiente.'
            ],
            'nutricion': {
                'tiempo': '30 min',
                'porciones': '4',
                'dificultad': 'Fácil',
                'origen': 'Oaxaca'
            }
        },
    ],
    'jalisco': [
        {
            'nombre': 'Birria',
            'descripcion': 'Estofado de carne de res o chivo, cocinado con chiles y especias.',
            'ingredientes': ['Carne', 'Chiles', 'Especias'],
            'etiquetas': ['Birria', 'Carne', 'Picante'],
            'icono': '🍲',
            'procedimiento': [
                'Marinar la carne con chiles y especias.',
                'Cocinar a fuego lento hasta que esté suave.',
                'Servir con tortillas y salsa.'
            ],
            'nutricion': {
                'tiempo': '3 horas',
                'porciones': '8',
                'dificultad': 'Media',
                'origen': 'Jalisco'
            }
        },
        {
            'nombre': 'Tortas Ahogadas',
            'descripcion': 'Bollo de pan relleno de carnitas y bañado en salsa picante.',
            'ingredientes': ['Pan', 'Carnitas', 'Salsa picante'],
            'etiquetas': ['Torta', 'Picante', 'Carnitas'],
            'icono': '🥪',
            'procedimiento': [
                'Rellenar el pan con carnitas.',
                'Bañar en salsa picante.',
                'Servir inmediatamente.'
            ],
            'nutricion': {
                'tiempo': '45 min',
                'porciones': '4',
                'dificultad': 'Fácil',
                'origen': 'Jalisco'
            }
        },
    ],
    # Puedes agregar más estados y recetas aquí...
}

@recetas_api.route('/api/recetas/<estado>')
def get_recetas_estado(estado):
    recetas = RECETAS.get(estado.lower(), [])
    return jsonify({'recetas': recetas})

from flask import Blueprint, request, render_template

eventos_bp = Blueprint('eventos', __name__, url_prefix='/eventos')

# Datos ejemplo
eventos_data = [
    {"nombre": "Festival de Música Rock", "categoria": "musica", "ubicacion": "cdmx", "fecha": "2025-08-01", "descripcion": "Evento de música rock en CDMX.", "imagen": "static/img/feria_san_marcos.jpg"},
    {"nombre": "Feria de Arte Contemporáneo", "categoria": "arte", "ubicacion": "guadalajara", "fecha": "2025-09-15", "descripcion": "Exposición de arte contemporáneo en Guadalajara.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.56.54 PM.jpg"},
    {"nombre": "Feria Gastronómica Oaxaca", "categoria": "gastronomia", "ubicacion": "oaxaca", "fecha": "2025-07-10", "descripcion": "Descubre los sabores de Oaxaca.", "imagen": "/static/img/gastronomia.jpg"},
    {"nombre": "Concierto Jazz Veracruz", "categoria": "musica", "ubicacion": "veracruz", "fecha": "2025-06-20", "descripcion": "Jazz en vivo en Veracruz.", "imagen": "/static/img/jazz.jpg"},
    {"nombre": "Exposición Fotográfica Monterrey", "categoria": "arte", "ubicacion": "monterrey", "fecha": "2025-10-05", "descripcion": "Fotografía contemporánea.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.56.54 PM.jpg"},
    {"nombre": "Festival del Taco CDMX", "categoria": "gastronomia", "ubicacion": "cdmx", "fecha": "2025-09-12", "descripcion": "Celebración de tacos mexicanos.", "imagen": "/static/img/taco.jpg"},
    {"nombre": "Maratón de Guadalajara", "categoria": "deporte", "ubicacion": "guadalajara", "fecha": "2025-11-02", "descripcion": "Carrera anual en Guadalajara.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.56.54 PM.jpg"},
    {"nombre": "Festival de Cine Mexicano", "categoria": "cine", "ubicacion": "cdmx", "fecha": "2025-07-25", "descripcion": "Presentación de películas mexicanas.", "imagen": "/static/img/cine.jpg"},
    {"nombre": "Feria Artesanal Chiapas", "categoria": "arte", "ubicacion": "chiapas", "fecha": "2025-08-15", "descripcion": "Artesanías tradicionales.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.57.00 PM.jpg"},
    {"nombre": "Festival de Salsa Veracruz", "categoria": "musica", "ubicacion": "veracruz", "fecha": "2025-10-20", "descripcion": "Baile y música salsa.", "imagen": "/static/img/salsa.jpg"},
    {"nombre": "Feria del Queso Oaxaca", "categoria": "gastronomia", "ubicacion": "oaxaca", "fecha": "2025-09-01", "descripcion": "Quesos artesanales de Oaxaca.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.56.54 PM.jpg"},
    {"nombre": "Expo Tecnología Monterrey", "categoria": "tecnologia", "ubicacion": "monterrey", "fecha": "2025-11-15", "descripcion": "Innovaciones tecnológicas.", "imagen": "/static/img/tecnologia.jpg"},
    {"nombre": "Carnaval de Veracruz", "categoria": "cultura", "ubicacion": "veracruz", "fecha": "2025-02-25", "descripcion": "Fiesta tradicional.", "imagen": "/static/img/carnaval.jpg"},
    {"nombre": "Festival de Danza CDMX", "categoria": "arte", "ubicacion": "cdmx", "fecha": "2025-08-30", "descripcion": "Presentaciones de danza contemporánea.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.57.00 PM.jpg"},
    {"nombre": "Feria del Chocolate Oaxaca", "categoria": "gastronomia", "ubicacion": "oaxaca", "fecha": "2025-10-10", "descripcion": "Degustación de chocolates.", "imagen": "/static/img/chocolate.jpg"},
    {"nombre": "Concierto Pop Guadalajara", "categoria": "musica", "ubicacion": "guadalajara", "fecha": "2025-07-18", "descripcion": "Música pop en vivo.", "imagen": "/static/img/pop.jpg"},
    {"nombre": "Festival de Jazz CDMX", "categoria": "musica", "ubicacion": "cdmx", "fecha": "2025-09-25", "descripcion": "Jazz internacional en la ciudad.", "imagen": "/static/img/jazz_cdmx.jpg"},
    {"nombre": "Exposición Pintura Monterrey", "categoria": "arte", "ubicacion": "monterrey", "fecha": "2025-08-12", "descripcion": "Pintura contemporánea.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.57.00 PM.jpg"},
    {"nombre": "Feria del Mole Puebla", "categoria": "gastronomia", "ubicacion": "puebla", "fecha": "2025-09-30", "descripcion": "Mole tradicional de Puebla.", "imagen": "/static/img/mole.jpg"},
    {"nombre": "Festival de Rock Guadalajara", "categoria": "musica", "ubicacion": "guadalajara", "fecha": "2025-10-22", "descripcion": "Rock en vivo.", "imagen": "/static/img/rock_gdl.jpg"},
    {"nombre": "Exposición de Escultura CDMX", "categoria": "arte", "ubicacion": "cdmx", "fecha": "2025-11-05", "descripcion": "Esculturas modernas.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.57.00 PM.jpg"},
    {"nombre": "Feria de Café Veracruz", "categoria": "gastronomia", "ubicacion": "veracruz", "fecha": "2025-08-07", "descripcion": "Café artesanal de Veracruz.", "imagen": "/static/img/cafe.jpg"},
    {"nombre": "Festival de Teatro Monterrey", "categoria": "arte", "ubicacion": "monterrey", "fecha": "2025-07-28", "descripcion": "Obras teatrales.", "imagen": "/static/img/teatro.jpg"},
    {"nombre": "Feria del Pulque CDMX", "categoria": "gastronomia", "ubicacion": "cdmx", "fecha": "2025-08-19", "descripcion": "Bebida tradicional mexicana.", "imagen": "/static/img/pulque.jpg"},
    {"nombre": "Concierto de Banda Guadalajara", "categoria": "musica", "ubicacion": "guadalajara", "fecha": "2025-09-14", "descripcion": "Música de banda en vivo.", "imagen": "/static/img/banda.jpg"},
    {"nombre": "Festival de Literatura CDMX", "categoria": "cultura", "ubicacion": "cdmx", "fecha": "2025-10-02", "descripcion": "Presentación de libros y autores.", "imagen": "/static/img/literatura.jpg"},
    {"nombre": "Feria del Mezcal Oaxaca", "categoria": "gastronomia", "ubicacion": "oaxaca", "fecha": "2025-10-18", "descripcion": "Degustación de mezcal.", "imagen": "/static/img/mezcal.jpg"},
    {"nombre": "Festival de Música Clásica Puebla", "categoria": "musica", "ubicacion": "puebla", "fecha": "2025-11-11", "descripcion": "Conciertos de música clásica.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.57.00 PM.jpg"},
    {"nombre": "Expo de Diseño Monterrey", "categoria": "arte", "ubicacion": "monterrey", "fecha": "2025-07-15", "descripcion": "Diseño gráfico y moda.", "imagen": "/static/img/diseno.jpg"},
    {"nombre": "Feria del Pan Oaxaca", "categoria": "gastronomia", "ubicacion": "oaxaca", "fecha": "2025-09-22", "descripcion": "Panadería tradicional.", "imagen": "/static/img/pan.jpg"},
    {"nombre": "Festival de Hip-Hop CDMX", "categoria": "musica", "ubicacion": "cdmx", "fecha": "2025-08-26", "descripcion": "Hip-Hop y rap.", "imagen": "/static/img/hiphop.jpg"},
    {"nombre": "Feria del Vino Baja California", "categoria": "gastronomia", "ubicacion": "baja california", "fecha": "2025-10-28", "descripcion": "Vinos mexicanos.", "imagen": "/static/img/vino.jpg"},
    {"nombre": "Festival de Cine Monterrey", "categoria": "cine", "ubicacion": "monterrey", "fecha": "2025-11-20", "descripcion": "Presentación de películas.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.57.01 PM (1).jpg"},
    {"nombre": "Concierto de Mariachi Guadalajara", "categoria": "musica", "ubicacion": "guadalajara", "fecha": "2025-07-20", "descripcion": "Mariachi tradicional.", "imagen": "/static/img/mariachi.jpg"},
    {"nombre": "Feria de Libros CDMX", "categoria": "cultura", "ubicacion": "cdmx", "fecha": "2025-09-05", "descripcion": "Venta y exposición de libros.", "imagen": "/static/img/libros.jpg"},
    {"nombre": "Festival de Danza Folklórica Oaxaca", "categoria": "arte", "ubicacion": "oaxaca", "fecha": "2025-08-17", "descripcion": "Danza tradicional.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.57.01 PM (1).jpg"},
    {"nombre": "Feria de Cerámica Puebla", "categoria": "arte", "ubicacion": "puebla", "fecha": "2025-09-29", "descripcion": "Cerámica artesanal.", "imagen": "/static/img/ceramica.jpg"},
    {"nombre": "Festival de Música Electrónica CDMX", "categoria": "musica", "ubicacion": "cdmx", "fecha": "2025-10-10", "descripcion": "Electrónica y DJ.", "imagen": "/static/img/electronica.jpg"},
    {"nombre": "Feria del Queso y Vino Guadalajara", "categoria": "gastronomia", "ubicacion": "guadalajara", "fecha": "2025-11-18", "descripcion": "Quesos y vinos regionales.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.57.05 PM.jpg"},
    {"nombre": "Exposición de Fotografía Oaxaca", "categoria": "arte", "ubicacion": "oaxaca", "fecha": "2025-07-22", "descripcion": "Fotografía artística.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.57.01 PM (1).jpg"},
    {"nombre": "Festival de Teatro CDMX", "categoria": "arte", "ubicacion": "cdmx", "fecha": "2025-08-14", "descripcion": "Obras teatrales diversas.", "imagen": "/static/img/teatro_cdmx.jpg"},
    {"nombre": "Feria del Chocolate Guadalajara", "categoria": "gastronomia", "ubicacion": "guadalajara", "fecha": "2025-09-19", "descripcion": "Chocolate artesanal.", "imagen": "/static/img/chocolate_gdl.jpg"},
    {"nombre": "Concierto de Reggae Veracruz", "categoria": "musica", "ubicacion": "veracruz", "fecha": "2025-10-23", "descripcion": "Reggae y música tropical.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.57.00 PM.jpg"},
    {"nombre": "Feria de Artesanías CDMX", "categoria": "arte", "ubicacion": "cdmx", "fecha": "2025-11-07", "descripcion": "Artesanía tradicional mexicana.", "imagen": "/static/img/artesanias_cdmx.jpg"},
    {"nombre": "Festival Gastronómico Puebla", "categoria": "gastronomia", "ubicacion": "puebla", "fecha": "2025-08-18", "descripcion": "Sabores de Puebla.", "imagen": "/static/img/gastronomia_puebla.jpg"},
    {"nombre": "Concierto de Música Clásica Monterrey", "categoria": "musica", "ubicacion": "monterrey", "fecha": "2025-09-26", "descripcion": "Orquesta sinfónica.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.57.05 PM.jpg"},
    {"nombre": "Feria del Mezcal CDMX", "categoria": "gastronomia", "ubicacion": "cdmx", "fecha": "2025-10-13", "descripcion": "Degustación de mezcal.", "imagen": "/static/img/mezcal_cdmx.jpg"},
    {"nombre": "Festival de Literatura Guadalajara", "categoria": "cultura", "ubicacion": "guadalajara", "fecha": "2025-11-21", "descripcion": "Presentación de autores.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.57.05 PM.jpg"},
    {"nombre": "Feria del Pan Monterrey", "categoria": "gastronomia", "ubicacion": "monterrey", "fecha": "2025-07-30", "descripcion": "Panadería artesanal.", "imagen": "/static/img/pan_mty.jpg"},
    {"nombre": "Festival de Salsa CDMX", "categoria": "musica", "ubicacion": "cdmx", "fecha": "2025-08-27", "descripcion": "Baile y música salsa.", "imagen": "static/img/WhatsApp Image 2025-07-14 at 6.57.00 PM.jpg"},
    {"nombre": "Feria de Vino Baja California", "categoria": "gastronomia", "ubicacion": "baja california", "fecha": "2025-10-29", "descripcion": "Vinos mexicanos de calidad.", "imagen": "/static/img/vino_bc.jpg"},
]
@eventos_bp.route('/')
def mostrar_eventos():
    q = request.args.get('q', '').lower()
    categoria = request.args.get('categoria', '').lower()
    ubicacion = request.args.get('ubicacion', '').lower()

    def evento_coincide(evento):
        texto_valido = (q in evento['nombre'].lower() or q in evento['descripcion'].lower() or q in evento['ubicacion'].lower()) if q else True
        categoria_valida = (evento['categoria'] == categoria) if categoria else True
        ubicacion_valida = (evento['ubicacion'] == ubicacion) if ubicacion else True
        return texto_valido and categoria_valida and ubicacion_valida

    eventos_filtrados = list(filter(evento_coincide, eventos_data))

    # Generar listas únicas para sugerencias
    nombres = sorted(list({e['nombre'] for e in eventos_data}))
    ubicaciones = sorted(list({e['ubicacion'] for e in eventos_data}))
    categorias = sorted(list({e['categoria'] for e in eventos_data}))

    return render_template('eventos.html',
                           eventos=eventos_filtrados,
                           nombres=nombres,
                           ubicaciones=ubicaciones,
                           categorias=categorias)
import os

tours_data = [
    {
        "filename": "tour-valle-sagrado-vip.html",
        "title": "Tour Valle Sagrado VIP",
        "subtitle": "Historia, Tradición y Paisajes Majestuosos",
        "price": "$69",
        "image": "valle_sagrado.png",
        "resumen": '''<p>Nuestro <strong>Tour Valle Sagrado VIP</strong> te lleva en un recorrido exclusivo por el corazón del imperio Inca. A diferencia de los tours tradicionales, visitaremos los fascinantes andenes de Moray y las impresionantes salineras de Maras, además de los imponentes complejos arqueológicos de Pisaq y Ollantaytambo.</p>
        <p>Disfrutarás de un exquisito almuerzo buffet con lo mejor de la gastronomía peruana en Urubamba. Este viaje es ideal para quienes buscan conectar con la cultura andina de una manera más profunda y cómoda.</p>''',
        "itinerario": '''
        <div class="itinerary-day fade-up">
            <h3 class="day-title" style="color:var(--color-primary);">Día Único: Exploración del Valle Sagrado</h3>
            <div class="day-content">
                <p><strong>07:00 AM:</strong> Recojo de tu hotel en Cusco y viaje en transporte turístico hacia el mirador de Taray para apreciar la inmensidad del Valle Sagrado.</p>
                <p><strong>09:00 AM:</strong> Visita guiada por el complejo arqueológico de <strong>Pisaq</strong>, famoso por su cementerio Inca y terrazas agrícolas. Luego exploraremos su colorido mercado artesanal.</p>
                <p><strong>12:00 PM:</strong> Almuerzo buffet turístico en <strong>Urubamba</strong>, donde degustarás platillos típicos hechos con ingredientes locales.</p>
                <p><strong>14:00 PM:</strong> Recorrido por la majestuosa fortaleza de <strong>Ollantaytambo</strong>, el último pueblo inca viviente.</p>
                <p><strong>16:00 PM:</strong> Continuaremos hacia el centro agrícola de <strong>Moray</strong> y finalizaremos en las deslumbrantes <strong>Salineras de Maras</strong> antes de retornar a Cusco (llegada aprox. 19:00 hrs).</p>
            </div>
        </div>''',
        "precios": '''
        <ul style="line-height: 1.8;">
            <li><strong>Precio por Adulto:</strong> $69.00 USD</li>
            <li><strong>Precio para Estudiantes:</strong> $60.00 USD</li>
        </ul>
        <br>
        <h4>Incluye:</h4>
        <ul>
            <li>Transporte turístico de primera clase.</li>
            <li>Guía profesional bilingüe (Inglés/Español).</li>
            <li>Almuerzo buffet en restaurante campestre.</li>
            <li>Asistencia permanente.</li>
        </ul>
        <br>
        <h4>No Incluye:</h4>
        <ul>
            <li>Boleto Turístico del Cusco (BTC).</li>
            <li>Entrada a Salineras (S/. 10.00).</li>
        </ul>''',
        "recomendaciones": '''
        <ul>
            <li>Llevar el Boleto Turístico del Cusco en físico.</li>
            <li>Vestir en capas (frío por la mañana/noche, calor al mediodía).</li>
            <li>Llevar sombrero, lentes de sol y bloqueador solar.</li>
            <li>Zapatillas cómodas para caminar por los sitios arqueológicos.</li>
            <li>Llevar dinero en efectivo (Soles) para compras en los mercados artesanales o entradas adicionales.</li>
        </ul>'''
    },
    {
        "filename": "tour-montana-7-colores.html",
        "title": "Tour Montaña 7 Colores",
        "subtitle": "Un desafío a más de 5,000 metros de altura",
        "price": "$49",
        "image": "montana_colores.png",
        "resumen": '''<p>Atrévete a conquistar la cima del <strong>Vinicunca</strong>, mundialmente conocida como la Montaña de 7 Colores. Este tour te llevará a través de paisajes alucinantes rodeados de picos nevados y comunidades andinas tradicionales.</p>
        <p>Una caminata exigente pero inmensamente gratificante que culmina con una de las vistas naturales más espectaculares del planeta. Incluye la visita opcional al impresionante Valle Rojo.</p>''',
        "itinerario": '''
        <div class="itinerary-day fade-up">
            <h3 class="day-title" style="color:var(--color-primary);">Día Único: Aventura en el Vinicunca</h3>
            <div class="day-content">
                <p><strong>04:00 AM:</strong> Recojo temprano de tu hotel en Cusco para aprovechar la mañana. Viaje en transporte privado por 2 horas hasta Cusipata.</p>
                <p><strong>06:00 AM:</strong> Parada para disfrutar de un desayuno nutritivo estilo buffet que te dará la energía necesaria para la caminata.</p>
                <p><strong>07:00 AM:</strong> Continuamos el viaje hasta el punto de inicio de la caminata en Fulawasipata (4,600 msnm).</p>
                <p><strong>08:30 AM:</strong> Inicio de la caminata (aprox. 1.5 a 2 horas) rodeados de llamas, alpacas y la vista del majestuoso nevado Ausangate.</p>
                <p><strong>10:30 AM:</strong> Llegada a la <strong>Montaña de 7 Colores (5,020 msnm)</strong>. Tiempo libre para fotografías y explicaciones del guía. (Opción de visitar el Valle Rojo).</p>
                <p><strong>12:00 PM:</strong> Retorno al campamento y traslado a Cusipata para el almuerzo buffet.</p>
                <p><strong>17:00 PM:</strong> Llegada aproximada a la ciudad del Cusco.</p>
            </div>
        </div>''',
        "precios": '''
        <ul style="line-height: 1.8;">
            <li><strong>Precio por Adulto:</strong> $49.00 USD</li>
        </ul>
        <br>
        <h4>Incluye:</h4>
        <ul>
            <li>Transporte turístico ida y vuelta.</li>
            <li>Desayuno y Almuerzo buffet.</li>
            <li>Guía profesional especializado en alta montaña.</li>
            <li>Botiquín de primeros auxilios y balón de oxígeno.</li>
            <li>Tickets de ingreso a la Montaña.</li>
        </ul>
        <br>
        <h4>No Incluye:</h4>
        <ul>
            <li>Caballos para el ascenso (se pueden alquilar en el sitio).</li>
            <li>Ingreso al Valle Rojo (Opcional S/. 20.00).</li>
        </ul>''',
        "recomendaciones": '''
        <ul>
            <li><strong>Aclimatación:</strong> Es obligatorio pasar al menos 2 días en Cusco antes de realizar este tour.</li>
            <li>Ropa de abrigo: casaca impermeable, guantes, chalina, gorro de lana.</li>
            <li>Zapatos de trekking con buen agarre.</li>
            <li>Llevar bastones de caminata (recomendado).</li>
            <li>Hojas de coca, caramelos de limón y mucha agua.</li>
        </ul>'''
    },
    {
        "filename": "tour-laguna-humantay.html",
        "title": "Tour Laguna Humantay",
        "subtitle": "La Joya Turquesa al Pie del Nevado Salkantay",
        "price": "$39",
        "image": "valle_sagrado.png",
        "resumen": '''<p>La <strong>Laguna Humantay</strong> es uno de los tesoros naturales más hermosos del Perú. Sus aguas de color turquesa cristalino reflejan el imponente glaciar del mismo nombre, creando un paisaje de ensueño.</p>
        <p>Esta aventura de un día es perfecta para los amantes de la naturaleza y la fotografía, ofreciendo una caminata rodeada de la majestuosidad de la cordillera de Vilcabamba y la energía de los Apus (montañas sagradas).</p>''',
        "itinerario": '''
        <div class="itinerary-day fade-up">
            <h3 class="day-title" style="color:var(--color-primary);">Día Único: Trekking a la Laguna Turquesa</h3>
            <div class="day-content">
                <p><strong>04:30 AM:</strong> Pasaremos por tu hotel para iniciar el viaje rumbo al noroeste de Cusco, pasando por pueblos pintorescos.</p>
                <p><strong>07:00 AM:</strong> Llegada al poblado de Mollepata, donde disfrutaremos de un delicioso y reconfortante desayuno.</p>
                <p><strong>08:30 AM:</strong> Continuamos en carro por un camino de herradura hasta Soraypampa (3,900 msnm), el punto de inicio de nuestra caminata.</p>
                <p><strong>09:30 AM:</strong> Iniciamos el ascenso. La caminata dura aproximadamente 1 hora y 45 minutos. El sendero es empinado pero las vistas del nevado Salkantay te dejarán sin aliento.</p>
                <p><strong>11:15 AM:</strong> ¡Llegada a la <strong>Laguna Humantay (4,200 msnm)</strong>! Tiempo libre para disfrutar del paisaje, tomar fotos y participar en una pequeña ceremonia andina con hojas de coca.</p>
                <p><strong>12:30 PM:</strong> Descenso de regreso a Soraypampa.</p>
                <p><strong>14:00 PM:</strong> Almuerzo buffet en Mollepata.</p>
                <p><strong>18:00 PM:</strong> Retorno a la ciudad del Cusco.</p>
            </div>
        </div>''',
        "precios": '''
        <ul style="line-height: 1.8;">
            <li><strong>Precio por Adulto:</strong> $39.00 USD</li>
        </ul>
        <br>
        <h4>Incluye:</h4>
        <ul>
            <li>Transporte turístico (Ida y Vuelta).</li>
            <li>Guía profesional bilingüe.</li>
            <li>Desayuno y Almuerzo buffet.</li>
            <li>Ticket de ingreso a Humantay.</li>
            <li>Botiquín de primeros auxilios y oxígeno.</li>
        </ul>
        <br>
        <h4>No Incluye:</h4>
        <ul>
            <li>Alquiler de caballo (S/. 90.00 aprox).</li>
            <li>Gastos personales.</li>
        </ul>''',
        "recomendaciones": '''
        <ul>
            <li>Llevar ropa abrigadora y rompevientos (el clima cambia rápidamente).</li>
            <li>Zapatos de trekking cómodos y resistentes al agua.</li>
            <li>Llevar poncho para la lluvia.</li>
            <li>Protector solar y lentes de sol (la radiación es alta).</li>
            <li>Snacks energéticos (chocolates, frutos secos) y agua.</li>
        </ul>'''
    },
    {
        "filename": "tour-machu-picchu-full-day.html",
        "title": "Machu Picchu Full Day",
        "subtitle": "Descubre una de las 7 Maravillas del Mundo",
        "price": "$297",
        "image": "machu_picchu.png",
        "resumen": '''<p>Cumple tu sueño de conocer <strong>Machu Picchu</strong>, la legendaria Ciudad Perdida de los Incas. Este tour de día completo está diseñado meticulosamente para que disfrutes de la maravilla sin preocuparte por la logística.</p>
        <p>Viajaremos en un tren panorámico a través de la exuberante ceja de selva hasta llegar a Aguas Calientes, desde donde ascenderemos para ser testigos de la grandeza arquitectónica y espiritual de este santuario histórico.</p>''',
        "itinerario": '''
        <div class="itinerary-day fade-up">
            <h3 class="day-title" style="color:var(--color-primary);">Día Único: La Magia de Machu Picchu</h3>
            <div class="day-content">
                <p><strong>04:00 AM:</strong> Recojo de tu hotel en Cusco y traslado en bus hacia la estación de tren en Ollantaytambo (aprox. 1 hora y 45 mins).</p>
                <p><strong>06:10 AM:</strong> Abordamos el tren turístico. El viaje dura cerca de 2 horas ofreciendo vistas impresionantes del río Vilcanota y la transición de los andes a la selva.</p>
                <p><strong>08:00 AM:</strong> Llegada al pueblo de Aguas Calientes. Nuestro personal te estará esperando para llevarte a la estación de buses Consettur.</p>
                <p><strong>08:30 AM:</strong> Viaje en bus ecológico por 30 minutos (carretera Hiram Bingham) zigzagueando la montaña hasta la entrada de la ciudadela.</p>
                <p><strong>09:30 AM:</strong> ¡Ingreso a <strong>Machu Picchu</strong>! Disfrutarás de un tour guiado de 2 a 3 horas visitando el Templo del Sol, el Intihuatana, la Plaza Principal y los sectores agrícolas/urbanos.</p>
                <p><strong>13:00 PM:</strong> Bus de bajada a Aguas Calientes. Tiempo libre para almorzar en el pueblo y explorar sus callecitas o el mercado artesanal.</p>
                <p><strong>16:22 PM:</strong> Tren de retorno hacia Ollantaytambo.</p>
                <p><strong>18:30 PM:</strong> Bus de retorno desde Ollantaytambo hasta tu hotel en Cusco, llegando alrededor de las 20:30 PM.</p>
            </div>
        </div>''',
        "precios": '''
        <ul style="line-height: 1.8;">
            <li><strong>Adultos (Extranjeros):</strong> $297.00 USD</li>
            <li><strong>Comunidad Andina (Perú, Colombia, Ecuador, Bolivia):</strong> $260.00 USD</li>
            <li><strong>Estudiantes (con carnet universitario válido):</strong> Descuento de $20.00 USD</li>
        </ul>
        <br>
        <h4>Incluye:</h4>
        <ul>
            <li>Traslados Cusco - Ollantaytambo - Cusco.</li>
            <li>Tickets de Tren Turístico (Ida y Vuelta).</li>
            <li>Tickets de Bus Aguas Calientes - Machu Picchu (Ida y Vuelta).</li>
            <li>Ticket de ingreso a Machu Picchu (Circuito principal).</li>
            <li>Guía oficial de turismo experto.</li>
        </ul>
        <br>
        <h4>No Incluye:</h4>
        <ul>
            <li>Alimentación (Almuerzo en Aguas Calientes).</li>
            <li>Ingreso a las montañas Huayna Picchu o Machu Picchu Montaña.</li>
        </ul>''',
        "recomendaciones": '''
        <ul>
            <li><strong>Documentos:</strong> Pasaporte original o DNI obligatorio (el mismo con el que se compró el ticket).</li>
            <li>El clima en Machu Picchu es subtropical (caluroso y húmedo), lleva ropa ligera y transpirable.</li>
            <li>Llevar repelente de mosquitos (muy importante).</li>
            <li>Prohibido llevar mochilas grandes (máximo 20L), drones, palos selfie y paraguas.</li>
            <li>Reserva con al menos 2 meses de anticipación debido al aforo limitado.</li>
        </ul>'''
    }
]

import re

base_dir = r"C:\Users\USER\Documents\musoq-peru-expedition"
template_file = os.path.join(base_dir, "tour-detalle.html")

with open(template_file, 'r', encoding='utf-8') as f:
    template_html = f.read()

for tour in tours_data:
    new_html = template_html
    new_html = new_html.replace('{{TITLE}}', tour['title'])
    new_html = new_html.replace('{{SUBTITLE}}', tour['subtitle'])
    new_html = new_html.replace('{{RESUMEN_HTML}}', tour['resumen'])
    new_html = new_html.replace('{{ITINERARIO_HTML}}', tour['itinerario'])
    new_html = new_html.replace('{{PRECIOS_HTML}}', tour['precios'])
    new_html = new_html.replace('{{RECOMENDACIONES_HTML}}', tour['recomendaciones'])
    new_html = new_html.replace('{{PRICE_TAG}}', tour['price'])
    
    # Update image
    new_html = re.sub(r"url\('images/machu_picchu\.png'\)", f"url('images/{tour['image']}')", new_html)

    filepath = os.path.join(base_dir, tour['filename'])
    with open(filepath, 'w', encoding='utf-8') as fw:
        fw.write(new_html)
    
    print(f"Generado con éxito: {tour['filename']}")

print("Los 4 tours principales han sido generados con texto redactado por experto.")

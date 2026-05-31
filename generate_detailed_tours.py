import os
import re
import unicodedata

# Helper to create slugs for filenames
def slugify(value):
    value = str(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

def txt_to_html(text):
    lines = [p.strip() for p in text.split('\n') if len(p.strip()) > 5]
    if not lines:
        return "<p>Información no disponible actualmente.</p>"
    return "".join(f"<p>{line}</p>" for line in lines)

base_dir = r"C:\Users\USER\Documents\musoq-peru-expedition"
text_file = r"C:\Users\USER\Downloads\prompts_extracted.txt"
template_file = os.path.join(base_dir, "tour-detalle.html")
tours_catalog_file = os.path.join(base_dir, "tours.html")

print("Ejecutando Generador Avanzado de Tours...")

with open(text_file, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

with open(template_file, 'r', encoding='utf-8') as f:
    template_html = f.read()

# Buscamos secciones de tour (separadas por TITULO PRINCIPAL)
sections = text.split("TÍTULO PRINCIPAL")

tours = []
seen_titles = set()

# Lista de imágenes rotativas relacionadas
images = ['valle_sagrado.png', 'machu_picchu.png', 'montana_colores.png']
categories = ['Tours Culturales', 'Tours de Aventura', 'Paquetes Culturales', 'Tours Tradicionales']

for idx, section in enumerate(sections[1:]):
    # Título
    title_match = re.search(r'[:]?\s*[“"\'«]?(.*?)[”"\'»\n]', section)
    if not title_match: continue
    
    title = title_match.group(1).strip()
    if len(title) < 5 or "PROMPT" in title.upper() or "SECCIÓN" in title.upper(): continue
    
    # Evitar duplicados exactos
    if title.lower() in seen_titles: continue
    seen_titles.add(title.lower())
    
    slug = slugify(title)
    if not slug: continue

    # Subtítulo
    subtitle = "Descubre esta increíble experiencia con Musoq Peru Expedition"
    sub_match = re.search(r'SUBTÍTULO[:]?\s*[“"\'«]?(.*?)[”"\'»\n]', section)
    if sub_match:
        subtitle = sub_match.group(1).strip()

    # ---- EXTRACCIÓN AVANZADA DE TABS ----

    # 1. Resumen
    resumen_match = re.search(r'Resumen.*?\n(.*?)(?=Itinerario|Día|Precio|Recomendac|==|$)', section, re.IGNORECASE | re.DOTALL)
    resumen_html = txt_to_html(resumen_match.group(1)) if resumen_match else "<p>Este tour te llevará por los paisajes más impresionantes, diseñado exclusivamente para viajeros que buscan calidad, aventura y conexión cultural.</p>"

    # 2. Itinerario (Día 1, Día 2...)
    days_matches = re.finditer(r'D[ií]a (\d+)[^\n]*\n(.*?)(?=\nD[ií]a \d+|Precios|Recomendaciones|=|$)', section, re.IGNORECASE | re.DOTALL)
    itinerario_html = ""
    for match in days_matches:
        day_num = match.group(1)
        day_text = re.sub(r'(TÍTULO|DESCRIPCIÓN|IMAGENES|DISEÑO)[:]', '', match.group(2), flags=re.IGNORECASE)
        itinerario_html += f'''
        <div class="itinerary-day fade-up">
            <h3 class="day-title" style="color:var(--color-primary);">Día {day_num}</h3>
            <div class="day-content">
                {txt_to_html(day_text)}
            </div>
            <div class="day-gallery">
                <img src="images/{images[idx % 3]}" alt="{title}" class="img-zoom">
                <img src="images/{images[(idx+1) % 3]}" alt="Viaje" class="img-zoom">
            </div>
        </div>
        '''
    if not itinerario_html:
        itinerario_html = f"<div class='itinerary-day'><p>El itinerario detallado se proporcionará al momento de la reserva.</p></div>"

    # 3. Precios
    precios_match = re.search(r'(?i)Precios.*?\n(.*?)(?=Recomendaciones|==|$)', section, re.DOTALL)
    precios_html = txt_to_html(precios_match.group(1)) if precios_match else "<p>Precio base: <strong>Consultar tarifa</strong></p><p>Incluye todos los traslados y guiado profesional.</p>"

    # 4. Recomendaciones
    rec_match = re.search(r'(?i)Recomendaciones.*?\n(.*?)(?===|$)', section, re.DOTALL)
    rec_html = txt_to_html(rec_match.group(1)) if rec_match else "<ul><li>Pasaporte original</li><li>Ropa cómoda y zapatillas de trekking</li><li>Bloqueador solar y sombrero</li></ul>"

    # Construir HTML
    new_html = template_html
    new_html = new_html.replace('{{TITLE}}', title)
    new_html = new_html.replace('{{SUBTITLE}}', subtitle)
    new_html = new_html.replace('{{RESUMEN_HTML}}', resumen_html)
    new_html = new_html.replace('{{ITINERARIO_HTML}}', itinerario_html)
    new_html = new_html.replace('{{PRECIOS_HTML}}', precios_html)
    new_html = new_html.replace('{{RECOMENDACIONES_HTML}}', rec_html)
    new_html = new_html.replace('{{PRICE_TAG}}', "Consultar")
    
    # Asignar imagen animada de fondo alternando entre las 3
    bg_img = images[idx % 3]
    new_html = re.sub(r"url\('images/machu_picchu\.png'\)", f"url('images/{bg_img}')", new_html)

    # Guardar
    filename = f'tour-{slug}.html'
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as fw:
        fw.write(new_html)
    
    tours.append({
        'title': title,
        'subtitle': subtitle[:60] + "...",
        'file': filename,
        'category': categories[idx % len(categories)],
        'image': bg_img
    })

print(f"Extracción Exacta completada: {len(tours)} tours sin duplicados.")

# Actualizar tours.html
with open(tours_catalog_file, 'r', encoding='utf-8') as f:
    tours_html = f.read()

tours_grid_html = ""
for t in tours:
    cat_class = slugify(t.get('category', 'Todos'))
    tours_grid_html += f'''
            <div class="tour-card glass-card fade-up tour-item {cat_class}">
                <div class="card-img-wrapper">
                    <img src="images/{t['image']}" alt="{t['title']}">
                    <div class="card-overlay"></div>
                    <span class="price-tag">Descubrir</span>
                </div>
                <div class="card-content">
                    <p style="font-size: 0.8rem; color: var(--color-primary); font-weight: bold; margin-bottom: 5px;">{t['category'].upper()}</p>
                    <h3 style="color:var(--color-text-dark);">{t['title']}</h3>
                    <p style="color:#555; margin-bottom:15px; font-size:0.9rem;">{t['subtitle']}</p>
                    <a href="{t['file']}" class="btn btn-primary" style="width:100%; padding:10px;">Ver detalles exactos</a>
                </div>
            </div>
    '''

tours_pattern = re.compile(r'(<div class="tours-grid"[^>]*>).*?(?=</div>\s*<br><br>\s*</main>)', re.DOTALL)
new_tours_html = tours_pattern.sub(r'\1\n' + tours_grid_html + '\n', tours_html)

with open(tours_catalog_file, 'w', encoding='utf-8') as fw:
    fw.write(new_tours_html)

print("¡Catálogo actualizado con pestañas de categorías y contenido avanzado!")

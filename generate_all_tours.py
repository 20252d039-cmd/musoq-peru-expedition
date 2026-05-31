import os
import re
import unicodedata

# Helper to create slugs for filenames
def slugify(value):
    value = str(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

# Paths
base_dir = r"C:\Users\USER\Documents\musoq-peru-expedition"
text_file = r"C:\Users\USER\Downloads\prompts_extracted.txt"
template_file = os.path.join(base_dir, "tour-detalle.html")
tours_catalog_file = os.path.join(base_dir, "tours.html")

print("Leyendo el archivo gigante de texto...")
with open(text_file, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Read the template
with open(template_file, 'r', encoding='utf-8') as f:
    template_html = f.read()

# Find all potential tours using TÍTULO PRINCIPAL
# We split the text by "TÍTULO PRINCIPAL"
sections = text.split("TÍTULO PRINCIPAL")

tours = []
for section in sections[1:]: # Skip the first chunk before any title
    # The title usually comes right after, enclosed in quotes or just text until a newline
    title_match = re.search(r'[:]?\s*[“"\'«]?(.*?)[”"\'»\n]', section)
    if not title_match:
        continue
    
    title = title_match.group(1).strip()
    if len(title) < 5 or "PROMPT" in title.upper() or "SECCIÓN" in title.upper():
        continue
        
    slug = slugify(title)
    if not slug:
        continue

    # Try to extract subtitle
    subtitle = ""
    sub_match = re.search(r'SUBTÍTULO[:]?\s*[“"\'«]?(.*?)[”"\'»\n]', section)
    if sub_match:
        subtitle = sub_match.group(1).strip()

    # Extract days (Día 1, Día 2, etc.)
    days_matches = re.finditer(r'D[ií]a (\d+)[^\n]*\n(.*?)(?=\nD[ií]a \d+|=|$)', section, re.IGNORECASE | re.DOTALL)
    
    days_html = ""
    day_count = 0
    for match in days_matches:
        day_num = match.group(1)
        day_text_raw = match.group(2).strip()
        # Clean up the day text
        # Remove extra "TITULO:", "DESCRIPCION:", etc.
        day_text = re.sub(r'(TÍTULO|DESCRIPCIÓN|IMAGENES|DISEÑO)[:]', '', day_text_raw, flags=re.IGNORECASE)
        # Get just the first few paragraphs
        paragraphs = [p.strip() for p in day_text.split('\n') if len(p.strip()) > 20]
        
        day_html = f'''
        <div class="itinerary-day fade-up delay-{min(day_count, 3)}">
            <h3 class="day-title">Día {day_num}</h3>
            <div class="day-content">
        '''
        for p in paragraphs[:3]: # limit to 3 paragraphs to keep it clean
            day_html += f'<p>{p}</p>'
            
        day_html += '''
            </div>
            <div class="day-gallery">
                <img src="images/valle_sagrado.png" alt="Paisaje" class="img-zoom">
                <img src="images/machu_picchu.png" alt="Aventura" class="img-zoom">
            </div>
        </div>
        '''
        days_html += day_html
        day_count += 1

    if day_count == 0:
        # If no days found, maybe it's just a general description, we just add a default block
        desc_lines = [p.strip() for p in section.split('\n') if len(p.strip()) > 30]
        if desc_lines:
            days_html = f'''
            <div class="itinerary-day fade-up">
                <h3 class="day-title">Descripción General</h3>
                <div class="day-content">
                    <p>{desc_lines[0]}</p>
                </div>
                <div class="day-gallery">
                    <img src="images/valle_sagrado.png" alt="Paisaje" class="img-zoom">
                </div>
            </div>
            '''

    # Generate the new HTML
    new_html = template_html
    # Replace Title
    new_html = re.sub(r'<h1 class="tour-title">.*?</h1>', f'<h1 class="tour-title">{title}</h1>', new_html, flags=re.DOTALL)
    # Replace Subtitle
    new_html = re.sub(r'<h2 class="tour-subtitle">.*?</h2>', f'<h2 class="tour-subtitle">{subtitle}</h2>', new_html, flags=re.DOTALL)
    # Replace Days Content
    # We replace everything between <!-- Día 1 --> and </div> <!-- End Column -->
    # Actually, we can just replace the whole content inside <div class="tour-content"> after the separator
    
    # We need to inject the days_html
    # Let's replace the hardcoded days with the dynamic ones
    pattern = re.compile(r'(<div class="tour-separator"></div>\s*</div>).*?(?=<!-- Columna Derecha)', re.DOTALL)
    new_html = pattern.sub(r'\1\n' + days_html + '\n</div>\n', new_html)

    # Save the file
    filename = f'tour-{slug}.html'
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as fw:
        fw.write(new_html)
    
    print(f"Generado: {filename} ({title})")
    
    tours.append({
        'title': title,
        'subtitle': subtitle[:50] + "..." if subtitle else "Descubre esta maravillosa experiencia.",
        'file': filename,
        'days': day_count
    })

print(f"\n¡Se generaron {len(tours)} páginas de tours con éxito!")

# Update tours.html to include all these dynamically!
with open(tours_catalog_file, 'r', encoding='utf-8') as f:
    tours_html = f.read()

# We need to build the grid of tours
tours_grid_html = ""
delay = 0
for tour in tours:
    tours_grid_html += f'''
            <div class="tour-card glass-card fade-up delay-{delay % 3}">
                <div class="card-img-wrapper">
                    <img src="images/machu_picchu.png" alt="{tour['title']}">
                    <div class="card-overlay"></div>
                    <span class="price-tag">Consultar</span>
                </div>
                <div class="card-content">
                    <h3 style="color:var(--color-text-dark);">{tour['title']}</h3>
                    <p style="color:#555; margin-bottom:15px; font-size:0.9rem;">{tour['subtitle']}</p>
                    <a href="{tour['file']}" class="btn btn-primary" style="width:100%; padding:10px;">Ver detalles</a>
                </div>
            </div>
    '''
    delay += 1

# Inject into tours.html
tours_pattern = re.compile(r'(<div class="tours-grid"[^>]*>).*?(?=</div>\s*<br><br>\s*</main>)', re.DOTALL)
new_tours_html = tours_pattern.sub(r'\1\n' + tours_grid_html + '\n', tours_html)

with open(tours_catalog_file, 'w', encoding='utf-8') as fw:
    fw.write(new_tours_html)

print("¡El catálogo de tours (tours.html) ha sido actualizado con todos los tours!")

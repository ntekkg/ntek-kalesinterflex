#!/usr/bin/env python3
import base64, json

with open('/Users/user/Downloads/photo.png', 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('ascii')
logo_mime = 'image/png'

with open('/Users/user/Downloads/Fiberglass.png', 'rb') as f:
    arnet_photo_b64 = base64.b64encode(f.read()).decode('ascii')

with open('/Users/user/Downloads/photo_2026-05-05 16.42.28.jpeg', 'rb') as f:
    img_leccese_dark_sand = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('ascii')

with open('/Users/user/Downloads/PIETRA CAPRI.jpg', 'rb') as f:
    img_c_stone_white = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('ascii')

with open('/Users/user/Downloads/photo_2026-05-05 16.42.24.jpeg', 'rb') as f:
    img_innovation_orange = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('ascii')

with open('/Users/user/Downloads/2 (51).jpg', 'rb') as f:
    _walnut_b64 = base64.b64encode(f.read()).decode('ascii')
WALNUT_TEX_URI = 'data:image/jpeg;base64,' + _walnut_b64

products = [
    # Stone Look
    {"cat": "stone", "collection": "Earth Collection", "name": "Rapolano Ivory", "new": True,
     "img": "https://cdn.kale.com.tr/0/0/earth-collection-rapolano-ivory-matte-kalesinterflex-porcelain-slab-160x320/2ff3dc79-76c1-4308-8f94-e9e0f0fed8db/650/2",
     "dl": "earth-collection-rapolano-ivory"},
    {"cat": "stone", "collection": "Earth Collection", "name": "Rapolano Silver", "new": True,
     "img": "https://cdn.kale.com.tr/0/0/earth-collection-rapolano-silver-matte-kalesinterflex-porcelain-slab-160x320/020bf45e-d130-4a97-8e58-5707d2c7b8ac/650/2",
     "dl": "earth-collection-rapolano-silver"},
    {"cat": "stone", "collection": "Earth Collection", "name": "Travertine Ivory",
     "img": "https://cdn.kale.com.tr/0/0/earth-collection-travertine-ivory-matte-kalesinterflex-porcelain-slab-160x320/15ee1de1-d81f-406d-91c6-de53d8bf2984/650/2",
     "dl": "earth-collection-travertine-ivory"},
    {"cat": "stone", "collection": "Earth Collection", "name": "Travertine Silver",
     "img": "https://cdn.kale.com.tr/0/0/earth-collection-travertine-silver-matte-kalesinterflex-porcelain-slab-160x320/99f9840c-4789-4549-9aaf-c66c6348b84f/650/2",
     "dl": "earth-collection-travertine-silver"},
    {"cat": "stone", "collection": "Calcario Collection", "name": "Grey",
     "img": "https://cdn.kale.com.tr/0/0/calcario-matte-grey-kalesinterflex-porcelain-slab-162x323/1f7a4398-2c98-4e8a-ae3a-ced22ef007ca/650/2",
     "dl": "calcario-collection-grey"},
    {"cat": "stone", "collection": "Calcario Collection", "name": "Light Line",
     "img": "https://cdn.kale.com.tr/0/0/calcario-lg-matte-kalesinterflex-porcelain-slab-160x320/81189a2d-2e2b-4bbf-8385-c9b7991c95a1/650/2",
     "dl": "calcario-collection-light-line"},
    {"cat": "stone", "collection": "Calcario Collection", "name": "Line Griege", "new": True,
     "img": "https://cdn.kale.com.tr/0/0/calcario-collection-line-griege-matte-kalesinterflex-porcelain-slab-162x323/7cb6092d-abcb-4ab1-92e8-8cebaf9f96ba/650/2",
     "dl": "calcario-collection-line-griege"},
    {"cat": "stone", "collection": "Stoneland", "name": "Pietra Di Gre Bone",
     "img": "https://cdn.kale.com.tr/0/0/stoneland-matte-pietra-di-gre-bone-kalesinterflex-porcelain-slab-160x320/e09c1e94-cbc3-4588-8683-e4040bd97993/650/2",
     "dl": "stoneland-pietra-di-gre-bone"},
    {"cat": "stone", "collection": "Alaska", "name": "White",
     "img": "https://cdn.kale.com.tr/0/0/alaska-white-glossy-kalesinterflex-porcelain-slab-162x323/dfc3b51c-b2ac-4b10-888a-8cc6a90e65fa/650/2",
     "dl": "alaska-white"},
    {"cat": "stone", "collection": "Olimpo", "name": "Olimpo",
     "img": "https://cdn.kale.com.tr/0/0/olimpo-matte-kalesinterflex-porcelain-slab-162x323/109a1512-2478-4947-87cd-b3b663bcfe0a/650/2",
     "dl": "olimpo"},
    {"cat": "stone", "collection": "Ocean", "name": "White",
     "img": "https://cdn.kale.com.tr/0/0/ocean-beyaz-mat-kalesinterflex-porselen-plaka-100x300/f5667cc2-6ba3-4900-9a48-a3432a2d72bf/650/2",
     "dl": "ocean-white"},
    {"cat": "stone", "collection": "Ocean", "name": "Black",
     "img": "https://cdn.kale.com.tr/0/0/ocean-black-matte-kalesinterflex-porcelain-slab-100x300/b1f6ba3a-60b5-4ffb-a4e3-0c89ee508039/650/2",
     "dl": "ocean-black"},
    {"cat": "stone", "collection": "Natural Stone", "name": "Leccese Light Sand",
     "img": "https://cdn.kale.com.tr/0/0/natural-stone-matte-leccese-light-sand-kalesinterflex-porcelain-slab-100x300/43fc4b3b-eb7d-42b8-a101-688aecc94705/650/2",
     "dl": "natural-stone-leccese-light-sand"},
    {"cat": "stone", "collection": "Natural Stone", "name": "Leccese Dark Sand",
     "img": img_leccese_dark_sand,
     "dl": "natural-stone-leccese-dark-sand"},
    {"cat": "stone", "collection": "Natural Stone", "name": "Pietra Blue",
     "img": "https://cdn.kale.com.tr/0/0/natural-stone-mat-pietra-mavi-kalesinterflex-porselen-plaka-100x300/480db647-094e-4b90-aeaa-188b258e81d6/650/2",
     "dl": "natural-stone-pietra-blue"},
    {"cat": "stone", "collection": "Natural Stone", "name": "Pietra Grey",
     "img": "https://cdn.kale.com.tr/0/0/natural-stone-matte-pietra-grey-kalesinterflex-porcelain-slab-100x300/e2adcf00-dab0-4aa4-9748-27f5c537d6c3/650/2",
     "dl": "natural-stone-pietra-grey"},
    {"cat": "stone", "collection": "Natural Stone", "name": "Pietra Capri",
     "img": img_c_stone_white,
     "dl": "pietra-capri"},
    {"cat": "stone", "collection": "C-Stone", "name": "White",
     "img": "https://cdn.kale.com.tr/0/0/uptown-light-matte-kalesinterflex-porcelain-slab-120x360/bc4d41e0-795a-432f-9e30-9c0337ed4dfc/650/2",
     "dl": "c-stone-white"},
    {"cat": "stone", "collection": "C-Stone", "name": "Beige",
     "img": "https://cdn.kale.com.tr/0/0/c-stone-matte-beige-kalesinterflex-porcelain-slab-100x300/7a969787-8556-4790-b0c6-b56b137cf719/650/2",
     "dl": "c-stone-beige"},
    {"cat": "stone", "collection": "C-Stone", "name": "Grey",
     "img": "https://cdn.kale.com.tr/0/0/c-stone-mat-gri-kalesinterflex-porselen-plaka-100x300/d18b60fb-3bb9-4867-98ab-000c32b15949/650/2",
     "dl": "c-stone-grey"},
    {"cat": "stone", "collection": "C-Stone", "name": "Brown",
     "img": "https://cdn.kale.com.tr/0/0/c-stone-matte-dark-brown-kalesinterflex-porcelain-slab-100x300/cfab493e-c392-42fe-8fe5-c55e0467f99e/650/2",
     "dl": "c-stone-brown"},
    {"cat": "stone", "collection": "C-Stone", "name": "Anthracite",
     "img": "https://cdn.kale.com.tr/0/0/c-stone-matte-antracite-kalesinterflex-porcelain-slab-120x360/ff4c0535-e924-4fb8-ab8e-fe14145188b0/650/2",
     "dl": "c-stone-anthracite"},
    {"cat": "stone", "collection": "Uptown", "name": "Light",
     "img": "https://cdn.kale.com.tr/0/0/uptown-light-matte-kalesinterflex-porcelain-slab-120x360/bc4d41e0-795a-432f-9e30-9c0337ed4dfc/650/2",
     "dl": "uptown-light"},
    {"cat": "stone", "collection": "Uptown", "name": "Dark",
     "img": "https://cdn.kale.com.tr/0/0/uptown-dark-matte-kalesinterflex-porcelain-slab-100x300/d09e07b5-5046-4c84-93d0-c2b687b8c709/650/2",
     "dl": "uptown-dark"},
    {"cat": "stone", "collection": "Limestone", "name": "Limestone",
     "img": "https://cdn.kale.com.tr/0/0/marbles-mat-limestone-kalesinterflex-porselen-plaka-120x360/403fbeb4-ce22-4a94-9394-ca7ffc7d0ba8/650/2",
     "dl": "limestone"},
    {"cat": "stone", "collection": "Stone Gallery", "name": "Quartz Ash", "new": True,
     "img": "https://cdn.kale.com.tr/0/0/stone-gallery-matte-quartz-ash-kalesinterflex-porcelain-slab-100x300/d19584a1-17f3-40dc-abe8-659fa1ae28d8/650/2",
     "dl": "stone-gallery-quartz-ash"},
    {"cat": "stone", "collection": "Marbles", "name": "Marble Dark", "new": True,
     "img": "https://cdn.kale.com.tr/0/0/marbles-matte-marble-dark-2/a20242db-b194-4c07-9954-24875b4a3d26/650/2",
     "dl": "marbles-marble-dark"},
    {"cat": "stone", "collection": "Marbles", "name": "Travertino Sand", "new": True,
     "img": "https://cdn.kale.com.tr/0/0/marbles-matte-travertino-kalesinterflex-porcelain-slab-120x360/c0bdfa03-0722-4d34-996f-89f380a0c3b5/650/2",
     "dl": "marbles-travertino"},
    # Cement Look
    {"cat": "cement", "collection": "Luxury Cement", "name": "White",
     "img": "https://cdn.kale.com.tr/0/0/luxury-cement-matte-white-kalesinterflex-porcelain-slab-162x323/9b15f7ef-a9b9-473b-b41c-09d42fd23c5c/650/2",
     "dl": "luxury-cement-white"},
    {"cat": "cement", "collection": "Luxury Cement", "name": "Cement",
     "img": "https://cdn.kale.com.tr/0/0/luxury-cement-matte-cement-kalesinterflex-porcelain-slab-160x320/88750286-309d-48d1-b71d-b32fbfc99aeb/650/2",
     "dl": "luxury-cement-cement"},
    {"cat": "cement", "collection": "Luxury Cement", "name": "Grey",
     "img": "https://cdn.kale.com.tr/0/0/luxury-cement-matte-gray-kalesinterflex-porcelain-slab-162x323/b7613820-2d28-4ded-a6a7-4487b6b889e7/650/2",
     "dl": "luxury-cement-grey"},
    {"cat": "cement", "collection": "Luxury Cement", "name": "Taupe",
     "img": "https://cdn.kale.com.tr/0/0/luxury-cement-matte-taupe-kalesinterflex-porcelain-slab-100x300/5a0060dc-7ff3-4792-ad7a-24a4f495e7be/650/2",
     "dl": "luxury-cement-taupe"},
    {"cat": "cement", "collection": "Luxury Cement", "name": "Beige",
     "img": "https://cdn.kale.com.tr/0/0/luxury-cement-matte-beige-kalesinterflex-porcelain-slab-160x320/7a7bea30-f31f-4873-82b5-970d5c2b6916/650/2",
     "dl": "luxury-cement-beige"},
    {"cat": "cement", "collection": "Luxury Cement", "name": "Anthracite",
     "img": "https://cdn.kale.com.tr/0/0/luxury-cement-matte-anthracite-kalesinterflex-porcelain-slab-162x323/741dbf41-3484-4587-a81a-e9b2eab7dda7/650/2",
     "dl": "luxury-cement-anthracite"},
    {"cat": "cement", "collection": "Hued", "name": "Off White",
     "img": "https://cdn.kale.com.tr/0/0/hued-matte-off-white-kalesinterflex-porcelain-slab-100x300/5a109e11-e4a5-42ab-8011-0932456f2d74/650/2",
     "dl": "hued-off-white"},
    {"cat": "cement", "collection": "Hued", "name": "Grey",
     "img": "https://cdn.kale.com.tr/0/0/hued-matte-grey-kalesinterflex-porcelain-slab-100x300/449149b8-1a92-48e1-9f75-fc1ebd58956f/650/2",
     "dl": "hued-grey"},
    {"cat": "cement", "collection": "Hued", "name": "Dark Grey",
     "img": "https://cdn.kale.com.tr/0/0/hued-matte-dark-grey-kalesinterflex-porcelain-slab-100x300/84358595-7edf-4f69-9d09-ddbbda5806d0/650/2",
     "dl": "hued-dark-grey"},
    {"cat": "cement", "collection": "Hued", "name": "Anthracite",
     "img": "https://cdn.kale.com.tr/0/0/hued-matte-antracite-kalesinterflex-porcelain-slab-120x360/6b6965a0-27da-436e-b0de-9c268af1a8a9/650/2",
     "dl": "hued-anthracite"},
    {"cat": "cement", "collection": "Highway", "name": "Bone",
     "img": "https://cdn.kale.com.tr/0/0/highway-mat-kemik-kalesinterflex-porselen-plaka-162x323/44ec81aa-48e8-43e8-9f67-980562b99725/650/2",
     "dl": "highway-bone"},
    {"cat": "cement", "collection": "Arche", "name": "White",
     "img": "https://cdn.kale.com.tr/0/0/arche-matte-white-kalesinterflex-porcelain-slab-100x300/68f0b7fa-1118-43a2-ac9a-4d08e9922d44/650/2",
     "dl": "arche-white"},
    {"cat": "cement", "collection": "Arche", "name": "Grey",
     "img": "https://cdn.kale.com.tr/0/0/arche-matte-grey-kalesinterflex-porcelain-slab-100x300/ea322e4d-a265-4305-aa20-363023a71a0e/650/2",
     "dl": "arche-grey"},
    {"cat": "cement", "collection": "Factory", "name": "Black",
     "img": "https://cdn.kale.com.tr/0/0/factory-matte-black-kalesinterflex-kalesinterflex-porcelain-slab-100x300/51401bd6-c0de-4390-99bc-97286dc41f16/650/2",
     "dl": "factory-black"},
    # Metal Look
    {"cat": "metal", "collection": "Metallic", "name": "Anthracite",
     "img": "https://cdn.kale.com.tr/0/0/metallic-matte-anthracite-kalesinterflex-porcelain-slab-162x323/1d0abf26-3302-40f4-ba7d-3f7166b559ff/650/2",
     "dl": "metallic-anthracite"},
    {"cat": "metal", "collection": "Metallic", "name": "Coral",
     "img": "https://cdn.kale.com.tr/0/0/metalik-matte-coral-sinterflex-porcelain-tile-120x360/9196aa1b-ded5-4212-9c09-ddafce658ab8/650/2",
     "dl": "metallic-coral"},
    {"cat": "metal", "collection": "Corten", "name": "Corten",
     "img": "https://cdn.kale.com.tr/0/0/corten-matte-kalesinterflex-porcelain-slab-162x323/0288734c-7db8-4ff7-9bba-64c14201c177/650/2",
     "dl": "corten"},
    # Solid Colors
    {"cat": "solid", "collection": "Innovation", "name": "Mega White",
     "img": "https://cdn.kale.com.tr/0/0/innovation-matte-mega-white-kalesinterflex-porcelain-slab-100x300/ed4279a9-1640-42d2-83d7-57d07c3356ea/650/2",
     "dl": "innovation-mega-white"},
    {"cat": "solid", "collection": "Innovation", "name": "Mega Black",
     "img": "https://cdn.kale.com.tr/0/0/innovation-matte-mega-black-kalesinterflex-porcelain-slab-100x300/98353e9c-a217-447c-b195-707d9952cfc0/650/2",
     "dl": "innovation-mega-black"},
    {"cat": "solid", "collection": "Innovation", "name": "Beige",
     "img": "https://cdn.kale.com.tr/0/0/innovation-matte-beige-kalesinterflex-porcelain-slab-100x300/c14bec0e-aa53-4175-8842-6047c189e91d/650/2",
     "dl": "innovation-beige"},
    {"cat": "solid", "collection": "Innovation", "name": "Beige Grey",
     "img": "https://cdn.kale.com.tr/0/0/innovation-matte-beige-grey-kalesinterflex-porcelain-slab-100x300/3b36b3c3-cbd6-442f-86e4-cce292415c3e/650/2",
     "dl": "innovation-beige-grey"},
    {"cat": "solid", "collection": "Innovation", "name": "Cement Grey",
     "img": "https://cdn.kale.com.tr/0/0/innovation-matte-cement-grey-kalesinterflex-porcelain-slab-100x300/d53e6769-b09f-4551-94e6-7f77e7f6dcb4/650/2",
     "dl": "innovation-cement-grey"},
    {"cat": "solid", "collection": "Innovation", "name": "Dark Grey",
     "img": "https://cdn.kale.com.tr/0/0/nnovation-mat-koyu-gri-kalesinterflex-porselen-plaka-100x300/54f89c5c-6cf9-4d77-9c97-60ebda0131fa/650/2",
     "dl": "innovation-dark-grey"},
    {"cat": "solid", "collection": "Innovation", "name": "Brown",
     "img": "https://cdn.kale.com.tr/0/0/nnovation-mat-kahve-kalesinterflex-porselen-plaka-100x300/4e550039-09e5-4619-b680-0b467a676529/650/2",
     "dl": "innovation-brown"},
    {"cat": "solid", "collection": "Innovation", "name": "Coral",
     "img": "https://cdn.kale.com.tr/0/0/innovation-matte-coral-kalesinterflex-porcelain-slab-100x300/aa2c1a40-b82b-4303-8ece-83d980eb77d6/650/2",
     "dl": "innovation-coral"},
    {"cat": "solid", "collection": "Innovation", "name": "Orange",
     "img": img_innovation_orange,
     "dl": "innovation-orange"},
    {"cat": "solid", "collection": "Innovation", "name": "Pistachio Green",
     "img": "https://cdn.kale.com.tr/0/0/innovation-matte-pistachio-green-kalesinterflex-porcelain-slab-100x300/9053730a-93be-4457-8c1e-c335ad9ced02/650/2",
     "dl": "innovation-pistachio-green"},
    # Wood Look
    {"cat": "wood", "collection": "Woodline", "name": "Oak",
     "img": "https://cdn.kale.com.tr/0/0/woodline-matte-oak-kalesinterflex-porcelain-slab-100x300/26bc6926-3e37-4c0c-a9da-bbcedfc219a9/650/2",
     "dl": "woodline-oak"},
    {"cat": "wood", "collection": "Woodline", "name": "Cherry",
     "img": "https://cdn.kale.com.tr/0/0/woodline-matte-cherry-kalesinterflex-porcelain-slab-100x300/446b7062-5cad-4d16-8f18-182df582889a/650/2",
     "dl": "woodline-cherry"},
    {"cat": "wood", "collection": "Woodline", "name": "Walnut",
     "img": "https://cdn.kale.com.tr/0/0/woodline-matte-walnut-kalesinterflex-porcelain-slab-100x300/89bc6c0d-29ea-439b-b00a-4d5e57c6e71c/650/2",
     "dl": "woodline-walnut"},
    {"cat": "wood", "collection": "Shell Wood", "name": "Dark",
     "img": "https://cdn.kale.com.tr/0/0/shell-wood-matte-dark-kalesinterflex-porcelain-slab-120x360/af10c40e-a37f-4136-a997-604616f82663/650/2",
     "dl": "shell-wood-dark"},
    {"cat": "wood", "collection": "Hollywood", "name": "Brown",
     "img": "https://cdn.kale.com.tr/0/0/hollywood-matte-brown-kalesinterflex-porcelain-slab-120x360/bca176c5-5445-4e31-b41c-031fc1fed689/650/2",
     "dl": "hollywood-brown"},
    {"cat": "wood", "collection": "Hollywood", "name": "Beige",
     "img": "https://cdn.kale.com.tr/0/0/hollywood-matte-beige-kalesinterflex-porcelain-slab-120x360/c76d43cc-1efd-4d1a-bc7b-201e58a11f3f/650/2",
     "dl": "hollywood-beige"},
    {"cat": "wood", "collection": "BG Plank", "name": "104",
     "img": "https://cdn.kale.com.tr/0/0/plank-bg-104-matte-kalesinterflex-porcelain-slab-100x300/9230e85d-0f23-41a2-9e52-f1e65a52df9b/650/2",
     "dl": "bg-plank-104"},
    {"cat": "wood", "collection": "BG Plank", "name": "110",
     "img": "https://cdn.kale.com.tr/0/0/plank-bg-110-matte-kalesinterflex-porcelain-slab-100x300/721d8874-0456-4d23-944b-25ec812d5716/650/2",
     "dl": "bg-plank-110"},
    {"cat": "wood", "collection": "BG Plank", "name": "111",
     "img": "https://cdn.kale.com.tr/0/0/plank-bg-111-matte-kalesinterflex-porcelain-slab-100x300/bddb121b-13a4-4dd1-8e5f-c27f12c50684/650/2",
     "dl": "bg-plank-111"},
]

# Translations — collection/product names and "Kalesinterflex" are never translated
T = {
    "ru": {
        "page_title": "NTEK — Официальный дистрибьютор Kalesinterflex в Кыргызстане",
        "nav_about": "О материале",
        "nav_collections": "Коллекции",
        "nav_contacts": "Контакты",
        "nav_tag": "Официальный дистрибьютор · КР",
        "hero_eyebrow": "Kalesinterflex · Официальный дистрибьютор в Кыргызстане",
        "hero_h1": "Архитектурные<br>поверхности<br><em>нового поколения</em>",
        "hero_sub": "Тончайшие керамические фасадные плиты 1000×3000 мм при толщине от 3 мм. Для смелых архитектурных решений.",
        "hero_cta1": "Смотреть коллекции ↓",
        "hero_cta2": "О материале",
        "stat1_n": "3–5 мм",
        "stat1_l": "Толщина для фасадов",
        "stat2_n": "7 кг/м²",
        "stat2_l": "Самый лёгкий материал",
        "stat3_n": "100×300 / 120×360",
        "stat3_l": "Форматы плит, см",
        "stat4_n": "A1",
        "stat4_l": "Класс огнестойкости",
        "strip1_t": "Фасады и интерьеры",
        "strip1_s": "Универсальное применение",
        "strip2_t": "Негорючий, класс A1",
        "strip2_s": "Абсолютная пожаробезопасность",
        "strip3_t": "Гибкость и обработка",
        "strip3_s": "Радиус изгиба от 5.5 м",
        "strip4_t": "Экологичное производство",
        "strip4_s": "CO₂ в 1000 раз меньше",
        "about_lbl": "О материале",
        "about_h2": "Что такое<br>Kalesinterflex?",
        "about_p1": "Kalesinterflex — революционный материал для облицовки фасадов и интерьеров. Это первая в Турции крупноформатная порцеляновая плита размером 1000×3000 мм с толщиной от 3 мм, разработанная для самых требовательных архитектурных проектов.",
        "about_p2": "Благодаря уникальной технологии производства, материал сочетает исключительную прочность с гибкостью, минимальным весом и безупречной эстетикой. Доступен в матовом, полированном и атласном исполнениях.",
        "spec1_v": "1000×3000 / 1200×3600",
        "spec1_k": "Форматы плит, мм",
        "spec2_v": "3–5 мм",
        "spec2_k": "Толщина для фасадов",
        "spec3_v": "7 кг/м²",
        "spec3_k": "Вес при толщине 3 мм",
        "spec4_v": "A1",
        "spec4_k": "Класс пожарной безопасности",
        "cat_lbl": "Каталог 2024",
        "cat_h2": "Коллекции Kalesinterflex",
        "cat_sub": "Нажмите «Скачать текстуру» для загрузки изображения в высоком разрешении для использования в проектах.",
        "f_all": "Все коллекции",
        "f_stone": "Натуральный камень",
        "f_cement": "Цемент",
        "f_metal": "Металл",
        "f_solid": "Однотонные",
        "f_wood": "Дерево",
        "btn_dl": "Скачать текстуру",
        "btn_loading": "Загрузка...",
        "contacts_lbl": "Свяжитесь с нами",
        "contacts_h2": "Контакты NTEK",
        "contacts_sub": "Официальный дистрибьютор Kalesinterflex в Кыргызстане. Консультация по материалам, расчёт и доставка.",
        "c_wa_label": "WhatsApp",
        "c_wa_sub": "Написать в WhatsApp",
        "c_ph_label": "Телефон",
        "c_ph_sub": "Звонки",
        "c_ig_label": "Instagram",
        "c_ig_sub": "Проекты и новинки",
        "c_addr_label": "Адрес офиса",
        "c_addr_val": "Исанова 119",
        "c_addr_sub": "Бишкек, Кыргызстан",
        "ft_desc": "NTEK — официальный дистрибьютор Kalesinterflex в Кыргызстане. Поставки материала для архитектурных, дизайнерских и строительных проектов.",
        "ft_nav_h": "Навигация",
        "ft_home": "Главная",
        "ft_about": "О материале",
        "ft_collections": "Коллекции",
        "ft_contacts": "Контакты",
        "ft_cat_h": "Коллекции",
        "ft_stone": "Натуральный камень",
        "ft_cement": "Цемент",
        "ft_metal": "Металл",
        "ft_solid": "Однотонные",
        "ft_wood": "Дерево",
        "ft_contact_h": "Контакты",
        "ft_wa_l": "WhatsApp",
        "ft_ph_l": "Телефон",
        "ft_ig_l": "Instagram",
        "ft_addr_l": "Адрес",
        "ft_addr_v": "Исанова 119, Бишкек",
        "ft_copy": "© 2024 NTEK. Все права защищены.",
        "ft_kale": "Официальный сайт Kale →",
        "toast_done": "✓ Текстура загружена: ",
        "toast_tab": "Открыто в новой вкладке — сохраните изображение",
        "slab_lbl": "Kalesinterflex · 3 мм",
        "slab_h2": "Тончайшая плита",
        "slab_sub": "Перетащите для вращения",
        "arnet_lbl": "Технология армирования",
        "arnet_h2": "Система AR-Net",
        "arnet_sub": "Специализированная армирующая сетка для фасадных панелей",
        "arnet_p1": "Каждая панель Kalesinterflex армирована сеткой AR-Net из щёлочестойкого стекловолокна. В отличие от стандартных интерьерных сеток E-Net, AR-Net обеспечивает долговременную защиту от агрессивного воздействия цементных клеёв и атмосферной щёлочи.",
        "arnet_p2": "Система армирования гарантирует структурную целостность панели при ударных нагрузках, исключает расслоение и сохраняет безопасность фасада на протяжении всего срока эксплуатации здания.",
        "arnet_f1_t": "Щёлочестойкость",
        "arnet_f1_s": "AR-стекловолокно сохраняет прочность в контакте с цементными системами и агрессивными клеями",
        "arnet_f2_t": "Ударопрочность",
        "arnet_f2_s": "Структурная целостность панели при механических и ударных нагрузках",
        "arnet_f3_t": "Долговечность",
        "arnet_f3_s": "Надёжная работа в условиях переменного климата на протяжении всего срока службы",
        "arnet_f4_t": "Безопасность фасада",
        "arnet_f4_s": "Обязательный стандарт для наружных работ, сертифицированный для фасадных систем",
        "arnet_cmp_h": "AR-Net vs E-Net",
        "arnet_cmp_sub": "Только AR-Net обеспечивает необходимые характеристики для применения в фасадных системах",
        "arnet_ar": "AR-Net",
        "arnet_en": "E-Net (стандарт)",
        "arnet_c1": "Стойкость к щёлочи",
        "arnet_c2": "Адгезия к фасадным клеям",
        "arnet_c3": "Долгосрочная прочность",
        "arnet_c4": "Фасадное применение",
        "arnet_good": "✓",
        "arnet_bad": "✗",
        "arnet_canvas_lbl": "AR-Net · Армирующая сетка",
        "facade_lbl": "Вентилируемый фасад",
        "facade_h2": "Система монтажа · Шаг за шагом",
        "facade_step": "Шаг",
        "facade_prev": "← Назад",
        "facade_next": "Далее →",
        "facade_hint": "Нажмите «Далее», чтобы собрать фасад слой за слоем",
        "facade_s1": "Несущая стена",
        "facade_s1d": "Кирпичная или бетонная конструкция",
        "facade_s2": "L-кронштейны и термопрокладки",
        "facade_s2d": "Анкер через термопрокладку в несущую стену",
        "facade_s3": "Базальтовая теплоизоляция",
        "facade_s3d": "Базальтовые плиты вокруг кронштейнов, крепёж зонтичными дюбелями",
        "facade_s4": "Ветрозащитная мембрана",
        "facade_s4d": "Паропроницаемая мембрана натянута поверх утеплителя",
        "facade_s5": "Вертикальные T-профили",
        "facade_s5d": "Алюминиевый T-профиль заклёпками к L-кронштейнам",
        "facade_s6": "Лента и клей на полке профиля",
        "facade_s6d": "Двусторонняя лента + полиуретановый клей Kalekim на полке",
        "facade_s7": "Панели Kalesinterflex",
        "facade_s7d": "3 мм · Прижимаются к профилю, лента удерживает до отверждения клея",
    },
    "en": {
        "page_title": "NTEK — Official Kalesinterflex Distributor in Kyrgyzstan",
        "nav_about": "About",
        "nav_collections": "Collections",
        "nav_contacts": "Contacts",
        "nav_tag": "Official Distributor · KR",
        "hero_eyebrow": "Kalesinterflex · Official Distributor in Kyrgyzstan",
        "hero_h1": "Architectural<br>Surfaces of<br><em>a New Generation</em>",
        "hero_sub": "Ultra-thin ceramic facade slabs 1000×3000 mm from 3 mm thick. For bold architectural solutions.",
        "hero_cta1": "View Collections ↓",
        "hero_cta2": "About the Material",
        "stat1_n": "3–5 mm",
        "stat1_l": "Facade Thickness",
        "stat2_n": "7 kg/m²",
        "stat2_l": "Lightest Material",
        "stat3_n": "100×300 / 120×360",
        "stat3_l": "Slab Formats, cm",
        "stat4_n": "A1",
        "stat4_l": "Fire Resistance Class",
        "strip1_t": "Facades & Interiors",
        "strip1_s": "Universal Application",
        "strip2_t": "Non-Combustible, Class A1",
        "strip2_s": "Absolute Fire Safety",
        "strip3_t": "Flexibility & Processing",
        "strip3_s": "Bending Radius from 5.5 m",
        "strip4_t": "Sustainable Production",
        "strip4_s": "CO₂ 1000× Lower",
        "about_lbl": "About the Material",
        "about_h2": "What is<br>Kalesinterflex?",
        "about_p1": "Kalesinterflex is a revolutionary material for facade and interior cladding. It is Turkey's first large-format porcelain slab measuring 1000×3000 mm with a thickness from 3 mm, developed for the most demanding architectural projects.",
        "about_p2": "Thanks to its unique manufacturing technology, the material combines exceptional strength with flexibility, minimal weight, and impeccable aesthetics. Available in matte, polished, and satin finishes.",
        "spec1_v": "1000×3000 / 1200×3600",
        "spec1_k": "Slab Formats, mm",
        "spec2_v": "3–5 mm",
        "spec2_k": "Facade Thickness",
        "spec3_v": "7 kg/m²",
        "spec3_k": "Weight at 3 mm",
        "spec4_v": "A1",
        "spec4_k": "Fire Safety Class",
        "cat_lbl": "Catalogue 2024",
        "cat_h2": "Kalesinterflex Collections",
        "cat_sub": "Click \"Download Texture\" to get a high-resolution image for use in your projects.",
        "f_all": "All Collections",
        "f_stone": "Natural Stone",
        "f_cement": "Cement",
        "f_metal": "Metal",
        "f_solid": "Solid Colours",
        "f_wood": "Wood",
        "btn_dl": "Download Texture",
        "btn_loading": "Loading...",
        "contacts_lbl": "Get in Touch",
        "contacts_h2": "NTEK Contacts",
        "contacts_sub": "Official Kalesinterflex distributor in Kyrgyzstan. Material consultation, quotation, and delivery.",
        "c_wa_label": "WhatsApp",
        "c_wa_sub": "Message via WhatsApp",
        "c_ph_label": "Phone",
        "c_ph_sub": "Calls",
        "c_ig_label": "Instagram",
        "c_ig_sub": "Projects & New Arrivals",
        "c_addr_label": "Office Address",
        "c_addr_val": "Isanova 119",
        "c_addr_sub": "Bishkek, Kyrgyzstan",
        "ft_desc": "NTEK — official Kalesinterflex distributor in Kyrgyzstan. Supply of material for architectural, design, and construction projects.",
        "ft_nav_h": "Navigation",
        "ft_home": "Home",
        "ft_about": "About",
        "ft_collections": "Collections",
        "ft_contacts": "Contacts",
        "ft_cat_h": "Collections",
        "ft_stone": "Natural Stone",
        "ft_cement": "Cement",
        "ft_metal": "Metal",
        "ft_solid": "Solid Colours",
        "ft_wood": "Wood",
        "ft_contact_h": "Contacts",
        "ft_wa_l": "WhatsApp",
        "ft_ph_l": "Phone",
        "ft_ig_l": "Instagram",
        "ft_addr_l": "Address",
        "ft_addr_v": "Isanova 119, Bishkek",
        "ft_copy": "© 2024 NTEK. All rights reserved.",
        "ft_kale": "Official Kale Website →",
        "toast_done": "✓ Texture downloaded: ",
        "toast_tab": "Opened in new tab — save the image",
        "slab_lbl": "Kalesinterflex · 3 mm",
        "slab_h2": "The Thinnest Slab",
        "slab_sub": "Drag to rotate",
        "arnet_lbl": "Reinforcement Technology",
        "arnet_h2": "AR-Net System",
        "arnet_sub": "Specialised reinforcement mesh for facade panels",
        "arnet_p1": "Every Kalesinterflex panel is reinforced with AR-Net alkali-resistant glass fibre mesh. Unlike standard interior E-Net meshes, AR-Net provides long-term protection against the aggressive effects of cement adhesives and atmospheric alkali.",
        "arnet_p2": "The reinforcement system guarantees the panel's structural integrity under impact loads, prevents delamination, and maintains facade safety throughout the building's entire service life.",
        "arnet_f1_t": "Alkali Resistance",
        "arnet_f1_s": "AR glass fibre retains full strength in contact with cement systems and aggressive facade adhesives",
        "arnet_f2_t": "Impact Resistance",
        "arnet_f2_s": "Structural integrity of the panel under mechanical and impact loads",
        "arnet_f3_t": "Durability",
        "arnet_f3_s": "Reliable performance in variable climates throughout the entire service life",
        "arnet_f4_t": "Facade Safety",
        "arnet_f4_s": "Mandatory standard for exterior applications, certified for facade systems",
        "arnet_cmp_h": "AR-Net vs E-Net",
        "arnet_cmp_sub": "Only AR-Net provides the required properties for facade system applications",
        "arnet_ar": "AR-Net",
        "arnet_en": "E-Net (standard)",
        "arnet_c1": "Alkali resistance",
        "arnet_c2": "Adhesion to facade adhesives",
        "arnet_c3": "Long-term strength retention",
        "arnet_c4": "Facade application",
        "arnet_good": "✓",
        "arnet_bad": "✗",
        "arnet_canvas_lbl": "AR-Net · Reinforcement Mesh",
        "facade_lbl": "Ventilated Facade",
        "facade_h2": "Installation System · Step by Step",
        "facade_step": "Step",
        "facade_prev": "← Back",
        "facade_next": "Next →",
        "facade_hint": "Press Next to assemble the facade layer by layer",
        "facade_s1": "Structural Wall",
        "facade_s1d": "Brick or concrete base structure",
        "facade_s2": "L-Brackets & Thermal Breaks",
        "facade_s2d": "Anchor bolt through thermal pad into structural wall",
        "facade_s3": "Basalt Wool Insulation",
        "facade_s3d": "Basalt boards around brackets, secured with mushroom plugs",
        "facade_s4": "Windproof Membrane",
        "facade_s4d": "Vapour-permeable membrane stretched over insulation layer",
        "facade_s5": "Vertical T-Profiles",
        "facade_s5d": "Aluminium T-profile riveted to L-bracket arms",
        "facade_s6": "Tape & Adhesive on Profile",
        "facade_s6d": "Double-sided tape + Kalekim PU adhesive bead on flange",
        "facade_s7": "Kalesinterflex Panels",
        "facade_s7d": "3 mm · Pressed to profile — tape grabs instantly while adhesive cures",
    },
    "ky": {
        "page_title": "NTEK — Кыргызстандагы Kalesinterflex расмий дистрибьютору",
        "nav_about": "Материал жөнүндө",
        "nav_collections": "Коллекциялар",
        "nav_contacts": "Байланыш",
        "nav_tag": "Расмий дистрибьютор · КР",
        "hero_eyebrow": "Kalesinterflex · Кыргызстандагы расмий дистрибьютор",
        "hero_h1": "Жаңы муундун<br>архитектуралык<br><em>беттери</em>",
        "hero_sub": "Калыңдыгы 3 ммден, 1000×3000 мм өлчөмүндөгү жука керамикалык фасад плиталары. Чечкиндүү архитектуралык долбоорлор үчүн.",
        "hero_cta1": "Коллекцияларды көрүү ↓",
        "hero_cta2": "Материал жөнүндө",
        "stat1_n": "3–5 мм",
        "stat1_l": "Фасад калыңдыгы",
        "stat2_n": "7 кг/м²",
        "stat2_l": "Эң жеңил материал",
        "stat3_n": "100×300 / 120×360",
        "stat3_l": "Плита форматтары, см",
        "stat4_n": "A1",
        "stat4_l": "Өрткө туруктуулук классы",
        "strip1_t": "Фасад жана интерьер",
        "strip1_s": "Универсалдуу колдонуу",
        "strip2_t": "Жанбайт, A1 классы",
        "strip2_s": "Абсолюттук өрт коопсуздугу",
        "strip3_t": "Ийкемдүүлүк жана иштетүү",
        "strip3_s": "Ийилүү радиусу 5.5 мден",
        "strip4_t": "Экологиялык өндүрүш",
        "strip4_s": "CO₂ 1000 эсе аз",
        "about_lbl": "Материал жөнүндө",
        "about_h2": "Kalesinterflex<br>деген эмне?",
        "about_p1": "Kalesinterflex — фасад жана интерьерди каптоо үчүн революциялык материал. Бул Түркиядагы биринчи ири форматтагы фарфор плита — 1000×3000 мм, калыңдыгы 3 ммден, эң талапчан архитектуралык долбоорлор үчүн иштелип чыккан.",
        "about_p2": "Уникалдуу өндүрүш технологиясынын аркасында материал өзгөчө бекемдикти, ийкемдүүлүктү, минималдуу салмакты жана кемчиликсиз эстетиканы айкалыштырат. Матт, жылтыр жана атлас беттемелеринде жеткиликтүү.",
        "spec1_v": "1000×3000 / 1200×3600",
        "spec1_k": "Плита форматтары, мм",
        "spec2_v": "3–5 мм",
        "spec2_k": "Фасад үчүн калыңдык",
        "spec3_v": "7 кг/м²",
        "spec3_k": "3 мм калыңдыктагы салмак",
        "spec4_v": "A1",
        "spec4_k": "Өрт коопсуздугу классы",
        "cat_lbl": "2024 Каталогу",
        "cat_h2": "Kalesinterflex Коллекциялары",
        "cat_sub": "Долбоорлордо колдонуу үчүн жогорку сапаттагы сүрөт жүктөп алуу үчүн «Текстураны жүктөп алуу» баскычын басыңыз.",
        "f_all": "Бардык коллекциялар",
        "f_stone": "Табигый таш",
        "f_cement": "Цемент",
        "f_metal": "Металл",
        "f_solid": "Бир түстүү",
        "f_wood": "Жыгач",
        "btn_dl": "Текстураны жүктөп алуу",
        "btn_loading": "Жүктөлүүдө...",
        "contacts_lbl": "Биз менен байланышыңыз",
        "contacts_h2": "NTEK Байланыштары",
        "contacts_sub": "Кыргызстандагы Kalesinterflex расмий дистрибьютору. Материалдар боюнча кеңешүү, эсептөө жана жеткирүү.",
        "c_wa_label": "WhatsApp",
        "c_wa_sub": "WhatsApp аркылуу жазуу",
        "c_ph_label": "Телефон",
        "c_ph_sub": "Чалуулар",
        "c_ig_label": "Instagram",
        "c_ig_sub": "Долбоорлор жана жаңылыктар",
        "c_addr_label": "Офис дареги",
        "c_addr_val": "Исанова 119",
        "c_addr_sub": "Бишкек, Кыргызстан",
        "ft_desc": "NTEK — Кыргызстандагы Kalesinterflex расмий дистрибьютору. Архитектуралык, дизайнердик жана курулуш долбоорлору үчүн материал жеткирүү.",
        "ft_nav_h": "Навигация",
        "ft_home": "Башкы бет",
        "ft_about": "Материал жөнүндө",
        "ft_collections": "Коллекциялар",
        "ft_contacts": "Байланыш",
        "ft_cat_h": "Коллекциялар",
        "ft_stone": "Табигый таш",
        "ft_cement": "Цемент",
        "ft_metal": "Металл",
        "ft_solid": "Бир түстүү",
        "ft_wood": "Жыгач",
        "ft_contact_h": "Байланыш",
        "ft_wa_l": "WhatsApp",
        "ft_ph_l": "Телефон",
        "ft_ig_l": "Instagram",
        "ft_addr_l": "Дарек",
        "ft_addr_v": "Исанова 119, Бишкек",
        "ft_copy": "© 2024 NTEK. Бардык укуктар корголгон.",
        "ft_kale": "Kale расмий сайты →",
        "toast_done": "✓ Текстура жүктөлдү: ",
        "toast_tab": "Жаңы өтмөктө ачылды — сүрөттү сактаңыз",
        "slab_lbl": "Kalesinterflex · 3 мм",
        "slab_h2": "Эң жука плита",
        "slab_sub": "Айлантуу үчүн сүйрөңүз",
        "arnet_lbl": "Арматуралоо технологиясы",
        "arnet_h2": "AR-Net системасы",
        "arnet_sub": "Фасад панелдери үчүн атайын арматуралоо тору",
        "arnet_p1": "Ар бир Kalesinterflex панели щелочко туруктуу AR-Net айнек жибинен жасалган тор менен арматураланган. Стандарттык E-Net интерьер торлорунан айырмаланып, AR-Net цемент клейлеринин жана атмосфералык агрессиялуу чөйрөнүн таасиринен узак мөөнөттүү коргоону камсыздайт.",
        "arnet_p2": "Арматуралоо системасы панелдин структуралык бүтүндүгүн удар жүктөрүндө камсыздайт, катмарлардын ажырашынын алдын алат жана бинанын бүткүл кызмат мөөнөтүндө фасаддын коопсуздугун сактайт.",
        "arnet_f1_t": "Щелочтук туруктуулук",
        "arnet_f1_s": "AR айнек жиби цемент системалары жана агрессиялуу фасад клейлери менен байланышта бекемдигин толук сактайт",
        "arnet_f2_t": "Соккуга туруктуулук",
        "arnet_f2_s": "Механикалык жана ударлык жүктөрдө панелдин структуралык бүтүндүгү",
        "arnet_f3_t": "Узак мөөнөттүүлүк",
        "arnet_f3_s": "Бүткүл эксплуатация мезгилинде ар түрдүү климатта ишенимдүү иштөө",
        "arnet_f4_t": "Фасад коопсуздугу",
        "arnet_f4_s": "Тышкы иштер үчүн милдеттүү стандарт, фасад системалары үчүн сертификатталган",
        "arnet_cmp_h": "AR-Net vs E-Net",
        "arnet_cmp_sub": "Фасад системалары үчүн керектүү мүнөздөмөлөрдү AR-Net гана камсыз кылат",
        "arnet_ar": "AR-Net",
        "arnet_en": "E-Net (стандарт)",
        "arnet_c1": "Щелочтук туруктуулук",
        "arnet_c2": "Фасад клейлерине адгезия",
        "arnet_c3": "Узак мөөнөттүү бекемдик",
        "arnet_c4": "Фасад колдонуу",
        "arnet_good": "✓",
        "arnet_bad": "✗",
        "arnet_canvas_lbl": "AR-Net · Арматуралоо тору",
        "facade_lbl": "Желдетилген фасад",
        "facade_h2": "Монтаж системасы · Кадам-кадам",
        "facade_step": "Кадам",
        "facade_prev": "← Артка",
        "facade_next": "Кийинки →",
        "facade_hint": "Фасадды катмар-катмар жыйноо үчүн «Кийинки» баскычын басыңыз",
        "facade_s1": "Туруктуу дубал",
        "facade_s1d": "Кирпичтен же бетондон жасалган негизги конструкция",
        "facade_s2": "L-кронштейндер жана термо прокладкалар",
        "facade_s2d": "Анкер болт термо прокладка аркылуу туруктуу дубалга бекитилет",
        "facade_s3": "Базальт жылуулук изоляциясы",
        "facade_s3d": "Базальт плиталар кронштейндер айланасына, зонт дюбелдери менен бекитилет",
        "facade_s4": "Шамал коргоочу мембрана",
        "facade_s4d": "Буу өткөзгүч мембрана изоляциянын үстүнө тартылат",
        "facade_s5": "Вертикалдык T-профилдер",
        "facade_s5d": "Алюминий T-профил L-кронштейн колдоруна заклёпкалар менен бекитилет",
        "facade_s6": "Профил фланцына лента жана желим",
        "facade_s6d": "Эки тараптуу лента + Kalekim PU желим фланцтын четине",
        "facade_s7": "Kalesinterflex панелдери",
        "facade_s7d": "3 мм · Профилге каратылат — лента дароо кармайт",
    }
}

T_json = json.dumps(T, ensure_ascii=False)

# ── Slab 3D section ─────────────────────────────────────────────────────────
# CSS and JS kept as plain strings (no f-string) to avoid brace-escaping issues

SLAB_CSS = """
/* SLAB 3D */
.slab3d{background:#0e0e0e;padding:80px 5% 72px}
.slab3d-inner{max-width:900px;margin:0 auto;display:flex;flex-direction:column;align-items:center;gap:0}
.slab3d .sec-lbl{color:#c4a882}
.slab3d .sec-lbl::before,.slab3d .sec-lbl::after{background:#c4a882}
.slab3d .sec-h2{color:#fff}
.slab3d .sec-head{margin-bottom:12px}
.slab3d-hint{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.28);margin-top:6px;margin-bottom:36px;text-align:center}
.slab3d-canvas-wrap{position:relative;width:380px;height:520px;cursor:grab;touch-action:none}
.slab3d-canvas-wrap:active{cursor:grabbing}
#slabCanvas{width:100%;height:100%;display:block}
.slab3d-footer{margin-top:28px;display:flex;flex-direction:column;align-items:center;gap:14px}
.slab3d-label{font-family:'Playfair Display',serif;font-size:20px;font-weight:400;color:#fff;letter-spacing:.04em;min-height:28px}
@media(max-width:480px){.slab3d-canvas-wrap{width:280px;height:390px}}
"""

SLAB_JS = """
<script type="importmap">
{"imports":{"three":"https://unpkg.com/three@0.160.0/build/three.module.min.js"}}
</script>
<script type="module">
import * as THREE from 'three';

const SLAB_URL  = 'https://cdn.kale.com.tr/0/0/woodline-matte-walnut-kalesinterflex-porcelain-slab-100x300/89bc6c0d-29ea-439b-b00a-4d5e57c6e71c/650/2';
const SLAB_NAME = 'Woodline · Walnut';

const wrap    = document.querySelector('.slab3d-canvas-wrap');
const canvas  = document.getElementById('slabCanvas');
const labelEl = document.getElementById('slabLabel');
if (!canvas) { console.warn('slabCanvas not found'); }
else initSlab();

function makeNetTex() {
  const sz = 256, cell = 24, r = 6;
  const cv = document.createElement('canvas');
  cv.width = cv.height = sz;
  const ctx = cv.getContext('2d');
  ctx.fillStyle = '#b0acaa';
  ctx.fillRect(0, 0, sz, sz);
  const n = Math.ceil(sz / cell) + 2;
  function sh(x0, x1, y) {
    const g = ctx.createLinearGradient(0, y - r, 0, y + r);
    g.addColorStop(0, '#c8c4be'); g.addColorStop(.35, '#e0dbd6');
    g.addColorStop(.65, '#e8e4e0'); g.addColorStop(1, '#a8a4a0');
    ctx.beginPath(); ctx.lineWidth = r * 2; ctx.lineCap = 'butt';
    ctx.strokeStyle = g; ctx.moveTo(x0, y); ctx.lineTo(x1, y); ctx.stroke();
  }
  function sv(x, y0, y1) {
    const g = ctx.createLinearGradient(x - r, 0, x + r, 0);
    g.addColorStop(0, '#b8b4b0'); g.addColorStop(.35, '#d4d0cc');
    g.addColorStop(.65, '#dedad6'); g.addColorStop(1, '#9c9894');
    ctx.beginPath(); ctx.lineWidth = r * 2; ctx.lineCap = 'butt';
    ctx.strokeStyle = g; ctx.moveTo(x, y0); ctx.lineTo(x, y1); ctx.stroke();
  }
  for (let row = 0; row < n; row++) for (let col = 0; col < n; col++)
    if ((row + col) % 2 !== 0) sh(col * cell - cell / 2, col * cell + cell / 2, row * cell);
  for (let col = 0; col < n; col++) sv(col * cell, -cell / 2, sz + cell / 2);
  for (let row = 0; row < n; row++) for (let col = 0; col < n; col++)
    if ((row + col) % 2 === 0) sh(col * cell - cell / 2, col * cell + cell / 2, row * cell);
  const tex = new THREE.CanvasTexture(cv);
  tex.wrapS = tex.wrapT = THREE.RepeatWrapping;
  tex.repeat.set(3, 9);
  return tex;
}

function makeWoodTex() {
  const W = 256, H = 768;
  const cv = document.createElement('canvas');
  cv.width = W; cv.height = H;
  const ctx = cv.getContext('2d');
  const imgd = ctx.createImageData(W, H);
  const px = imgd.data;
  for (let y = 0; y < H; y++) {
    const t = y / H;
    const grain = Math.sin(t * Math.PI * 48) * 0.42
                + Math.sin(t * Math.PI * 19 + 1.1) * 0.28
                + Math.sin(t * Math.PI * 112 + Math.sin(t * Math.PI * 7) * 3.0) * 0.18
                + Math.sin(t * Math.PI * 290 + Math.sin(t * Math.PI * 31) * 1.5) * 0.07;
    const r = Math.max(0, Math.min(255, Math.round(112 + grain * 55)));
    const g = Math.max(0, Math.min(255, Math.round(70  + grain * 38)));
    const b = Math.max(0, Math.min(255, Math.round(32  + grain * 22)));
    for (let x = 0; x < W; x++) {
      const i = (y * W + x) * 4;
      px[i] = r; px[i+1] = g; px[i+2] = b; px[i+3] = 255;
    }
  }
  ctx.putImageData(imgd, 0, 0);
  const tex = new THREE.CanvasTexture(cv);
  tex.wrapS = tex.wrapT = THREE.RepeatWrapping;
  tex.repeat.set(1, 1);
  return tex;
}

function initSlab() {
  const W = () => wrap.clientWidth;
  const H = () => wrap.clientHeight;

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.setSize(W(), H());
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.15;

  const scene  = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(30, W() / H(), 0.1, 100);
  camera.position.set(0, 0.4, 11.5);
  camera.lookAt(0, 0.2, 0);

  scene.add(new THREE.AmbientLight(0xffffff, 0.3));
  const key = new THREE.DirectionalLight(0xfff8f0, 1.3);
  key.position.set(4, 7, 6); scene.add(key);
  const fill = new THREE.DirectionalLight(0xe8d4b8, 0.25);
  fill.position.set(-4, -2, 3); scene.add(fill);
  const rim = new THREE.DirectionalLight(0xffffff, 0.45);
  rim.position.set(0, -5, -5); scene.add(rim);

  const geo   = new THREE.BoxGeometry(1.8, 5.4, 0.065);
  const edge  = new THREE.MeshStandardMaterial({ color: 0xe8e2d8, roughness: 0.25, metalness: 0.05 });
  const back  = new THREE.MeshStandardMaterial({ map: makeNetTex(), roughness: 0.65 });
  const front = new THREE.MeshStandardMaterial({ roughness: 0.65, metalness: 0.02 });
  const slab  = new THREE.Mesh(geo, [edge, edge, edge, edge, front, back]);
  scene.add(slab);

  if (labelEl) labelEl.textContent = SLAB_NAME;

  new THREE.TextureLoader().load('WALNUT_TEX_PLACEHOLDER', tex => {
    tex.colorSpace = THREE.SRGBColorSpace;
    front.map = tex;
    front.needsUpdate = true;
  });

  async function loadTex() {
    let bUrl = null;
    try {
      const r1 = await fetch(SLAB_URL);
      if (r1.ok) bUrl = URL.createObjectURL(await r1.blob());
    } catch(_) {}
    if (!bUrl) {
      try {
        const r2 = await fetch('https://corsproxy.io/?url=' + encodeURIComponent(SLAB_URL));
        if (r2.ok) bUrl = URL.createObjectURL(await r2.blob());
      } catch(_) {}
    }
    if (!bUrl) { return; }
    new THREE.TextureLoader().load(bUrl, tex => {
      tex.colorSpace = THREE.SRGBColorSpace;
      front.map = tex;
      front.needsUpdate = true;
      setTimeout(() => URL.revokeObjectURL(bUrl), 60000);
    });
  }
  loadTex();

  let rotY = 0, rotX = -0.1;
  let isDragging = false, lastX = 0, lastY = 0;
  let velX = 0, velY = 0;
  let autoT = 0;
  const AUTO_SPEED = 0.011;

  const onDown = e => {
    isDragging = true;
    lastX = e.touches ? e.touches[0].clientX : e.clientX;
    lastY = e.touches ? e.touches[0].clientY : e.clientY;
    velX = velY = 0;
  };
  const onMove = e => {
    if (!isDragging) return;
    const cx = e.touches ? e.touches[0].clientX : e.clientX;
    const cy = e.touches ? e.touches[0].clientY : e.clientY;
    velX = (cx - lastX) * 0.013;
    velY = (cy - lastY) * 0.008;
    rotY += velX; rotX += velY;
    rotX = Math.max(-0.5, Math.min(0.5, rotX));
    lastX = cx; lastY = cy;
  };
  const onUp = () => { isDragging = false; };

  canvas.addEventListener('mousedown',  onDown);
  canvas.addEventListener('touchstart', onDown, { passive: true });
  window.addEventListener('mousemove',  onMove);
  window.addEventListener('touchmove',  onMove, { passive: true });
  window.addEventListener('mouseup',    onUp);
  window.addEventListener('touchend',   onUp);

  function animate() {
    requestAnimationFrame(animate);
    if (!isDragging) {
      autoT += 0.014;
      if (Math.abs(velX) > 0.0003) { velX *= 0.92; rotY += velX; }
      else { velX = 0; rotY += AUTO_SPEED; }
      if (Math.abs(velY) > 0.0003) { velY *= 0.92; rotX += velY; }
      else rotX += (Math.sin(autoT * 0.38) * 0.52 - rotX) * 0.04;
    }
    slab.rotation.y = rotY;
    slab.rotation.x = rotX;
    renderer.render(scene, camera);
  }
  animate();

  const ro = new ResizeObserver(() => {
    renderer.setSize(W(), H());
    camera.aspect = W() / H();
    camera.updateProjectionMatrix();
  });
  ro.observe(wrap);
}
</script>
"""
SLAB_JS = SLAB_JS.replace('WALNUT_TEX_PLACEHOLDER', WALNUT_TEX_URI)

ARNET_CSS = """
/* AR-NET SECTION */
.arnet{padding:96px 5%;background:var(--surface)}
.arnet-inner{max-width:1440px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start}
.arnet-h2{font-family:'Playfair Display',serif;font-size:clamp(26px,3vw,44px);font-weight:400;color:var(--dark);line-height:1.2;margin-bottom:24px}
.arnet-features{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:32px}
.arnet-feat{padding:18px 20px;background:var(--bg);border:1px solid var(--border)}
.arnet-feat-t{font-size:10.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin-bottom:7px}
.arnet-feat-s{font-size:12.5px;color:var(--mid);line-height:1.6}
.arnet-visual{display:flex;flex-direction:column;gap:20px}
.arnet-canvas-wrap{overflow:hidden;background:#cac6be;position:relative}
.arnet-img{display:block;width:100%;height:290px;object-fit:cover}
.arnet-canvas-lbl{font-size:10px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--accent)}
.arnet-cmp-h{font-size:11.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--dark);margin-bottom:12px}
.arnet-cmp-note{font-size:12px;color:var(--mid);margin-bottom:16px;line-height:1.6}
.cmp-table{width:100%;border-collapse:collapse;font-size:13px}
.cmp-table th,.cmp-table td{padding:10px 14px;text-align:left;border-bottom:1px solid var(--border)}
.cmp-table thead tr{background:var(--bg)}
.cmp-table th{font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--mid)}
.cmp-table th:nth-child(2),.cmp-table th:nth-child(3){text-align:center}
.cmp-table td:nth-child(2){text-align:center;color:#2a9d4a;font-weight:700;font-size:17px}
.cmp-table td:nth-child(3){text-align:center;color:#c0392b;font-weight:700;font-size:17px}
@media(max-width:960px){.arnet-inner{grid-template-columns:1fr;gap:48px}}
@media(max-width:480px){.arnet-features{grid-template-columns:1fr}}
"""

ARNET_JS = """
<script>
(function(){
  var cv = document.getElementById('arnetCanvas');
  if (!cv) return;
  function draw() {
    var W = cv.offsetWidth || 400;
    var H = cv.offsetHeight || 290;
    var dpr = devicePixelRatio || 1;
    cv.width  = Math.round(W * dpr);
    cv.height = Math.round(H * dpr);
    var ctx = cv.getContext('2d');
    ctx.scale(dpr, dpr);
    var cell = 36, r = 9;
    var cols = Math.ceil(W / cell) + 2;
    var rows = Math.ceil(H / cell) + 2;
    ctx.fillStyle = '#c4bfb8';
    ctx.fillRect(0, 0, W, H);
    function sh(x0, x1, y) {
      var g = ctx.createLinearGradient(0, y - r, 0, y + r);
      g.addColorStop(0,   '#b8b3ac');
      g.addColorStop(.28, '#ddd8d2');
      g.addColorStop(.5,  '#eee9e3');
      g.addColorStop(.72, '#d8d3cc');
      g.addColorStop(1,   '#a8a39c');
      ctx.beginPath(); ctx.lineWidth = r * 2; ctx.lineCap = 'butt';
      ctx.strokeStyle = g; ctx.moveTo(x0, y); ctx.lineTo(x1, y); ctx.stroke();
      ctx.beginPath(); ctx.lineWidth = r * .45; ctx.strokeStyle = 'rgba(255,255,255,.3)';
      ctx.moveTo(x0, y - r * .28); ctx.lineTo(x1, y - r * .28); ctx.stroke();
    }
    function sv(x, y0, y1) {
      var g = ctx.createLinearGradient(x - r, 0, x + r, 0);
      g.addColorStop(0,   '#b0aba4');
      g.addColorStop(.28, '#d4cfc8');
      g.addColorStop(.5,  '#e4dfd8');
      g.addColorStop(.72, '#ccc7c0');
      g.addColorStop(1,   '#a09b94');
      ctx.beginPath(); ctx.lineWidth = r * 2; ctx.lineCap = 'butt';
      ctx.strokeStyle = g; ctx.moveTo(x, y0); ctx.lineTo(x, y1); ctx.stroke();
      ctx.beginPath(); ctx.lineWidth = r * .4; ctx.strokeStyle = 'rgba(255,255,255,.26)';
      ctx.moveTo(x - r * .22, y0); ctx.lineTo(x - r * .22, y1); ctx.stroke();
    }
    for (var row = 0; row < rows; row++)
      for (var col = 0; col < cols; col++)
        if ((row + col) % 2 !== 0) sh(col * cell - cell / 2, col * cell + cell / 2, row * cell);
    for (var col2 = 0; col2 < cols; col2++) sv(col2 * cell, -cell / 2, H + cell / 2);
    for (var row2 = 0; row2 < rows; row2++)
      for (var col3 = 0; col3 < cols; col3++)
        if ((row2 + col3) % 2 === 0) sh(col3 * cell - cell / 2, col3 * cell + cell / 2, row2 * cell);
    var vg = ctx.createRadialGradient(W/2, H/2, H * .2, W/2, H/2, H * .72);
    vg.addColorStop(0, 'rgba(0,0,0,0)');
    vg.addColorStop(1, 'rgba(0,0,0,.3)');
    ctx.fillStyle = vg; ctx.fillRect(0, 0, W, H);
  }
  if (document.readyState === 'complete') draw(); else window.addEventListener('load', draw);
  window.addEventListener('resize', draw);
})();
</script>
"""

FACADE_CSS = """
/* FACADE ASSEMBLY */
.facade-section{background:#080808;padding:80px 5% 72px}
.facade-inner{max-width:1000px;margin:0 auto;display:flex;flex-direction:column;align-items:center}
.facade-section .sec-lbl{color:#c4a882}
.facade-section .sec-lbl::before,.facade-section .sec-lbl::after{background:#c4a882}
.facade-section .sec-h2{color:#fff}
.facade-section .sec-head{margin-bottom:24px;width:100%}
.facade-canvas-wrap{width:100%;background:#0d0d0d}
#facadeCanvas{width:100%;height:500px;display:block}
.facade-step-info{margin-top:20px;display:flex;flex-direction:column;align-items:center;gap:8px;width:100%}
.facade-slabels{position:relative;min-height:52px;width:100%;text-align:center}
.facade-slabel{position:absolute;top:0;left:0;right:0;text-align:center;transition:opacity .3s,transform .3s;opacity:0;transform:translateY(6px);pointer-events:none}
.facade-slabel.on{opacity:1;transform:translateY(0);pointer-events:auto}
.facade-slabel-name{font-family:'Playfair Display',serif;font-size:19px;font-weight:400;color:#fff;letter-spacing:.04em}
.facade-slabel-desc{font-size:11px;color:rgba(255,255,255,.36);letter-spacing:.06em;margin-top:5px}
.facade-step-counter{font-size:10px;color:rgba(255,255,255,.22);letter-spacing:.18em;text-transform:uppercase}
.facade-controls{display:flex;gap:14px;align-items:center;margin-top:10px}
.facade-btn{background:transparent;border:1px solid rgba(255,255,255,.18);color:rgba(255,255,255,.55);padding:8px 20px;font-size:10.5px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;cursor:pointer;transition:all .2s;line-height:1}
.facade-btn:hover:not(:disabled){border-color:#c4a882;color:#c4a882}
.facade-btn:disabled{opacity:.2;cursor:default}
.facade-fdots{display:flex;gap:6px;align-items:center}
.facade-fdot{width:6px;height:6px;border-radius:50%;background:rgba(255,255,255,.2);border:none;padding:0;cursor:pointer;transition:all .2s}
.facade-fdot.on{background:#c4a882;transform:scale(1.4)}
.facade-fdot:hover:not(.on){background:rgba(255,255,255,.5)}
@media(max-width:600px){#facadeCanvas{height:320px}}
"""

FACADE_JS = """
<script type="module">
import * as THREE from 'three';

const canvas = document.getElementById('facadeCanvas');
if (!canvas) throw 0;
const wrap = canvas.parentElement;

const lerp  = (a,b,t) => a+(b-a)*t;
const clamp = (v,lo,hi) => Math.max(lo,Math.min(hi,v));
const ease  = t => 1-Math.pow(1-t,3);

const renderer = new THREE.WebGLRenderer({canvas,antialias:true});
renderer.setPixelRatio(Math.min(devicePixelRatio,2));
renderer.setSize(wrap.clientWidth, canvas.offsetHeight||500);
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.1;
renderer.shadowMap.enabled = true;

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x080808);

const camera = new THREE.PerspectiveCamera(28, wrap.clientWidth/(canvas.offsetHeight||500), 0.1, 100);
camera.position.set(3.8, 2.6, 5.8);
camera.lookAt(0, 0.5, 0.3);

scene.add(new THREE.AmbientLight(0xffffff, 0.4));
const sun = new THREE.DirectionalLight(0xfff8f0, 1.5);
sun.position.set(4,8,6); sun.castShadow=true; sun.shadow.mapSize.set(1024,1024);
scene.add(sun);
const fill = new THREE.DirectionalLight(0xd0e4f0,0.3); fill.position.set(-4,2,4); scene.add(fill);

function makeBrickTex() {
  const cw=256,ch=256,cv=document.createElement('canvas');
  cv.width=cw; cv.height=ch;
  const ctx=cv.getContext('2d');
  ctx.fillStyle='#181818'; ctx.fillRect(0,0,cw,ch);
  const bw=48,bh=22,gap=3;
  for(let row=0;row*(bh+gap)<ch+bh;row++){
    const off=(row%2)*(bw/2);
    for(let col=-1;col*(bw+gap)-off<cw+bw;col++){
      const s=0.16+Math.random()*0.07;
      ctx.fillStyle=`rgb(${Math.round(s*255)},${Math.round(s*245)},${Math.round(s*235)})`;
      ctx.fillRect(col*(bw+gap)-off+gap/2, row*(bh+gap)+gap/2, bw, bh);
    }
  }
  const t=new THREE.CanvasTexture(cv);
  t.wrapS=t.wrapT=THREE.RepeatWrapping; t.repeat.set(3,4); return t;
}
function makeInsTex() {
  const cv=document.createElement('canvas'); cv.width=cv.height=128;
  const ctx=cv.getContext('2d');
  ctx.fillStyle='#d4cfc4'; ctx.fillRect(0,0,128,128);
  for(let i=0;i<700;i++){
    ctx.beginPath(); ctx.arc(Math.random()*128,Math.random()*128,Math.random()*1.6,0,Math.PI*2);
    ctx.fillStyle=`rgba(0,0,0,${Math.random()*.09})`; ctx.fill();
  }
  const t=new THREE.CanvasTexture(cv);
  t.wrapS=t.wrapT=THREE.RepeatWrapping; t.repeat.set(5,10); return t;
}

const M={
  wall:    new THREE.MeshStandardMaterial({map:makeBrickTex(),roughness:.95}),
  ins:     new THREE.MeshStandardMaterial({map:makeInsTex(),color:0xcec9be,roughness:.88}),
  bracket: new THREE.MeshStandardMaterial({color:0xa0a09a,roughness:.28,metalness:.78}),
  thermal: new THREE.MeshStandardMaterial({color:0xf0ece4,roughness:.82}),
  membrane:new THREE.MeshStandardMaterial({color:0xc8ddf0,roughness:.5,transparent:true,opacity:0.70}),
  rail:    new THREE.MeshStandardMaterial({color:0xb0b0a6,roughness:.2,metalness:.88}),
  tape:    new THREE.MeshStandardMaterial({color:0xb03020,roughness:.6,emissive:0x180000}),
  adhesive:new THREE.MeshStandardMaterial({color:0x7a7060,roughness:.95}),
  panel:   new THREE.MeshStandardMaterial({color:0xf2eee8,roughness:.52}),
};

function bx(w,h,d,mat,x=0,y=0,z=0){
  const m=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),mat);
  m.position.set(x,y,z); m.castShadow=m.receiveShadow=true; return m;
}
function cyl(r,h,mat,x=0,y=0,z=0,rx=0){
  const m=new THREE.Mesh(new THREE.CylinderGeometry(r,r,h,8),mat);
  m.position.set(x,y,z); m.rotation.x=rx; return m;
}
function grp(...c){const g=new THREE.Group(); c.forEach(x=>g.add(x)); return g;}

/* Depth (Z) positions along camera axis */
const ZWF=0.25;   /* wall front face                     */
const ZBT=0.37;   /* bracket tip = insulation front face  */
const ZMF=0.374;  /* windproof membrane front face        */
const ZFF=0.475;  /* T-profile flange front face          */
const ZPB=0.488;  /* panel back face                      */

/* L1 — Structural wall */
const L1=grp(bx(2.4,3.2,.25,M.wall,0,.5,.125));

/* L2 — L-shaped brackets + thermal break pads, bolted into wall */
function mkBracket(px,py){
  return grp(
    bx(.15,.13,.006,M.thermal,px,py,ZWF+.001),
    bx(.12,.11,.014,M.bracket,px,py,ZWF+.009),
    bx(.10,.013,ZBT-ZWF+.01,M.bracket,px,py,ZWF+(ZBT-ZWF)/2+.005),
    cyl(.009,.28,M.bracket,px,py,ZWF-.08,Math.PI/2)
  );
}
const L2=grp(mkBracket(-.62,1.2),mkBracket(-.62,-.2),mkBracket(.62,1.2),mkBracket(.62,-.2));

/* L3 — Basalt wool insulation fitted around brackets, with mushroom plugs */
function mkMushroom(px,py){
  return grp(
    cyl(.038,.008,M.thermal,px,py,ZBT+.001,Math.PI/2),
    cyl(.004,.120,M.thermal,px,py,ZBT-.060,Math.PI/2)
  );
}
const L3=grp(
  bx(1.15,3.2,.12,M.ins,-0.62,.5,ZWF+.06),
  bx(1.15,3.2,.12,M.ins, 0.62,.5,ZWF+.06),
  mkMushroom(-.30,.90), mkMushroom(.30,.90),
  mkMushroom(-.30,-.10), mkMushroom(.30,-.10),
  mkMushroom(-.90,.30), mkMushroom(.90,.30)
);

/* L4 — Windproof vapour-permeable membrane over insulation */
const L4=grp(bx(2.4,3.2,.004,M.membrane,0,.5,ZBT+.002));

/* L5 — Vertical aluminium T-profiles riveted to bracket arms */
function mkRail(px){
  return grp(
    bx(.006,3.2,.092,M.rail,px,.5,ZMF+.046),
    bx(.100,3.2,.010,M.rail,px,.5,ZMF+.096)
  );
}
const L5=grp(mkRail(-.62),mkRail(.62));

/* L6 — Double-sided facade tape + Kalekim PU adhesive on profile flange */
const L6=grp(
  bx(.022,3.2,.005,M.tape,    -.635,.5,ZFF+.0025),
  bx(.022,3.2,.005,M.tape,     .605,.5,ZFF+.0025),
  bx(.020,3.2,.008,M.adhesive,-.605,.5,ZFF+.004),
  bx(.020,3.2,.008,M.adhesive, .635,.5,ZFF+.004)
);

/* L7 — Kalesinterflex 3 mm panels — full wall coverage, vertical joint only */
const PW=1.1985, PG=0.0015;
const L7=grp(
  bx(PW,3.2,.006,M.panel,-(PG+PW/2), 0.5, ZPB+.003),
  bx(PW,3.2,.006,M.panel,  PG+PW/2,  0.5, ZPB+.003)
);

(async()=>{
  const url='https://cdn.kale.com.tr/0/0/innovation-matte-mega-white-kalesinterflex-porcelain-slab-100x300/ed4279a9-1640-42d2-83d7-57d07c3356ea/650/2';
  let bUrl=null;
  try{const r=await fetch(url);if(r.ok)bUrl=URL.createObjectURL(await r.blob());}catch(_){}
  if(!bUrl)try{const r=await fetch('https://corsproxy.io/?url='+encodeURIComponent(url));if(r.ok)bUrl=URL.createObjectURL(await r.blob());}catch(_){}
  if(!bUrl)return;
  new THREE.TextureLoader().load(bUrl,tex=>{
    tex.colorSpace=THREE.SRGBColorSpace;
    M.panel.map=tex; M.panel.needsUpdate=true;
    setTimeout(()=>URL.revokeObjectURL(bUrl),60000);
  });
})();

const LAYERS=[L1,L2,L3,L4,L5,L6,L7];
const FLY=[[0,0,-2.5],[0,0,3.2],[-4,0,0],[0,5,0],[-4,0,0],[4,0,0],[0,0,3.6]];
LAYERS.forEach(l=>{scene.add(l);l.visible=false;});

let cur=0;
const active=new Array(7).fill(false);
const animGen=new Array(7).fill(0);

function flyIn(i){
  const l=LAYERS[i],[fx,fy,fz]=FLY[i];
  l.position.set(fx,fy,fz); l.visible=true;
  const t0=performance.now(),dur=820,gen=++animGen[i];
  function tick(now){
    if(animGen[i]!==gen)return;
    const p=ease(clamp((now-t0)/dur,0,1));
    l.position.set(lerp(fx,0,p),lerp(fy,0,p),lerp(fz,0,p));
    if(p<1)requestAnimationFrame(tick); else l.position.set(0,0,0);
  }
  requestAnimationFrame(tick);
}

function goTo(idx){
  cur=clamp(idx,0,6);
  LAYERS.forEach((l,i)=>{
    if(i<=cur){l.visible=true;if(!active[i]){active[i]=true;flyIn(i);}}
    else{l.visible=false;active[i]=false;l.position.set(0,0,0);}
  });
  updateUI();
}

function updateUI(){
  document.querySelectorAll('.facade-slabel').forEach(el=>{
    el.classList.toggle('on',+el.dataset.step===cur);
  });
  const cnt=document.getElementById('facadeStepNum');
  if(cnt)cnt.textContent=cur+1;
  const prev=document.getElementById('facadePrev');
  const next=document.getElementById('facadeNext');
  if(prev)prev.disabled=cur===0;
  if(next)next.disabled=cur===6;
  const dots=document.getElementById('facadeDots');
  if(dots)dots.innerHTML=LAYERS.map((_,j)=>
    `<button class="facade-fdot${j===cur?' on':''}" onclick="window._facadeGo(${j})" aria-label="${j+1}"></button>`
  ).join('');
}

window._facadeGo=goTo;
document.getElementById('facadePrev')?.addEventListener('click',()=>goTo(cur-1));
document.getElementById('facadeNext')?.addEventListener('click',()=>goTo(cur+1));

new IntersectionObserver(entries=>{
  if(entries[0].isIntersecting&&cur===0&&!active[0])goTo(0);
},{threshold:.2}).observe(canvas);

(function animate(){requestAnimationFrame(animate);renderer.render(scene,camera);})();

new ResizeObserver(()=>{
  const w=wrap.clientWidth,h=canvas.offsetHeight||500;
  renderer.setSize(w,h); camera.aspect=w/h; camera.updateProjectionMatrix();
}).observe(wrap);
</script>
"""

_local = [(p['dl'], p['img']) for p in products if p['img'].startswith('data:')]
local_css = '\n'.join(
    f'.li-{dl}{{background-image:url("{img}")}}'
    for dl, img in _local
)
local_imgs_js = 'const localImgs={' + ','.join(f'"{dl}":"{img}"' for dl, img in _local) + '};'

def make_card(p):
    new_badge = '<span class="badge-new">NEW</span>' if p.get('new') else ''
    is_local = p['img'].startswith('data:')
    if is_local:
        img_tag = f'<div class="card-img li-{p["dl"]}"></div>'
        dl_arg = f"localImgs['{p['dl']}']"
    else:
        dl_url = p['img'].replace('/650/2', '/1200/2')
        img_tag = f'<img class="card-img" src="{p["img"]}" alt="{p["collection"]} {p["name"]}" loading="lazy">'
        dl_arg = f"'{dl_url}'"
    return f'''    <div class="card" data-cat="{p['cat']}">
      <div class="card-img-wrap">
        {img_tag}
        {new_badge}
      </div>
      <div class="card-body">
        <div class="card-col">{p['collection']}</div>
        <div class="card-nm">{p['name']}</div>
      </div>
      <button class="card-dl" data-i18n="btn_dl" onclick="downloadTexture({dl_arg}, '{p['dl']}.jpg', this)">
        <span>↓</span> Скачать текстуру
      </button>
    </div>'''

cards_html = '\n'.join(make_card(p) for p in products)

html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-i18n="page_title">NTEK — Официальный дистрибьютор Kalesinterflex в Кыргызстане</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#f5f3ef;
  --surface:#ffffff;
  --dark:#111111;
  --mid:#666666;
  --light:#aaaaaa;
  --accent:#8B6F4E;
  --accent-light:#c4a882;
  --border:#e2ddd6;
  --shadow:0 2px 16px rgba(0,0,0,0.07);
  --shadow-hover:0 12px 40px rgba(0,0,0,0.14);
}}
html{{scroll-behavior:smooth}}
body{{font-family:'Inter',sans-serif;background:var(--bg);color:var(--dark);line-height:1.6;-webkit-font-smoothing:antialiased}}

/* NAV */
nav{{
  position:fixed;top:0;left:0;right:0;z-index:200;
  background:rgba(17,17,17,0.97);
  backdrop-filter:blur(16px);
  height:70px;display:flex;align-items:center;padding:0 5%;
  border-bottom:1px solid rgba(255,255,255,0.05);
}}
.nav-inner{{display:flex;align-items:center;justify-content:space-between;width:100%;max-width:1440px;margin:0 auto;gap:24px}}
.nav-logo img{{height:44px;mix-blend-mode:screen;display:block}}
.nav-links{{display:flex;gap:32px;list-style:none}}
.nav-links a{{color:rgba(255,255,255,0.65);text-decoration:none;font-size:12.5px;font-weight:500;letter-spacing:.06em;text-transform:uppercase;transition:color .2s}}
.nav-links a:hover{{color:#fff}}
.nav-right{{display:flex;align-items:center;gap:14px}}
.nav-tag{{font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,0.5);border:1px solid rgba(255,255,255,0.15);padding:5px 14px;border-radius:2px;white-space:nowrap}}
.lang-sw{{display:flex;gap:1px;background:rgba(255,255,255,.08);padding:3px;border-radius:3px}}
.lb{{padding:5px 9px;font-size:10.5px;font-weight:700;letter-spacing:.05em;background:transparent;color:rgba(255,255,255,.4);border:none;cursor:pointer;transition:all .15s;border-radius:2px;line-height:1}}
.lb.on{{background:rgba(255,255,255,.18);color:#fff}}
.lb:hover:not(.on){{color:rgba(255,255,255,.75)}}

/* HERO */
.hero{{
  margin-top:70px;position:relative;
  height:calc(100vh - 70px);min-height:580px;max-height:860px;
  overflow:hidden;display:flex;align-items:center;
}}
.hero-mosaic{{position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:2px}}
.hero-tile{{background-size:cover;background-position:center}}
.hero-tile:nth-child(1){{background-image:url('https://cdn.kale.com.tr/0/0/earth-collection-rapolano-ivory-matte-kalesinterflex-porcelain-slab-160x320/2ff3dc79-76c1-4308-8f94-e9e0f0fed8db/650/2');grid-row:1/3}}
.hero-tile:nth-child(2){{background-image:url('https://cdn.kale.com.tr/0/0/corten-matte-kalesinterflex-porcelain-slab-162x323/0288734c-7db8-4ff7-9bba-64c14201c177/650/2')}}
.hero-tile:nth-child(3){{background-image:url('https://cdn.kale.com.tr/0/0/luxury-cement-matte-white-kalesinterflex-porcelain-slab-162x323/9b15f7ef-a9b9-473b-b41c-09d42fd23c5c/650/2')}}
.hero-tile:nth-child(4){{background-image:url('https://cdn.kale.com.tr/0/0/woodline-matte-walnut-kalesinterflex-porcelain-slab-100x300/89bc6c0d-29ea-439b-b00a-4d5e57c6e71c/650/2')}}
.hero-tile:nth-child(5){{background-image:url('https://cdn.kale.com.tr/0/0/metallic-matte-anthracite-kalesinterflex-porcelain-slab-162x323/1d0abf26-3302-40f4-ba7d-3f7166b559ff/650/2')}}
.hero-overlay{{position:absolute;inset:0;background:linear-gradient(105deg,rgba(10,10,10,.92) 0%,rgba(10,10,10,.72) 40%,rgba(10,10,10,.2) 100%)}}
.hero-content{{position:relative;z-index:2;padding:0 5%;max-width:700px}}
.hero-eyebrow{{font-size:11px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--accent-light);margin-bottom:22px;display:flex;align-items:center;gap:12px}}
.hero-eyebrow::before{{content:'';display:block;width:32px;height:1px;background:var(--accent-light)}}
.hero-h1{{font-family:'Playfair Display',serif;font-size:clamp(38px,5.2vw,68px);font-weight:400;color:#fff;line-height:1.1;margin-bottom:26px}}
.hero-h1 em{{font-style:italic;color:var(--accent-light)}}
.hero-sub{{font-size:15px;color:rgba(255,255,255,.6);line-height:1.8;max-width:480px;margin-bottom:44px}}
.hero-cta{{display:flex;gap:14px;flex-wrap:wrap}}
.btn-dark{{background:var(--accent);color:#fff;border:none;padding:15px 36px;font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;gap:8px;transition:background .2s,transform .15s}}
.btn-dark:hover{{background:#7a5f3f;transform:translateY(-2px)}}
.btn-ghost{{background:transparent;color:rgba(255,255,255,.8);border:1px solid rgba(255,255,255,.25);padding:14px 36px;font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;cursor:pointer;text-decoration:none;display:inline-block;transition:all .2s}}
.btn-ghost:hover{{border-color:rgba(255,255,255,.8);color:#fff}}
.hero-bottom{{position:absolute;bottom:0;left:0;right:0;z-index:2;padding:24px 5%;display:flex;align-items:center;gap:40px;background:linear-gradient(to top,rgba(0,0,0,.5) 0%,transparent 100%)}}
.hero-stat{{display:flex;flex-direction:column;gap:4px}}
.hero-stat-n{{font-size:22px;font-weight:700;color:#fff;line-height:1}}
.hero-stat-l{{font-size:10px;color:rgba(255,255,255,.45);letter-spacing:.08em;text-transform:uppercase}}
.hero-sep{{width:1px;height:36px;background:rgba(255,255,255,.15)}}

/* STRIP */
.strip{{background:var(--dark);display:grid;grid-template-columns:repeat(4,1fr)}}
.strip-item{{padding:22px 28px;border-right:1px solid rgba(255,255,255,.07);display:flex;align-items:center;gap:16px}}
.strip-item:last-child{{border-right:none}}
.strip-icon{{font-size:20px;line-height:1}}
.strip-t{{font-size:11.5px;font-weight:700;color:#fff;letter-spacing:.07em;text-transform:uppercase}}
.strip-s{{font-size:11px;color:rgba(255,255,255,.38);margin-top:3px}}

/* ABOUT */
.about{{padding:104px 5%;max-width:1440px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:96px;align-items:center}}
.lbl{{font-size:10.5px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);margin-bottom:14px;display:flex;align-items:center;gap:10px}}
.lbl::before{{content:'';display:block;width:24px;height:1px;background:var(--accent)}}
.about-h2{{font-family:'Playfair Display',serif;font-size:clamp(26px,3vw,44px);font-weight:400;color:var(--dark);line-height:1.2;margin-bottom:24px}}
.about-p{{font-size:14.5px;color:var(--mid);line-height:1.85;margin-bottom:14px}}
.about-specs{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:32px}}
.spec{{padding:18px 20px;background:var(--surface);border:1px solid var(--border)}}
.spec-v{{font-size:18px;font-weight:700;color:var(--dark);line-height:1}}
.spec-k{{font-size:10px;color:var(--light);letter-spacing:.1em;text-transform:uppercase;margin-top:6px}}
.img-grid{{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:280px 280px;gap:4px}}
.img-cell{{background-size:cover;background-position:center}}
.img-cell:first-child{{grid-row:1/3;grid-column:1}}

/* COLLECTIONS */
.collections{{padding:96px 5%}}
.sec-head{{text-align:center;margin-bottom:56px}}
.sec-lbl{{font-size:10.5px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);margin-bottom:12px;display:flex;align-items:center;justify-content:center;gap:10px}}
.sec-lbl::before,.sec-lbl::after{{content:'';display:block;width:24px;height:1px;background:var(--accent)}}
.sec-h2{{font-family:'Playfair Display',serif;font-size:clamp(26px,3vw,44px);font-weight:400;color:var(--dark);margin-bottom:14px}}
.sec-sub{{font-size:14.5px;color:var(--mid);max-width:520px;margin:0 auto;line-height:1.7}}
.filters{{display:flex;gap:6px;justify-content:center;flex-wrap:wrap;margin-bottom:52px}}
.ftab{{padding:9px 24px;font-size:11.5px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;border:1.5px solid var(--border);background:var(--surface);color:var(--mid);cursor:pointer;transition:all .2s;border-radius:1px}}
.ftab:hover{{border-color:var(--dark);color:var(--dark)}}
.ftab.on{{background:var(--dark);color:#fff;border-color:var(--dark)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:20px;max-width:1440px;margin:0 auto}}

/* CARD */
.card{{background:var(--surface);border:1px solid var(--border);overflow:hidden;transition:box-shadow .3s,transform .3s;display:flex;flex-direction:column}}
.card:hover{{box-shadow:var(--shadow-hover);transform:translateY(-5px)}}
.card.hide{{display:none}}
.card-img-wrap{{position:relative;padding-bottom:195%;overflow:hidden;background:#e8e5e0}}
.card-img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;background-size:cover;background-position:center;background-repeat:no-repeat;transition:transform .5s ease;display:block}}
.card:hover .card-img{{transform:scale(1.05)}}
.badge-new{{position:absolute;top:12px;right:12px;background:var(--dark);color:#fff;font-size:9px;font-weight:700;letter-spacing:.12em;padding:4px 9px;line-height:1.5;text-transform:uppercase}}
.card-body{{padding:16px 18px 12px;flex:1;display:flex;flex-direction:column;gap:5px}}
.card-col{{font-size:9.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}}
.card-nm{{font-size:12.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--dark);line-height:1.25}}
.card-dl{{width:100%;padding:12px 16px;background:var(--dark);color:#fff;border:none;font-size:10.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;cursor:pointer;transition:background .2s;display:flex;align-items:center;justify-content:center;gap:7px;margin-top:auto}}
.card-dl:hover{{background:var(--accent)}}
.card-dl:active{{transform:scale(.98)}}
.card-dl.busy{{opacity:.55;pointer-events:none}}

/* CONTACTS */
.contacts{{padding:96px 5%;background:var(--surface)}}
.contacts-inner{{max-width:1440px;margin:0 auto}}
.contacts-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:28px;margin-top:56px}}
.contact-card{{background:var(--bg);border:1px solid var(--border);padding:32px 28px;display:flex;flex-direction:column;gap:10px}}
.contact-card-icon{{font-size:24px;line-height:1;margin-bottom:4px;display:flex;align-items:center}}
.contact-card-label{{font-size:9.5px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--accent)}}
.contact-card-value{{font-size:15px;font-weight:600;color:var(--dark);line-height:1.4;text-decoration:none}}
a.contact-card-value:hover{{color:var(--accent)}}
.contact-card-sub{{font-size:12px;color:var(--mid)}}

/* FOOTER */
footer{{background:var(--dark);padding:72px 5% 36px}}
.ft-inner{{max-width:1440px;margin:0 auto}}
.ft-top{{display:grid;grid-template-columns:2.2fr 1fr 1fr 1.3fr;gap:56px;padding-bottom:52px;border-bottom:1px solid rgba(255,255,255,.07);margin-bottom:28px}}
.ft-logo{{margin-bottom:14px}}
.ft-logo img{{height:38px;mix-blend-mode:screen;opacity:.9}}
.ft-desc{{font-size:13px;color:rgba(255,255,255,.38);line-height:1.8;max-width:260px;margin-top:14px}}
.ft-col-h{{font-size:10px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.85);margin-bottom:18px}}
.ft-list{{list-style:none;display:flex;flex-direction:column;gap:9px}}
.ft-list a{{color:rgba(255,255,255,.4);text-decoration:none;font-size:13px;transition:color .2s}}
.ft-list a:hover{{color:rgba(255,255,255,.85)}}
.ft-contact-row{{margin-bottom:14px}}
.ft-cl{{font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.28)}}
.ft-cv{{font-size:13px;color:rgba(255,255,255,.6);margin-top:3px}}
.ft-cv a{{color:rgba(255,255,255,.6);text-decoration:none}}
.ft-cv a:hover{{color:rgba(255,255,255,.9)}}
.ft-bottom{{display:flex;justify-content:space-between;align-items:center}}
.ft-copy{{font-size:11.5px;color:rgba(255,255,255,.22)}}
.ft-kale-link{{font-size:11.5px;color:rgba(255,255,255,.3);text-decoration:none;transition:color .2s}}
.ft-kale-link:hover{{color:rgba(255,255,255,.7)}}

/* TOAST */
#toast{{position:fixed;bottom:28px;left:50%;transform:translateX(-50%) translateY(90px);background:var(--dark);color:#fff;padding:13px 28px;font-size:12.5px;font-weight:500;border-radius:2px;box-shadow:0 8px 32px rgba(0,0,0,.3);transition:transform .32s cubic-bezier(.2,.8,.3,1);z-index:9999;pointer-events:none;white-space:nowrap}}
#toast.up{{transform:translateX(-50%) translateY(0)}}

/* FADE IN */
.fi{{opacity:0;transform:translateY(22px);transition:opacity .65s,transform .65s}}
.fi.v{{opacity:1;transform:translateY(0)}}

.sep{{border:none;border-top:1px solid var(--border)}}

@media(max-width:1100px){{
  .about{{grid-template-columns:1fr;gap:48px}}
  .img-grid{{grid-template-rows:220px 220px}}
  .ft-top{{grid-template-columns:1fr 1fr;gap:40px}}
}}
@media(max-width:768px){{
  .nav-links{{display:none}}
  .nav-tag{{display:none}}
  .strip{{grid-template-columns:1fr 1fr}}
  .hero-bottom{{gap:20px}}
  .hero-stat-n{{font-size:18px}}
  .grid{{grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}}
  .ft-top{{grid-template-columns:1fr}}
  .ft-bottom{{flex-direction:column;gap:10px;text-align:center}}
}}
@media(max-width:480px){{
  .grid{{grid-template-columns:1fr 1fr;gap:10px}}
  .hero-eyebrow{{font-size:10px}}
  .hero-stat-n{{font-size:16px}}
}}
{SLAB_CSS}
{ARNET_CSS}
{FACADE_CSS}
{local_css}
</style>
</head>
<body>

<nav>
  <div class="nav-inner">
    <a href="#top" class="nav-logo" style="text-decoration:none">
      <img src="data:{logo_mime};base64,{logo_b64}" alt="NTEK">
    </a>
    <ul class="nav-links">
      <li><a href="#about" data-i18n="nav_about">О материале</a></li>
      <li><a href="#collections" data-i18n="nav_collections">Коллекции</a></li>
      <li><a href="#contacts" data-i18n="nav_contacts">Контакты</a></li>
    </ul>
    <div class="nav-right">
      <span class="nav-tag" data-i18n="nav_tag">Официальный дистрибьютор · КР</span>
      <div class="lang-sw">
        <button class="lb on" onclick="setLang('ru')">RU</button>
        <button class="lb" onclick="setLang('en')">EN</button>
        <button class="lb" onclick="setLang('ky')">КЫ</button>
      </div>
    </div>
  </div>
</nav>

<section class="hero" id="top">
  <div class="hero-mosaic" aria-hidden="true">
    <div class="hero-tile"></div>
    <div class="hero-tile"></div>
    <div class="hero-tile"></div>
    <div class="hero-tile"></div>
    <div class="hero-tile"></div>
  </div>
  <div class="hero-overlay"></div>
  <div class="hero-content">
    <p class="hero-eyebrow" data-i18n="hero_eyebrow">Kalesinterflex &nbsp;·&nbsp; Официальный дистрибьютор в Кыргызстане</p>
    <h1 class="hero-h1" data-i18n-html="hero_h1">Архитектурные<br>поверхности<br><em>нового поколения</em></h1>
    <p class="hero-sub" data-i18n="hero_sub">Тончайшие керамические фасадные плиты 1000×3000 мм при толщине от 3 мм. Для смелых архитектурных решений.</p>
    <div class="hero-cta">
      <a href="#collections" class="btn-dark" data-i18n="hero_cta1">Смотреть коллекции ↓</a>
      <a href="#about" class="btn-ghost" data-i18n="hero_cta2">О материале</a>
    </div>
  </div>
  <div class="hero-bottom">
    <div class="hero-stat">
      <div class="hero-stat-n" data-i18n="stat1_n">3–5 мм</div>
      <div class="hero-stat-l" data-i18n="stat1_l">Толщина для фасадов</div>
    </div>
    <div class="hero-sep"></div>
    <div class="hero-stat">
      <div class="hero-stat-n" data-i18n="stat2_n">7 кг/м²</div>
      <div class="hero-stat-l" data-i18n="stat2_l">Самый лёгкий материал</div>
    </div>
    <div class="hero-sep"></div>
    <div class="hero-stat">
      <div class="hero-stat-n" data-i18n="stat3_n">100×300 / 120×360</div>
      <div class="hero-stat-l" data-i18n="stat3_l">Форматы плит, см</div>
    </div>
    <div class="hero-sep"></div>
    <div class="hero-stat">
      <div class="hero-stat-n" data-i18n="stat4_n">A1</div>
      <div class="hero-stat-l" data-i18n="stat4_l">Класс огнестойкости</div>
    </div>
  </div>
</section>

<div class="strip">
  <div class="strip-item"><span class="strip-icon">🏗</span><div><div class="strip-t" data-i18n="strip1_t">Фасады и интерьеры</div><div class="strip-s" data-i18n="strip1_s">Универсальное применение</div></div></div>
  <div class="strip-item"><span class="strip-icon">🔥</span><div><div class="strip-t" data-i18n="strip2_t">Негорючий, класс A1</div><div class="strip-s" data-i18n="strip2_s">Абсолютная пожаробезопасность</div></div></div>
  <div class="strip-item"><span class="strip-icon">✂️</span><div><div class="strip-t" data-i18n="strip3_t">Гибкость и обработка</div><div class="strip-s" data-i18n="strip3_s">Радиус изгиба от 5.5 м</div></div></div>
  <div class="strip-item"><span class="strip-icon">🌿</span><div><div class="strip-t" data-i18n="strip4_t">Экологичное производство</div><div class="strip-s" data-i18n="strip4_s">CO₂ в 1000 раз меньше</div></div></div>
</div>

<section id="about">
  <div class="about">
    <div class="fi">
      <p class="lbl" data-i18n="about_lbl">О материале</p>
      <h2 class="about-h2" data-i18n-html="about_h2">Что такое<br>Kalesinterflex?</h2>
      <p class="about-p" data-i18n="about_p1">Kalesinterflex — революционный материал для облицовки фасадов и интерьеров. Это первая в Турции крупноформатная порцеляновая плита размером 1000×3000 мм с толщиной от 3 мм, разработанная для самых требовательных архитектурных проектов.</p>
      <p class="about-p" data-i18n="about_p2">Благодаря уникальной технологии производства, материал сочетает исключительную прочность с гибкостью, минимальным весом и безупречной эстетикой. Доступен в матовом, полированном и атласном исполнениях.</p>
      <div class="about-specs">
        <div class="spec"><div class="spec-v" data-i18n="spec1_v">1000×3000 / 1200×3600</div><div class="spec-k" data-i18n="spec1_k">Форматы плит, мм</div></div>
        <div class="spec"><div class="spec-v" data-i18n="spec2_v">3–5 мм</div><div class="spec-k" data-i18n="spec2_k">Толщина для фасадов</div></div>
        <div class="spec"><div class="spec-v" data-i18n="spec3_v">7 кг/м²</div><div class="spec-k" data-i18n="spec3_k">Вес при толщине 3 мм</div></div>
        <div class="spec"><div class="spec-v" data-i18n="spec4_v">A1</div><div class="spec-k" data-i18n="spec4_k">Класс пожарной безопасности</div></div>
      </div>
    </div>
    <div class="img-grid fi">
      <div class="img-cell" style="background-image:url('https://cdn.kale.com.tr/0/0/calcario-collection-line-griege-matte-kalesinterflex-porcelain-slab-162x323/7cb6092d-abcb-4ab1-92e8-8cebaf9f96ba/650/2')"></div>
      <div class="img-cell" style="background-image:url('https://cdn.kale.com.tr/0/0/corten-matte-kalesinterflex-porcelain-slab-162x323/0288734c-7db8-4ff7-9bba-64c14201c177/650/2')"></div>
      <div class="img-cell" style="background-image:url('https://cdn.kale.com.tr/0/0/woodline-matte-cherry-kalesinterflex-porcelain-slab-100x300/446b7062-5cad-4d16-8f18-182df582889a/650/2')"></div>
    </div>
  </div>
</section>

<hr class="sep">

<section class="slab3d">
  <div class="slab3d-inner">
    <div class="sec-head">
      <p class="sec-lbl" data-i18n="slab_lbl">Kalesinterflex · 3 мм</p>
      <h2 class="sec-h2" data-i18n="slab_h2">Тончайшая плита</h2>
    </div>
    <p class="slab3d-hint" data-i18n="slab_sub">Перетащите для вращения</p>
    <div class="slab3d-canvas-wrap">
      <canvas id="slabCanvas"></canvas>
    </div>
    <div class="slab3d-footer">
      <div class="slab3d-label" id="slabLabel">Woodline · Walnut</div>
    </div>
  </div>
</section>

<hr class="sep">

<section class="arnet">
  <div class="arnet-inner">
    <div class="fi">
      <p class="lbl" data-i18n="arnet_lbl">Технология армирования</p>
      <h2 class="arnet-h2" data-i18n="arnet_h2">Система AR-Net</h2>
      <p class="about-p" data-i18n="arnet_p1">Каждая панель Kalesinterflex армирована сеткой AR-Net из щёлочестойкого стекловолокна.</p>
      <p class="about-p" data-i18n="arnet_p2">Система армирования гарантирует структурную целостность панели при ударных нагрузках.</p>
      <div class="arnet-features">
        <div class="arnet-feat">
          <div class="arnet-feat-t" data-i18n="arnet_f1_t">Щёлочестойкость</div>
          <div class="arnet-feat-s" data-i18n="arnet_f1_s">AR-стекловолокно сохраняет прочность в контакте с цементными системами</div>
        </div>
        <div class="arnet-feat">
          <div class="arnet-feat-t" data-i18n="arnet_f2_t">Ударопрочность</div>
          <div class="arnet-feat-s" data-i18n="arnet_f2_s">Структурная целостность при механических воздействиях</div>
        </div>
        <div class="arnet-feat">
          <div class="arnet-feat-t" data-i18n="arnet_f3_t">Долговечность</div>
          <div class="arnet-feat-s" data-i18n="arnet_f3_s">Надёжная работа в условиях переменного климата</div>
        </div>
        <div class="arnet-feat">
          <div class="arnet-feat-t" data-i18n="arnet_f4_t">Безопасность фасада</div>
          <div class="arnet-feat-s" data-i18n="arnet_f4_s">Обязательный стандарт для наружных работ</div>
        </div>
      </div>
    </div>
    <div class="arnet-visual fi">
      <div class="arnet-canvas-wrap">
        <img class="arnet-img" src="data:image/png;base64,{arnet_photo_b64}" alt="AR-Net fibre mesh close-up">
      </div>
      <div class="arnet-canvas-lbl" data-i18n="arnet_canvas_lbl">AR-Net · Армирующая сетка</div>
      <div>
        <div class="arnet-cmp-h" data-i18n="arnet_cmp_h">AR-Net vs E-Net</div>
        <p class="arnet-cmp-note" data-i18n="arnet_cmp_sub">Только AR-Net обеспечивает необходимые характеристики для фасадных систем</p>
        <table class="cmp-table">
          <thead>
            <tr>
              <th></th>
              <th data-i18n="arnet_ar">AR-Net</th>
              <th data-i18n="arnet_en">E-Net (стандарт)</th>
            </tr>
          </thead>
          <tbody>
            <tr><td data-i18n="arnet_c1">Стойкость к щёлочи</td><td data-i18n="arnet_good">✓</td><td data-i18n="arnet_bad">✗</td></tr>
            <tr><td data-i18n="arnet_c2">Адгезия к фасадным клеям</td><td data-i18n="arnet_good">✓</td><td data-i18n="arnet_bad">✗</td></tr>
            <tr><td data-i18n="arnet_c3">Долгосрочная прочность</td><td data-i18n="arnet_good">✓</td><td data-i18n="arnet_bad">✗</td></tr>
            <tr><td data-i18n="arnet_c4">Фасадное применение</td><td data-i18n="arnet_good">✓</td><td data-i18n="arnet_bad">✗</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>

<hr class="sep">

<section class="facade-section" id="facade">
  <div class="facade-inner">
    <div class="sec-head fi">
      <p class="sec-lbl" data-i18n="facade_lbl">Вентилируемый фасад</p>
      <h2 class="sec-h2" data-i18n="facade_h2">Система монтажа · Шаг за шагом</h2>
    </div>
    <div class="facade-canvas-wrap">
      <canvas id="facadeCanvas"></canvas>
    </div>
    <div class="facade-step-info">
      <div class="facade-slabels">
        <div class="facade-slabel on" data-step="0"><div class="facade-slabel-name" data-i18n="facade_s1">Несущая стена</div><div class="facade-slabel-desc" data-i18n="facade_s1d">Кирпичная или бетонная конструкция</div></div>
        <div class="facade-slabel" data-step="1"><div class="facade-slabel-name" data-i18n="facade_s2">L-кронштейны и термопрокладки</div><div class="facade-slabel-desc" data-i18n="facade_s2d">Анкер через термопрокладку в несущую стену</div></div>
        <div class="facade-slabel" data-step="2"><div class="facade-slabel-name" data-i18n="facade_s3">Базальтовая теплоизоляция</div><div class="facade-slabel-desc" data-i18n="facade_s3d">Базальтовые плиты вокруг кронштейнов, крепёж зонтичными дюбелями</div></div>
        <div class="facade-slabel" data-step="3"><div class="facade-slabel-name" data-i18n="facade_s4">Ветрозащитная мембрана</div><div class="facade-slabel-desc" data-i18n="facade_s4d">Паропроницаемая мембрана натянута поверх утеплителя</div></div>
        <div class="facade-slabel" data-step="4"><div class="facade-slabel-name" data-i18n="facade_s5">Вертикальные T-профили</div><div class="facade-slabel-desc" data-i18n="facade_s5d">Алюминиевый T-профиль заклёпками к L-кронштейнам</div></div>
        <div class="facade-slabel" data-step="5"><div class="facade-slabel-name" data-i18n="facade_s6">Лента и клей на полке профиля</div><div class="facade-slabel-desc" data-i18n="facade_s6d">Двусторонняя лента + полиуретановый клей Kalekim на полке</div></div>
        <div class="facade-slabel" data-step="6"><div class="facade-slabel-name" data-i18n="facade_s7">Панели Kalesinterflex</div><div class="facade-slabel-desc" data-i18n="facade_s7d">3 мм · Прижимаются к профилю, лента удерживает до отверждения клея</div></div>
      </div>
      <div class="facade-step-counter"><span data-i18n="facade_step">Шаг</span> <span id="facadeStepNum">1</span> / 7</div>
      <div class="facade-controls">
        <button class="facade-btn" id="facadePrev" disabled data-i18n="facade_prev">← Назад</button>
        <div class="facade-fdots" id="facadeDots"></div>
        <button class="facade-btn" id="facadeNext" data-i18n="facade_next">Далее →</button>
      </div>
    </div>
  </div>
</section>

<hr class="sep">

<section class="collections" id="collections">
  <div class="sec-head fi">
    <p class="sec-lbl" data-i18n="cat_lbl">Каталог 2024</p>
    <h2 class="sec-h2" data-i18n="cat_h2">Коллекции Kalesinterflex</h2>
    <p class="sec-sub" data-i18n="cat_sub">Нажмите «Скачать текстуру» для загрузки изображения в высоком разрешении для использования в проектах.</p>
  </div>
  <div class="filters" id="filters">
    <button class="ftab on" data-f="all" data-i18n="f_all">Все коллекции</button>
    <button class="ftab" data-f="stone" data-i18n="f_stone">Натуральный камень</button>
    <button class="ftab" data-f="cement" data-i18n="f_cement">Цемент</button>
    <button class="ftab" data-f="metal" data-i18n="f_metal">Металл</button>
    <button class="ftab" data-f="solid" data-i18n="f_solid">Однотонные</button>
    <button class="ftab" data-f="wood" data-i18n="f_wood">Дерево</button>
  </div>
  <div class="grid" id="grid">
{cards_html}
  </div>
</section>

<hr class="sep">

<section class="contacts" id="contacts">
  <div class="contacts-inner">
    <div class="sec-head fi">
      <p class="sec-lbl" data-i18n="contacts_lbl">Свяжитесь с нами</p>
      <h2 class="sec-h2" data-i18n="contacts_h2">Контакты NTEK</h2>
      <p class="sec-sub" data-i18n="contacts_sub">Официальный дистрибьютор Kalesinterflex в Кыргызстане. Консультация по материалам, расчёт и доставка.</p>
    </div>
    <div class="contacts-grid fi">
      <div class="contact-card">
        <div class="contact-card-icon"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24"><path fill="#25D366" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg></div>
        <div class="contact-card-label" data-i18n="c_wa_label">WhatsApp</div>
        <a href="https://wa.me/996556442207" target="_blank" class="contact-card-value">+996 556 442 207</a>
        <div class="contact-card-sub" data-i18n="c_wa_sub">Написать в WhatsApp</div>
      </div>
      <div class="contact-card">
        <div class="contact-card-icon">📞</div>
        <div class="contact-card-label" data-i18n="c_ph_label">Телефон</div>
        <a href="tel:+996777420000" class="contact-card-value">+996 777 420 000</a>
        <div class="contact-card-sub" data-i18n="c_ph_sub">Звонки</div>
      </div>
      <div class="contact-card">
        <div class="contact-card-icon"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24"><defs><radialGradient id="ig-rg" cx="30%" cy="107%" r="150%"><stop offset="0%" stop-color="#fdf497"/><stop offset="45%" stop-color="#fd5949"/><stop offset="60%" stop-color="#d6249f"/><stop offset="90%" stop-color="#285AEB"/></radialGradient></defs><rect x="1.5" y="1.5" width="21" height="21" rx="6" ry="6" fill="url(#ig-rg)"/><circle cx="12" cy="12" r="5.2" fill="none" stroke="white" stroke-width="1.8"/><circle cx="17.8" cy="6.2" r="1.3" fill="white"/></svg></div>
        <div class="contact-card-label" data-i18n="c_ig_label">Instagram</div>
        <a href="https://instagram.com/ntek.facade" target="_blank" class="contact-card-value">@ntek.facade</a>
        <div class="contact-card-sub" data-i18n="c_ig_sub">Проекты и новинки</div>
      </div>
      <div class="contact-card">
        <div class="contact-card-icon">📍</div>
        <div class="contact-card-label" data-i18n="c_addr_label">Адрес офиса</div>
        <a href="https://2gis.kg/bishkek/firm/70000001019341726?m=74.592188%2C42.87945%2F16" target="_blank" class="contact-card-value" data-i18n="c_addr_val">Исанова 119</a>
        <div class="contact-card-sub" data-i18n="c_addr_sub">Бишкек, Кыргызстан</div>
      </div>
    </div>
  </div>
</section>

<hr class="sep">

<footer id="footer">
  <div class="ft-inner">
    <div class="ft-top">
      <div>
        <div class="ft-logo">
          <img src="data:{logo_mime};base64,{logo_b64}" alt="NTEK">
        </div>
        <p class="ft-desc" data-i18n="ft_desc">NTEK — официальный дистрибьютор Kalesinterflex в Кыргызстане. Поставки материала для архитектурных, дизайнерских и строительных проектов.</p>
      </div>
      <div>
        <div class="ft-col-h" data-i18n="ft_nav_h">Навигация</div>
        <ul class="ft-list">
          <li><a href="#top" data-i18n="ft_home">Главная</a></li>
          <li><a href="#about" data-i18n="ft_about">О материале</a></li>
          <li><a href="#collections" data-i18n="ft_collections">Коллекции</a></li>
          <li><a href="#contacts" data-i18n="ft_contacts">Контакты</a></li>
        </ul>
      </div>
      <div>
        <div class="ft-col-h" data-i18n="ft_cat_h">Коллекции</div>
        <ul class="ft-list">
          <li><a href="#" onclick="filterBy('stone');return false" data-i18n="ft_stone">Натуральный камень</a></li>
          <li><a href="#" onclick="filterBy('cement');return false" data-i18n="ft_cement">Цемент</a></li>
          <li><a href="#" onclick="filterBy('metal');return false" data-i18n="ft_metal">Металл</a></li>
          <li><a href="#" onclick="filterBy('solid');return false" data-i18n="ft_solid">Однотонные</a></li>
          <li><a href="#" onclick="filterBy('wood');return false" data-i18n="ft_wood">Дерево</a></li>
        </ul>
      </div>
      <div>
        <div class="ft-col-h" data-i18n="ft_contact_h">Контакты</div>
        <div class="ft-contact-row">
          <div class="ft-cl" data-i18n="ft_wa_l">WhatsApp</div>
          <div class="ft-cv"><a href="https://wa.me/996556442207" target="_blank">+996 556 442 207</a></div>
        </div>
        <div class="ft-contact-row">
          <div class="ft-cl" data-i18n="ft_ph_l">Телефон</div>
          <div class="ft-cv"><a href="tel:+996777420000">+996 777 420 000</a></div>
        </div>
        <div class="ft-contact-row">
          <div class="ft-cl" data-i18n="ft_ig_l">Instagram</div>
          <div class="ft-cv"><a href="https://instagram.com/ntek.facade" target="_blank">@ntek.facade</a></div>
        </div>
        <div class="ft-contact-row">
          <div class="ft-cl" data-i18n="ft_addr_l">Адрес</div>
          <div class="ft-cv"><a href="https://2gis.kg/bishkek/firm/70000001019341726?m=74.592188%2C42.87945%2F16" target="_blank" data-i18n="ft_addr_v">Исанова 119, Бишкек</a></div>
        </div>
      </div>
    </div>
    <div class="ft-bottom">
      <span class="ft-copy" data-i18n="ft_copy">&copy; 2024 NTEK. Все права защищены.</span>
      <a href="https://www.kale.com.tr" target="_blank" class="ft-kale-link" data-i18n="ft_kale">Официальный сайт Kale →</a>
    </div>
  </div>
</footer>

<div id="toast"></div>

<script>
{local_imgs_js}
const T = {T_json};
let lang = localStorage.getItem('ntek_lang') || 'ru';

function setLang(l) {{
  lang = l;
  localStorage.setItem('ntek_lang', l);
  document.documentElement.lang = l === 'ky' ? 'ky' : l;

  // plain text
  document.querySelectorAll('[data-i18n]').forEach(el => {{
    const k = el.dataset.i18n;
    if (T[l][k] !== undefined) el.textContent = T[l][k];
  }});
  // html content (headings with <br>/<em>)
  document.querySelectorAll('[data-i18n-html]').forEach(el => {{
    const k = el.dataset.i18nHtml;
    if (T[l][k] !== undefined) el.innerHTML = T[l][k];
  }});
  // page title
  document.title = T[l]['page_title'];

  // language buttons active state
  document.querySelectorAll('.lb').forEach(b => {{
    b.classList.toggle('on', b.textContent.trim().toLowerCase() === (l === 'ky' ? 'кы' : l));
  }});
}}

// init on load
setLang(lang);

// Filter
const tabs = document.querySelectorAll('.ftab');
const cards = document.querySelectorAll('.card');

function filterBy(f) {{
  tabs.forEach(t => t.classList.toggle('on', t.dataset.f === f));
  cards.forEach(c => c.classList.toggle('hide', f !== 'all' && c.dataset.cat !== f));
  document.getElementById('collections').scrollIntoView({{behavior:'smooth'}});
}}
tabs.forEach(tab => tab.addEventListener('click', () => filterBy(tab.dataset.f)));

// Download — uses CORS proxy so the file saves directly instead of opening in a tab
async function downloadTexture(url, filename, btn) {{
  btn.classList.add('busy');
  btn.innerHTML = '<span>⏳</span> ' + T[lang].btn_loading;
  if (url.startsWith('data:')) {{
    try {{
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      showToast(T[lang].toast_done + filename);
    }} finally {{
      btn.classList.remove('busy');
      btn.innerHTML = '<span>↓</span> ' + T[lang].btn_dl;
    }}
    return;
  }}
  const proxy = 'https://corsproxy.io/?url=' + encodeURIComponent(url);
  try {{
    const res = await fetch(proxy);
    if (!res.ok) throw new Error('proxy error');
    const blob = await res.blob();
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(() => URL.revokeObjectURL(a.href), 8000);
    showToast(T[lang].toast_done + filename);
  }} catch(e) {{
    window.open(url, '_blank');
    showToast(T[lang].toast_tab);
  }} finally {{
    btn.classList.remove('busy');
    btn.innerHTML = '<span>↓</span> ' + T[lang].btn_dl;
  }}
}}

// Toast
let toastTimer;
function showToast(msg) {{
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('up');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove('up'), 3400);
}}

// Fade in on scroll
const fi = document.querySelectorAll('.fi');
const io = new IntersectionObserver(entries => {{
  entries.forEach(e => {{ if(e.isIntersecting) {{ e.target.classList.add('v'); io.unobserve(e.target); }} }});
}}, {{threshold:0.1}});
fi.forEach(el => io.observe(el));
</script>
{SLAB_JS}
{FACADE_JS}
</body>
</html>'''

with open('/Users/user/ntek-kalesinterflex/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Done! {len(products)} products, {len(html)} chars")

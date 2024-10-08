import csv

data = [
    ("Paris, Eiffel Kulesi", "https://img.pixers.pics/pho_wat(s3:700/FO/49/90/13/47/700_FO49901347_074bc91718442cbe6199bb180e894b56.jpg,467,700,cms:2018/10/5bd1b6b8d04b8_220x50-watermark.png,over,247,650,jpg)/stickers-eiffel-tower-at-sunrise-paris.jpg.jpg"),
    ("Paris, Louvre Müzesi", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Louvre_Museum_Wikimedia_Commons.jpg/800px-Louvre_Museum_Wikimedia_Commons.jpg"),
    ("Paris, Notre Dame Katedrali", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Notre_Dame_dalla_Senna.jpg/1200px-Notre_Dame_dalla_Senna.jpg"),
    ("Paris, Montmartre", "https://media.tacdn.com/media/attractions-splice-spp-674x446/06/6c/76/07.jpg"),
    ("Paris, Sacré-cœur Bazilikası", "https://upload.wikimedia.org/wikipedia/commons/b/bf/Sacre-coeur-paris.jpg"),
    ("Paris, Champs Élysées", "https://parisjetaime.com/data/layout_image/20120_Vue-a%C3%A9rienne-des-Champs-Elys%C3%A9es--630x405--%C2%A9-iStock.jpg"),
    ("Paris, Moulin Rouge", "https://medias.moulinrouge.fr/wp-content/uploads/2023/12/Facade-BMR-2010-2-%C2%A9Moulin-Rouge%C2%AE-J.Habas_.jpg"),
    ("Paris, Pantheon", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Pantheon_of_Paris_007.JPG/250px-Pantheon_of_Paris_007.JPG"),
    ("Paris, Centre Pompidou", "https://media.cntraveler.com/photos/5a85a096c5f2863a6e7b97d5/16:9/w_2560,c_limit/Centre-Pompidou_2018_GettyImages-535471213.jpg"),
    ("Paris, Saint Louis of Les Invalids Cathedral", "https://upload.wikimedia.org/wikipedia/commons/1/12/0_Cath%C3%A9drale_Saint-Louis-des-Invalides.JPG"),
    ("Londra, Buckingham Sarayı", "https://i.pinimg.com/736x/3d/02/67/3d0267965bbe64a8dc01c4681f2ec53e.jpg"),
    ("Londra, British Museum", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/British_Museum_Great_Court%2C_London%2C_UK_-_Diliff.jpg/2086px-British_Museum_Great_Court%2C_London%2C_UK_-_Diliff.jpg"),
    ("Londra, Tower of London", "https://upload.wikimedia.org/wikipedia/commons/2/2c/Tower_of_London_viewed_from_the_River_Thames.jpg"),
    ("Londra, Tate Modern", "https://upload.wikimedia.org/wikipedia/commons/0/00/Tate_Modern_-_Bankside_Power_Station.jpg"),
    ("Londra, London Eye", "https://www.londoneye.com/media/famji01b/22747_london-eye_1a_pano_0092_98_rgb_ns_licensed_until_jun2025.jpg"),
    ("Londra, Hyde Park", "https://upload.wikimedia.org/wikipedia/commons/f/f3/Hyde_Park_London_from_the_air.jpg"),
    ("Londra, National Gallery", "https://upload.wikimedia.org/wikipedia/commons/d/de/Galer%C3%ADa_Nacional%2C_Londres%2C_Inglaterra%2C_2014-08-07%2C_DD_035.JPG"),
    ("Londra, Covent Garden", "https://upload.wikimedia.org/wikipedia/commons/4/47/Covent_Garden_Piazza_with_London_Transport_Museum_-_geograph.org.uk_-_215169.jpg"),
    ("Londra, Camden Market", "https://wp-media.camdenmarket.com/wp-content/uploads/2023/05/03144145/stables.webp"),
    ("Londra, Royal Borough of Greenwich", "https://diginomica.com/sites/default/files/images/2020-11/C8116709-07DE-44CB-91DF-E0613F595974.jpeg"),
    ("Londra, The Shard", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/The_Shard_in_March_2017_%28cropped%29.jpg/1200px-The_Shard_in_March_2017_%28cropped%29.jpg"),
    ("Roma, Kolezyum", "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=3336825892297028823"),
    ("Roma, Pantheon", "https://upload.wikimedia.org/wikipedia/commons/e/ef/Pantheon_Rom_1_cropped.jpg"),
    ("Roma, Piazza Navona", "https://www.archeoroma.org/wp-content/uploads/2020/02/piazza-navona-roma-558x400.jpg"),
    ("Roma, Sant'Angelo Kalesi", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Engelsburg_und_Engelsbr%C3%BCcke_abends.jpg/800px-Engelsburg_und_Engelsbr%C3%BCcke_abends.jpg"),
    ("Roma, Trastevere", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0f/85/90/fd/bancarelle.jpg?w=1200&h=1200&s=1"),
    ("Roma, Piazza Venezia", "https://www.turismoroma.it/sites/default/files/piazzavenezia.jpg"),
    ("Barselona, Sagrada Família", "https://cdn.britannica.com/15/194815-050-08B5E7D1/Nativity-facade-Sagrada-Familia-cathedral-Barcelona-Spain.jpg"),
    ("Barselona, Park Guell", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Parc_guell_-_panoramio.jpg/800px-Parc_guell_-_panoramio.jpg"),
    ("Barselona, La Rambla", "https://www.shutterstock.com/image-photo/la-rambla-pedestrian-street-barcelona-600nw-2233015419.jpg"),
    ("Barselona, Gothic Quarter", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Barcelona_-_Carrer_del_Bisbe.jpg/640px-Barcelona_-_Carrer_del_Bisbe.jpg"),
    ("Barselona, Camp Nou", "https://media.cntraveler.com/photos/5d1ba00e94f7490008610682/16:9/w_2560,c_limit/Camp_Nou-2019_GettyImages-544827412.jpg"),
    ("Barselona, Port Vell", "https://a.cdn-hotels.com/gdcs/production174/d1795/9b022936-d42a-4ed4-ba8a-6b9e2c461855.jpg"),
    ("Barselona, la Ribera", "https://cdn02.visitbarcelona.com/files/5445-19067-Imagen/La_Ribera_Barcelona_c1.jpg"),
    ("Amsterdam, Rijksmuseum", "https://media.tacdn.com/media/attractions-splice-spp-674x446/12/33/94/d5.jpg"),
    ("Amsterdam, Vondelpark", "https://upload.wikimedia.org/wikipedia/commons/3/3b/Amsterdam%2C_Vondelpark%2C_at_the_pond-2.jpg"),
    ("Amsterdam, Dam Meydanı", "https://cdn.getyourguide.com/img/tour/71221f26fba20b852329db6e11a014709be0101a6e397518cf6ce92a8012fd03.jpg/145.jpg"),
    ("Amsterdam, Rembrandtplein", "https://upload.wikimedia.org/wikipedia/commons/d/d7/NieuwRembrandtplein.JPG"),
    ("Amsterdam, Beurs van Berlage", "https://beursvanberlage.com/app/uploads/2022/04/20220329_Beurs_van_Berlage_Booking_080_42718.jpg"),
    ("Amsterdam, Hortus Botanicus", "https://img.atlasobscura.com/bKA0VF-MIs4qk0Ps94D1sFkTyoLxNUCWEF00Lc6figI/rt:fit/w:600/c:3024:2016:nowe:0:1429/q:81/sm:1/scp:1/ar:1/aHR0cHM6Ly9hdGxh/cy1kZXYuczMuYW1h/em9uYXdzLmNvbS91/cGxvYWRzL3BsYWNl/X2ltYWdlcy9hYjFh/MGExZC0yN2QzLTQ2/ZmUtOGM2OS1jYTA0/YmVkMTEwY2M2N2Ji/ODNhMGZlNmMyYzJm/MDBfMzc2QTg4Q0It/OEU2NS00NkQxLTkx/RTgtQ0VBMkMzMTlB/NDg4LmpwZWc.jpg"),
    ("New York, Times Square", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/New_york_times_square-terabass.jpg/1200px-New_york_times_square-terabass.jpg"),
    ("New York, Central Park", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Global_Citizen_Festival_Central_Park_New_York_City_from_NYonAir_%2815351915006%29.jpg/300px-Global_Citizen_Festival_Central_Park_New_York_City_from_NYonAir_%2815351915006%29.jpg"),
    ("New York, Empire State Building", "https://upload.wikimedia.org/wikipedia/commons/1/10/Empire_State_Building_%28aerial_view%29.jpg"),
    ("New York, Statue of Liberty", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Lady_Liberty_under_a_blue_sky_%28cropped%29.jpg/1200px-Lady_Liberty_under_a_blue_sky_%28cropped%29.jpg"),
    ("New York, Rockefeller Center", "https://cdn.sanity.io/images/bs9rmafh/main/35cd754a5a600d0ba4432fde38b9cfe8a7423dea-1600x1067.webp?w=800&h=534&fit=crop"),
    ("New York, One World Trade Center", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/One_World_Trade_Center_%28cropped_9_to_16%29.jpg/250px-One_World_Trade_Center_%28cropped_9_to_16%29.jpg"),
    ("Tokyo, Tokyo Disneyland Hotel", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/15/cc/59/4b/caption.jpg?w=700&h=-1&s=1"),
    ("Tokyo, Ueno Park", "https://www.japan-guide.com/g18/3019_02.jpg"),
    ("Tokyo, Tokyo Skytree", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Tokyo_Skytree_2023.jpg/1200px-Tokyo_Skytree_2023.jpg"),
    ("Tokyo, Odaiba", "https://www.japan-guide.com/g18/3008_01.jpg"),
    ("Tokyo, Tokyo Metropolitan Government Main Building 1", "https://www.japantimes.co.jp/japantimes/uploads/images/2024/02/07/279362.jpg"),
    ("Tokyo, Akihabara", "https://cdn.cheapoguides.com/wp-content/uploads/sites/2/2020/05/akihabara-iStock-484915982-1024x600.jpg")
]

# CSV dosyasına verileri yazma
with open('yerler.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Başlık satırını yazma
    writer.writerow(["Konum", "Link"])
    # Veri satırlarını yazma
    writer.writerows(data)

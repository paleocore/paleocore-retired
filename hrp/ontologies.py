BASIS_OF_RECORD_VOCABULARY = (("FossilSpecimen", "Fossil"), ("HumanObservation", "Observation"))
HRP_BASIS_OF_RECORD_VOCABULARY = (("Collection", "Collection"), ("Observation", "Observation"))
ITEM_TYPE_VOCABULARY = (
    ("Artifactual", "Artifactual"),
    ("Faunal", "Faunal"),
    ("Floral", "Floral"),
    ("Geological", "Geological")
)

COLLECTING_METHOD_VOCABULARY = (("Surface Standard", "Surface Standard"),
                                ("Surface Intensive", "Surface Intensive"),
                                ("Surface Complete", "Surface Complete"),
                                ("Exploratory Survey", "Exploratory Survey"),
                                ("Dry Screen 5mm", "Dry Screen 5mm"),
                                ("Dry Screen 2mm", "Dry Screen 2mm"),
                                ("Wet Screen 1mm", "Wet Screen 1mm"))

HRP_COLLECTING_METHOD_VOCABULARY = (("Survey", "Survey"),
                                    ("dryscreen5mm", "dryscreen5mm"),
                                    ("wetscreen1mm", "wetscreen1mm"))

COLLECTOR_CHOICES = (("Zeresenay Alemseged", "Zeresenay Alemseged"),
                     ("Andrew Barr", "Andrew Barr"),
                     ("Rene Bobe", "Rene Bobe"),
                     ("Denis Geraads", "Denis Geraads"),
                     ("Weldeyared Hailu", "Waldeyared Hailu"),
                     ("Shannon McPherron", "Shannon McPherron"),
                     ("Denne Reed", "Denne Reed"),
                     ("Jonathan Wynn", "Jonathan Wynn"))

HRP_COLLECTOR_CHOICES = (("C.J. Campisano", "C.J. Campisano"),
                         ("W.H. Kimbel", "W.H. Kimbel"),
                         ("T.K. Nalley", "T.K. Nalley"),
                         ("D.N. Reed", "D.N. Reed"),
                         ("K.E. Reed", "K.E. Reed"),
                         ("B.J. Schoville", "B.J. Schoville"),
                         ("A.E. Shapiro", "A.E. Shapiro"),
                         ("HFS Student", "HFS Student"),
                         ("HRP Team", "HRP Team"),
                         ("Afar Team", "Afar Team"),
                         )

HRP_IDENTIFIER_CHOICES = (('Z. Alemseged', 'Z. Alemseged'),
                          ('R.L. Bernor', 'R.L. Bernor'),
                          ('R. Bobe-Quinteros', 'R. Bobe-Quinteros'),
                          ('P. Brodkorb', 'P. Brodkorb'),
                          ('H.B.S. Cooke', 'H.B.S. Cooke'),
                          ('E. Delson', 'E. Delson'),
                          ('C. Denys', 'C. Denys'),
                          ('G.G. Eck', 'G.G. Eck'),
                          ('V. Eisenmann', 'V. Eisenmann'),
                          ('N. Fessaha', 'N. Fessaha'),
                          ('L.J. Flynn', 'L.J. Flynn'),
                          ('S.R. Frost', 'S.R. Frost'),
                          ('A.W. Gentry', 'A.W. Gentry'),
                          ('D. Geraads', 'D. Geraads'),
                          ('R. Geze', 'R. Geze'),
                          ('F.C. Howell', 'F.C. Howell'),
                          ('Institute Staff', 'Institute Staff'),
                          ('D.C. Johanson', 'D.C. Johanson'),
                          ('W.H. Kimbel', 'W.H. Kimbel'),
                          ('H.B. Krentza', 'H.B. Krentza'),
                          ('B.M. Latimer', 'B.M. Latimer'),
                          ('M.E. Lewis', 'M.E. Lewis'),
                          ('C.A. Lockwood', 'C.A. Lockwood'),
                          ('T.K. Nalley', 'T.K. Nalley'),
                          ('G. Petter', 'G. Petter'),
                          ('J.C. Rage', 'J.C. Rage'),
                          ('D. Reed', 'D. Reed'),
                          ('K.E. Reed', 'K.E. Reed'),
                          ('J. Rowan', 'J. Rowan'),
                          ('M. Sabatier', 'M. Sabatier'),
                          ('B.J. Schoville', 'B.J. Schoville'),
                          ('A.E. Shapiro', 'A.E. Shapiro'),
                          ('G. Suwa', 'G. Suwa'),
                          ('E.S. Vrba', 'E.S. Vrba'),
                          ('L.A. Werdelin', 'L.A. Werdelin'),
                          ('H.B. Wesselman', 'H.B. Wesselman'),
                          ('T.D. White', 'T.D. White'),
                          )

HRP_COLLECTION_CODES = (("A.L.", "A.L."),)

SIDE_VOCABULARY = (("Left", "Left"),
                   ("Right", "Right"),
                   ("Both", "Both"),
                   ("Axial", "Axial"),  # a median, unsided element
                   ("Unknown", "Unknown"))

SKULL_BONES = (("complete skull", "complete skull"),
               ("partial skull", "partial skull"),
               ("temporal", "temporal"),
               ("frontal", "frontal"),  # a median, unsided element
               ("occipital", "occipital"),
               ("parietal", "parietal"))

VERTEBRATE_CLASSES = (("Mammalia", "Mammalia"),
                      ("Reptilia", "Reptilia"),
                      ("Aves", "Aves"),
                      ("Pisces", "Pisces"),
                      ("Amphibia", "Amphibia"),
                      ("Assorted", "Assorted"))

MAMMALIAN_ORDERS = (("Primates", "Primates"),
                    ("Condylarthra", "Condylarthra"),
                    ("Perissodactyla", "Perissodactyla"),
                    ("Artiodactyla", "Artiodactyla"),
                    ("Rodentia", "Rodentia"),
                    ("Carnivora", "Carnivora"),
                    ("Creodonta", "Creodonta"),
                    ("Insectivora", "Insectivora"),
                    ("Lipotyphyla", "Lipotyphyla"),
                    ("Tillodontia", "Tillodontia"),
                    ("Mammalia indet.", "Mammalia indet."),
                    ("Pantodonta", "Pantodonta"),
                    ("Marsupialia", "Marsupialia"),
                    ("Cimolesta", "Cimolesta"),
                    ("Multituberculata", "Multituberculata"))

UPPER_TEETH = (("Incisor/", "Incisor/"),
               ("I1/", "I1/"),
               ("I2/", "I2/"),
               ("I3/", "I3/"),
               ("I4/", "I4/"),
               ("Canine/", "Canine/"),
               ("Premolar/", "Premolar/"),
               ("P1/", "P1/"),
               ("P2/", "P2/"),
               ("P3/", "P3/"),
               ("P4/", "P4/"),
               ("Molar/", "Molar/"),
               ("M1/", "M1/"),
               ("M2/", "M2/"),
               ("M2/", "M2/"),
               ("M3/", "M3/"))

LOWER_TEETH = (("/Incisor", "/Incisor"),
               ("I/1", "I/1"),
               ("I/2", "I/2"),
               ("I/3", "I/3"),
               ("I/4", "I/4"),
               ("/Canine", "/Canine"),
               ("/Premolar", "/Premolar"),
               ("P/1", "P/1"),
               ("P/2", "P/2"),
               ("P/3", "P/3"),
               ("P/4", "P/4"),
               ("/Molar", "/Molar"),
               ("M/1", "M/1"),
               ("M/2", "M/2"),
               ("M/2", "M/2"),
               ("M/3", "M/3"))

FORELIMB_ELEMENTS = (("scapula", "scapula"),
                     ("humerus", "humerus"),
                     ("distal humerus", "distal humerus"),
                     ("proximal humerus", "proximal humerus"),
                     ("humeral shaft", "humeral shaft"),
                     ("radius", "radius"),
                     ("distal radius", "distal radius"),
                     ("proximal radius", "proximal radius"),
                     ("ulna", "ulna"),
                     ("distal ulna", "distal ulna"),
                     ("proximal ulna", "proximal ulna"),
                     ("carpal element", "carpal element"),
                     ("podial", "podial"))

HINDLIMB_ELEMENTS = (("pelvis", "pelvis"),
                     ("ischium", "ischium"),
                     ("ilium", "ilium"),
                     ("pubis", "pubis"),
                     ("femur", "femur"),
                     ("distal femur", "distal femur"),
                     ("proximal femur", "proximal femur"),
                     ("tibia", "tibia"),
                     ("distal tibia", "distal tibia"),
                     ("proiximal tibia", "proiximal tibia"),
                     ("fibula", "fibula"),
                     ("distal fibula", "distal fibula"),
                     ("proximal fibula", "proximal fibula"),
                     ("tarsal element", "tarsal element"),
                     ("astragalus", "astragalus"),
                     ("calcaneus", "calcaneus"),
                     ("cuboid", "cuboid"),
                     ("podial", "podial"))

MANDIBLE = (("edentulous mandible", "edentulous mandible"),
            ("symphysis", "symphysis"),
            ("condyle", "condyle"),
            ("With teeth", "With teeth"))

MAXILLA = (("edentulous", "edentulous"),
           ("With teeth", "With teeth"))

VERTEBRAE = (("caudal", "caudal"),
             ("lumbar", "lumbar"),
             ("thoracic", "thoracic"),
             ("cervical", "cervical"),
             ("unidentified", "unidentified"))

MISCELLANEOUS = (("tooth", "tooth"),
                 ("bone", "bone"),
                 ("tooth fragment", "tooth fragment"),
                 ("bone fragment", "bone fragment"),
                 ("cranial fragment", "cranial fragment"),
                 ("carapace", "carapace"),
                 ("dermal element", "dermal element"))

TIME_OF_DAY = (("AM", "AM"),
               ("PM", "PM"))

GNATHIC = (("mandible with teeth", "mandible with teeth"),
           ("edentulous mandible", "edentulous mandible"),
           ("maxilla with teeth", "maxilla with teeth"),
           ("edentulous maxilla", "edentulous maxilla"),
           ("mandibular symphysis", "mandibular symphysis"),
           ("mandibular condyle", "mandibular condyle"))

NALMA_CHOICES = (("Wasatchian", "Wasatchian"),
                 ("Clarkforkian", "Clarkforkian"))

CONTINENT_CHOICES = (("Africa", "Africa"), ("Europe", "Europe"), ("Asia", "Asia"), ("North America", "North America"),
                     ("South America", "South America"), ("Australia", "Australia"), ("Antarctica", "Antarctica"))

REGION_CHOICES = (("southern_africa", "southern Africa"), ("eastern_africa", "eastern Africa"),
                  ("northern_africa", "northern Africa"), ("", ""), ("", ""))

EPOCH_CHOICES = (("Pliocene", "Pliocene"), ("Pleistocene", "Pleistocene"), ("Holocene", "Holocene"))

MATERIAL_CHOICES = (("basketry", "basketry"), ("building material", "building material"), ("ceramic", "ceramic"),
                    ("chipped stone", "chipped stone"), ("dating sample", "dating sample"),
                    ("fauna", "fauna"), ("fire-cracked rock", "fire-cracked rock"), ("glass", "glass"),
                    ("ground stone", "ground stone"), ("hide", "hide"), ("human remains", "human remains"),
                    ("macrobotanical", "macrobotanical"), ("metal", "metal"), ("mineral", "mineral"),
                    ("pollen", "pollen"), ("shell", "shell"), ("textile", "textile"),
                    ("wood", "wood"))  # Choice list comes from tDAR"

SETTING_CHOICES = (("open-air", "open-air"), ("cave", "cave"), ("rockshelter", "rockshelter"))

HRP_ELEMENT_STANDARD = (
    ('astragalus', 'astragalus'),
    ('bacculum', 'bacculum'),
    ('bone (indet.)', 'bone (indet.)'),
    ('calcaneus', 'calcaneus'),
    ('canine', 'canine'),
    ('capitate', 'capitate'),
    ('carapace', 'carapace'),
    ('carpal (indet.)', 'carpal (indet.)'),
    ('carpal/tarsal', 'carpal/tarsal'),
    ('carpometacarpus', 'carpometacarpus'),
    ('carpus', 'carpus'),
    ('chela', 'chela'),
    ('clavicle', 'clavicle'),
    ('coccyx', 'coccyx'),
    ('coprolite', 'coprolite'),
    ('cranium', 'cranium'),
    ('cranium w/horn core', 'cranium w/horn core'),
    ('cuboid', 'cuboid'),
    ('cubonavicular', 'cubonavicular'),
    ('cuneiform', 'cuneiform'),
    ('dermal plate', 'dermal plate'),
    ('egg shell', 'egg shell'),
    ('endocast', 'endocast'),
    ('ethmoid', 'ethmoid'),
    ('femur', 'femur'),
    ('fibula', 'fibula'),
    ('frontal', 'frontal'),
    ('hamate', 'hamate'),
    ('horn core', 'horn core'),
    ('humerus', 'humerus'),
    ('hyoid', 'hyoid'),
    ('Ilium', 'Ilium'),
    ('incisor', 'incisor'),
    ('innominate', 'innominate'),
    ('ischium', 'ischium'),
    ('lacrimal', 'lacrimal'),
    ('long bone ', 'long bone '),
    ('lunate', 'lunate'),
    ('mandible', 'mandible'),
    ('manus', 'manus'),
    ('maxilla', 'maxilla'),
    ('metacarpal', 'metacarpal'),
    ('metapodial', 'metapodial'),
    ('metatarsal', 'metatarsal'),
    ('molar', 'molar'),
    ('nasal', 'nasal'),
    ('navicular', 'navicular'),
    ('naviculocuboid', 'naviculocuboid'),
    ('occipital', 'occipital'),
    ('ossicone', 'ossicone'),
    ('parietal', 'parietal'),
    ('patella', 'patella'),
    ('pes', 'pes'),
    ('phalanx', 'phalanx'),
    ('pisiform', 'pisiform'),
    ('plastron', 'plastron'),
    ('premaxilla', 'premaxilla'),
    ('premolar', 'premolar'),
    ('pubis', 'pubis'),
    ('radioulna', 'radioulna'),
    ('radius', 'radius'),
    ('rib', 'rib'),
    ('sacrum', 'sacrum'),
    ('scaphoid', 'scaphoid'),
    ('scapholunar', 'scapholunar'),
    ('scapula', 'scapula'),
    ('scute', 'scute'),
    ('sesamoid', 'sesamoid'),
    ('shell', 'shell'),
    ('skeleton', 'skeleton'),
    ('skull', 'skull'),
    ('sphenoid', 'sphenoid'),
    ('sternum', 'sternum'),
    ('talon', 'talon'),
    ('talus', 'talus'),
    ('tarsal (indet.)', 'tarsal (indet.)'),
    ('tarsometatarsus', 'tarsometatarsus'),
    ('tarsus', 'tarsus'),
    ('temporal', 'temporal'),
    ('tibia', 'tibia'),
    ('tibiotarsus', 'tibiotarsus'),
    ('tooth (indet.)', 'tooth (indet.)'),
    ('trapezium', 'trapezium'),
    ('trapezoid', 'trapezoid'),
    ('triquetrum', 'triquetrum'),
    ('ulna', 'ulna'),
    ('vertebra', 'vertebra'),
    ('vomer', 'vomer'),
    ('zygomatic', 'zygomatic'),
)

HRP_ELEMENT_ADDITIONAL = (('pharyngeal teeth', 'pharyngeal teeth'),
                          ('molars', 'molars'),
                          ('tusk', 'tusk'),
                          ('horn corn', 'horn corn'),
                          ('spine', 'spine'),
                          ('silicified wood', 'silicified wood'),
                          ('dentary', 'dentary'),
                          ('cleithrum', 'cleithrum'),
                          ('skull plate', 'skull plate'),
                          ('basicranium', 'basicranium'),
                          ('angulararticular', 'angulararticular'),
                          ('ribs', 'ribs'),
                          ('lateral ethmoid', 'lateral ethmoid'),
                          ('pterotic', 'pterotic'),
                          ('tooth roots', 'tooth roots'),
                          ('shells', 'shells'),
                          ('pharyngeal tooth', 'pharyngeal tooth'),
                          ('ilium', 'ilium'),
                          ('hemimandible', 'hemimandible'),
                          ('pectoral spine', 'pectoral spine'),
                          ('palate', 'palate'),
                          ('pelvis', 'pelvis'),
                          ('long bone', 'long bone'),
                          ('axis', 'axis'),
                          ('acetabulum', 'acetabulum'),
                          ('magnum', 'magnum'),
                          ('hemi-mandible', 'hemi-mandible'),
                          ('weberian', 'weberian'),
                          ('supraoccipital', 'supraoccipital'),
                          ('anguloarticular', 'anguloarticular')
                          )

HRP_ELEMENT_CHOICES = HRP_ELEMENT_STANDARD + HRP_ELEMENT_ADDITIONAL

HRP_ELEMENT_PORTION_CHOICES = (
    ('almost complete', 'almost complete'),
    ('anterior', 'anterior'),
    ('basal', 'basal'),
    ('complete', 'complete'),
    ('diaphysis', 'diaphysis'),
    ('diaphysis+distal', 'diaphysis+distal'),
    ('diaphysis+proximal', 'diaphysis+proximal'),
    ('distal', 'distal'),
    ('dorsal', 'dorsal'),
    ('epiphysis', 'epiphysis'),
    ('fragment', 'fragment'),
    ('fragments', 'fragments'),
    ('indeterminate', 'indeterminate'),
    ('lateral', 'lateral'),
    ('medial', 'medial'),
    ('midsection', 'midsection'),
    ('midsection+basal', 'midsection+basal'),
    ('midsection+distal', 'midsection+distal'),
    ('posterior', 'posterior'),
    ('proximal', 'proximal'),
    ('symphysis', 'symphysis'),
    ('ventral', 'ventral'),
)

HRP_ELEMENT_NUMBER_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('3(medial)', '3(medial)'),
    ('4', '4'),
    ('4(lateral)', '4(lateral)'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('2-7', '2-7'),
    ('8-12', '8-12'),
    ('indeterminate', 'indeterminate'),
)

HRP_ELEMENT_MODIFIER_CHOICES = (
    ('articulated', 'articulated'),
    ('caudal', 'caudal'),
    ('cervical', 'cervical'),
    ('coccygeal', 'coccygeal'),
    ('distal', 'distal'),
    ('intermediate', 'intermediate'),
    ('lower', 'lower'),
    ('lumbar', 'lumbar'),
    ('manual', 'manual'),
    ('manual distal', 'manual distal'),
    ('manual intermediate', 'manual intermediate'),
    ('manual proximal', 'manual proximal'),
    ('pedal', 'pedal'),
    ('pedal distal', 'pedal distal'),
    ('pedal intermediate', 'pedal intermediate'),
    ('pedal proximal', 'pedal proximal'),
    ('proximal', 'proximal'),
    ('sacral', 'sacral'),
    ('thoracic', 'thoracic'),
    ('upper', 'upper'),
    ('indeterminate', 'indeterminate')
)

HRP_SIDE_CHOICES = (
    (u'L', u'L'),
    (u'R', u'R'),
    (u'Indeterminate', u'Indeterminate'),
    (u'L+R', u'L+R')
)

COUNTRY_CHOICES = (
    ('United States of America', 'United States of America'),
    ('Afghanistan', 'Afghanistan'),
    ('Aland Islands', 'Aland Islands'),
    ('Albania', 'Albania'),
    ('Algeria', 'Algeria'),
    ('American Samoa', 'American Samoa'),
    ('Andorra', 'Andorra'),
    ('Angola', 'Angola'),
    ('Anguilla', 'Anguilla'),
    ('Antigua and Barbuda', 'Antigua and Barbuda'),
    ('Argentina', 'Argentina'),
    ('Armenia', 'Armenia'),
    ('Aruba', 'Aruba'),
    ('Australia', 'Australia'),
    ('Austria', 'Austria'),
    ('Azerbaijan', 'Azerbaijan'),
    ('Bahamas', 'Bahamas'),
    ('Bahrain', 'Bahrain'),
    ('Bangladesh', 'Bangladesh'),
    ('Barbados', 'Barbados'),
    ('Belarus', 'Belarus'),
    ('Belgium', 'Belgium'),
    ('Belize', 'Belize'),
    ('Benin', 'Benin'),
    ('Bermuda', 'Bermuda'),
    ('Bhutan', 'Bhutan'),
    ('Bolivia', 'Bolivia'),
    ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
    ('Botswana', 'Botswana'),
    ('Brazil', 'Brazil'),
    ('British Virgin Islands', 'British Virgin Islands'),
    ('Brunei Darussalam', 'Brunei Darussalam'),
    ('Bulgaria', 'Bulgaria'),
    ('Burkina Faso', 'Burkina Faso'),
    ('Burundi', 'Burundi'),
    ('Cambodia', 'Cambodia'),
    ('Cameroon', 'Cameroon'),
    ('Canada', 'Canada'),
    ('Cape Verde', 'Cape Verde'),
    ('Cayman Islands', 'Cayman Islands'),
    ('Central African Republic', 'Central African Republic'),
    ('Chad', 'Chad'),
    ('Channel Islands', 'Channel Islands'),
    ('Chile', 'Chile'),
    ('China', 'China'),
    ('China - Hong Kong', 'China - Hong Kong'),
    ('China - Macao', 'China - Macao'),
    ('Colombia', 'Colombia'),
    ('Comoros', 'Comoros'),
    ('Congo', 'Congo'),
    ('Cook Islands', 'Cook Islands'),
    ('Costa Rica', 'Costa Rica'),
    ('Cote d\'Ivoire', 'Cote d\'Ivoire'),
    ('Croatia', 'Croatia'),
    ('Cuba', 'Cuba'),
    ('Cyprus', 'Cyprus'),
    ('Czech Republic', 'Czech Republic'),
    ('Democratic People\'s Republic of Korea', 'Democratic People\'s Republic of Korea'),
    ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'),
    ('Denmark', 'Denmark'),
    ('Djibouti', 'Djibouti'),
    ('Dominica', 'Dominica'),
    ('Dominican Republic', 'Dominican Republic'),
    ('Ecuador', 'Ecuador'),
    ('Egypt', 'Egypt'),
    ('El Salvador', 'El Salvador'),
    ('Equatorial Guinea', 'Equatorial Guinea'),
    ('Eritrea', 'Eritrea'),
    ('Estonia', 'Estonia'),
    ('Ethiopia', 'Ethiopia'),
    ('Faeroe Islands', 'Faeroe Islands'),
    ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'),
    ('Fiji', 'Fiji'),
    ('Finland', 'Finland'),
    ('France', 'France'),
    ('French Guiana', 'French Guiana'),
    ('French Polynesia', 'French Polynesia'),
    ('Gabon', 'Gabon'),
    ('Gambia', 'Gambia'),
    ('Georgia', 'Georgia'),
    ('Germany', 'Germany'),
    ('Ghana', 'Ghana'),
    ('Gibraltar', 'Gibraltar'),
    ('Greece', 'Greece'),
    ('Greenland', 'Greenland'),
    ('Grenada', 'Grenada'),
    ('Guadeloupe', 'Guadeloupe'),
    ('Guam', 'Guam'),
    ('Guatemala', 'Guatemala'),
    ('Guernsey', 'Guernsey'),
    ('Guinea', 'Guinea'),
    ('Guinea-Bissau', 'Guinea-Bissau'),
    ('Guyana', 'Guyana'),
    ('Haiti', 'Haiti'),
    ('Holy See (Vatican City)', 'Holy See (Vatican City)'),
    ('Honduras', 'Honduras'),
    ('Hungary', 'Hungary'),
    ('Iceland', 'Iceland'),
    ('India', 'India'),
    ('Indonesia', 'Indonesia'),
    ('Iran', 'Iran'),
    ('Iraq', 'Iraq'),
    ('Ireland', 'Ireland'),
    ('Isle of Man', 'Isle of Man'),
    ('Israel', 'Israel'),
    ('Italy', 'Italy'),
    ('Jamaica', 'Jamaica'),
    ('Japan', 'Japan'),
    ('Jersey', 'Jersey'),
    ('Jordan', 'Jordan'),
    ('Kazakhstan', 'Kazakhstan'),
    ('Kenya', 'Kenya'),
    ('Kiribati', 'Kiribati'),
    ('Kuwait', 'Kuwait'),
    ('Kyrgyzstan', 'Kyrgyzstan'),
    ('Lao People\'s Democratic Republic', 'Lao People\'s Democratic Republic'),
    ('Latvia', 'Latvia'),
    ('Lebanon', 'Lebanon'),
    ('Lesotho', 'Lesotho'),
    ('Liberia', 'Liberia'),
    ('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'),
    ('Liechtenstein', 'Liechtenstein'),
    ('Lithuania', 'Lithuania'),
    ('Luxembourg', 'Luxembourg'),
    ('Macedonia', 'Macedonia'),
    ('Madagascar', 'Madagascar'),
    ('Malawi', 'Malawi'),
    ('Malaysia', 'Malaysia'),
    ('Maldives', 'Maldives'),
    ('Mali', 'Mali'),
    ('Malta', 'Malta'),
    ('Marshall Islands', 'Marshall Islands'),
    ('Martinique', 'Martinique'),
    ('Mauritania', 'Mauritania'),
    ('Mauritius', 'Mauritius'),
    ('Mayotte', 'Mayotte'),
    ('Mexico', 'Mayotte'),
    ('Micronesia, Federated States of', 'Micronesia, Federated States of'),
    ('Monaco', 'Monaco'),
    ('Mongolia', 'Mongolia'),
    ('Montenegro', 'Montenegro'),
    ('Montserrat', 'Montserrat'),
    ('Morocco', 'Morocco'),
    ('Mozambique', 'Mozambique'),
    ('Myanmar', 'Myanmar'),
    ('Namibia', 'Namibia'),
    ('Nauru', 'Nauru'),
    ('Nepal', 'Nepal'),
    ('Netherlands', 'Netherlands'),
    ('Netherlands Antilles', 'Netherlands Antilles'),
    ('New Caledonia', 'New Caledonia'),
    ('New Zealand', 'New Zealand'),
    ('Nicaragua', 'Nicaragua'),
    ('Niger', 'Niger'),
    ('Nigeria', 'Nigeria'),
    ('Niue', 'Niue'),
    ('Norfolk Island', 'Norfolk Island'),
    ('Northern Mariana Islands', 'Northern Mariana Islands'),
    ('Norway', 'Norway'),
    ('Occupied Palestinian Territory', 'Occupied Palestinian Territory'),
    ('Oman', 'Oman'),
    ('Pakistan', 'Pakistan'),
    ('Palau', 'Palau'),
    ('Panama', 'Panama'),
    ('Papua New Guinea', 'Papua New Guinea'),
    ('Paraguay', 'Paraguay'),
    ('Peru', 'Peru'),
    ('Philippines', 'Philippines'),
    ('Pitcairn', 'Pitcairn'),
    ('Poland', 'Poland'),
    ('Portugal', 'Portugal'),
    ('Puerto Rico', 'Puerto Rico'),
    ('Qatar', 'Qatar'),
    ('Republic of Korea', 'Republic of Korea'),
    ('Republic of Moldova', 'Republic of Moldova'),
    ('Reunion', 'Reunion'),
    ('Romania', 'Romania'),
    ('Russian Federation', 'Russian Federation'),
    ('Rwanda', 'Rwanda'),
    ('Saint-Barthelemy', 'Saint-Barthelemy'),
    ('Saint Helena', 'Saint Helena'),
    ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
    ('Saint Lucia', 'Saint Lucia'),
    ('Saint-Martin (French part)', 'Saint-Martin (French part)'),
    ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'),
    ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
    ('Samoa', 'Samoa'),
    ('San Marino', 'San Marino'),
    ('Sao Tome and Principe', 'Sao Tome and Principe'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Senegal', 'Senegal'),
    ('Serbia', 'Serbia'),
    ('Seychelles', 'Seychelles'),
    ('Sierra Leone', 'Sierra Leone'),
    ('Singapore', 'Singapore'),
    ('Slovakia', 'Slovakia'),
    ('Slovenia', 'Slovenia'),
    ('Solomon Islands', 'Solomon Islands'),
    ('Somalia', 'Somalia'),
    ('South Africa', 'South Africa'),
    ('Spain', 'Spain'),
    ('Sri Lanka', 'Sri Lanka'),
    ('Sudan', 'Sudan'),
    ('Suriname', 'Suriname'),
    ('Svalbard and Jan Mayen Islands', 'Svalbard and Jan Mayen Islands'),
    ('Swaziland', 'Swaziland'),
    ('Sweden', 'Sweden'),
    ('Switzerland', 'Switzerland'),
    ('Syrian Arab Republic', 'Syrian Arab Republic'),
    ('Tajikistan', 'Tajikistan'),
    ('Thailand', 'Thailand'),
    ('Timor-Leste', 'Timor-Leste'),
    ('Togo', 'Togo'),
    ('Tokelau', 'Tokelau'),
    ('Tonga', 'Tonga'),
    ('Trinidad and Tobago', 'Trinidad and Tobago'),
    ('Tunisia', 'Tunisia'),
    ('Turkey', 'Turkey'),
    ('Turkmenistan', 'Turkmenistan'),
    ('Turks and Caicos Islands', 'Turks and Caicos Islands'),
    ('Tuvalu', 'Tuvalu'),
    ('Uganda', 'Uganda'),
    ('Ukraine', 'Ukraine'),
    ('United Arab Emirates', 'United Arab Emirates'),
    ('United Kingdom', 'United Kingdom'),
    ('United Republic of Tanzania', 'United Republic of Tanzania'),
    ('United States of America', 'United States of America'),
    ('United States Virgin Islands', 'United States Virgin Islands'),
    ('Uruguay', 'Uruguay'),
    ('Uzbekistan', 'Uzbekistan'),
    ('Vanuatu', 'Vanuatu'),
    ('Venezuela (Bolivarian Republic of)', 'Venezuela (Bolivarian Republic of)'),
    ('Viet Nam', 'Viet Nam'),
    ('Wallis and Futuna Islands', 'Wallis and Futuna Islands'),
    ('Western Sahara', 'Western Sahara'),
    ('Yemen', 'Yemen'),
    ('Zambia', 'Zambia'),
    ('Zimbabwe', 'Zimbabwe'),
)

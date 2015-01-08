
BASIS_OF_RECORD_VOCABULARY = (("FossilSpecimen", "Fossil"), ("HumanObservation", "Observation"))
ITEM_TYPE_VOCABULARY = (("Artifactual", "Artifactual"), ("Faunal", "Faunal"), ("Floral", "Floral"), ("Geological", "Geological"))
COLLECTING_METHOD_VOCABULARY = (("Surface Standard", "Surface Standard"),
                                ("Surface Intensive", "Surface Intensive"),
                                ("Surface Complete", "Surface Complete"),
                                ("Exploratory Survey", "Exploratory Survey"),
                                ("Dry Screen 5mm", "Dry Screen 5mm"),
                                ("Dry Screen 2mm", "Dry Screen 2mm"),
                                ("Wet Screen 1mm", "Wet Screen 1mm"))

COLLECTOR_CHOICES = (("Zeresenay Alemseged", "Zeresenay Alemseged"),
                     ("Rene Bobe", "Rene Bobe"),
                     ("Denis Geraads", "Denis Geraads"),
                     ("Shannon McPherron", "Shannon McPherron"),
                     ("Denne Reed", "Denne Reed"),
                     ("Jonathan Wynn", "Jonathan Wynn"))

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
                   ("Reptilia", "Reptilia"),
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
























































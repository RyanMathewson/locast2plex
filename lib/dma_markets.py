
# from https://gist.github.com/sillypog/4080120
major_cities = [
    {'fcc_dma_str': 'SHERMAN-ADA', 'city': 'Ada', 'dma_code': 657, 'latitude': 34.774531000000003, 'longitude': -96.678344899999999, 'region': 'OK', 'slug': 'ada-ok'},
    {'fcc_dma_str': 'CLEVELAND-AKRON (CANTON)', 'city': 'Akron', 'dma_code': 510, 'latitude': 41.081444699999999, 'longitude': -81.519005300000003, 'region': 'OH', 'slug': 'akron-oh'},
    {'fcc_dma_str': 'ALBANY GA', 'city': 'Albany', 'dma_code': 525, 'latitude': 31.578507399999999, 'longitude': -84.155741000000006, 'region': 'GA', 'slug': 'albany-ga'},
    {'fcc_dma_str': 'ALEXANDRIA LA', 'city': 'Alexandria', 'dma_code': 644, 'latitude': 31.311293599999999, 'longitude': -92.445137099999997, 'region': 'LA', 'slug': 'alexandria-la'},
    {'fcc_dma_str': 'ALPENA', 'city': 'Alpena', 'dma_code': 583, 'latitude': 45.061679400000003, 'longitude': -83.432752800000003, 'region': 'MI', 'slug': 'alpena-mi'},
    {'fcc_dma_str': 'JOHNSTOWN-ALTOONA-ST COLGE', 'city': 'Altoona', 'dma_code': 574, 'latitude': 40.5186809, 'longitude': -78.394735900000001, 'region': 'PA', 'slug': 'altoona-pa'},
    {'fcc_dma_str': 'AMARILLO', 'city': 'Amarillo', 'dma_code': 634, 'latitude': 35.221997100000003, 'longitude': -101.8312969, 'region': 'TX', 'slug': 'amarillo-tx'},
    {'fcc_dma_str': 'DES MOINES-AMES', 'city': 'Ames', 'dma_code': 679, 'latitude': 42.023350000000001, 'longitude': -93.625622000000007, 'region': 'IA', 'slug': 'ames-ia'},
    {'fcc_dma_str': 'ANCHORAGE', 'city': 'Anchorage', 'dma_code': 743, 'latitude': 61.2180556, 'longitude': -149.9002778, 'region': 'AK', 'slug': 'anchorage-ak'},
    {'fcc_dma_str': 'GREENVILLE-SPARTANBURG-ASHEVILLE-ANDERSON', 'city': 'Anderson', 'dma_code': 567, 'latitude': 34.503439399999998, 'longitude': -82.650133199999999, 'region': 'SC', 'slug': 'anderson-sc'},
    {'fcc_dma_str': 'GREEN BAY-APPLETON', 'city': 'Appleton', 'dma_code': 658, 'latitude': 44.261930900000003, 'longitude': -88.415384700000004, 'region': 'WI', 'slug': 'appleton-wi'},
    {'fcc_dma_str': 'ATLANTA', 'city': 'Atlanta', 'dma_code': 524, 'latitude': 33.748995399999998, 'longitude': -84.387982399999999, 'region': 'GA', 'slug': 'atlanta-ga'},
    {'fcc_dma_str': 'PORTLAND-AUBURN', 'city': 'Auburn', 'dma_code': 500, 'latitude': 44.097850899999997, 'longitude': -70.231165500000003, 'region': 'ME', 'slug': 'auburn-me'},
    {'fcc_dma_str': 'AUGUSTA', 'city': 'Augusta', 'dma_code': 520, 'latitude': 33.469999999999999, 'longitude': -81.974999999999994, 'region': 'GA', 'slug': 'augusta-ga'},
    {'fcc_dma_str': 'ROCHESTR-MASON CITY-AUSTIN', 'city': 'Austin', 'dma_code': 611, 'latitude': 43.6666296, 'longitude': -92.974636700000005, 'region': 'MN', 'slug': 'austin-mn'},
    {'fcc_dma_str': 'AUSTIN', 'city': 'Austin', 'dma_code': 635, 'latitude': 30.267153, 'longitude': -97.743060799999995, 'region': 'TX', 'slug': 'austin-tx'},
    {'fcc_dma_str': 'BAKERSFIELD', 'city': 'Bakersfield', 'dma_code': 800, 'latitude': 35.3732921, 'longitude': -119.01871250000001, 'region': 'CA', 'slug': 'bakersfield-ca'},
    {'fcc_dma_str': 'BALTIMORE', 'city': 'Baltimore', 'dma_code': 512, 'latitude': 39.290384799999998, 'longitude': -76.612189299999997, 'region': 'MD', 'slug': 'baltimore-md'},
    {'fcc_dma_str': 'BANGOR', 'city': 'Bangor', 'dma_code': 537, 'latitude': 44.801182099999998, 'longitude': -68.777813800000004, 'region': 'ME', 'slug': 'bangor-me'},
    {'fcc_dma_str': 'BATON ROUGE', 'city': 'Baton Rouge', 'dma_code': 716, 'latitude': 30.450746200000001, 'longitude': -91.154550999999998, 'region': 'LA', 'slug': 'baton-rouge-la'},
    {'fcc_dma_str': 'GRAND RAPIDS-KALMZOO-B.CRK', 'city': 'Battle Creek', 'dma_code': 563, 'latitude': 42.3211522, 'longitude': -85.179714200000006, 'region': 'MI', 'slug': 'battle-creek-mi'},
    {'fcc_dma_str': 'FLINT-SAGINAW-BAY CITY', 'city': 'Bay City', 'dma_code': 513, 'latitude': 43.594467700000003, 'longitude': -83.888864699999999, 'region': 'MI', 'slug': 'bay-city-mi'},
    {'fcc_dma_str': 'BEND OR', 'city': 'Bend', 'dma_code': 821, 'latitude': 44.058172800000001, 'longitude': -121.31530960000001, 'region': 'OR', 'slug': 'bend-or'},
    {'fcc_dma_str': 'BILLINGS', 'city': 'Billings', 'dma_code': 756, 'latitude': 45.783285599999999, 'longitude': -108.5006904, 'region': 'MT', 'slug': 'billings-mt'},
    {'fcc_dma_str': 'BINGHAMTON', 'city': 'Binghamton', 'dma_code': 502, 'latitude': 42.098686700000002, 'longitude': -75.917973799999999, 'region': 'NY', 'slug': 'binghamton-ny'},
    {'fcc_dma_str': 'BIRMINGHAM (ANN TUSC)', 'city': 'Birmingham', 'dma_code': 630, 'latitude': 33.520660800000002, 'longitude': -86.802490000000006, 'region': 'AL', 'slug': 'birmingham-al'},
    {'fcc_dma_str': 'PEORIA-BLOOMINGTON', 'city': 'Bloomington', 'dma_code': 675, 'latitude': 40.484202699999997, 'longitude': -88.993687300000005, 'region': 'IL', 'slug': 'bloomington-il'},
    {'fcc_dma_str': 'BOISE', 'city': 'Boise', 'dma_code': 757, 'latitude': 43.613739000000002, 'longitude': -116.237651, 'region': 'ID', 'slug': 'boise-id'},
    {'fcc_dma_str': 'BOWLING GREEN', 'city': 'Bowling Green', 'dma_code': 736, 'latitude': 36.990319900000003, 'longitude': -86.443601799999996, 'region': 'KY', 'slug': 'bowling-green-ky'},
    {'fcc_dma_str': 'BUTTE-BOZEMAN', 'city': 'Bozeman', 'dma_code': 754, 'latitude': 45.683459999999997, 'longitude': -111.050499, 'region': 'MT', 'slug': 'bozeman-mt'},
    {'fcc_dma_str': 'WACO-TEMPLE-BRYAN', 'city': 'Bryan', 'dma_code': 625, 'latitude': 30.674364300000001, 'longitude': -96.369963200000001, 'region': 'TX', 'slug': 'bryan-tx'},
    {'fcc_dma_str': 'BUFFALO', 'city': 'Buffalo', 'dma_code': 514, 'latitude': 42.886446800000002, 'longitude': -78.878368899999998, 'region': 'NY', 'slug': 'buffalo-ny'},
    {'fcc_dma_str': 'TRAVERSE CITY-CADILLAC', 'city': 'Cadillac', 'dma_code': 540, 'latitude': 44.251952600000003, 'longitude': -85.401161900000005, 'region': 'MI', 'slug': 'cadillac-mi'},
    {'fcc_dma_str': 'CHAMPAIGN&SPRNGFLD-DECATUR', 'city': 'Champaign', 'dma_code': 648, 'latitude': 39.8403147, 'longitude': -88.9548001, 'region': 'IL', 'slug': 'champaign-il'},
    {'fcc_dma_str': 'CHARLESTON SC', 'city': 'Charleston', 'dma_code': 519, 'latitude': 32.776565599999998, 'longitude': -79.930921600000005, 'region': 'SC', 'slug': 'charleston-sc'},
    {'fcc_dma_str': 'CHARLOTTE', 'city': 'Charlotte', 'dma_code': 517, 'latitude': 35.227086900000003, 'longitude': -80.843126699999999, 'region': 'NC', 'slug': 'charlotte-nc'},
    {'fcc_dma_str': 'CHARLOTTESVILLE', 'city': 'Charlottesville', 'dma_code': 584, 'latitude': 38.029305899999997, 'longitude': -78.476678100000001, 'region': 'VA', 'slug': 'charlottesville-va'},
    {'fcc_dma_str': 'CHATTANOOGA', 'city': 'Chattanooga', 'dma_code': 575, 'latitude': 35.045629699999999, 'longitude': -85.309680099999994, 'region': 'TN', 'slug': 'chattanooga-tn'},
    {'fcc_dma_str': 'CHICAGO', 'city': 'Chicago', 'dma_code': 602, 'latitude': 41.850033000000003, 'longitude': -87.650052299999999, 'region': 'IL', 'slug': 'chicago-il'},
    {'fcc_dma_str': 'CINCINNATI', 'city': 'Cincinnati', 'dma_code': 515, 'latitude': 39.136111100000001, 'longitude': -84.503055599999996, 'region': 'OH', 'slug': 'cincinnati-oh'},
    {'fcc_dma_str': 'TRI-CITIES TN-VA', 'city': 'Cities', 'dma_code': 531, 'latitude': 36.472723000000002, 'longitude': -82.410686200000001, 'region': 'TN-VA', 'slug': 'cities-tn-va'},
    {'fcc_dma_str': 'COLUMBIA SC', 'city': 'Columbia', 'dma_code': 546, 'latitude': 34.000710400000003, 'longitude': -81.034814400000002, 'region': 'SC', 'slug': 'columbia-sc'},
    {'fcc_dma_str': 'COLUMBUS GA (OPELIKA AL)', 'city': 'Columbus', 'dma_code': 522, 'latitude': 32.4609764, 'longitude': -84.9877094, 'region': 'GA', 'slug': 'columbus-ga'},
    {'fcc_dma_str': 'COLUMBUS OH', 'city': 'Columbus', 'dma_code': 535, 'latitude': 39.961175500000003, 'longitude': -82.998794200000006, 'region': 'OH', 'slug': 'columbus-oh'},
    {'fcc_dma_str': 'CORPUS CHRISTI', 'city': 'Corpus Christi', 'dma_code': 600, 'latitude': 27.800582800000001, 'longitude': -97.396381000000005, 'region': 'TX', 'slug': 'corpus-christi-tx'},
    {'fcc_dma_str': 'DAYTON', 'city': 'Dayton', 'dma_code': 542, 'latitude': 39.758947800000001, 'longitude': -84.191606899999996, 'region': 'OH', 'slug': 'dayton-oh'},
    {'fcc_dma_str': 'HUNTSVILLE-DECATUR (FLOR)', 'city': 'Decatur', 'dma_code': 691, 'latitude': 34.605925300000003, 'longitude': -86.983341699999997, 'region': 'AL', 'slug': 'decatur-al'},
    {'fcc_dma_str': 'DENVER', 'city': 'Denver', 'dma_code': 751, 'latitude': 39.739153600000002, 'longitude': -104.9847034, 'region': 'CO', 'slug': 'denver-co'},
    {'fcc_dma_str': 'DETROIT', 'city': 'Detroit', 'dma_code': 505, 'latitude': 42.331426999999998, 'longitude': -83.0457538, 'region': 'MI', 'slug': 'detroit-mi'},
    {'fcc_dma_str': 'MINOT-BISMARCK-DICKINSON', 'city': 'Dickinson', 'dma_code': 687, 'latitude': 46.879175600000003, 'longitude': -102.78962420000001, 'region': 'ND', 'slug': 'dickinson-nd'},
    {'fcc_dma_str': 'DOTHAN', 'city': 'Dothan', 'dma_code': 606, 'latitude': 31.223231299999998, 'longitude': -85.3904888, 'region': 'AL', 'slug': 'dothan-al'},
    {'fcc_dma_str': 'RALEIGH-DURHAM (FAYETVLLE)', 'city': 'Durham', 'dma_code': 560, 'latitude': 35.994032900000001, 'longitude': -78.898618999999997, 'region': 'NC', 'slug': 'durham-nc'},
    {'fcc_dma_str': 'LA CROSSE-EAU CLAIRE', 'city': 'Eau Claire', 'dma_code': 702, 'latitude': 44.811349, 'longitude': -91.498494100000002, 'region': 'WI', 'slug': 'eau-claire-wi'},
    {'fcc_dma_str': 'YUMA-EL CENTRO', 'city': 'El Centro', 'dma_code': 771, 'latitude': 32.792000000000002, 'longitude': -115.56305140000001, 'region': 'CA', 'slug': 'el-centro-ca'},
    {'fcc_dma_str': 'MONROE-EL DORADO', 'city': 'El Dorado', 'dma_code': 628, 'latitude': 33.210973, 'longitude': -92.665901, 'region': 'AR', 'slug': 'el-dorado-ar'},
    {'fcc_dma_str': 'EL PASO (LAS CRUCES)', 'city': 'El Paso', 'dma_code': 765, 'latitude': 31.758719800000001, 'longitude': -106.4869314, 'region': 'TX', 'slug': 'el-paso-tx'},
    {'fcc_dma_str': 'SOUTH BEND-ELKHART', 'city': 'Elkhart', 'dma_code': 588, 'latitude': 41.681993499999997, 'longitude': -85.9766671, 'region': 'IN', 'slug': 'elkhart-in'},
    {'fcc_dma_str': 'ELMIRA (CORNING)', 'city': 'Elmira', 'dma_code': 565, 'latitude': 42.089796499999999, 'longitude': -76.807733799999994, 'region': 'NY', 'slug': 'elmira-ny'},
    {'fcc_dma_str': 'ERIE', 'city': 'Erie', 'dma_code': 516, 'latitude': 42.129224100000002, 'longitude': -80.085059000000001, 'region': 'PA', 'slug': 'erie-pa'},
    {'fcc_dma_str': 'EUGENE', 'city': 'Eugene', 'dma_code': 801, 'latitude': 44.052069099999997, 'longitude': -123.08675359999999, 'region': 'OR', 'slug': 'eugene-or'},
    {'fcc_dma_str': 'EUREKA', 'city': 'Eureka', 'dma_code': 802, 'latitude': 40.8020712, 'longitude': -124.16367289999999, 'region': 'CA', 'slug': 'eureka-ca'},
    {'fcc_dma_str': 'EVANSVILLE', 'city': 'Evansville', 'dma_code': 649, 'latitude': 37.974764399999998, 'longitude': -87.5558482, 'region': 'IN', 'slug': 'evansville-in'},
    {'fcc_dma_str': 'FAIRBANKS', 'city': 'Fairbanks', 'dma_code': 745, 'latitude': 64.837777799999998, 'longitude': -147.7163889, 'region': 'AK', 'slug': 'fairbanks-ak'},
    {'fcc_dma_str': 'MIAMI-FT. LAUDERDALE', 'city': 'Ft. Lauderdale', 'dma_code': 528, 'latitude': 26.122308400000001, 'longitude': -80.143378600000005, 'region': 'FL', 'slug': 'ft-lauderdale-fl'},
    {'fcc_dma_str': 'WEST PALM BEACH-FT. PIERCE', 'city': 'Ft. Pierce', 'dma_code': 548, 'latitude': 27.446705600000001, 'longitude': -80.325605600000003, 'region': 'FL', 'slug': 'ft-pierce-fl'},
    {'fcc_dma_str': 'FT. WAYNE', 'city': 'Ft. Wayne', 'dma_code': 509, 'latitude': 41.130604099999999, 'longitude': -85.128859700000007, 'region': 'IN', 'slug': 'ft-wayne-in'},
    {'fcc_dma_str': 'DALLAS-FT. WORTH', 'city': 'Ft. Worth', 'dma_code': 623, 'latitude': 32.725408999999999, 'longitude': -97.320849600000003, 'region': 'TX', 'slug': 'ft-worth-tx'},
    {'fcc_dma_str': 'GAINESVILLE', 'city': 'Gainesville', 'dma_code': 592, 'latitude': 29.651634399999999, 'longitude': -82.324826200000004, 'region': 'FL', 'slug': 'gainesville-fl'},
    {'fcc_dma_str': 'GLENDIVE', 'city': 'Glendive', 'dma_code': 798, 'latitude': 47.108491000000001, 'longitude': -104.710419, 'region': 'MT', 'slug': 'glendive-mt'},
    {'fcc_dma_str': 'GREAT FALLS', 'city': 'Great Falls', 'dma_code': 755, 'latitude': 47.500235400000001, 'longitude': -111.3008083, 'region': 'MT', 'slug': 'great-falls-mt'},
    {'fcc_dma_str': 'GREENWOOD-GREENVILLE', 'city': 'Greenville', 'dma_code': 647, 'latitude': 33.410116100000003, 'longitude': -91.061773500000001, 'region': 'MS', 'slug': 'greenville-ms'},
    {'fcc_dma_str': 'BILOXI-GULFPORT', 'city': 'Gulfport', 'dma_code': 746, 'latitude': 30.3674198, 'longitude': -89.0928155, 'region': 'MS', 'slug': 'gulfport-ms'},
    {'fcc_dma_str': 'HARRISONBURG', 'city': 'Harrisonburg', 'dma_code': 569, 'latitude': 38.449568800000002, 'longitude': -78.8689155, 'region': 'VA', 'slug': 'harrisonburg-va'},
    {'fcc_dma_str': 'HARTFORD & NEW HAVEN', 'city': 'Hartford', 'dma_code': 533, 'latitude': 41.763711100000002, 'longitude': -72.685093199999997, 'region': 'CT', 'slug': 'hartford-ct'},
    {'fcc_dma_str': 'HELENA', 'city': 'Helena', 'dma_code': 766, 'latitude': 46.595804999999999, 'longitude': -112.02703099999999, 'region': 'MT', 'slug': 'helena-mt'},
    {'fcc_dma_str': 'SPRINGFIELD-HOLYOKE', 'city': 'Holyoke', 'dma_code': 543, 'latitude': 42.204258600000003, 'longitude': -72.616200899999995, 'region': 'MA', 'slug': 'holyoke-ma'},
    {'fcc_dma_str': 'HONOLULU', 'city': 'Honolulu', 'dma_code': 744, 'latitude': 21.306944399999999, 'longitude': -157.8583333, 'region': 'HI', 'slug': 'honolulu-hi'},
    {'fcc_dma_str': 'HOUSTON', 'city': 'Houston', 'dma_code': 618, 'latitude': 29.762884400000001, 'longitude': -95.383061499999997, 'region': 'TX', 'slug': 'houston-tx'},
    {'fcc_dma_str': 'CHARLESTON-HUNTINGTON', 'city': 'Huntington', 'dma_code': 564, 'latitude': 38.419249600000001, 'longitude': -82.445154000000002, 'region': 'WV', 'slug': 'huntington-wv'},
    {'fcc_dma_str': 'WICHITA-HUTCHINSON PLUS', 'city': 'Hutchinson', 'dma_code': 678, 'latitude': 38.060844500000002, 'longitude': -97.929774300000005, 'region': 'KS', 'slug': 'hutchinson-ks'},
    {'fcc_dma_str': 'INDIANAPOLIS', 'city': 'Indianapolis', 'dma_code': 527, 'latitude': 39.768376500000002, 'longitude': -86.158042300000005, 'region': 'IN', 'slug': 'indianapolis-in'},
    {'fcc_dma_str': 'CEDAR RAPIDS-WTRLO-IWC&DUB', 'city': 'Iowa City', 'dma_code': 637, 'latitude': 41.677204000000003, 'longitude': -91.5162792, 'region': 'IA', 'slug': 'iowa-city-ia'},
    {'fcc_dma_str': 'JACKSON TN', 'city': 'Jackson', 'dma_code': 639, 'latitude': 35.614516899999998, 'longitude': -88.813946900000005, 'region': 'TN', 'slug': 'jackson-tn'},
    {'fcc_dma_str': 'JACKSON MS', 'city': 'Jackson', 'dma_code': 718, 'latitude': 32.298757299999998, 'longitude': -90.184810299999995, 'region': 'MS', 'slug': 'jackson-ms'},
    {'fcc_dma_str': 'JACKSONVILLE', 'city': 'Jacksonville', 'dma_code': 561, 'latitude': 30.332183799999999, 'longitude': -81.655651000000006, 'region': 'FL', 'slug': 'jacksonville-fl'},
    {'fcc_dma_str': 'COLUMBIA-JEFFERSON CITY', 'city': 'Jefferson City', 'dma_code': 604, 'latitude': 38.576701700000001, 'longitude': -92.173516399999997, 'region': 'MO', 'slug': 'jefferson-city-mo'},
    {'fcc_dma_str': 'JONESBORO', 'city': 'Jonesboro', 'dma_code': 734, 'latitude': 35.842296699999999, 'longitude': -90.704279, 'region': 'AR', 'slug': 'jonesboro-ar'},
    {'fcc_dma_str': 'JUNEAU', 'city': 'Juneau', 'dma_code': 747, 'latitude': 58.301944399999996, 'longitude': -134.4197222, 'region': 'AK', 'slug': 'juneau-ak'},
    {'fcc_dma_str': 'KANSAS CITY', 'city': 'Kansas City', 'dma_code': 616, 'latitude': 39.099726500000003, 'longitude': -94.578566699999996, 'region': 'MO', 'slug': 'kansas-city-mo'},
    {'fcc_dma_str': 'LINCOLN & HASTINGS-KRNY', 'city': 'Kearney', 'dma_code': 722, 'latitude': 40.699959, 'longitude': -99.083106999999998, 'region': 'NE', 'slug': 'kearney-ne'},
    {'fcc_dma_str': 'YAKIMA-PASCO-RCHLND-KNNWCK', 'city': 'Kennewick', 'dma_code': 810, 'latitude': 46.2112458, 'longitude': -119.1372338, 'region': 'WA', 'slug': 'kennewick-wa'},
    {'fcc_dma_str': 'QUINCY-HANNIBAL-KEOKUK', 'city': 'Keokuk', 'dma_code': 717, 'latitude': 40.402524999999997, 'longitude': -91.394372000000004, 'region': 'IA', 'slug': 'keokuk-ia'},
    {'fcc_dma_str': 'OTTUMWA-KIRKSVILLE', 'city': 'Kirksville', 'dma_code': 631, 'latitude': 40.194753900000002, 'longitude': -92.583249600000002, 'region': 'MO', 'slug': 'kirksville-mo'},
    {'fcc_dma_str': 'MEDFORD-KLAMATH FALLS', 'city': 'Klamath Falls', 'dma_code': 813, 'latitude': 42.224867000000003, 'longitude': -121.7816704, 'region': 'OR', 'slug': 'klamath-falls-or'},
    {'fcc_dma_str': 'KNOXVILLE', 'city': 'Knoxville', 'dma_code': 557, 'latitude': 35.960638400000001, 'longitude': -83.9207392, 'region': 'TN', 'slug': 'knoxville-tn'},
    {'fcc_dma_str': 'LAFAYETTE IN', 'city': 'Lafayette', 'dma_code': 582, 'latitude': 40.416702200000003, 'longitude': -86.875286900000006, 'region': 'IN', 'slug': 'lafayette-in'},
    {'fcc_dma_str': 'LAFAYETTE LA', 'city': 'Lafayette', 'dma_code': 642, 'latitude': 30.2240897, 'longitude': -92.019842699999998, 'region': 'LA', 'slug': 'lafayette-la'},
    {'fcc_dma_str': 'LAKE CHARLES', 'city': 'Lake Charles', 'dma_code': 643, 'latitude': 30.226594899999998, 'longitude': -93.217375799999999, 'region': 'LA', 'slug': 'lake-charles-la'},
    {'fcc_dma_str': 'LANSING', 'city': 'Lansing', 'dma_code': 551, 'latitude': 42.732534999999999, 'longitude': -84.555534699999995, 'region': 'MI', 'slug': 'lansing-mi'},
    {'fcc_dma_str': 'LAREDO', 'city': 'Laredo', 'dma_code': 749, 'latitude': 27.506406999999999, 'longitude': -99.507542099999995, 'region': 'TX', 'slug': 'laredo-tx'},
    {'fcc_dma_str': 'LAS VEGAS', 'city': 'Las Vegas', 'dma_code': 839, 'latitude': 36.114646, 'longitude': -115.172816, 'region': 'NV', 'slug': 'las-vegas-nv'},
    {'fcc_dma_str': 'HATTIESBURG-LAUREL', 'city': 'Laurel', 'dma_code': 710, 'latitude': 31.694050900000001, 'longitude': -89.130612400000004, 'region': 'MS', 'slug': 'laurel-ms'},
    {'fcc_dma_str': 'LEXINGTON', 'city': 'Lexington', 'dma_code': 541, 'latitude': 38.031713600000003, 'longitude': -84.495135899999994, 'region': 'KY', 'slug': 'lexington-ky'},
    {'fcc_dma_str': 'LIMA', 'city': 'Lima', 'dma_code': 558, 'latitude': 40.742550999999999, 'longitude': -84.105225599999997, 'region': 'OH', 'slug': 'lima-oh'},
    {'fcc_dma_str': 'TYLER-LONGVIEW(LFKN&NCGD)', 'city': 'Longview', 'dma_code': 709, 'latitude': 32.500703700000003, 'longitude': -94.740489100000005, 'region': 'TX', 'slug': 'longview-tx'},
    {'fcc_dma_str': 'LOS ANGELES', 'city': 'Los Angeles', 'dma_code': 803, 'latitude': 34.052234200000001, 'longitude': -118.24368490000001, 'region': 'CA', 'slug': 'los-angeles-ca'},
    {'fcc_dma_str': 'LOUISVILLE', 'city': 'Louisville', 'dma_code': 529, 'latitude': 38.254237600000003, 'longitude': -85.759406999999996, 'region': 'KY', 'slug': 'louisville-ky'},
    {'fcc_dma_str': 'LUBBOCK', 'city': 'Lubbock', 'dma_code': 651, 'latitude': 33.577863100000002, 'longitude': -101.8551665, 'region': 'TX', 'slug': 'lubbock-tx'},
    {'fcc_dma_str': 'ROANOKE-LYNCHBURG', 'city': 'Lynchburg', 'dma_code': 573, 'latitude': 37.4137536, 'longitude': -79.142246400000005, 'region': 'VA', 'slug': 'lynchburg-va'},
    {'fcc_dma_str': 'MACON', 'city': 'Macon', 'dma_code': 503, 'latitude': 32.840694599999999, 'longitude': -83.632402200000001, 'region': 'GA', 'slug': 'macon-ga'},
    {'fcc_dma_str': 'MADISON', 'city': 'Madison', 'dma_code': 669, 'latitude': 43.073051700000001, 'longitude': -89.401230200000001, 'region': 'WI', 'slug': 'madison-wi'},
    {'fcc_dma_str': 'BOSTON (MANCHESTER)', 'city': 'Manchester', 'dma_code': 506, 'latitude': 42.995639699999998, 'longitude': -71.454789099999999, 'region': 'NH', 'slug': 'manchester-nh'},
    {'fcc_dma_str': 'MANKATO', 'city': 'Mankato', 'dma_code': 737, 'latitude': 44.163577500000002, 'longitude': -93.999399600000004, 'region': 'MN', 'slug': 'mankato-mn'},
    {'fcc_dma_str': 'MARQUETTE', 'city': 'Marquette', 'dma_code': 553, 'latitude': 46.543544199999999, 'longitude': -87.395416999999995, 'region': 'MI', 'slug': 'marquette-mi'},
    {'fcc_dma_str': 'HARLINGEN-WSLCO-BRNSVL-MCA', 'city': 'McAllen', 'dma_code': 636, 'latitude': 26.2034071, 'longitude': -98.230012400000007, 'region': 'TX', 'slug': 'mcallen-tx'},
    {'fcc_dma_str': 'ORLANDO-DAYTONA BCH-MELBRN', 'city': 'Melbourne', 'dma_code': 534, 'latitude': 28.083626899999999, 'longitude': -80.608108900000005, 'region': 'FL', 'slug': 'melbourne-fl'},
    {'fcc_dma_str': 'MEMPHIS', 'city': 'Memphis', 'dma_code': 640, 'latitude': 35.149534299999999, 'longitude': -90.048980099999994, 'region': 'TN', 'slug': 'memphis-tn'},
    {'fcc_dma_str': 'MERIDIAN', 'city': 'Meridian', 'dma_code': 711, 'latitude': 32.364309800000001, 'longitude': -88.703655999999995, 'region': 'MS', 'slug': 'meridian-ms'},
    {'fcc_dma_str': 'ODESSA-MIDLAND', 'city': 'Midland', 'dma_code': 633, 'latitude': 31.997345599999999, 'longitude': -102.0779146, 'region': 'TX', 'slug': 'midland-tx'},
    {'fcc_dma_str': 'MILWAUKEE', 'city': 'Milwaukee', 'dma_code': 617, 'latitude': 43.038902499999999, 'longitude': -87.906473599999998, 'region': 'WI', 'slug': 'milwaukee-wi'},
    {'fcc_dma_str': 'MISSOULA', 'city': 'Missoula', 'dma_code': 762, 'latitude': 46.872146000000001, 'longitude': -113.99399819999999, 'region': 'MT', 'slug': 'missoula-mt'},
    {'fcc_dma_str': 'SACRAMNTO-STKTON-MODESTO', 'city': 'Modesto', 'dma_code': 862, 'latitude': 37.639097200000002, 'longitude': -120.9968782, 'region': 'CA', 'slug': 'modesto-ca'},
    {'fcc_dma_str': 'DAVENPORT-R.ISLAND-MOLINE', 'city': 'Moline', 'dma_code': 682, 'latitude': 41.506700299999999, 'longitude': -90.515134200000006, 'region': 'IL', 'slug': 'moline-il'},
    {'fcc_dma_str': 'MONTGOMERY-SELMA', 'city': 'Montgomery', 'dma_code': 698, 'latitude': 32.366805200000002, 'longitude': -86.299968899999996, 'region': 'AL', 'slug': 'montgomery-al'},
    {'fcc_dma_str': 'GRAND JUNCTION-MONTROSE', 'city': 'Montrose', 'dma_code': 773, 'latitude': 38.478319800000001, 'longitude': -107.8761738, 'region': 'CO', 'slug': 'montrose-co'},
    {'fcc_dma_str': 'PADUCAH-CAPE GIRARD-HARSBG', 'city': 'Mount Vernon', 'dma_code': 632, 'latitude': 38.317271400000003, 'longitude': -88.903120099999995, 'region': 'IL', 'slug': 'mount-vernon-il'},
    {'fcc_dma_str': 'MYRTLE BEACH-FLORENCE', 'city': 'Myrtle Beach', 'dma_code': 570, 'latitude': 33.689060300000001, 'longitude': -78.886694300000002, 'region': 'SC', 'slug': 'myrtle-beach-sc'},
    {'fcc_dma_str': 'FT. MYERS-NAPLES', 'city': 'Naples', 'dma_code': 571, 'latitude': 26.142035799999999, 'longitude': -81.794810299999995, 'region': 'FL', 'slug': 'naples-fl'},
    {'fcc_dma_str': 'NASHVILLE', 'city': 'Nashville', 'dma_code': 659, 'latitude': 36.165889900000003, 'longitude': -86.784443199999998, 'region': 'TN', 'slug': 'nashville-tn'},
    {'fcc_dma_str': 'PROVIDENCE-NEW BEDFORD', 'city': 'New Bedford', 'dma_code': 521, 'latitude': 41.636215200000002, 'longitude': -70.934205000000006, 'region': 'MA', 'slug': 'new-bedford-ma'},
    {'fcc_dma_str': 'NEW ORLEANS', 'city': 'New Orleans', 'dma_code': 622, 'latitude': 29.964722200000001, 'longitude': -90.070555600000006, 'region': 'LA', 'slug': 'new-orleans-la'},
    {'fcc_dma_str': 'NEW YORK', 'city': 'New York', 'dma_code': 501, 'latitude': 40.714269100000003, 'longitude': -74.005972900000003, 'region': 'NY', 'slug': 'new-york-ny'},
    {'fcc_dma_str': 'NORFOLK-PORTSMTH-NEWPT NWS', 'city': 'Newport News', 'dma_code': 544, 'latitude': 36.978758800000001, 'longitude': -76.428003000000004, 'region': 'VA', 'slug': 'newport-news-va'},
    {'fcc_dma_str': 'NORTH PLATTE', 'city': 'North Platte', 'dma_code': 740, 'latitude': 41.1238873, 'longitude': -100.7654232, 'region': 'NE', 'slug': 'north-platte-ne'},
    {'fcc_dma_str': 'BLUEFIELD-BECKLEY-OAK HILL', 'city': 'Oak Hill', 'dma_code': 559, 'latitude': 37.972333900000002, 'longitude': -81.148713499999999, 'region': 'WV', 'slug': 'oak-hill-wv'},
    {'fcc_dma_str': 'OKLAHOMA CITY', 'city': 'Oklahoma City', 'dma_code': 650, 'latitude': 35.467560200000001, 'longitude': -97.5164276, 'region': 'OK', 'slug': 'oklahoma-city-ok'},
    {'fcc_dma_str': 'OMAHA', 'city': 'Omaha', 'dma_code': 652, 'latitude': 41.254005999999997, 'longitude': -95.999257999999998, 'region': 'NE', 'slug': 'omaha-ne'},
    {'fcc_dma_str': 'PALM SPRINGS', 'city': 'Palm Springs', 'dma_code': 804, 'latitude': 33.830296099999998, 'longitude': -116.5452921, 'region': 'CA', 'slug': 'palm-springs-ca'},
    {'fcc_dma_str': 'PANAMA CITY', 'city': 'Panama City', 'dma_code': 656, 'latitude': 30.158812900000001, 'longitude': -85.6602058, 'region': 'FL', 'slug': 'panama-city-fl'},
    {'fcc_dma_str': 'PARKERSBURG', 'city': 'Parkersburg', 'dma_code': 597, 'latitude': 39.266741799999998, 'longitude': -81.561513500000004, 'region': 'WV', 'slug': 'parkersburg-wv'},
    {'fcc_dma_str': 'MOBILE-PENSACOLA (FT WALT)', 'city': 'Pensacola ', 'dma_code': 686, 'latitude': 30.421309000000001, 'longitude': -87.216914900000006, 'region': 'FL', 'slug': 'pensacola-fl'},
    {'fcc_dma_str': 'RICHMOND-PETERSBURG', 'city': 'Petersburg', 'dma_code': 556, 'latitude': 37.227927899999997, 'longitude': -77.401926700000004, 'region': 'VA', 'slug': 'petersburg-va'},
    {'fcc_dma_str': 'PHILADELPHIA', 'city': 'Philadelphia', 'dma_code': 504, 'latitude': 39.952334999999998, 'longitude': -75.163788999999994, 'region': 'PA', 'slug': 'philadelphia-pa'},
    {'fcc_dma_str': 'PHOENIX (PRESCOTT)', 'city': 'Phoenix', 'dma_code': 753, 'latitude': 33.448377100000002, 'longitude': -112.0740373, 'region': 'AZ', 'slug': 'phoenix-az'},
    {'fcc_dma_str': 'LITTLE ROCK-PINE BLUFF', 'city': 'Pine Bluff', 'dma_code': 693, 'latitude': 34.228431200000003, 'longitude': -92.003195500000004, 'region': 'AR', 'slug': 'pine-bluff-ar'},
    {'fcc_dma_str': 'JOPLIN-PITTSBURG', 'city': 'Pittsburg', 'dma_code': 603, 'latitude': 37.410884000000003, 'longitude': -94.70496, 'region': 'KS', 'slug': 'pittsburg-ks'},
    {'fcc_dma_str': 'PITTSBURGH', 'city': 'Pittsburgh', 'dma_code': 508, 'latitude': 40.440624800000002, 'longitude': -79.995886400000003, 'region': 'PA', 'slug': 'pittsburgh-pa'},
    {'fcc_dma_str': 'BURLINGTON-PLATTSBURGH', 'city': 'Plattsburgh', 'dma_code': 523, 'latitude': 44.699487300000001, 'longitude': -73.452912400000002, 'region': 'NY', 'slug': 'plattsburgh-ny'},
    {'fcc_dma_str': 'IDAHO FALLS-POCATELLO', 'city': 'Pocatello', 'dma_code': 758, 'latitude': 42.8713032, 'longitude': -112.4455344, 'region': 'ID', 'slug': 'pocatello-id'},
    {'fcc_dma_str': 'BEAUMONT-PORT ARTHUR', 'city': 'Port Arthur', 'dma_code': 692, 'latitude': 29.884950400000001, 'longitude': -93.939947000000004, 'region': 'TX', 'slug': 'port-arthur-tx'},
    {'fcc_dma_str': 'PORTLAND OR', 'city': 'Portland', 'dma_code': 820, 'latitude': 45.5234515, 'longitude': -122.6762071, 'region': 'OR', 'slug': 'portland-or'},
    {'fcc_dma_str': 'PRESQUE ISLE', 'city': 'Presque Isle', 'dma_code': 552, 'latitude': 46.681153000000002, 'longitude': -68.0158615, 'region': 'ME', 'slug': 'presque-isle-me'},
    {'fcc_dma_str': 'COLORADO SPRINGS-PUEBLO', 'city': 'Pueblo', 'dma_code': 752, 'latitude': 38.254447200000001, 'longitude': -104.6091409, 'region': 'CO', 'slug': 'pueblo-co'},
    {'fcc_dma_str': 'RAPID CITY', 'city': 'Rapid City', 'dma_code': 764, 'latitude': 44.080543400000003, 'longitude': -103.23101490000001, 'region': 'SD', 'slug': 'rapid-city-sd'},
    {'fcc_dma_str': 'CHICO-REDDING', 'city': 'Redding', 'dma_code': 868, 'latitude': 40.586539600000002, 'longitude': -122.3916754, 'region': 'CA', 'slug': 'redding-ca'},
    {'fcc_dma_str': 'RENO', 'city': 'Reno', 'dma_code': 811, 'latitude': 39.529632900000003, 'longitude': -119.8138027, 'region': 'NV', 'slug': 'reno-nv'},
    {'fcc_dma_str': 'WAUSAU-RHINELANDER', 'city': 'Rhinelander', 'dma_code': 705, 'latitude': 45.636622799999998, 'longitude': -89.412075299999998, 'region': 'WI', 'slug': 'rhinelander-wi'},
    {'fcc_dma_str': 'CASPER-RIVERTON', 'city': 'Riverton', 'dma_code': 767, 'latitude': 43.024959199999998, 'longitude': -108.3801036, 'region': 'WY', 'slug': 'riverton-wy'},
    {'fcc_dma_str': 'ROCHESTER NY', 'city': 'Rochester', 'dma_code': 538, 'latitude': 43.154784499999998, 'longitude': -77.615556699999999, 'region': 'NY', 'slug': 'rochester-ny'},
    {'fcc_dma_str': 'ROCKFORD', 'city': 'Rockford', 'dma_code': 610, 'latitude': 42.271131099999998, 'longitude': -89.093995199999995, 'region': 'IL', 'slug': 'rockford-il'},
    {'fcc_dma_str': 'FT. SMITH-FAY-SPRNGDL-RGRS', 'city': 'Rogers', 'dma_code': 670, 'latitude': 36.332019600000002, 'longitude': -94.118536599999999, 'region': 'AR', 'slug': 'rogers-ar'},
    {'fcc_dma_str': 'MONTEREY-SALINAS', 'city': 'Salinas', 'dma_code': 828, 'latitude': 36.677737200000003, 'longitude': -121.6555013, 'region': 'CA', 'slug': 'salinas-ca'},
    {'fcc_dma_str': 'SALISBURY', 'city': 'Salisbury', 'dma_code': 576, 'latitude': 38.360673599999998, 'longitude': -75.599369199999998, 'region': 'MD', 'slug': 'salisbury-md'},
    {'fcc_dma_str': 'SALT LAKE CITY', 'city': 'Salt Lake City', 'dma_code': 770, 'latitude': 40.760779300000003, 'longitude': -111.89104740000001, 'region': 'UT', 'slug': 'salt-lake-city-ut'},
    {'fcc_dma_str': 'SAN ANGELO', 'city': 'San Angelo', 'dma_code': 661, 'latitude': 31.463772299999999, 'longitude': -100.4370375, 'region': 'TX', 'slug': 'san-angelo-tx'},
    {'fcc_dma_str': 'SAN ANTONIO', 'city': 'San Antonio', 'dma_code': 641, 'latitude': 29.424121899999999, 'longitude': -98.493628200000003, 'region': 'TX', 'slug': 'san-antonio-tx'},
    {'fcc_dma_str': 'SAN DIEGO', 'city': 'San Diego', 'dma_code': 825, 'latitude': 32.715329199999999, 'longitude': -117.1572551, 'region': 'CA', 'slug': 'san-diego-ca'},
    {'fcc_dma_str': 'SAN FRANCISCO-OAK-SAN JOSE', 'city': 'San Jose', 'dma_code': 807, 'latitude': 37.339385700000001, 'longitude': -121.89495549999999, 'region': 'CA', 'slug': 'san-jose-ca'},
    {'fcc_dma_str': 'SANTABARBRA-SANMAR-SANLUOB', 'city': 'San Luis Obispo', 'dma_code': 855, 'latitude': 35.2827524, 'longitude': -120.6596156, 'region': 'CA', 'slug': 'san-luis-obispo-ca'},
    {'fcc_dma_str': 'ALBUQUERQUE-SANTA FE', 'city': 'Santa Fe', 'dma_code': 790, 'latitude': 35.686975199999999, 'longitude': -105.937799, 'region': 'NM', 'slug': 'santa-fe-nm'},
    {'fcc_dma_str': 'TAMPA-ST. PETE (SARASOTA)', 'city': 'Sarasota', 'dma_code': 539, 'latitude': 27.336434700000002, 'longitude': -82.530652700000005, 'region': 'FL', 'slug': 'sarasota-fl'},
    {'fcc_dma_str': 'SAVANNAH', 'city': 'Savannah', 'dma_code': 507, 'latitude': 32.0835407, 'longitude': -81.099834200000004, 'region': 'GA', 'slug': 'savannah-ga'},
    {'fcc_dma_str': 'CHEYENNE-SCOTTSBLUFF', 'city': 'Scottsbluff', 'dma_code': 759, 'latitude': 41.867139999999999, 'longitude': -103.660709, 'region': 'NE', 'slug': 'scottsbluff-ne'},
    {'fcc_dma_str': 'WILKES BARRE-SCRANTON', 'city': 'Scranton', 'dma_code': 577, 'latitude': 41.408968999999999, 'longitude': -75.662412200000006, 'region': 'PA', 'slug': 'scranton-pa'},
    {'fcc_dma_str': 'SHREVEPORT', 'city': 'Shreveport', 'dma_code': 612, 'latitude': 32.525151600000001, 'longitude': -93.750178899999995, 'region': 'LA', 'slug': 'shreveport-la'},
    {'fcc_dma_str': 'SIOUX CITY', 'city': 'Sioux City', 'dma_code': 624, 'latitude': 42.499994200000003, 'longitude': -96.400306900000004, 'region': 'IA', 'slug': 'sioux-city-ia'},
    {'fcc_dma_str': 'SIOUX FALLS(MITCHELL)', 'city': 'Sioux Falls', 'dma_code': 725, 'latitude': 43.549974900000002, 'longitude': -96.700327000000001, 'region': 'SD', 'slug': 'sioux-falls-sd'},
    {'fcc_dma_str': 'SPOKANE', 'city': 'Spokane', 'dma_code': 881, 'latitude': 47.658780200000002, 'longitude': -117.42604660000001, 'region': 'WA', 'slug': 'spokane-wa'},
    {'fcc_dma_str': 'SPRINGFIELD MO', 'city': 'Springfield', 'dma_code': 619, 'latitude': 37.215325999999997, 'longitude': -93.298243600000006, 'region': 'MO', 'slug': 'springfield-mo'},
    {'fcc_dma_str': 'ST. JOSEPH', 'city': 'St. Joseph', 'dma_code': 638, 'latitude': 39.7577778, 'longitude': -94.836388900000003, 'region': 'MO', 'slug': 'st-joseph-mo'},
    {'fcc_dma_str': 'ST. LOUIS', 'city': 'St. Louis', 'dma_code': 609, 'latitude': 38.646991, 'longitude': -90.224967000000007, 'region': 'MO', 'slug': 'st-louis-mo'},
    {'fcc_dma_str': 'MINNEAPOLIS-ST. PAUL', 'city': 'St. Paul', 'dma_code': 613, 'latitude': 44.944167, 'longitude': -93.086074999999994, 'region': 'MN', 'slug': 'st-paul-mn'},
    {'fcc_dma_str': 'WHEELING-STEUBENVILLE', 'city': 'Steubenville', 'dma_code': 554, 'latitude': 40.369790500000001, 'longitude': -80.633963800000004, 'region': 'OH', 'slug': 'steubenville-oh'},
    {'fcc_dma_str': 'DULUTH-SUPERIOR', 'city': 'Superior', 'dma_code': 676, 'latitude': 46.720773700000002, 'longitude': -92.104079600000006, 'region': 'WI', 'slug': 'superior-wi'},
    {'fcc_dma_str': 'ABILENE-SWEETWATER', 'city': 'Sweetwater', 'dma_code': 662, 'latitude': 32.470951900000003, 'longitude': -100.4059384, 'region': 'TX', 'slug': 'sweetwater-tx'},
    {'fcc_dma_str': 'SYRACUSE', 'city': 'Syracuse', 'dma_code': 555, 'latitude': 43.048122100000001, 'longitude': -76.147424400000006, 'region': 'NY', 'slug': 'syracuse-ny'},
    {'fcc_dma_str': 'SEATTLE-TACOMA', 'city': 'Tacoma', 'dma_code': 819, 'latitude': 47.252876800000003, 'longitude': -122.4442906, 'region': 'WA', 'slug': 'tacoma-wa'},
    {'fcc_dma_str': 'TERRE HAUTE', 'city': 'Terre Haute', 'dma_code': 581, 'latitude': 39.4667034, 'longitude': -87.413909200000006, 'region': 'IN', 'slug': 'terre-haute-in'},
    {'fcc_dma_str': 'TALLAHASSEE-THOMASVILLE', 'city': 'Thomasville', 'dma_code': 530, 'latitude': 30.836581500000001, 'longitude': -83.978780799999996, 'region': 'GA', 'slug': 'thomasville-ga'},
    {'fcc_dma_str': 'TOLEDO', 'city': 'Toledo', 'dma_code': 547, 'latitude': 41.663938299999998, 'longitude': -83.555211999999997, 'region': 'OH', 'slug': 'toledo-oh'},
    {'fcc_dma_str': 'TOPEKA', 'city': 'Topeka', 'dma_code': 605, 'latitude': 39.048333599999999, 'longitude': -95.678037099999997, 'region': 'KS', 'slug': 'topeka-ks'},
    {'fcc_dma_str': 'ALBANY-SCHENECTADY-TROY', 'city': 'Troy', 'dma_code': 532, 'latitude': 42.728411700000002, 'longitude': -73.691785100000004, 'region': 'NY', 'slug': 'troy-ny'},
    {'fcc_dma_str': 'TUCSON (SIERRA VISTA)', 'city': 'Tucson', 'dma_code': 789, 'latitude': 32.221742900000002, 'longitude': -110.926479, 'region': 'AZ', 'slug': 'tucson-az'},
    {'fcc_dma_str': 'TULSA', 'city': 'Tulsa', 'dma_code': 671, 'latitude': 36.153981600000002, 'longitude': -95.992774999999995, 'region': 'OK', 'slug': 'tulsa-ok'},
    {'fcc_dma_str': 'TWIN FALLS', 'city': 'Twin Falls', 'dma_code': 760, 'latitude': 42.562966799999998, 'longitude': -114.46087110000001, 'region': 'ID', 'slug': 'twin-falls-id'},
    {'fcc_dma_str': 'UTICA', 'city': 'Utica', 'dma_code': 526, 'latitude': 43.100903000000002, 'longitude': -75.232664, 'region': 'NY', 'slug': 'utica-ny'},
    {'fcc_dma_str': 'FARGO-VALLEY CITY', 'city': 'Valley City', 'dma_code': 724, 'latitude': 46.923312899999999, 'longitude': -98.003154699999996, 'region': 'ND', 'slug': 'valley-city-nd'},
    {'fcc_dma_str': 'VICTORIA', 'city': 'Victoria', 'dma_code': 626, 'latitude': 28.805267400000002, 'longitude': -97.003598199999999, 'region': 'TX', 'slug': 'victoria-tx'},
    {'fcc_dma_str': 'FRESNO-VISALIA', 'city': 'Visalia', 'dma_code': 866, 'latitude': 36.330228400000003, 'longitude': -119.2920585, 'region': 'CA', 'slug': 'visalia-ca'},
    {'fcc_dma_str': 'WASHINGTON DC (HAGRSTWN)', 'city': 'Washington DC ', 'dma_code': 511, 'latitude': 38.895111800000002, 'longitude': -77.036365799999999, 'region': 'MD', 'slug': 'washington-dc-md'},
    {'fcc_dma_str': 'GREENVILLE-N.BERN-WASHNGTN', 'city': 'Washington', 'dma_code': 545, 'latitude': 35.546551700000002, 'longitude': -77.052174199999996, 'region': 'NC', 'slug': 'washington-nc'},
    {'fcc_dma_str': 'WATERTOWN', 'city': 'Watertown', 'dma_code': 549, 'latitude': 43.974783799999997, 'longitude': -75.910756500000005, 'region': 'NY', 'slug': 'watertown-ny'},
    {'fcc_dma_str': 'COLUMBUS-TUPELO-WEST POINT', 'city': 'West Point', 'dma_code': 673, 'latitude': 33.607618600000002, 'longitude': -88.6503254, 'region': 'MS', 'slug': 'west-point-ms'},
    {'fcc_dma_str': 'CLARKSBURG-WESTON', 'city': 'Weston', 'dma_code': 598, 'latitude': 39.038427400000003, 'longitude': -80.467313000000004, 'region': 'WV', 'slug': 'weston-wv'},
    {'fcc_dma_str': 'WICHITA FALLS & LAWTON', 'city': 'Wichita Falls', 'dma_code': 627, 'latitude': 33.695379099999997, 'longitude': -98.308844100000002, 'region': 'OK', 'slug': 'wichita-falls-ok'},
    {'fcc_dma_str': 'WILMINGTON', 'city': 'Wilmington', 'dma_code': 550, 'latitude': 34.225725500000003, 'longitude': -77.944710200000003, 'region': 'NC', 'slug': 'wilmington-nc'},
    {'fcc_dma_str': 'GREENSBORO-H.POINT-W.SALEM', 'city': 'Winston Salem', 'dma_code': 518, 'latitude': 36.099859600000002, 'longitude': -80.244215999999994, 'region': 'NC', 'slug': 'winston-salem-nc'},
    {'fcc_dma_str': 'HARRISBURG-LNCSTR-LEB-YORK', 'city': 'York', 'dma_code': 566, 'latitude': 39.962598399999997, 'longitude': -76.727744999999999, 'region': 'PA', 'slug': 'york-pa'},
    {'fcc_dma_str': 'YOUNGSTOWN', 'city': 'Youngstown', 'dma_code': 536, 'latitude': 41.099780299999999, 'longitude': -80.649519400000003, 'region': 'OH', 'slug': 'youngstown-oh'},
    {'fcc_dma_str': 'ZANESVILLE', 'city': 'Zanesville', 'dma_code': 596, 'latitude': 39.940345299999997, 'longitude': -82.013192399999994, 'region': 'OH', 'slug': 'zanesville-oh'},
    {'fcc_dma_str': 'BIRMINGHAM', 'city': 'Binghamton', 'dma_code': 502, 'latitude': 42.098686700000002, 'longitude': -75.917973799999999, 'region': 'NY', 'slug': 'binghamton-ny'},
    {'fcc_dma_str': 'GREENVLL-SPART-ASHEVLL-AND', 'city': 'Anderson', 'dma_code': 567, 'latitude': 34.503439399999998, 'longitude': -82.650133199999999, 'region': 'SC', 'slug': 'anderson-sc'},
    {'fcc_dma_str': 'GUAM', 'city': 'Guam', 'dma_code': 596, 'latitude': 39.940345299999997, 'longitude': -82.013192399999994, 'region': 'OH', 'slug': 'zanesville-oh'},
    {'fcc_dma_str': 'ION', 'city': 'Akron', 'dma_code': 510, 'latitude': 41.081444699999999, 'longitude': -81.519005300000003, 'region': 'OH', 'slug': 'akron-oh'}, # due to bad data putting channel affiliation in dma
    {'fcc_dma_str': 'PUERTO RICO', 'city': 'Puerto Rico', 'dma_code': 490, 'latitude': 36.152852, 'longitude': -96.5573665, 'region': 'PR', 'slug': 'puerto-rico'},
    {'fcc_dma_str': 'VIRGIN ISLANDS', 'city': 'Virgin Islands', 'dma_code': 491, 'latitude': 18.0659719, 'longitude': -65.2991776, 'region': 'VI', 'slug': 'virgin-islands'},
    {'fcc_dma_str': 'GUAM', 'city': 'Guam', 'dma_code': 495, 'latitude': 13.4506574, 'longitude': 144.5086191, 'region': 'GU', 'slug': 'guam'}
]


def get_dma_info(dma):
    dma_info = []
    for city_item in major_cities:
        if int(city_item["dma_code"]) == int(dma):
            dma_info.append(city_item)
    return dma_info
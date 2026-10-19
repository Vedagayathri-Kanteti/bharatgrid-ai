"""
Complete Pan-India Electricity Grid Hierarchy:
All 28 States and 8 Union Territories of India (36 Total Entities).
Each State/UT contains real districts, villages, and substation feeders with GPS coordinates,
DISCOM names, feeder types, and localized climate profiles.
"""

INDIAN_GRID_DATA = {
    # ------------------ 28 STATES ------------------
    "Andhra Pradesh": {
        "discom": "APEPDCL / APSPDCL",
        "districts": {
            "Visakhapatnam": {
                "Gajuwaka Industrial Substation": {"lat": 17.6905, "lon": 83.2185, "climate": "Coastal Humid Industrial", "base_load_mw": 75, "type": "Industrial & Domestic"},
                "Bheemunipatnam (Bheemili) Coastal Village": {"lat": 17.8911, "lon": 83.4539, "climate": "Coastal Sea Breeze (Pleasant)", "base_load_mw": 25, "type": "Fishing Village & Tourism"},
                "Anakapalle Rural Feeder": {"lat": 17.6913, "lon": 83.0039, "climate": "Semi-Coastal Humid Heat", "base_load_mw": 38, "type": "Jaggery Market & Village"}
            },
            "Vijayawada (NTR)": {
                "Benz Circle Urban Substation": {"lat": 16.5062, "lon": 80.6480, "climate": "Extreme Krishna Basin Heat (44C+)", "base_load_mw": 80, "type": "Urban Commercial & Homes"},
                "Ibrahimpatnam Thermal Feeder": {"lat": 16.5884, "lon": 80.5255, "climate": "Riverfront Humid Heat", "base_load_mw": 45, "type": "Thermal Worker Village & Domestic"},
                "Gannavaram Rural Feeder": {"lat": 16.5413, "lon": 80.8016, "climate": "Humid Delta Heat", "base_load_mw": 35, "type": "Airport & Village Mixed"}
            },
            "Guntur": {
                "Amaravati Capital Feeder": {"lat": 16.5735, "lon": 80.3575, "climate": "Hot Delta River Plains", "base_load_mw": 50, "type": "Institutional & Village"},
                "Tenali Rural Substation": {"lat": 16.2430, "lon": 80.6400, "climate": "Humid Fertile Delta", "base_load_mw": 42, "type": "Paddy Agricultural & Homes"},
                "Mangalagiri Handloom Village": {"lat": 16.4357, "lon": 80.5594, "climate": "Dry Hot Foothills", "base_load_mw": 36, "type": "Weavers Village & Domestic"}
            },
            "Anantapur": {
                "Kadiri Village Feeder": {"lat": 14.1132, "lon": 78.1633, "climate": "Rayalaseema Severe Drought Heat", "base_load_mw": 28, "type": "Arid Village & Groundnut Farms"},
                "Dharmavaram Silk Feeder": {"lat": 14.4137, "lon": 77.7126, "climate": "Dry Scorching Heat", "base_load_mw": 35, "type": "Weaving Village & Domestic"},
                "Hindupur Industrial Feeder": {"lat": 13.8290, "lon": 77.4930, "climate": "Border Plateau Dry Heat", "base_load_mw": 40, "type": "Border Commercial & Rural"}
            }
        }
    },
    "Arunachal Pradesh": {
        "discom": "Department of Power, Arunachal Pradesh",
        "districts": {
            "Papum Pare (Itanagar)": {
                "Itanagar Capital Feeder": {"lat": 27.0844, "lon": 93.6053, "climate": "Sub-Tropical Mountain Pleasant", "base_load_mw": 24, "type": "Capital Domestic & Admin"},
                "Naharlagun Substation": {"lat": 27.1050, "lon": 93.6930, "climate": "Valley Mountain Breeze", "base_load_mw": 20, "type": "Commercial & Residential"}
            },
            "Tawang": {
                "Tawang Monastery Feeder": {"lat": 27.5861, "lon": 91.8594, "climate": "Cold Alpine Himalayan (14C Summer)", "base_load_mw": 12, "type": "High Altitude Village & Defense"},
                "Jang Hydro Feeder": {"lat": 27.5750, "lon": 91.9820, "climate": "Chilly Alpine Mountain Gorge", "base_load_mw": 8, "type": "Hydro Worker Hamlet"}
            },
            "East Siang (Pasighat)": {
                "Pasighat Riverfront Feeder": {"lat": 28.0667, "lon": 95.3333, "climate": "Siang River Valley Rain-Cooled", "base_load_mw": 16, "type": "Horticulture Village & Homes"}
            }
        }
    },
    "Assam": {
        "discom": "APDCL (Assam Power Distribution Co)",
        "districts": {
            "Kamrup Metropolitan (Guwahati)": {
                "Dispur Secretariat Feeder": {"lat": 26.1433, "lon": 91.7898, "climate": "Brahmaputra Valley Humid Heat", "base_load_mw": 65, "type": "Urban Administrative"},
                "Chandrapur Village Feeder": {"lat": 26.2333, "lon": 91.9333, "climate": "Riverfront Monsoon Humid", "base_load_mw": 25, "type": "Rural Village & Fishery"}
            },
            "Dibrugarh": {
                "Chabua Tea Estate Feeder": {"lat": 27.4833, "lon": 95.1833, "climate": "Lush Tea Garden Pleasant Breeze", "base_load_mw": 32, "type": "Tea Plantation Workers & Village"},
                "Moran Oil Town Feeder": {"lat": 27.1833, "lon": 94.9333, "climate": "Humid Upper Assam Plain", "base_load_mw": 28, "type": "Oil Field Hamlet & Domestic"}
            },
            "Cachar (Silchar)": {
                "Lakhipur Rural Feeder": {"lat": 24.8000, "lon": 93.0167, "climate": "Barak Valley Heavy Monsoon", "base_load_mw": 22, "type": "Village Homes & Paddy"}
            }
        }
    },
    "Bihar": {
        "discom": "NBPDCL / SBPDCL",
        "districts": {
            "Patna": {
                "Danapur Substation": {"lat": 25.6333, "lon": 85.0500, "climate": "Gangetic Plain Intense Summer Heat (43C)", "base_load_mw": 70, "type": "Urban Railway & Domestic"},
                "Fatuha Rural Feeder": {"lat": 25.5000, "lon": 85.3167, "climate": "Gangetic Agricultural Plain", "base_load_mw": 35, "type": "Village Homes & Tube Wells"}
            },
            "Gaya": {
                "Bodh Gaya Feeder": {"lat": 24.6951, "lon": 84.9913, "climate": "Severe Southern Bihar Summer Heat", "base_load_mw": 32, "type": "Pilgrim Town & Village"},
                "Sherghati Rural Substation": {"lat": 24.5667, "lon": 84.7833, "climate": "Dry Scorching Plain", "base_load_mw": 28, "type": "Village Households & Agriculture"}
            },
            "Muzaffarpur": {
                "Kanti Village Feeder": {"lat": 26.2000, "lon": 85.3000, "climate": "North Bihar Litchi Belt Heat", "base_load_mw": 36, "type": "Litchi Orchards & Village Homes"}
            }
        }
    },
    "Chhattisgarh": {
        "discom": "CSPDCL (State Power Distribution)",
        "districts": {
            "Raipur": {
                "Nava Raipur Smart Substation": {"lat": 21.1611, "lon": 81.7867, "climate": "Central Plateau High Summer Heat", "base_load_mw": 60, "type": "Smart City Admin & Homes"},
                "Abhanpur Rural Feeder": {"lat": 21.0500, "lon": 81.7500, "climate": "Mahanadi Basin Heat", "base_load_mw": 32, "type": "Rice Bowl Village & Irrigation"}
            },
            "Bastar (Jagdalpur)": {
                "Tokapal Tribal Village Feeder": {"lat": 19.0000, "lon": 81.8500, "climate": "Dense Sal Forest Pleasant Breeze", "base_load_mw": 18, "type": "Tribal Hamlets & Forest Produce"},
                "Chitrakote Falls Feeder": {"lat": 19.2083, "lon": 81.7083, "climate": "Waterfront Forest Breeze", "base_load_mw": 14, "type": "Eco-Tourism & Village"}
            },
            "Bilaspur": {
                "Kota Rural Feeder": {"lat": 22.3000, "lon": 82.0333, "climate": "Coal Belt Plain Heat", "base_load_mw": 38, "type": "Thermal Border & Village"}
            }
        }
    },
    "Goa": {
        "discom": "Goa Electricity Department",
        "districts": {
            "North Goa": {
                "Mapusa Substation": {"lat": 15.5937, "lon": 73.8142, "climate": "Coastal Tropical Sea Breeze", "base_load_mw": 40, "type": "Semi-Urban Domestic & Tourism"},
                "Arambol Coastal Village Feeder": {"lat": 15.6869, "lon": 73.7042, "climate": "Arabian Sea Breeze (Pleasant)", "base_load_mw": 22, "type": "Coastal Village & Fishing"}
            },
            "South Goa": {
                "Margao Central Substation": {"lat": 15.2832, "lon": 73.9862, "climate": "Coastal Humid Tropical", "base_load_mw": 48, "type": "Commercial & Residential"},
                "Canacona Southern Feeder": {"lat": 14.9989, "lon": 74.0478, "climate": "Foothill Sea Breeze", "base_load_mw": 20, "type": "Forest Border Village"}
            }
        }
    },
    "Gujarat": {
        "discom": "GUVNL (DGVCL / MGVCL / PGVCL / UGVCL)",
        "districts": {
            "Ahmedabad": {
                "Sanand Auto Belt Substation": {"lat": 22.9867, "lon": 72.3800, "climate": "Semi-Arid Intense Summer (44C)", "base_load_mw": 85, "type": "Industrial Auto & Village"},
                "Dholka Agricultural Feeder": {"lat": 22.7200, "lon": 72.4400, "climate": "Dry Scorching Plain", "base_load_mw": 38, "type": "Rural Village & Farming"}
            },
            "Kutch (Bhuj)": {
                "Nakhatrana Rural Feeder": {"lat": 23.3500, "lon": 69.2667, "climate": "Arid Desert Border Sun", "base_load_mw": 28, "type": "Kutch Embroidery Village & Wind Farms"},
                "Mandvi Coastal Port Feeder": {"lat": 22.8333, "lon": 69.3556, "climate": "Arabian Sea Salt Breeze", "base_load_mw": 32, "type": "Shipbuilding Port Village"}
            },
            "Surat": {
                "Bardoli Sugarcane Feeder": {"lat": 21.1200, "lon": 73.1100, "climate": "South Gujarat Humid Heat", "base_load_mw": 46, "type": "Sugar Co-op & Village Homes"}
            }
        }
    },
    "Haryana": {
        "discom": "DHBVN / UHBVN",
        "districts": {
            "Gurugram": {
                "Cyber City DLF Substation": {"lat": 28.4900, "lon": 77.0900, "climate": "Intense NCR Heatwave", "base_load_mw": 110, "type": "IT Corporate & Highrise Domestic"},
                "Sohna Rural Feeder": {"lat": 28.2500, "lon": 77.0667, "climate": "Aravalli Foothills Scorching Heat", "base_load_mw": 38, "type": "Hot Springs Village & Farming"}
            },
            "Hisar": {
                "Hansi Rural Substation": {"lat": 29.1000, "lon": 75.9667, "climate": "Semi-Arid Dry Heat (46C)", "base_load_mw": 44, "type": "Buffalo Dairy & Village Agriculture"},
                "Narnaund Village Feeder": {"lat": 29.2200, "lon": 76.1500, "climate": "Dry Plains Scorching Sun", "base_load_mw": 30, "type": "Wheat-Cotton Village Belt"}
            },
            "Karnal": {
                "Gharaunda Rice Mill Feeder": {"lat": 29.5400, "lon": 76.9700, "climate": "Basmati Belt Gangetic Plains", "base_load_mw": 42, "type": "Rice Processing & Rural Homes"}
            }
        }
    },
    "Himachal Pradesh": {
        "discom": "HPSEBL (Hydro Electric Board)",
        "districts": {
            "Shimla": {
                "Theog Apple Orchard Feeder": {"lat": 31.1219, "lon": 77.3562, "climate": "Cool Alpine Mountain (18C Summer)", "base_load_mw": 18, "type": "Apple Orchards & Village"},
                "Rohru Valley Substation": {"lat": 31.2045, "lon": 77.7523, "climate": "Chilly Himalayan River Valley", "base_load_mw": 22, "type": "Village Homes & Cold Storage"}
            },
            "Kullu (Manali)": {
                "Manali Town Feeder": {"lat": 32.2432, "lon": 77.1892, "climate": "Pleasant Himalayan Highland (16C)", "base_load_mw": 25, "type": "Mountain Tourism & Homes"},
                "Naggar Heritage Village": {"lat": 32.1444, "lon": 77.1697, "climate": "Cool Pine Forest Climate", "base_load_mw": 12, "type": "Village Households & Art"}
            },
            "Lahaul & Spiti": {
                "Kaza High Altitude Feeder": {"lat": 32.2276, "lon": 78.0710, "climate": "Cold High Desert (10C Summer)", "base_load_mw": 8, "type": "Remote Buddhist Mountain Village"},
                "Keylong Valley Substation": {"lat": 32.5710, "lon": 77.0320, "climate": "Chilly Mountain Oasis", "base_load_mw": 10, "type": "District Hamlet & Army Post"}
            }
        }
    },
    "Jharkhand": {
        "discom": "JBVNL (State Bijli Vitran)",
        "districts": {
            "Ranchi": {
                "Kanke Agro Plateau Feeder": {"lat": 23.4300, "lon": 85.3200, "climate": "Chota Nagpur Pleasant Plateau", "base_load_mw": 48, "type": "Veterinary University & Village"},
                "Bundu Tribal Village Feeder": {"lat": 23.1800, "lon": 85.5800, "climate": "Plateau Forest Breeze", "base_load_mw": 20, "type": "Lac Cultivation & Rural Homes"}
            },
            "Dhanbad": {
                "Jharia Coal Belt Substation": {"lat": 23.7500, "lon": 86.4200, "climate": "Severe Industrial Heat Corridor", "base_load_mw": 72, "type": "Colliery Village & Labor Hamlets"}
            },
            "East Singhbhum (Jamshedpur)": {
                "Ghatshila Copper Belt Feeder": {"lat": 22.5800, "lon": 86.4800, "climate": "Subarnarekha River Valley Heat", "base_load_mw": 34, "type": "Tribal Artisans & Domestic"}
            }
        }
    },
    "Karnataka": {
        "discom": "BESCOM / HESCOM / MESCOM / CHESCOM / GESCOM",
        "districts": {
            "Bengaluru Urban": {
                "Whitefield Tech Corridor": {"lat": 12.9698, "lon": 77.7500, "climate": "Pleasant Plateau (26C)", "base_load_mw": 120, "type": "Urban Commercial & IT"},
                "Electronic City Substation": {"lat": 12.8452, "lon": 77.6602, "climate": "Pleasant Urban Plateau", "base_load_mw": 90, "type": "Industrial & Domestic"}
            },
            "Mysuru": {
                "Nanjangud Industrial Village": {"lat": 12.1197, "lon": 76.6806, "climate": "Pleasant Deccan Basin", "base_load_mw": 45, "type": "Industrial & Village"},
                "Hunsur Rural Feeder": {"lat": 12.3083, "lon": 76.2917, "climate": "Breezy Foothills", "base_load_mw": 28, "type": "Tobacco & Paddy Farming"}
            },
            "Dakshina Kannada (Mangaluru)": {
                "Bantwal Coastal Village Feeder": {"lat": 12.8931, "lon": 75.0353, "climate": "Coastal Humid Tropical Breeze", "base_load_mw": 35, "type": "Arecanut Village & Homes"}
            }
        }
    },
    "Kerala": {
        "discom": "KSEB (Electricity Board)",
        "districts": {
            "Wayanad": {
                "Kalpetta Hill Feeder": {"lat": 11.6050, "lon": 76.0830, "climate": "Cool Mountain Coffee Belt (20C)", "base_load_mw": 18, "type": "Coffee Plantations & Village"},
                "Mananthavady Valley Feeder": {"lat": 11.8028, "lon": 76.0036, "climate": "Pleasant Forest Breeze", "base_load_mw": 16, "type": "Tea Estate Villages"}
            },
            "Ernakulam (Kochi)": {
                "Aluva Riverfront Feeder": {"lat": 10.1076, "lon": 76.3516, "climate": "Humid Coastal Tropical", "base_load_mw": 55, "type": "Suburban Homes & Small Industry"},
                "Paravur Coastal Village": {"lat": 10.1472, "lon": 76.2308, "climate": "Sea Breeze Coastal", "base_load_mw": 32, "type": "Backwater Village & Coir"}
            },
            "Palakkad": {
                "Chittur Windmill Basin Feeder": {"lat": 10.7000, "lon": 76.7200, "climate": "Palakkad Gap Dry Heat Corridor", "base_load_mw": 34, "type": "Wind Farm Villages & Paddy"}
            }
        }
    },
    "Madhya Pradesh": {
        "discom": "MPPKVVCL / MPMKVVCL / MPPoKVVCL",
        "districts": {
            "Bhopal": {
                "Berasia Rural Feeder": {"lat": 23.6300, "lon": 77.4300, "climate": "Malwa Plateau High Summer Heat", "base_load_mw": 35, "type": "Village Wheat Farms & Homes"},
                "Kolar Satellite Substation": {"lat": 23.1800, "lon": 77.4200, "climate": "Lakeside Suburban Heat", "base_load_mw": 48, "type": "Suburban Residential"}
            },
            "Indore": {
                "Sanwer Rural Agrotech Feeder": {"lat": 22.9800, "lon": 75.8300, "climate": "Malwa Fertile Plateau Heat", "base_load_mw": 42, "type": "Soybean Belt & Village Homes"},
                "Mhow Cantonment Feeder": {"lat": 22.5500, "lon": 75.7600, "climate": "Elevated Breezy Ridge", "base_load_mw": 36, "type": "Defense & Village Mixed"}
            },
            "Gwalior": {
                "Dabra Sugarcane Substation": {"lat": 25.9000, "lon": 78.3300, "climate": "Chambal Severe Summer Heat (46C)", "base_load_mw": 40, "type": "Sugar Mill & Village"}
            }
        }
    },
    "Maharashtra": {
        "discom": "MSEDCL (Mahavitaran)",
        "districts": {
            "Mumbai": {
                "Dharavi Central Substation": {"lat": 19.0402, "lon": 72.8508, "climate": "Dense Coastal Humid", "base_load_mw": 95, "type": "Small Scale Industrial & Homes"},
                "Andheri West Domestic Feeder": {"lat": 19.1363, "lon": 72.8277, "climate": "Coastal Sea Breeze", "base_load_mw": 110, "type": "Dense Residential"}
            },
            "Nagpur (Vidarbha)": {
                "Katol Orange Belt Feeder": {"lat": 21.2728, "lon": 78.5867, "climate": "Severe Vidarbha Heatwave (46C+)", "base_load_mw": 40, "type": "Orange Orchards & Village"},
                "Umred Rural Substation": {"lat": 20.8542, "lon": 79.3258, "climate": "Intense Scorching Plain", "base_load_mw": 36, "type": "Coal Belt Village & Agriculture"}
            },
            "Pune": {
                "Baramati Rural Agrotech Feeder": {"lat": 18.1517, "lon": 74.5772, "climate": "Dry Semi-Arid Heat", "base_load_mw": 50, "type": "Sugar Belt & Village Homes"},
                "Shirur Industrial Village": {"lat": 18.8272, "lon": 74.3789, "climate": "Dry Plateau Plain", "base_load_mw": 48, "type": "Auto Industry & Village"}
            }
        }
    },
    "Manipur": {
        "discom": "MSPDCL (Power Distribution Co)",
        "districts": {
            "Imphal West": {
                "Kangla Fort Heritage Feeder": {"lat": 24.8170, "lon": 93.9368, "climate": "Imphal Valley Pleasant (24C)", "base_load_mw": 30, "type": "Valley Capital & Handloom"},
                "Lamsang Rural Feeder": {"lat": 24.8833, "lon": 93.8667, "climate": "Valley Paddy Breeze", "base_load_mw": 16, "type": "Weaving Village & Farming"}
            },
            "Churachandpur": {
                "Lamka Hill Feeder": {"lat": 24.3333, "lon": 93.6833, "climate": "Highland Mountain Forest", "base_load_mw": 18, "type": "Tribal Hill Village & Homes"}
            }
        }
    },
    "Meghalaya": {
        "discom": "MeECL (Meghalaya Energy Corp)",
        "districts": {
            "East Khasi Hills (Shillong)": {
                "Shillong Peak Pine Feeder": {"lat": 25.5788, "lon": 91.8933, "climate": "Cool Pine Highlands (17C Summer)", "base_load_mw": 28, "type": "Scotland of the East Homes"},
                "Cherrapunji (Sohra) Rain Feeder": {"lat": 25.2702, "lon": 91.7323, "climate": "World Rainfall Capital / Chilly", "base_load_mw": 12, "type": "Eco-Hamlets & Tourism"}
            },
            "West Garo Hills (Tura)": {
                "Tura Ridge Feeder": {"lat": 25.5167, "lon": 90.2167, "climate": "Garo Hills Pleasant Sub-Tropical", "base_load_mw": 15, "type": "Spices Village & Domestic"}
            }
        }
    },
    "Mizoram": {
        "discom": "Power & Electricity Dept Mizoram",
        "districts": {
            "Aizawl": {
                "Durtlang Ridge Feeder": {"lat": 23.7700, "lon": 92.7300, "climate": "Cool Mountain Ridge (20C)", "base_load_mw": 25, "type": "Ridge Capital & Homes"},
                "Sairang River Feeder": {"lat": 23.7900, "lon": 92.6500, "climate": "Valley Riverfront Breeze", "base_load_mw": 14, "type": "Transit Hamlet & Bamboo"}
            },
            "Champhai": {
                "Zokhawthar Border Feeder": {"lat": 23.3600, "lon": 93.3300, "climate": "High Altitude Cool Border (16C)", "base_load_mw": 10, "type": "Border Grape Vineyards & Village"}
            }
        }
    },
    "Nagaland": {
        "discom": "Department of Power Nagaland",
        "districts": {
            "Kohima": {
                "Naga Heritage Village Kisama Feeder": {"lat": 25.6100, "lon": 94.1100, "climate": "Cool Mountain Highland (18C)", "base_load_mw": 18, "type": "Hornbill Festival Village & Homes"},
                "Jakhama Valley Feeder": {"lat": 25.5800, "lon": 94.1300, "climate": "Terrace Farming Valley Breeze", "base_load_mw": 12, "type": "Paddy Terraces & Village"}
            },
            "Dimapur": {
                "Chumukedima Foothill Substation": {"lat": 25.7900, "lon": 93.7700, "climate": "Sub-Tropical Plain Humid", "base_load_mw": 28, "type": "Commercial Gateway & Homes"}
            }
        }
    },
    "Odisha": {
        "discom": "GRIDCO (TPCODL / TPWODL / TPSODL / TPNODL)",
        "districts": {
            "Khordha (Bhubaneswar)": {
                "Chandrasekharpur IT Substation": {"lat": 20.3200, "lon": 85.8200, "climate": "Coastal Plains Humid Heat", "base_load_mw": 65, "type": "Urban IT & Domestic"},
                "Jatni Railway Feeder": {"lat": 20.1600, "lon": 85.7000, "climate": "Semi-Coastal Humid Plain", "base_load_mw": 38, "type": "Railway Hub & Village"}
            },
            "Ganjam (Berhampur)": {
                "Gopalpur-on-Sea Coastal Feeder": {"lat": 19.2600, "lon": 84.9000, "climate": "Bay of Bengal Sea Breeze (Pleasant)", "base_load_mw": 26, "type": "Port Village & Tourism"},
                "Aska Sugar Belt Feeder": {"lat": 19.6100, "lon": 84.6600, "climate": "Inland Hot Humid", "base_load_mw": 32, "type": "Sugarcane Farmers & Domestic"}
            },
            "Sambalpur": {
                "Burla Hirakud Dam Feeder": {"lat": 21.5000, "lon": 83.8700, "climate": "Severe Western Odisha Heat (45C)", "base_load_mw": 48, "type": "Hydro Town & Industrial"}
            }
        }
    },
    "Punjab": {
        "discom": "PSPCL (Punjab State Power Corp)",
        "districts": {
            "Ludhiana": {
                "Jagraon Rural Substation": {"lat": 30.7833, "lon": 75.4833, "climate": "Northern Agri Plain High Summer Heat", "base_load_mw": 48, "type": "Paddy Tube Wells & Village"},
                "Khanna Grain Market Feeder": {"lat": 30.7069, "lon": 76.2208, "climate": "Intense Summer Heat", "base_load_mw": 52, "type": "Grain Market Hub & Homes"}
            },
            "Amritsar": {
                "Ajnala Border Village Feeder": {"lat": 31.8417, "lon": 74.7611, "climate": "Border Agricultural Plain", "base_load_mw": 30, "type": "Border Villages & Irrigation"},
                "Majitha Rural Feeder": {"lat": 31.7611, "lon": 74.9528, "climate": "Plains Heat", "base_load_mw": 32, "type": "Village Homes & Farms"}
            },
            "Bathinda": {
                "Talwandi Sabo Rural Feeder": {"lat": 29.9800, "lon": 75.0900, "climate": "Malwa Cotton Belt Severe Heat (47C)", "base_load_mw": 40, "type": "Cotton Farming & Village"}
            }
        }
    },
    "Rajasthan": {
        "discom": "JVVNL / JdVVNL / AVVNL",
        "districts": {
            "Jodhpur": {
                "Phalodi Village Feeder (Hottest in India 50C)": {"lat": 27.1311, "lon": 72.3638, "climate": "Extreme Thar Desert Scorching (50C)", "base_load_mw": 30, "type": "Desert Village & Solar Park"},
                "Osian Desert Feeder": {"lat": 26.7265, "lon": 72.9090, "climate": "Severe Desert Heat", "base_load_mw": 25, "type": "Desert Village & Dunes"}
            },
            "Jaipur": {
                "Sanganer Urban Substation": {"lat": 26.8242, "lon": 75.7725, "climate": "Arid Plains Summer Heat", "base_load_mw": 75, "type": "Urban Homes & Textile"},
                "Chomu Rural Agricultural Feeder": {"lat": 27.1706, "lon": 75.7226, "climate": "Semi-Arid Farming Belt", "base_load_mw": 42, "type": "Vegetable Farms & Village"}
            },
            "Jaisalmer": {
                "Pokhran Desert Substation": {"lat": 26.9213, "lon": 71.9168, "climate": "Deep Desert Intense Solar Sun", "base_load_mw": 30, "type": "Defense & Desert Village"},
                "Sam Sand Dunes Feeder": {"lat": 26.8289, "lon": 70.5050, "climate": "Pure Desert Sand Sun", "base_load_mw": 18, "type": "Remote Desert Hamlet"}
            }
        }
    },
    "Sikkim": {
        "discom": "Power Department, Government of Sikkim",
        "districts": {
            "East Sikkim (Gangtok)": {
                "MG Marg Capital Feeder": {"lat": 27.3389, "lon": 88.6065, "climate": "Cool Himalayan Hill Haven (18C)", "base_load_mw": 22, "type": "Himalayan Capital & Tourism"},
                "Ranipool Valley Feeder": {"lat": 27.2800, "lon": 88.5800, "climate": "Sub-Alpine Mountain Valley", "base_load_mw": 16, "type": "River Valley Hamlets"}
            },
            "North Sikkim (Mangan)": {
                "Lachung Alpine Village Feeder": {"lat": 27.6900, "lon": 88.7400, "climate": "Cold Alpine Valley (12C Summer)", "base_load_mw": 8, "type": "High Himalayan Village & Apples"}
            }
        }
    },
    "Tamil Nadu": {
        "discom": "TANGEDCO",
        "districts": {
            "Chennai": {
                "Guindy Industrial Substation": {"lat": 13.0067, "lon": 80.2026, "climate": "Coastal Humid Heat", "base_load_mw": 85, "type": "Industrial & Domestic"},
                "Tambaram South Feeder": {"lat": 12.9249, "lon": 80.1000, "climate": "Suburban Humid Heat", "base_load_mw": 70, "type": "Residential & Transit"}
            },
            "Madurai": {
                "Melur Agricultural Feeder": {"lat": 10.0333, "lon": 78.3333, "climate": "Deep South Arid Heat", "base_load_mw": 38, "type": "Paddy & Jasmine Farming"},
                "Thirumangalam Rural Substation": {"lat": 9.8242, "lon": 77.9892, "climate": "Dry Scorching Plain", "base_load_mw": 35, "type": "Village Homes & Textile"}
            },
            "Nilgiris (Ooty)": {
                "Coonoor Tea Garden Feeder": {"lat": 11.3500, "lon": 76.8000, "climate": "Chilly Western Ghats Ridge (15C)", "base_load_mw": 18, "type": "Tea Plantations & Cold Climate"}
            }
        }
    },
    "Telangana": {
        "discom": "TSSPDCL / TSNPDCL",
        "districts": {
            "Hyderabad": {
                "Charminar Old City Feeder": {"lat": 17.3616, "lon": 78.4747, "climate": "Dense Urban Deccan Heat", "base_load_mw": 85, "type": "Urban Domestic & Commercial"},
                "Hitec City Cyberabad Substation": {"lat": 17.4435, "lon": 78.3772, "climate": "High-Tech Urban Heat", "base_load_mw": 110, "type": "Commercial & Residential"}
            },
            "Warangal": {
                "Dharmasagar Village Feeder": {"lat": 18.0022, "lon": 79.4312, "climate": "Rural Agricultural Plain", "base_load_mw": 35, "type": "Village Homes & Agri Pumps"},
                "Hanamkonda Substation": {"lat": 18.0138, "lon": 79.5519, "climate": "Central Telangana Plains", "base_load_mw": 55, "type": "Urban Domestic"}
            },
            "Nalgonda": {
                "Chityala Village Feeder": {"lat": 17.2289, "lon": 79.1306, "climate": "Rural High Heat Plain", "base_load_mw": 30, "type": "Village Households & Tube Wells"},
                "Miryalaguda Substation": {"lat": 16.8711, "lon": 79.5631, "climate": "Dry Semi-Arid Heat", "base_load_mw": 48, "type": "Rice Mill & Domestic"}
            },
            "Karimnagar": {
                "Ramagundam Industrial Feeder": {"lat": 18.8028, "lon": 79.4503, "climate": "Extreme Thermal Zone (46C+)", "base_load_mw": 95, "type": "Thermal & Industrial Mixed"},
                "Manakondur Village Feeder": {"lat": 18.3995, "lon": 79.1895, "climate": "Intense Summer Heat", "base_load_mw": 32, "type": "Agricultural & Rural Domestic"}
            }
        }
    },
    "Tripura": {
        "discom": "TSECL (Tripura State Electricity Corp)",
        "districts": {
            "West Tripura (Agartala)": {
                "Kunjaban Secretariat Feeder": {"lat": 23.8500, "lon": 91.2800, "climate": "Humid Delta Border Heat", "base_load_mw": 35, "type": "Capital Admin & Domestic"},
                "Ranirbazar Village Feeder": {"lat": 23.8300, "lon": 91.3600, "climate": "Howrah River Basin Humid", "base_load_mw": 18, "type": "Brick Kilns & Rural Homes"}
            },
            "Gomati (Udaipur)": {
                "Matabari Temple Feeder": {"lat": 23.5300, "lon": 91.4800, "climate": "Lakeside Monsoon Breeze", "base_load_mw": 16, "type": "Temple Town & Villages"}
            }
        }
    },
    "Uttar Pradesh": {
        "discom": "UPPCL (MVVNL / PVVNL / DVVNL / PuVVNL)",
        "districts": {
            "Lucknow": {
                "Malihabad Mango Belt Feeder": {"lat": 26.9213, "lon": 80.7107, "climate": "Gangetic Plain Intense Summer", "base_load_mw": 36, "type": "Mango Orchards & Village Homes"},
                "Mohanlalganj Village Feeder": {"lat": 26.6711, "lon": 80.9856, "climate": "Awadh Agricultural Plain", "base_load_mw": 34, "type": "Village Households & Tube Wells"}
            },
            "Varanasi": {
                "Pindra Rural Feeder": {"lat": 25.4855, "lon": 82.8512, "climate": "Eastern UP Extreme Summer Heat", "base_load_mw": 38, "type": "Rural Village & Farming"},
                "Sevapuri Weavers Village": {"lat": 25.3344, "lon": 82.7811, "climate": "Dense Gangetic Plain Heat", "base_load_mw": 30, "type": "Silk Weavers & Homes"}
            },
            "Agra": {
                "Fatehpur Sikri Heritage Feeder": {"lat": 27.0900, "lon": 77.6700, "climate": "Braj Arid Scorching Heat (45C)", "base_load_mw": 34, "type": "Heritage Village & Stone Crafters"}
            }
        }
    },
    "Uttarakhand": {
        "discom": "UPCL (Uttarakhand Power Corp)",
        "districts": {
            "Dehradun": {
                "Rishikesh Foothills Feeder": {"lat": 30.0869, "lon": 78.2676, "climate": "Ganga Riverfront Pleasant Breeze", "base_load_mw": 35, "type": "Ashrams & Riverfront Village"},
                "Mussoorie Ridge Feeder": {"lat": 30.4598, "lon": 78.0644, "climate": "Cool Himalayan Queen of Hills (18C)", "base_load_mw": 20, "type": "Hill Resort & Mountain Homes"}
            },
            "Nainital": {
                "Bhimtal Lake Feeder": {"lat": 29.3500, "lon": 79.5600, "climate": "Kumaon Lake Breeze (Pleasant)", "base_load_mw": 16, "type": "Lakeside Villages & Agriculture"}
            },
            "Chamoli": {
                "Joshimath Gateway Feeder": {"lat": 30.5500, "lon": 79.5600, "climate": "Chilly Alpine Pilgrim Valley", "base_load_mw": 12, "type": "Badrinath Base & Mountain Villages"}
            }
        }
    },
    "West Bengal": {
        "discom": "WBSEDCL (State Electricity Dist)",
        "districts": {
            "Kolkata": {
                "Salt Lake IT Sector V": {"lat": 22.5800, "lon": 88.4300, "climate": "Delta Tropical Humid Heat", "base_load_mw": 90, "type": "Tech Hub & Commercial"},
                "Jadavpur Domestic Feeder": {"lat": 22.4900, "lon": 88.3700, "climate": "Dense Urban Humid", "base_load_mw": 75, "type": "Dense Residential"}
            },
            "Darjeeling": {
                "Kurseong Tea Hills Feeder": {"lat": 26.8800, "lon": 88.2800, "climate": "Chilly Cloud-Capped Hills (15C)", "base_load_mw": 18, "type": "Darjeeling Tea Estates & Homes"},
                "Kalimpong Orchid Feeder": {"lat": 27.0600, "lon": 88.4700, "climate": "Pleasant Sub-Himalayan Ridge", "base_load_mw": 16, "type": "Floriculture & Mountain Village"}
            },
            "Purba Bardhaman": {
                "Katwa Rice Bowl Feeder": {"lat": 23.6500, "lon": 88.1300, "climate": "Gangetic Paddy Plain Heat", "base_load_mw": 38, "type": "Paddy Farmers & Domestic"}
            }
        }
    },

    # ------------------ 8 UNION TERRITORIES ------------------
    "Andaman and Nicobar Islands": {
        "discom": "Electricity Department, Andaman & Nicobar",
        "districts": {
            "South Andaman": {
                "Port Blair Marina Feeder": {"lat": 11.6234, "lon": 92.7265, "climate": "Oceanic Tropical Island Sea Breeze", "base_load_mw": 26, "type": "Island Capital & Defense"},
                "Havelock (Swaraj Dweep) Feeder": {"lat": 12.0000, "lon": 92.9800, "climate": "Pleasant Coastal Island Breeze", "base_load_mw": 10, "type": "Eco-Island Village & Tourism"}
            }
        }
    },
    "Chandigarh": {
        "discom": "Chandigarh Electricity Department",
        "districts": {
            "Chandigarh": {
                "Sector 17 City Centre Feeder": {"lat": 30.7415, "lon": 76.7681, "climate": "Shivalik Plains Summer Heat", "base_load_mw": 55, "type": "Planned Commercial & Homes"},
                "Manimajra Substation": {"lat": 30.7200, "lon": 76.8400, "climate": "Semi-Urban Plains Heat", "base_load_mw": 35, "type": "Old Township & Residential"}
            }
        }
    },
    "Dadra and Nagar Haveli and Daman and Diu": {
        "discom": "DNHDD Power Distribution Corp",
        "districts": {
            "Daman": {
                "Nani Daman Coastal Feeder": {"lat": 20.4283, "lon": 72.8397, "climate": "Arabian Sea Coastal Breeze", "base_load_mw": 32, "type": "Coastal Town & Fishermen Village"}
            },
            "Dadra and Nagar Haveli": {
                "Silvassa Industrial Feeder": {"lat": 20.2700, "lon": 73.0000, "climate": "Inland Humid Heat", "base_load_mw": 48, "type": "Manufacturing & Tribal Villages"}
            }
        }
    },
    "Delhi (NCT)": {
        "discom": "BRPL / BYPL / TPDDL",
        "districts": {
            "North Delhi": {
                "Narela Industrial Feeder": {"lat": 28.8500, "lon": 77.0900, "climate": "Severe Plains Summer Loo (45C+)", "base_load_mw": 65, "type": "Industrial & Resettlement Villages"},
                "Alipur Rural Feeder": {"lat": 28.8000, "lon": 77.1300, "climate": "Yamuna Agricultural Belt", "base_load_mw": 35, "type": "Rural Village & Greenhouses"}
            },
            "South Delhi": {
                "Saket Substation": {"lat": 28.5200, "lon": 77.2100, "climate": "Urban High Heat Island", "base_load_mw": 90, "type": "Urban Commercial & Homes"},
                "Chhatarpur Village Feeder": {"lat": 28.5000, "lon": 77.1800, "climate": "Aravalli Ridge Dry Heat", "base_load_mw": 45, "type": "Semi-Rural Village & Temples"}
            },
            "West Delhi": {
                "Najafgarh Rural Substation": {"lat": 28.6100, "lon": 76.9800, "climate": "Haryana Border Scorching Plains", "base_load_mw": 50, "type": "Agricultural Villages & Domestic"}
            }
        }
    },
    "Jammu and Kashmir": {
        "discom": "JPDCL / KPDCL (Power Development Dept)",
        "districts": {
            "Srinagar": {
                "Dal Lake Boulevard Feeder": {"lat": 34.0837, "lon": 74.7973, "climate": "Pleasant Kashmir Valley (22C Summer)", "base_load_mw": 38, "type": "Houseboats, Artisans & Homes"},
                "Hazratbal Substation": {"lat": 34.1200, "lon": 74.8400, "climate": "Valley Waterfront Breeze", "base_load_mw": 26, "type": "Pilgrim Centre & Village"}
            },
            "Baramulla (Gulmarg)": {
                "Gulmarg Alpine Meadow Feeder": {"lat": 34.0500, "lon": 74.3800, "climate": "Chilly Alpine Pine Forest (14C Summer)", "base_load_mw": 14, "type": "Ski Resort & Mountain Hamlets"}
            },
            "Jammu": {
                "R.S. Pura Border Feeder": {"lat": 32.6300, "lon": 74.7300, "climate": "Basmati Belt Scorching Plains (44C)", "base_load_mw": 35, "type": "Border Villages & Rice Farms"},
                "Akhnoor Chenab Feeder": {"lat": 32.9000, "lon": 74.7400, "climate": "Chenab Riverfront Plain", "base_load_mw": 28, "type": "Riverfront Village"}
            }
        }
    },
    "Ladakh": {
        "discom": "Ladakh Power Development Department",
        "districts": {
            "Leh": {
                "Leh Palace Capital Feeder": {"lat": 34.1526, "lon": 77.5771, "climate": "Cold High Desert (15C Summer, -15C Winter)", "base_load_mw": 16, "type": "Trans-Himalayan Capital & Tourism"},
                "Nubra Valley Feeder": {"lat": 34.6800, "lon": 77.5600, "climate": "Cold Desert Sand Dune Oasis", "base_load_mw": 8, "type": "Remote Double-Hump Camel Villages"}
            },
            "Kargil": {
                "Drass Valley Feeder (2nd Coldest Inhabited)": {"lat": 34.4300, "lon": 75.7500, "climate": "Extreme Sub-Zero Cold", "base_load_mw": 7, "type": "Gateway to Ladakh Mountain Village"}
            }
        }
    },
    "Lakshadweep": {
        "discom": "Lakshadweep Electricity Department",
        "districts": {
            "Lakshadweep": {
                "Kavaratti Island Feeder": {"lat": 10.5667, "lon": 72.6417, "climate": "Coral Atoll Tropical Sea Breeze", "base_load_mw": 8, "type": "Atoll Capital & Fishermen Homes"},
                "Agatti Island Airstrip Feeder": {"lat": 10.8500, "lon": 72.1800, "climate": "Lagoon Marine Breeze", "base_load_mw": 6, "type": "Coral Island Village & Airport"}
            }
        }
    },
    "Puducherry": {
        "discom": "Puducherry Electricity Department",
        "districts": {
            "Pondicherry": {
                "White Town Promenade Feeder": {"lat": 11.9338, "lon": 79.8353, "climate": "French Heritage Coastal Sea Breeze", "base_load_mw": 35, "type": "French Quarter & Tourism"},
                "Auroville Global Village Feeder": {"lat": 12.0070, "lon": 79.8106, "climate": "Pleasant Forest Belt Sea Breeze", "base_load_mw": 20, "type": "International Eco-Village & Solar"}
            },
            "Karaikal": {
                "Karaikal Port Feeder": {"lat": 10.9200, "lon": 79.8300, "climate": "Cauvery Delta Marine Coast", "base_load_mw": 24, "type": "Fishing Harbor & Port Village"}
            }
        }
    }
}

def get_indian_states():
    """Returns sorted list of all 36 States and Union Territories of India."""
    return sorted(list(INDIAN_GRID_DATA.keys()))

def get_districts_for_state(state_name="Telangana"):
    """Returns sorted list of districts in the selected state."""
    state_dict = INDIAN_GRID_DATA.get(state_name, INDIAN_GRID_DATA["Telangana"])
    return sorted(list(state_dict["districts"].keys()))

def get_villages_for_district(state_name="Telangana", district_name="Hyderabad"):
    """Returns sorted list of villages / substation feeders for the selected district."""
    state_dict = INDIAN_GRID_DATA.get(state_name, INDIAN_GRID_DATA["Telangana"])
    district_dict = state_dict["districts"].get(district_name, list(state_dict["districts"].values())[0])
    return sorted(list(district_dict.keys()))

def get_village_meta(state_name, district_name, village_name):
    """Fetches metadata (lat, lon, climate, base load, type) for the village."""
    state_dict = INDIAN_GRID_DATA.get(state_name, INDIAN_GRID_DATA["Telangana"])
    district_dict = state_dict["districts"].get(district_name, list(state_dict["districts"].values())[0])
    village_info = district_dict.get(village_name, list(district_dict.values())[0])
    return {
        **village_info,
        "discom": state_dict.get("discom", "State Electricity Board"),
        "state": state_name,
        "district": district_name,
        "village": village_name
    }

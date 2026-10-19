# 🇮🇳 BharatGrid: Pan-India Climate-Adaptive Electricity Management System
### Hyper-Local Power Allocation across all 28 States & 8 Union Territories

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Control_Center-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Analytics-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Open-Meteo](https://img.shields.io/badge/Open--Meteo-Satellite_API-4682B4?style=for-the-badge)](https://open-meteo.com/)

BharatGrid AI is an intelligent electricity allocation and power scheduling platform covering all 28 States and 8 Union Territories of India (36 Total Entities). Built for the Indian Power Grid (National Grid / One Nation One Grid) and State Electricity Distribution Companies (DISCOMs).

---

## Pan-India Geographic Coverage (All 36 States & UTs)

### 28 Indian States:
1. Andhra Pradesh (APEPDCL / APSPDCL) - Visakhapatnam, Vijayawada, Guntur, Anantapur
2. Arunachal Pradesh (Dept of Power, AP) - Papum Pare (Itanagar), Tawang, East Siang (Pasighat)
3. Assam (APDCL) - Kamrup (Guwahati), Dibrugarh (Chabua Tea Estate), Cachar (Silchar)
4. Bihar (NBPDCL / SBPDCL) - Patna (Danapur), Gaya (Bodh Gaya), Muzaffarpur (Kanti)
5. Chhattisgarh (CSPDCL) - Raipur, Bastar (Chitrakote Falls Feeder), Bilaspur
6. Goa (Goa Electricity Dept) - North Goa (Arambol Coastal Village), South Goa (Margao)
7. Gujarat (GUVNL - DGVCL, PGVCL) - Ahmedabad (Sanand), Kutch (Nakhatrana), Surat (Bardoli)
8. Haryana (DHBVN / UHBVN) - Gurugram (Cyber City, Sohna), Hisar, Karnal
9. Himachal Pradesh (HPSEBL) - Shimla (Theog Apple Orchards), Kullu (Manali), Lahaul & Spiti (Kaza)
10. Jharkhand (JBVNL) - Ranchi (Kanke Plateau), Dhanbad (Jharia Coal Belt), East Singhbhum
11. Karnataka (BESCOM / HESCOM) - Bengaluru (Whitefield, Electronic City), Mysuru, Mangaluru
12. Kerala (KSEB) - Wayanad (Kalpetta Coffee Belt), Kochi (Paravur Coastal), Palakkad
13. Madhya Pradesh (MPMKVVCL) - Bhopal, Indore (Sanwer Soybean Belt), Gwalior
14. Maharashtra (MSEDCL - Mahavitaran) - Mumbai, Nagpur (Katol Orange Belt), Pune (Baramati)
15. Manipur (MSPDCL) - Imphal West (Kangla Fort), Churachandpur (Lamka Hill Feeder)
16. Meghalaya (MeECL) - Shillong Peak Feeder, Cherrapunji (Sohra Rain Feeder), Tura
17. Mizoram (Power Dept) - Aizawl (Durtlang Ridge), Champhai (Zokhawthar Border Feeder)
18. Nagaland (Dept of Power) - Kohima (Naga Heritage Kisama Feeder), Dimapur
19. Odisha (TPCODL / TPWODL) - Bhubaneswar, Ganjam (Gopalpur-on-Sea), Sambalpur (Hirakud)
20. Punjab (PSPCL) - Ludhiana (Khanna Grain Market), Amritsar (Ajnala Border), Bathinda
21. Rajasthan (JVVNL / JdVVNL) - Jodhpur (Phalodi 50C), Jaipur (Amer), Jaisalmer (Pokhran)
22. Sikkim (Power Dept Sikkim) - Gangtok, Lachung Alpine Feeder (North Sikkim)
23. Tamil Nadu (TANGEDCO) - Chennai (Guindy), Madurai (Melur), Nilgiris (Coonoor / Ooty)
24. Telangana (TSSPDCL / TSNPDCL) - Hyderabad, Warangal, Nalgonda (Chityala), Karimnagar (Ramagundam)
25. Tripura (TSECL) - Agartala, Gomati (Matabari Temple Feeder)
26. Uttar Pradesh (UPPCL) - Lucknow (Malihabad Mango Belt), Varanasi (Sevapuri), Agra
27. Uttarakhand (UPCL) - Dehradun (Mussoorie Ridge), Nainital, Chamoli (Joshimath Gateway)
28. West Bengal (WBSEDCL) - Kolkata, Darjeeling (Kurseong Tea Hills), Purba Bardhaman

### 8 Union Territories:
29. Andaman and Nicobar Islands - South Andaman (Port Blair), Havelock Island (Swaraj Dweep)
30. Chandigarh - Sector 17 City Centre, Manimajra
31. Dadra and Nagar Haveli and Daman and Diu - Daman (Nani Daman Coastal Feeder), Silvassa
32. Delhi (NCT) (BRPL / BYPL / TPDDL) - North Delhi (Alipur), South Delhi (Saket), West Delhi (Najafgarh)
33. Jammu and Kashmir (JPDCL / KPDCL) - Srinagar (Dal Lake), Gulmarg Alpine Meadow, Jammu (R.S. Pura)
34. Ladakh (Ladakh PDD) - Leh (Nubra Valley Dunes), Kargil (Drass Valley Feeder)
35. Lakshadweep - Kavaratti Coral Atoll Feeder, Agatti Island
36. Puducherry - Pondicherry (Auroville Global Village), Karaikal Port Feeder

---

## Ground Reality & Operating Principles

In India, power cuts (load shedding) frequently affect rural villages, agricultural feeders, and small towns during peak mid-afternoon heat (1:00 PM - 5:00 PM) when temperatures reach 42C - 48C.

BharatGrid implements an automated, climate-driven policy:
1. Mid-Afternoon Extreme Heat:
   * Mandate: 100% UNINTERRUPTED CURRENT TO HOMES & VILLAGES. Fans and coolers stay operational. Zero power cuts permitted.
2. Cool, Chilly, or Breezy Weather:
   * Citizens utilize natural ventilation and open windows without needing heavy electrical cooling.
   * Action: PLANNED SAFE POWER CUT (ECO-CUT).
3. Watts Saved Calculation & Grid Rerouting:
   * Accurately tracks every Watt, Kilowatt-hour (kWh), and Megawatt (MW) conserved.
   * Reroutes conserved power across districts (e.g., from cool hill stations to heatwave-stressed plains).

---

## Quickstart

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```
Access at http://localhost:8501 in your browser.

---

## Resume Description

```markdown
BharatGrid - India Climate-Adaptive Electricity Allocation & Village Feeder Management
Tech Stack: Python, Streamlit, Plotly, Pandas, Open-Meteo Satellite API

- Designed a hyper-local climate-adaptive power scheduling platform for Indian State DISCOMs 
  (TSSPDCL, JVVNL, MSEDCL, BESCOM, etc.) covering all 36 Indian States and Union Territories.
- Formulated an algorithmic feeder-switching policy guaranteeing 100% uninterrupted power to 
  homes during peak mid-afternoon heat (42C-48C) and scheduling eco-cuts during cool breezes.
- Built a real-time conservation engine quantifying hourly Watts, kWh, and Megawatts saved by 
  leveraging natural cooling and ventilation in rural and urban communities.
- Programmed an Intra-State & Inter-District grid balancer diverting conserved electricity 
  from cool districts (e.g., Wayanad / Shimla) to heatwave-stressed villages (e.g., Phalodi / Nalgonda).
- Implemented an interactive DISCOM assistant engineer dashboard featuring 48-hour forward feeder logs 
  and real-time weather simulation controls.
```

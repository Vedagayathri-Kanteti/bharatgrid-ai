# BharatGrid: Climate-Adaptive Electricity Management System

A real-time power scheduling platform for Indian DISCOMs that aligns electricity distribution with weather conditions across all 28 states and 8 union territories.

**Live Application:** [https://bharatgrid-ai.streamlit.app/](https://bharatgrid-ai.streamlit.app/)

**Built with:** Python 3.11, Streamlit, Plotly, Pandas, Open-Meteo Satellite Weather API

---

## The Problem

In India, electricity distribution companies (DISCOMs) frequently resort to load shedding in rural villages and towns during peak summer afternoons (1:00 PM – 5:00 PM), precisely when temperatures reach 42°C to 48°C. This happens because cooling appliances run simultaneously across sectors, threatening transformer burnouts. 

At the same time, power is supplied continuously during cool mornings, pleasant monsoon evenings, or winter months when citizens do not require heavy mechanical cooling and can comfortably rely on natural ventilation.

---

## How BharatGrid Works

BharatGrid pulls hyper-local satellite weather data to automate grid scheduling:

1. **Extreme Heat & Sun (> 34°C):**
   * High heat index and intense solar radiation trigger a mandatory **100% full-current supply** to homes and villages. Fans, coolers, and refrigerators remain powered with zero load shedding.
2. **Cool & Breezy Weather (< 25°C):**
   * When ambient conditions are pleasant, the system schedules planned **energy-saving power cuts**. Citizens rely on natural airflow and open windows.
3. **Watts Saved Calculation:**
   * Quantifies the exact power conserved (Watts, kWh, and MWh) during cool periods.
4. **Inter-District Power Transfer:**
   * Simulates transferring conserved power from cool districts (e.g. hill stations or coastal areas) directly to heatwave-stressed plains and desert regions within the state grid.

---
## System Architecture

```text
Weather Data (Open-Meteo API)
          |
          v
Weather Data Processing
          |
          v
Climate-Aware Decision Engine
          |
          v
Power Scheduling Simulation
          |
          v
Energy Savings Calculation
          |
          v
Streamlit Dashboard
```
---

## Pan-India Coverage (All 36 States & UTs)

BharatGrid includes localized substations, feeder types, and DISCOM mappings across India:

### 28 States:
* **Andhra Pradesh** (APEPDCL / APSPDCL) — Visakhapatnam, Vijayawada, Guntur, Anantapur
* **Arunachal Pradesh** (Dept of Power, AP) — Itanagar, Tawang Monastery Feeder, Pasighat
* **Assam** (APDCL) — Kamrup (Guwahati), Dibrugarh (Chabua Tea Estate), Cachar (Silchar)
* **Bihar** (NBPDCL / SBPDCL) — Patna (Danapur), Gaya (Bodh Gaya), Muzaffarpur (Kanti)
* **Chhattisgarh** (CSPDCL) — Raipur, Bastar (Chitrakote Falls Feeder), Bilaspur
* **Goa** (Goa Electricity Dept) — North Goa (Arambol Coastal Village), South Goa (Margao)
* **Gujarat** (GUVNL - DGVCL, PGVCL) — Ahmedabad (Sanand), Kutch (Nakhatrana), Surat (Bardoli)
* **Haryana** (DHBVN / UHBVN) — Gurugram (Cyber City, Sohna), Hisar, Karnal
* **Himachal Pradesh** (HPSEBL) — Shimla (Theog Apple Orchards), Kullu (Manali), Lahaul & Spiti (Kaza)
* **Jharkhand** (JBVNL) — Ranchi (Kanke Plateau), Dhanbad (Jharia Coal Belt), East Singhbhum
* **Karnataka** (BESCOM / HESCOM) — Bengaluru (Whitefield, Electronic City), Mysuru, Mangaluru
* **Kerala** (KSEB) — Wayanad (Kalpetta Coffee Belt), Kochi (Paravur Coastal), Palakkad
* **Madhya Pradesh** (MPMKVVCL) — Bhopal, Indore (Sanwer Soybean Belt), Gwalior
* **Maharashtra** (MSEDCL - Mahavitaran) — Mumbai, Nagpur (Katol Orange Belt), Pune (Baramati)
* **Manipur** (MSPDCL) — Imphal West (Kangla Fort), Churachandpur (Lamka Hill Feeder)
* **Meghalaya** (MeECL) — Shillong Peak Feeder, Cherrapunji (Sohra Rain Feeder), Tura
* **Mizoram** (Power Dept) — Aizawl (Durtlang Ridge), Champhai (Zokhawthar Border Feeder)
* **Nagaland** (Dept of Power) — Kohima (Naga Heritage Kisama Feeder), Dimapur
* **Odisha** (TPCODL / TPWODL) — Bhubaneswar, Ganjam (Gopalpur-on-Sea), Sambalpur (Hirakud)
* **Punjab** (PSPCL) — Ludhiana (Khanna Grain Market), Amritsar (Ajnala Border), Bathinda
* **Rajasthan** (JVVNL / JdVVNL) — Jodhpur (Phalodi 50°C), Jaipur (Amer), Jaisalmer (Pokhran)
* **Sikkim** (Power Dept Sikkim) — Gangtok, Lachung Alpine Feeder (North Sikkim)
* **Tamil Nadu** (TANGEDCO) — Chennai (Guindy), Madurai (Melur), Nilgiris (Coonoor / Ooty)
* **Telangana** (TSSPDCL / TSNPDCL) — Hyderabad, Warangal, Nalgonda (Chityala), Karimnagar (Ramagundam)
* **Tripura** (TSECL) — Agartala, Gomati (Matabari Temple Feeder)
* **Uttar Pradesh** (UPPCL) — Lucknow (Malihabad Mango Belt), Varanasi (Sevapuri), Agra
* **Uttarakhand** (UPCL) — Dehradun (Mussoorie Ridge), Nainital, Chamoli (Joshimath Gateway)
* **West Bengal** (WBSEDCL) — Kolkata, Darjeeling (Kurseong Tea Hills), Purba Bardhaman

### 8 Union Territories:
* **Andaman and Nicobar Islands** — South Andaman (Port Blair), Havelock Island (Swaraj Dweep)
* **Chandigarh** — Sector 17 City Centre, Manimajra
* **Dadra and Nagar Haveli and Daman and Diu** — Daman, Silvassa
* **Delhi (NCT)** (BRPL / BYPL / TPDDL) — North Delhi (Alipur), South Delhi (Saket), West Delhi (Najafgarh)
* **Jammu and Kashmir** (JPDCL / KPDCL) — Srinagar (Dal Lake), Gulmarg Alpine Meadow, Jammu (R.S. Pura)
* **Ladakh** (Ladakh PDD) — Leh (Nubra Valley Dunes), Kargil (Drass Valley Feeder)
* **Lakshadweep** — Kavaratti Coral Atoll Feeder, Agatti Island
* **Puducherry** — Pondicherry (Auroville Global Village), Karaikal Port Feeder

---

## Running Locally

```bash
git clone https://github.com/Vedagayathri-Kanteti/bharatgrid-ai.git
cd bharatgrid-ai
pip install -r requirements.txt
streamlit run app.py
```

---

# Author
Vedagayathri Kanteti

---



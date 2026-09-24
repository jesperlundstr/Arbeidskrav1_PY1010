"""
PY1010 - Arbeidskrav 1

Jesper Lundström (jelun6183@usn.no)
08.09.2026
"""

# %% Data felles
L = 10000  # Kjørelengde/år [km]
F = 8.38  # Trafikkforsikringsavgift [kr/dag]

# %% Data elbil
Fe = 5000  # Forsikring [kr/år]
Se = 0.2  # Strømforbruk [kWh/km]
Pe = 2.00  # Strømpris [kr/kWh]
Be = 0.1  # Bomavgift [kr/km]

# %% Data bensinbil
Fb = 7500  # Forsikring [kr/år]
Pb = 1.0  # Drivstoffbruk [kr/km]
Bb = 0.3  # Bomavgift [kr/km]

# %% Beregninger
Ke = Fe + (F*365) + (Se*L*Pe) + (Be*L)  # Kostnad/år elbil [kr]

Kb = Fb + (F*365) + (L*Pb) + (Bb*L)  # Kostnad/år bensinbil [kr]

Kd = abs(Ke - Kb)  # Årlig kostnadsdifferanse [kr]

# %% Utskrift
print("Årlige kostnader for elbil er", Ke, "kr")
print("Årlige kostnader for bensinbil er", Kb, "kr")
print("Årlig kostnadsdifferanse er", Kd, "kr")
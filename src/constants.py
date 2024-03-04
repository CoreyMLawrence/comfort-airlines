from decimal import Decimal
from models.airport import Airport

# Simulation constants
MINUTES_PER_DAY = 1440
SIMULATION_DURATION_DAYS = 14
SIMULATION_DURATION = MINUTES_PER_DAY * SIMULATION_DURATION_DAYS

# Airport constants
DEFAULT_TAKEOFF_FEE = Decimal("2000")
DEFAULT_LANDING_FEE = Decimal("2000")
DEFAULT_GAS_PRICE = Decimal("6.19")

HUB_NAMES = {
    "O'Hare International Airport",
    "Denver International Airport"
    "Dallas/Fort Worth International Airport",
    "Hartsfield-Jackson Atlanta International Airport"
}

HUBS = {
    Airport(
        "Hartsfield-Jackson Atlanta International Airport", "ATL", "Atlanta", "Georgia", 33.63616168, -84.4293928, [], [], None,
        "Atlanta", 6144050, DEFAULT_GAS_PRICE, DEFAULT_TAKEOFF_FEE, DEFAULT_LANDING_FEE
    ),
    
    Airport(
        "Dallas/Fort Worth International Airport", "DFW", "Dallas;Fort Worth", "Texas", 32.89347974, -97.04431285, [], [], None,
        "Dallas-Fort Worth", 7637387, DEFAULT_GAS_PRICE, DEFAULT_TAKEOFF_FEE, DEFAULT_LANDING_FEE
    ),
    
    Airport(
        "Denver International Airport", "DEN", "Denver", "Colorado", 39.8559236, -104.676479, [], [], None,
        "Denver", 2963821, DEFAULT_GAS_PRICE, DEFAULT_TAKEOFF_FEE, DEFAULT_LANDING_FEE
    ),
    
    Airport(
        "O'Hare International Airport", "ORD", "Chicago", "Illinois", 41.9802264, -87.90899915, [], [], None,
        "Chicago", 9618502, DEFAULT_GAS_PRICE, DEFAULT_TAKEOFF_FEE, DEFAULT_LANDING_FEE
    )
}
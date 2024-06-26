from __future__ import annotations
from typing import Union, TYPE_CHECKING
from decimal import Decimal
from models.aircraft import AircraftStatus

if TYPE_CHECKING:
    from models.aircraft import Aircraft
    from models.route import Route
    
NGATES_HUB = 11
NMAINTENANCE_GATES_HUB = 3

class Airport:
    def __init__(self, name: str, iata_code: str, city: str, state: str, latitude: float, longitude: float, routes: list[Route], regional_airport: Union[Airport, None], metro_area: str, metro_population: int, gas_price: Decimal, takeoff_fee: Decimal, landing_fee: Decimal):
        if not type(name) is str or not name:
            raise ValueError("Airport name must be a non-empty string")
        
        if not type(name) is str or not iata_code:
            raise ValueError("Airport IATA code must be a non-empty string")
        
        if not type(city) is str or not city:
            raise ValueError("Airport city must be a non-empty string")
        
        if not type(state) is str or not state:
            raise ValueError("Airport state must be a non-empty string")
        
        if not type(latitude) is float or latitude < -90.0 or latitude > 90.0:
            raise ValueError("Airport latitude must be a float in the range [-90.0,90.0]")
        
        if not type(longitude) is float or longitude < -180.0 or longitude > 180.0:
            raise ValueError("Airport latitude must be a float in the range [-180.0,180.0]")

        if not type(gas_price) is Decimal or gas_price < Decimal("0.0"):
            raise ValueError("Airport gas price must be a Decimal in range [0.0, inf]")
        
        if not type(takeoff_fee) is Decimal:
            raise ValueError("Airport takeoff fee must be a Decimal")
        
        if not type(landing_fee) is Decimal:
            raise ValueError("Airport landing fee must be a Decimal")

        self.name = name
        self.iata_code = iata_code
        self.city = city
        self.state = state
        self.latitude = latitude
        self.longitude = longitude
        self.routes = routes
        self.regional_airport = regional_airport
        self.metro_area = metro_area
        self.metro_population = metro_population
        self.gates = 11 if self.is_hub else (min(metro_population // 1_000_000, 5))
        self.maintenance_gates = NMAINTENANCE_GATES_HUB if self.is_hub else 0
        self.gas_price = gas_price
        self.takeoff_fee = takeoff_fee
        self.landing_fee = landing_fee
        self.tarmac: list[Aircraft] = []
        self.maintenance_queue: list[Aircraft] = []
        
    @property
    def is_hub(self) -> bool:
        return self.regional_airport is None
    
    def assign_gate(self, aircraft: Aircraft) -> None:
        """Assigns the aircraft to a gate if there is a gate available, otherwise assigns it to the tarmac"""
        aircraft.location = self
        
        if aircraft.needs_maintenance:
            if self.maintenance_gates > 0:
                self.maintenance_gates -= 1
                aircraft.set_status(AircraftStatus.IN_MAINTENANCE)
            else:
                self.maintenance_queue.append(aircraft)
                aircraft.set_status(AircraftStatus.ON_TARMAC)
        else:
            if self.gates > 0:
                self.gates -= 1
                aircraft.set_status(AircraftStatus.DEBOARDING)
            else:
                self.tarmac.append(aircraft)
                aircraft.set_status(AircraftStatus.ON_TARMAC)
    
    def __repr__(self) -> str:
        return self.name
"""
Contrôleur principal pour la gestion des maisons, pièces et équipements.
"""
from models.database import (
    add_house, get_houses, delete_house, 
    add_room, get_rooms, delete_room,
    add_light, get_lights, update_light_state, delete_light,
    add_heating, get_heating, update_heating_temperature, delete_heating,
    get_all_dashboard_data
)

def create_house(nom_maison: str):
    if nom_maison and len(nom_maison.strip()) > 0:
        if len(fetch_houses()) >= 10:
            return None
        house_id = add_house(nom_maison.strip())
        return house_id
    return None

def fetch_houses():
    return get_houses()

def remove_house(house_id):
    delete_house(house_id)

def create_room(house_id, name, room_type):
    if name and len(name.strip()) > 0:
        if len(fetch_rooms(house_id)) >= 10:
            return None
        return add_room(house_id, name.strip(), room_type)
    return None

def fetch_rooms(house_id):
    return get_rooms(house_id)

def remove_room(room_id):
    delete_room(room_id)

def create_light(room_id):
    if len(fetch_lights(room_id)) >= 5:
        return None
    return add_light(room_id)

def fetch_lights(room_id):
    return get_lights(room_id)

def modify_light_state(light_id, is_on):
    update_light_state(light_id, is_on)

def remove_light(light_id):
    delete_light(light_id)

def create_heating(room_id):
    return add_heating(room_id)

def fetch_heating(room_id):
    return get_heating(room_id)

def modify_heating_temperature(heat_id, temperature):
    update_heating_temperature(heat_id, temperature)

def remove_heating(heat_id):
    delete_heating(heat_id)

def fetch_dashboard_data(house_id=None):
    return get_all_dashboard_data(house_id)
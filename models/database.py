"""
Module de gestion de la base de données SQLite pour DomoHouse.
Gère les maisons, pièces, éclairages et chauffages.
"""
import sqlite3
import os

# Chemin vers la base de données
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'domohouse.db')

def get_connection():
    """Crée et retourne une connexion à la base de données"""
    return sqlite3.connect(DB_PATH)

def init_db():
    """Initialise la base de données avec toutes les tables nécessaires"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS houses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            house_id INTEGER,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            FOREIGN KEY (house_id) REFERENCES houses (id) ON DELETE CASCADE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_id INTEGER,
            is_on BOOLEAN DEFAULT 0,
            FOREIGN KEY (room_id) REFERENCES rooms (id) ON DELETE CASCADE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS heating (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_id INTEGER,
            temperature INTEGER DEFAULT 18,
            FOREIGN KEY (room_id) REFERENCES rooms (id) ON DELETE CASCADE
        )
    ''')
    conn.commit()
    conn.close()

# ============== HOUSES ==============

def add_house(name):
    """Ajoute une nouvelle maison"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO houses (name) VALUES (?)', (name,))
    conn.commit()
    house_id = cursor.lastrowid
    conn.close()
    return house_id

def get_houses():
    """Récupère toutes les maisons"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM houses')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_house(house_id):
    """Supprime une maison et toutes ses dépendances"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM houses WHERE id = ?', (house_id,))
    conn.commit()
    conn.close()

# ============== ROOMS ==============

def add_room(house_id, name, room_type):
    """Ajoute une nouvelle pièce à une maison"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO rooms (house_id, name, type) VALUES (?, ?, ?)', (house_id, name, room_type))
    conn.commit()
    room_id = cursor.lastrowid
    conn.close()
    return room_id

def get_rooms(house_id):
    """Récupère toutes les pièces d'une maison"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, type FROM rooms WHERE house_id = ?', (house_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_room(room_id):
    """Supprime une pièce et tous ses équipements"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM rooms WHERE id = ?', (room_id,))
    conn.commit()
    conn.close()

# ============== LIGHTS ==============

def add_light(room_id):
    """Ajoute une nouvelle lampe à une pièce"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO lights (room_id) VALUES (?)', (room_id,))
    conn.commit()
    light_id = cursor.lastrowid
    conn.close()
    return light_id

def get_lights(room_id):
    """Récupère toutes les lampes d'une pièce"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, is_on FROM lights WHERE room_id = ?', (room_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_light_state(light_id, is_on):
    """Met à jour l'état d'une lampe"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE lights SET is_on = ? WHERE id = ?', (1 if is_on else 0, light_id))
    conn.commit()
    conn.close()

def delete_light(light_id):
    """Supprime une lampe"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM lights WHERE id = ?', (light_id,))
    conn.commit()
    conn.close()

# ============== HEATING ==============

def add_heating(room_id):
    """Ajoute un chauffage à une pièce (un seul par pièce)"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM heating WHERE room_id = ?', (room_id,))
    if cursor.fetchone():
        conn.close()
        return None
    cursor.execute('INSERT INTO heating (room_id) VALUES (?)', (room_id,))
    conn.commit()
    heat_id = cursor.lastrowid
    conn.close()
    return heat_id

def get_heating(room_id):
    """Récupère le chauffage d'une pièce"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, temperature FROM heating WHERE room_id = ?', (room_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def update_heating_temperature(heat_id, temperature):
    """Met à jour la température d'un chauffage"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE heating SET temperature = ? WHERE id = ?', (temperature, heat_id))
    conn.commit()
    conn.close()

def delete_heating(heat_id):
    """Supprime un chauffage"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM heating WHERE id = ?', (heat_id,))
    conn.commit()
    conn.close()

# ============== DASHBOARD ==============

def get_all_dashboard_data(house_id=None):
    """Récupère toutes les données pour le tableau de bord"""
    conn = get_connection()
    cursor = conn.cursor()
    query = '''
        SELECT h.name as house_name, r.id as room_id, r.name as room_name, r.type as room_type,
               (SELECT COUNT(*) FROM lights l WHERE l.room_id = r.id AND l.is_on = 1) as lights_on,
               (SELECT COUNT(*) FROM lights l WHERE l.room_id = r.id AND l.is_on = 0) as lights_off,
               (SELECT temperature FROM heating ht WHERE ht.room_id = r.id) as temp
        FROM houses h
        JOIN rooms r ON r.house_id = h.id
    '''

    if house_id:
        query += ' WHERE h.id = ?'
        cursor.execute(query, (house_id,))
    else:
        cursor.execute(query)

    rows = cursor.fetchall()
    conn.close()
    return rows

# Initialisation au chargement du module
init_db()

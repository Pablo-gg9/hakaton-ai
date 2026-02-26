import random
import json

with open("pokemon_data.json", "r") as f:
    POKEMON_DATA = {p["name"].lower(): p for p in json.load(f)}

with open("pokemon_moves.json", "r") as f:
    POKEMON_MOVES = json.load(f)

with open("moves_data.json", "r") as f:
    MOVES_DATA = json.load(f)

TYPE_CHART = {
    ("normal", "rock"): 0.5,
    ("normal", "steel"): 0.5,
    ("normal", "ghost"): 0,
    ("fire", "fire"): 0.5,
    ("fire", "water"): 0.5,
    ("fire", "grass"): 2,
    ("fire", "ice"): 2,
    ("fire", "bug"): 2,
    ("fire", "rock"): 0.5,
    ("fire", "dragon"): 0.5,
    ("fire", "steel"): 2,
    ("water", "fire"): 2,
    ("water", "water"): 0.5,
    ("water", "grass"): 0.5,
    ("water", "ground"): 2,
    ("water", "rock"): 2,
    ("water", "dragon"): 0.5,
    ("electric", "water"): 2,
    ("electric", "electric"): 0.5,
    ("electric", "grass"): 0.5,
    ("electric", "ground"): 0,
    ("electric", "flying"): 2,
    ("electric", "dragon"): 0.5,
    ("grass", "fire"): 0.5,
    ("grass", "water"): 2,
    ("grass", "grass"): 0.5,
    ("grass", "poison"): 0.5,
    ("grass", "ground"): 2,
    ("grass", "flying"): 0.5,
    ("grass", "bug"): 0.5,
    ("grass", "rock"): 2,
    ("grass", "dragon"): 0.5,
    ("grass", "steel"): 0.5,
    ("ice", "fire"): 0.5,
    ("ice", "water"): 0.5,
    ("ice", "grass"): 2,
    ("ice", "ice"): 0.5,
    ("ice", "ground"): 2,
    ("ice", "flying"): 2,
    ("ice", "bug"): 2,
    ("ice", "dragon"): 2,
    ("ice", "steel"): 0.5,
    ("fighting", "normal"): 2,
    ("fighting", "ice"): 2,
    ("fighting", "poison"): 0.5,
    ("fighting", "flying"): 0.5,
    ("fighting", "psychic"): 0.5,
    ("fighting", "bug"): 0.5,
    ("fighting", "rock"): 2,
    ("fighting", "ghost"): 0,
    ("fighting", "dark"): 2,
    ("fighting", "steel"): 2,
    ("fighting", "fairy"): 0.5,
    ("poison", "grass"): 2,
    ("poison", "poison"): 0.5,
    ("poison", "ground"): 0.5,
    ("poison", "rock"): 0.5,
    ("poison", "ghost"): 0.5,
    ("poison", "steel"): 0,
    ("poison", "fairy"): 2,
    ("ground", "fire"): 2,
    ("ground", "electric"): 2,
    ("ground", "grass"): 0.5,
    ("ground", "poison"): 2,
    ("ground", "flying"): 0,
    ("ground", "bug"): 0.5,
    ("ground", "rock"): 2,
    ("ground", "steel"): 2,
    ("flying", "electric"): 0.5,
    ("flying", "grass"): 2,
    ("flying", "fighting"): 2,
    ("flying", "bug"): 2,
    ("flying", "rock"): 0.5,
    ("flying", "steel"): 0.5,
    ("psychic", "fighting"): 2,
    ("psychic", "poison"): 2,
    ("psychic", "psychic"): 0.5,
    ("psychic", "dark"): 0,
    ("psychic", "steel"): 0.5,
    ("bug", "fire"): 0.5,
    ("bug", "grass"): 2,
    ("bug", "fighting"): 0.5,
    ("bug", "poison"): 0.5,
    ("bug", "flying"): 0.5,
    ("bug", "psychic"): 2,
    ("bug", "ghost"): 0.5,
    ("bug", "dark"): 2,
    ("bug", "steel"): 0.5,
    ("bug", "fairy"): 0.5,
    ("rock", "fire"): 2,
    ("rock", "ice"): 2,
    ("rock", "fighting"): 0.5,
    ("rock", "ground"): 0.5,
    ("rock", "flying"): 2,
    ("bug", "steel"): 0.5,
    ("ghost", "normal"): 0,
    ("ghost", "psychic"): 2,
    ("ghost", "ghost"): 2,
    ("ghost", "dark"): 0.5,
    ("dragon", "dragon"): 2,
    ("dragon", "steel"): 0.5,
    ("dragon", "fairy"): 0,
    ("steel", "fire"): 0.5,
    ("steel", "water"): 0.5,
    ("steel", "electric"): 0.5,
    ("steel", "ice"): 2,
    ("steel", "rock"): 2,
    ("steel", "steel"): 0.5,
    ("steel", "fairy"): 2,
    ("fairy", "fire"): 0.5,
    ("fairy", "fighting"): 2,
    ("fairy", "poison"): 0.5,
    ("fairy", "dragon"): 2,
    ("fairy", "dark"): 2,
    ("fairy", "steel"): 0.5,
}


def get_type_effectiveness(attack_type, defender_types):
    effectiveness = 1.0
    for def_type in defender_types:
        key = (attack_type, def_type.lower())
        if key in TYPE_CHART:
            effectiveness *= TYPE_CHART[key]
    return effectiveness


class Pokemon:
    def __init__(self, name, level=5):
        self.name = name.lower()
        self.level = level
        self.data = POKEMON_DATA.get(self.name)
        self.moves_names = POKEMON_MOVES.get(self.name, [])
        self.moves = []
        self.hp = 0
        self.max_hp = 0
        self.current_pp = {}

        if self.data:
            self._init_stats()
            self._init_moves()

    def _init_stats(self):
        base = self.data["stats"]["hp"]
        self.max_hp = int((base * 2 + 31) * self.level / 100) + self.level + 10
        self.hp = self.max_hp

        self.attack = (
            int((self.data["stats"]["attack"] * 2 + 31) * self.level / 100) + 5
        )
        self.defense = (
            int((self.data["stats"]["defense"] * 2 + 31) * self.level / 100) + 5
        )
        self.sp_attack = (
            int((self.data["stats"]["special_attack"] * 2 + 31) * self.level / 100) + 5
        )
        self.sp_defense = (
            int((self.data["stats"]["special_defense"] * 2 + 31) * self.level / 100) + 5
        )
        self.speed = int((self.data["stats"]["speed"] * 2 + 31) * self.level / 100) + 5

        self.types = [t.lower() for t in self.data["types"]]

    def _init_moves(self):
        for move_name in self.moves_names[:4]:
            move_data = MOVES_DATA.get(move_name)
            if move_data:
                self.moves.append(move_data)
                self.current_pp[move_name] = move_data["pp"]

    def get_move_by_name(self, name):
        for m in self.moves:
            if m["name"] == name:
                return m
        return None

    def use_pp(self, move_name):
        if move_name in self.current_pp and self.current_pp[move_name] > 0:
            self.current_pp[move_name] -= 1
            return True
        return False

    def is_fainted(self):
        return self.hp <= 0

    def display(self):
        return f"{self.data['name']} (Nv.{self.level}) HP:{self.hp}/{self.max_hp}"

    def show_moves(self):
        print(f"\n  Movimientos de {self.data['name']}:")
        for i, m in enumerate(self.moves, 1):
            pp = self.current_pp.get(m["name"], 0)
            power = m["power"] if m["power"] > 0 else "-"
            print(
                f"  {i}. {m['name'].replace('-', ' ').title()} | Poder: {power} | Tipo: {m['type']} | PP: {pp}/{m['pp']}"
            )


class Battle:
    def __init__(self, player_pokemon, enemy_pokemon):
        self.player = player_pokemon
        self.enemy = enemy_pokemon
        self.turn = 1
        self.log = []

    def calculate_damage(self, move, attacker, defender):
        if move["damage_class"] == "status":
            return 0, 1.0

        if random.randint(1, 100) > move["accuracy"]:
            return 0, 0.0

        power = move["power"]
        if move["damage_class"] == "physical":
            attack_stat = attacker.attack
            defense_stat = defender.defense
        else:
            attack_stat = attacker.sp_attack
            defense_stat = defender.sp_defense

        damage = (
            2 * attacker.level / 5 + 2
        ) * power * attack_stat / defense_stat / 50 + 2

        effectiveness = get_type_effectiveness(move["type"], defender.types)

        critical = 1
        if random.randint(1, 16) == 1:
            critical = 2

        stab = 1.5 if move["type"] in attacker.types else 1.0

        final_damage = int(
            damage * effectiveness * critical * stab * (random.randint(85, 100) / 100)
        )

        return final_damage, effectiveness

    def attack(self, attacker, defender, move):
        name = attacker.data["name"]
        move_name = move["name"].replace("-", " ").title()

        if not attacker.use_pp(move["name"]):
            self.log.append(f"  {name} no tiene PP para {move_name}!")
            return False

        if move["damage_class"] == "status":
            self.log.append(f"  {name} usó {move_name}!")
            return False

        damage, effectiveness = self.calculate_damage(move, attacker, defender)

        if effectiveness == 0.0:
            self.log.append(f"  {name} usó {move_name}! ¡No afecta al enemigo!")
        elif effectiveness > 1.0:
            self.log.append(f"  {name} usó {move_name}! ¡Es muy efectivo!")
        elif effectiveness < 1.0:
            self.log.append(f"  {name} usó {move_name}! No es muy efectivo...")
        else:
            self.log.append(f"  {name} usó {move_name}!")

        if damage > 0:
            defender.hp = max(0, defender.hp - damage)
            self.log.append(f"    ¡Infligió {damage} de daño!")

        return True

    def show_status(self):
        print("\n" + "=" * 50)
        print(f"  🆚 COMBATE: {self.player.data['name']} vs {self.enemy.data['name']}")
        print("=" * 50)

        player_hp_bar = "█" * int(20 * self.player.hp / self.player.max_hp)
        player_empty = "░" * (20 - len(player_hp_bar))
        enemy_hp_bar = "█" * int(20 * self.enemy.hp / self.enemy.max_hp)
        enemy_empty = "░" * (20 - len(enemy_hp_bar))

        print(f"\n  {self.enemy.data['name']} (Nv.{self.enemy.level})")
        print(
            f"  HP: [{enemy_hp_bar}{enemy_empty}] {self.enemy.hp}/{self.enemy.max_hp}"
        )

        print(f"\n  vs\n")

        print(f"  {self.player.data['name']} (Nv.{self.player.level})")
        print(
            f"  HP: [{player_hp_bar}{player_empty}] {self.player.hp}/{self.player.max_hp}"
        )
        print()

    def print_log(self):
        for entry in self.log:
            print(entry)
        self.log = []

    def player_turn(self, move_index):
        if move_index < 0 or move_index >= len(self.player.moves):
            self.log.append("  ¡Movimiento inválido!")
            return False

        move = self.player.moves[move_index]

        if self.player.speed >= self.enemy.speed:
            self.attack(self.player, self.enemy, move)
            self.print_log()
            if self.enemy.is_fainted():
                return True

            enemy_move = random.choice(self.enemy.moves)
            self.attack(self.enemy, self.player, enemy_move)
            self.print_log()
        else:
            enemy_move = random.choice(self.enemy.moves)
            self.attack(self.enemy, self.player, enemy_move)
            self.print_log()
            if self.player.is_fainted():
                return True

            self.attack(self.player, self.enemy, move)
            self.print_log()

        self.turn += 1
        return self.enemy.is_fainted()

    def run(self):
        print("\n" + "🎮" * 15)
        print("  ¡COMBATE POKÉMON COMIENZA!")
        print("🎮" * 15)

        self.show_status()

        while not self.player.is_fainted() and not self.enemy.is_fainted():
            print(f"\n--- Turno {self.turn} ---")
            self.player.show_moves()

            try:
                choice = int(input("\n👉 Elige movimiento (1-4): ")) - 1
            except ValueError:
                choice = 0

            winner = self.player_turn(choice)

            if winner is True:
                break

            self.show_status()

        print("\n" + "=" * 50)
        if self.enemy.is_fainted():
            print(f"  ¡{self.player.data['name']} gana el combate!")
            print(f"  🏆 ¡Victoria!")
        else:
            print(f"  ¡{self.player.data['name']} ha sido derrotado!")
            print(f"  💀 ¡Derrota!")
        print("=" * 50)

        return self.player.is_fainted() == False


CATEGORIES = {
    "azul": {"name": "Geografía de Videojuegos", "color": "Azul", "symbol": "🟦"},
    "marron": {"name": "Arte y Literatura", "color": "Marrón", "symbol": "🟫"},
    "amarillo": {
        "name": "Historia de Videojuegos",
        "color": "Amarillo",
        "symbol": "🟨",
    },
    "rosa": {"name": "Espectáculos", "color": "Rosa", "symbol": "🟪"},
    "verde": {"name": "Ciencia y Naturaleza", "color": "Verde", "symbol": "🟩"},
    "naranja": {"name": "Deportes y Pasatiempos", "color": "Naranja", "symbol": "🟧"},
}

QUESTIONS = {
    "azul": [
        {
            "question": "¿En qué país se desarrolla la saga 'The Legend of Zelda'?",
            "options": ["Japón", "Estados Unidos", "Corea del Sur", "China"],
            "answer": 0,
        },
        {
            "question": "¿Cuál es la ciudad principal del juego 'GTA V'?",
            "options": ["Liberty City", "Vice City", "Los Santos", "San Fierro"],
            "answer": 2,
        },
        {
            "question": "¿De qué país es la desarrolladora CD Projekt Red?",
            "options": ["Alemania", "Polonia", "Rusia", "Suecia"],
            "answer": 1,
        },
        {
            "question": "¿En qué continente está situado el reino de Hyrule?",
            "options": ["Europa", "Asia", "América", "Oceanía"],
            "answer": 1,
        },
        {
            "question": "¿Cuál es la capital de la región de Kanto en Pokémon?",
            "options": [
                "Pueblo Paleta",
                "Ciudad Celeste",
                "Ciudad Azafrán",
                "Verde Caída",
            ],
            "answer": 2,
        },
        {
            "question": "¿Dónde está basada la desarrolladora FromSoftware?",
            "options": ["Tokio", "Osaka", "Kioto", "Yokohama"],
            "answer": 0,
        },
        {
            "question": "¿Cuál es la ciudad ficticia de 'Cyberpunk 2077'?",
            "options": ["Night City", "Los Angeles", "Neo Tokyo", "Metropolis"],
            "answer": 0,
        },
        {
            "question": "¿En qué país se ubica el pueblo de 'Stardew Valley'?",
            "options": ["Estados Unidos", "Canadá", "Reino Unido", "Australia"],
            "answer": 0,
        },
    ],
    "marron": [
        {
            "question": "¿Quién es el creador de Mario?",
            "options": [
                "Satoru Iwata",
                "Shigeru Miyamoto",
                "Yuji Naka",
                "Hideo Kojima",
            ],
            "answer": 1,
        },
        {
            "question": "¿Qué artista compuso la banda sonora de 'The Last of Us'?",
            "options": [
                "Nobuo Uematsu",
                "Gustavo Santaolalla",
                "Koji Kondo",
                "Jesper Kyd",
            ],
            "answer": 1,
        },
        {
            "question": "¿Cuál fue el primer juego de la saga 'Final Fantasy'?",
            "options": [
                "Final Fantasy II",
                "Final Fantasy I",
                "Final Fantasy III",
                "Final Fantasy VI",
            ],
            "answer": 1,
        },
        {
            "question": "¿Qué estudio creó 'Journey'?",
            "options": [
                "FromSoftware",
                "Thatgamecompany",
                "Team Cherry",
                "Supergiant Games",
            ],
            "answer": 1,
        },
        {
            "question": "¿Quién pintó la portada original de 'Doom'?",
            "options": ["John Romero", "id Software", "Boris Vallejo", "Craig Mullins"],
            "answer": 2,
        },
        {
            "question": "¿Quién dirija el estudio 'Hideo Kojima Productions'?",
            "options": ["Hideo Kojima", "Yu Suzuki", "Suda51", "Shinji Mikami"],
            "answer": 0,
        },
        {
            "question": "¿Qué artista hizo la música de 'Nier'?",
            "options": [
                "Nobuo Uematsu",
                "Yoko Shimomura",
                "Manami Matsumae",
                "Koji Kondo",
            ],
            "answer": 1,
        },
        {
            "question": "¿Qué estudio desarrolló 'Hollow Knight'?",
            "options": ["Team Cherry", "Playdead", "Supergiant Games", "Mojang"],
            "answer": 0,
        },
    ],
    "amarillo": [
        {
            "question": "¿En qué año se lanzó el primer 'Super Mario Bros'?",
            "options": ["1983", "1985", "1987", "1981"],
            "answer": 1,
        },
        {
            "question": "¿Cuál fue el primer juego de PlayStation?",
            "options": ["Ridge Racer", "Wipeout", "Rayman", "Bugger"],
            "answer": 3,
        },
        {
            "question": "¿Cuántos años duró el desarrollo de 'Duke Nukem Forever'?",
            "options": ["5 años", "10 años", "15 años", "20 años"],
            "answer": 2,
        },
        {
            "question": "¿En qué año nació la franquicia 'Sonic the Hedgehog'?",
            "options": ["1989", "1991", "1993", "1995"],
            "answer": 1,
        },
        {
            "question": "¿Cuál fue el primer juego de 'The Legend of Zelda'?",
            "options": [
                "Zelda II",
                "Zelda I: The Hyrule Fantasy",
                "Ocarina of Time",
                "A Link to the Past",
            ],
            "answer": 1,
        },
        {
            "question": "¿En qué año salió 'Minecraft' oficialmente?",
            "options": ["2009", "2010", "2011", "2012"],
            "answer": 2,
        },
        {
            "question": "¿Cuándo se lanzó 'The Elder Scrolls V: Skyrim'?",
            "options": ["2010", "2011", "2012", "2013"],
            "answer": 1,
        },
        {
            "question": "¿Año de lanzamiento de 'Half-Life 2'?",
            "options": ["2002", "2003", "2004", "2005"],
            "answer": 2,
        },
    ],
    "rosa": [
        {
            "question": "¿Qué actor voicing a Nathan Drake en 'Uncharted'?",
            "options": ["Chris Pratt", "Nolan North", "Mark Wahlberg", "Tom Holland"],
            "answer": 1,
        },
        {
            "question": "¿Cuál es el juego más vendido de todos los tiempos?",
            "options": ["GTA V", "Minecraft", "Tetris", "Wii Sports"],
            "answer": 1,
        },
        {
            "question": "¿Qué juego popularizó el término 'JRPG'?",
            "options": [
                "Dragon Quest",
                "Final Fantasy",
                "Phantasy Star",
                "Chrono Trigger",
            ],
            "answer": 1,
        },
        {
            "question": "¿Qué saga de videojuegos se adaptó primero al cine?",
            "options": ["Mario", "Sonic", "Resident Evil", "Mortal Kombat"],
            "answer": 2,
        },
        {
            "question": "¿Qué personaje de Nintendo aparece en 'Super Smash Bros' original?",
            "options": ["Samus", "Captain Falcon", "Pikachu", "Kirby"],
            "answer": 0,
        },
        {
            "question": "¿Qué actor interpreta a Joel en la serie de 'The Last of Us'?",
            "options": [
                "Pedro Pascal",
                "Neil Patrick Harris",
                "Bryan Cranston",
                "Matthew McConaughey",
            ],
            "answer": 0,
        },
        {
            "question": "¿Cuál fue el primer juego de 'The Sims'?",
            "options": ["The Sims 2", "The Sims", "The Sims 3", "SimCity"],
            "answer": 1,
        },
        {
            "question": "¿Qué streamer popularizó 'Among Us'?",
            "options": ["Ninja", "Shroud", "xQc", "Tfue"],
            "answer": 2,
        },
    ],
    "verde": [
        {
            "question": "¿Cuántos bits tenía la Nintendo 64?",
            "options": ["32 bits", "64 bits", "128 bits", "16 bits"],
            "answer": 1,
        },
        {
            "question": "¿Qué lenguaje de programación se usó originalmente para crear 'Minecraft'?",
            "options": ["C++", "Python", "Java", "JavaScript"],
            "answer": 2,
        },
        {
            "question": "¿Qué tecnología de renderizado usa 'The Witcher 3'?",
            "options": ["CryEngine", "Unreal Engine", "REDengine", "Frostbite"],
            "answer": 2,
        },
        {
            "question": "¿Cuántos GB tiene un Blu-ray estándar?",
            "options": ["25 GB", "50 GB", "100 GB", "12 GB"],
            "answer": 1,
        },
        {
            "question": "¿Qué empresa creó el motor gráfico 'Unity'?",
            "options": ["Epic Games", "Unity Technologies", "Valve", "Crytek"],
            "answer": 1,
        },
        {
            "question": "¿Cuántos núcleos tiene un PS5?",
            "options": ["6", "8", "10", "12"],
            "answer": 1,
        },
        {
            "question": "¿Qué tipo de SSD usa PS5?",
            "options": ["SATA", "NVMe", "HDD", "Flash"],
            "answer": 1,
        },
        {
            "question": "¿Cuánta RAM tiene Xbox Series X?",
            "options": ["8 GB", "12 GB", "16 GB", "24 GB"],
            "answer": 2,
        },
    ],
    "naranja": [
        {
            "question": "¿Cuántos jugadores pueden jugar en 'Super Smash Bros. Ultimate'?",
            "options": ["4", "6", "8", "2"],
            "answer": 2,
        },
        {
            "question": "¿Qué deporte simula la saga 'FIFA'?",
            "options": ["Baloncesto", "Fútbol", "Béisbol", "Tenis"],
            "answer": 1,
        },
        {
            "question": "¿Cuál es el juego de mesa más antiguo adaptado a videojuegos?",
            "options": ["Ajedrez", "Dominó", "Backgammon", "Parchís"],
            "answer": 2,
        },
        {
            "question": "¿Cuántas bolas de dragón hay en 'Dragon Ball Z: Kakarot'?",
            "options": ["7", "9", "6", "5"],
            "answer": 0,
        },
        {
            "question": "¿Qué juego de golf aparece en 'Mario Golf: Super Rush'?",
            "options": ["Wii Sports", "Everybody's Golf", "Mario Golf", "Hot Shots"],
            "answer": 2,
        },
        {
            "question": "¿Cuántos golfers hay en 'Mario Golf'?",
            "options": ["8", "10", "12", "16"],
            "answer": 2,
        },
        {
            "question": "¿Qué juego de carreras tiene el 'Ring Rally'?",
            "options": [
                "Mario Kart",
                "Diddy Kong Racing",
                "Crash Team Racing",
                "Sonic Racing",
            ],
            "answer": 1,
        },
        {
            "question": "¿Cuántas bolas hay en bowling estándar?",
            "options": ["8", "9", "10", "12"],
            "answer": 2,
        },
    ],
}

GYM_LEADERS = {
    "azul": {"name": "Misty", "pokemon": "Starmie", "game": "Pokemon Amarillo"},
    "marron": {"name": "Brock", "pokemon": "Onix", "game": "Pokemon Rojo/Azul"},
    "amarillo": {"name": "Lt. Surge", "pokemon": "Raichu", "game": "Pokemon Rojo/Azul"},
    "rosa": {"name": "Erika", "pokemon": "Vileplume", "game": "Pokemon Rojo/Azul"},
    "verde": {"name": "Koga", "pokemon": "Muk", "game": "Pokemon Rojo/Azul"},
    "naranja": {"name": "Giovanni", "pokemon": "Rhydon", "game": "Pokemon Rojo/Azul"},
}

CATEGORY_POSITIONS = {
    0: "azul",
    3: "marron",
    6: "amarillo",
    9: "rosa",
    12: "verde",
    15: "naranja",
    19: "azul",
    22: "marron",
    25: "amarillo",
    28: "rosa",
    31: "verde",
    34: "naranja",
    38: "azul",
    41: "marron",
    44: "amarillo",
    47: "rosa",
    50: "verde",
    53: "naranja",
    57: "azul",
    60: "marron",
}

WILD_POKEMON = [
    "pikachu",
    "charmander",
    "squirtle",
    "bulbasaur",
    "meowth",
    "psyduck",
    "mankey",
    "poliwag",
    "bellsprout",
    "drowzee",
    "magikarp",
    "eevee",
    "snorlax",
    "raticate",
    "fearow",
    "arbok",
    "pidgeotto",
    "golbat",
    "venonat",
    "venomoth",
]

BOX_POKEMON = [
    "rattata",
    "spearow",
    "ekans",
    "pidgey",
    "sandshrew",
    "nidoran-f",
    "nidoran-m",
    "clefairy",
    "vulpix",
    "jigglypuff",
    "zubat",
    "oddish",
    "paras",
    "diglett",
    "meowth",
]

GYM_LEADER_POKEMON = {
    "azul": "starmie",
    "marron": "onix",
    "amarillo": "raichu",
    "rosa": "vileplume",
    "verde": "muk",
    "naranja": "rhydon",
}

MAX_POKEMON = 6
TOTAL_SPACES = 63


class TrivialVideojuegos:
    def __init__(self, player_name):
        self.player_name = player_name
        self.position = 0
        self.quesitos = set()
        self.pokedex = []
        self.pc_storage = []
        self.used_pokemon = []
        self.used_questions = {cat: [] for cat in QUESTIONS.keys()}
        self.total_questions = 0
        self.correct_answers = 0
        self.turns_played = 0

    def print_header(self, title):
        print("\n" + "=" * 50)
        print(f"  {title}")
        print("=" * 50)

    def print_status(self):
        print(f"\n🎮 Jugador: {self.player_name}")
        print(f"📍 Posición: {self.position}/63")
        print(f"🧀 Quesitos: {len(self.quesitos)}/6")
        print(
            f"🐾 Equipo: {len(self.pokedex)}/{MAX_POKEMON} | PC: {len(self.pc_storage)}"
        )

    def show_board(self):
        print("\n" + "=" * 60)
        print("                    TABLERO TRIVIAL PURSUIT")
        print("=" * 60)

        category_symbols = {k: v["symbol"] for k, v in CATEGORIES.items()}
        center = "    🏆    "

        print(
            f"\n      {category_symbols['azul']}  {category_symbols['marron']}  {category_symbols['amarillo']}  {category_symbols['rosa']}  {category_symbols['verde']}  {category_symbols['naranja']}"
        )
        print(f"        0    3    6    9   12   15")
        print(f"     ┌────┬────┬────┬────┬────┬────┐")

        for row in range(5):
            spaces = []
            for col in range(6):
                if row == 2 and col == 2:
                    spaces.append(center)
                elif row == 2 and col == 3:
                    pos_marker = (
                        f" {self.player_name[0]} "
                        if self.position == 0 or row == 0
                        else "    "
                    )
                    spaces.append(f" P{pos_marker}")
                else:
                    spaces.append("    ")
            print(f"     │{'│'.join(spaces)}│")
            if row < 4:
                print(f"     ├────┼────┼────┼────┼────┼────┤")

        print(f"     └────┴────┴────┴────┴────┴────┘")
        print(f"        57   60  (centro)   19   22")
        print("=" * 60)

    def show_pokedex(self):
        self.print_header("📱 TU EQUIPO")
        if not self.pokedex:
            print("\nNo tienes ningún Pokémon en tu equipo.")
        else:
            for i, p in enumerate(self.pokedex, 1):
                if isinstance(p, Pokemon):
                    types = "/".join(p.data["types"])
                    print(
                        f"  {i}. {p.data['name']} (Nv.{p.level}) HP:{p.hp}/{p.max_hp} ({types})"
                    )
                else:
                    print(f"  {i}. {p['name']} ({p['type']})")
        print()

    def show_pc(self):
        self.print_header("💻 PC DE POKÉMON - ALMACÉN")
        if not self.pc_storage:
            print("\nEl PC está vacío.")
        else:
            print(f"\nTienes {len(self.pc_storage)} Pokémon en el PC:")
            for i, p in enumerate(self.pc_storage, 1):
                if isinstance(p, Pokemon):
                    types = "/".join(p.data["types"])
                    print(
                        f"  {i}. {p.data['name']} (Nv.{p.level}) HP:{p.hp}/{p.max_hp} ({types})"
                    )
                else:
                    print(f"  {i}. {p['name']} ({p['type']})")

        if len(self.pokedex) < MAX_POKEMON and self.pc_storage:
            print("\n📤 Opciones:")
            print("  1. Sacar Pokémon del PC a tu equipo")
            print("  2. Volver")
            try:
                choice = int(input("\n👉 Opción: "))
                if choice == 1:
                    self.withdraw_from_pc()
            except ValueError:
                pass
        print()

    def deposit_to_pc(self):
        if not self.pokedex:
            print("No tienes Pokémon en tu equipo para depositar.")
            return

        self.show_pokedex()
        try:
            idx = int(input("👉 Número del Pokémon a depositar: ")) - 1
            if 0 <= idx < len(self.pokedex):
                pokemon = self.pokedex.pop(idx)
                name = (
                    pokemon.data["name"]
                    if isinstance(pokemon, Pokemon)
                    else pokemon["name"]
                )
                self.pc_storage.append(pokemon)
                print(f"📦 {name} ha sido depositado en el PC.")
        except ValueError:
            print("Opción inválida.")

    def withdraw_from_pc(self):
        if not self.pc_storage:
            print("El PC está vacío.")
            return

        if len(self.pokedex) >= MAX_POKEMON:
            print("Tu equipo está lleno. Deposita un Pokémon primero.")
            return

        self.show_pc()
        try:
            idx = int(input("👉 Número del Pokémon a sacar: ")) - 1
            if 0 <= idx < len(self.pc_storage):
                pokemon = self.pc_storage.pop(idx)
                self.pokedex.append(pokemon)
                name = (
                    pokemon.data["name"]
                    if isinstance(pokemon, Pokemon)
                    else pokemon["name"]
                )
                print(f"📤 {name} ha sido añadido a tu equipo.")
        except ValueError:
            print("Opción inválida.")

    def manage_pokemon_menu(self):
        while True:
            self.print_header("👤 GESTIÓN DE POKÉMON")
            print(
                f"  Equipo: {len(self.pokedex)}/{MAX_POKEMON} | PC: {len(self.pc_storage)}"
            )
            print("\n  1. Ver equipo")
            print("  2. Ver PC")
            print("  3. Depositar al PC")
            print("  4. Sacar del PC")
            print("  5. Volver al juego")

            try:
                choice = int(input("\n👉 Opción: "))
                if choice == 1:
                    self.show_pokedex()
                elif choice == 2:
                    self.show_pc()
                elif choice == 3:
                    self.deposit_to_pc()
                elif choice == 4:
                    self.withdraw_from_pc()
                elif choice == 5:
                    break
            except ValueError:
                print("Opción inválida.")

    def get_random_question(self, category):
        available = [
            q for q in QUESTIONS[category] if q not in self.used_questions[category]
        ]
        if not available:
            self.used_questions[category] = []
            available = QUESTIONS[category]
        question = random.choice(available)
        self.used_questions[category].append(question)
        return question

    def get_pokemon_info(self, name):
        data = POKEMON_DATA.get(name.lower())
        if data:
            types = "/".join(data["types"])
            return {"name": data["name"], "type": types}
        return {"name": name.title(), "type": "Unknown"}

    def battle_gym_leader(self, category):
        leader = GYM_LEADERS[category]
        pokemon_name = GYM_LEADER_POKEMON[category]
        pokemon_info = self.get_pokemon_info(pokemon_name)
        self.print_header(f"LÍDER DE GIMNASIO: {leader['name']}")
        print(f"🎯 Te desafía con su {pokemon_info['name']} ({pokemon_info['type']})!")
        print(f"📺 Juego: {leader['game']}")
        question = self.get_random_question(category)
        return question, leader, pokemon_name

    def get_wild_pokemon(self):
        all_pokemon = WILD_POKEMON + BOX_POKEMON
        available = [p for p in all_pokemon if p not in self.used_pokemon]
        if not available:
            self.used_pokemon = []
            available = all_pokemon
        pokemon = random.choice(available)
        self.used_pokemon.append(pokemon)
        return pokemon

    def wild_pokemon_encounter(self):
        pokemon_name = self.get_wild_pokemon()
        pokemon_info = self.get_pokemon_info(pokemon_name)
        self.print_header("🦁 POKÉMON SALVAJE!")
        print(f"¡Un {pokemon_info['name']} ({pokemon_info['type']}) apareció!")
        category = random.choice(list(QUESTIONS.keys()))
        question = self.get_random_question(category)
        return question, pokemon_name

    def ask_question(self, question_data, context=""):
        print(f"\n{context}")
        print(f"❓ {question_data['question']}")
        for i, option in enumerate(question_data["options"]):
            print(f"  {i + 1}. {option}")

        while True:
            try:
                answer = int(input("\n👉 Tu respuesta (1-4): ")) - 1
                if 0 <= answer <= 3:
                    break
                print("Ingresa 1-4")
            except ValueError:
                print("Ingresa un número válido")

        self.total_questions += 1
        if answer == question_data["answer"]:
            print("\n✅ ¡CORRECTO!")
            self.correct_answers += 1
            return True
        else:
            correct = question_data["options"][question_data["answer"]]
            print(f"\n❌ INCORRECTO. Era: {correct}")
            return False

    def move_player(self, steps=1):
        self.position += steps
        if self.position > TOTAL_SPACES:
            self.position = self.position % TOTAL_SPACES
        print(f"\n🏃 Te mueves {steps} espacios. Posición: {self.position}")

        if self.position in CATEGORY_POSITIONS:
            cat = CATEGORY_POSITIONS[self.position]
            print(
                f"📍 ¡Casilla de {CATEGORIES[cat]['color']}! {CATEGORIES[cat]['symbol']}"
            )

    def add_quesito(self, category):
        info = CATEGORIES[category]
        if category not in self.quesitos:
            self.quesitos.add(category)
            print(f"\n🧀 ¡QUESITO {info['color'].upper()}! ({info['name']})")
        else:
            print(f"\n✨ Ya tienes el quesito {info['color']}.")

    def capture_pokemon(self, pokemon_name_or_obj):
        if isinstance(pokemon_name_or_obj, str):
            pokemon_obj = Pokemon(pokemon_name_or_obj, level=random.randint(3, 7))
            if not pokemon_obj.data:
                info = self.get_pokemon_info(pokemon_name_or_obj)
                print(f"🎉 ¡Capturaste a {info['name']}!")
                pokemon_obj = {"name": info["name"], "type": info["type"]}
        else:
            pokemon_obj = pokemon_name_or_obj
            if isinstance(pokemon_obj, Pokemon):
                print(f"🎉 ¡Capturaste a {pokemon_obj.data['name']}!")
            else:
                print(f"🎉 ¡Capturaste a {pokemon_obj['name']}!")

        if isinstance(pokemon_obj, Pokemon):
            poke_to_add = pokemon_obj
        else:
            poke_to_add = pokemon_obj

        if len(self.pokedex) < MAX_POKEMON:
            self.pokedex.append(poke_to_add)
        else:
            print(f"\n🔄 Equipo lleno ({MAX_POKEMON}). ¿Qué hacer?")
            print("  1. Sustituir un Pokémon")
            print("  2. Depositar en PC")
            print("  3. No capturar")
            try:
                choice = int(input("\n👉 Opción: "))
                if choice == 1:
                    self.show_pokedex()
                    idx = int(input("👉 Pokémon a sustituir: ")) - 1
                    if 0 <= idx < len(self.pokedex):
                        old = self.pokedex[idx]
                        old_name = (
                            old.data["name"]
                            if isinstance(old, Pokemon)
                            else old["name"]
                        )
                        new_name = (
                            poke_to_add.data["name"]
                            if isinstance(poke_to_add, Pokemon)
                            else poke_to_add["name"]
                        )
                        self.pokedex[idx] = poke_to_add
                        print(f"🔄 {old_name} → {new_name}")
                elif choice == 2:
                    self.pc_storage.append(poke_to_add)
                    new_name = (
                        poke_to_add.data["name"]
                        if isinstance(poke_to_add, Pokemon)
                        else poke_to_add["name"]
                    )
                    print(f"📦 {new_name} guardado en PC.")
                else:
                    print("✋ No capturaste nada.")
            except ValueError:
                print("No capturaste nada.")

    def play_turn(self):
        self.print_status()

        print("\n📋 Menú:")
        print("  1. 🎲 Jugar turno")
        print("  2. 👤 Gestionar Pokémon")
        print("  3. 🧀 Ver quesitos")
        print("  4. 📊 Ver tablero")

        try:
            option = int(input("\n👉 Opción: "))
        except ValueError:
            option = 1

        if option == 2:
            self.manage_pokemon_menu()
            return False
        elif option == 3:
            self.print_header("🧀 QUESITOS")
            for k, v in CATEGORIES.items():
                status = "✅" if k in self.quesitos else "❌"
                print(f"  {status} {v['symbol']} {v['color']}: {v['name']}")
            input("\nEnter...")
            return False
        elif option == 4:
            self.show_board()
            input("\nEnter...")
            return False

        self.show_board()
        input("\n🎲 Presiona Enter para lanzar el dado...")

        dice = random.randint(1, 6)
        print(f"\n🎲 ¡Sacaste un {dice}!")

        self.move_player(dice)
        self.turns_played += 1

        question, pokemon_name = self.wild_pokemon_encounter()

        print(f"\n¡Un {pokemon_name} apareció!")

        if self.pokedex:
            print("\n📋 ¿Qué quieres hacer?")
            print("  1. 💬 Responder pregunta (capturar)")
            print("  2. ⚔️ Combatir")
            try:
                choice = int(input("\n👉 Opción: "))
            except ValueError:
                choice = 1
        else:
            choice = 1

        if choice == 2 and self.pokedex:
            enemy_pokemon = Pokemon(pokemon_name, level=random.randint(3, 7))
            print(
                f"¡Un {enemy_pokemon.data['name']} (Nv.{enemy_pokemon.level}) apareció!"
            )

            print("\n👤 Elige tu Pokémon:")
            for i, p in enumerate(self.pokedex, 1):
                if isinstance(p, Pokemon):
                    print(
                        f"  {i}. {p.data['name']} (Nv.{p.level}) HP:{p.hp}/{p.max_hp}"
                    )
                else:
                    print(f"  {i}. {p['name']}")
            try:
                idx = int(input("\n👉 Pokémon: ")) - 1
                if 0 <= idx < len(self.pokedex):
                    player_pokemon = self.pokedex[idx]
                    if isinstance(player_pokemon, Pokemon):
                        battle = Battle(player_pokemon, enemy_pokemon)
                        victory = battle.run()
                        if victory:
                            self.capture_pokemon(pokemon_name)
                    else:
                        print(
                            "Este Pokémon necesita ser actualizado. Responde la pregunta."
                        )
                        correct = self.ask_question(
                            question, f"\n¡Captura a {pokemon_name}!"
                        )
                        if correct:
                            self.capture_pokemon(pokemon_name)
                else:
                    correct = self.ask_question(
                        question, f"\n¡Captura a {pokemon_name}!"
                    )
                    if correct:
                        self.capture_pokemon(pokemon_name)
            except ValueError:
                correct = self.ask_question(question, f"\n¡Captura a {pokemon_name}!")
                if correct:
                    self.capture_pokemon(pokemon_name)
        else:
            correct = self.ask_question(question, f"\n¡Captura a {pokemon_name}!")
            if correct:
                self.capture_pokemon(pokemon_name)

        if len(self.pokedex) >= 3:
            print("\n🏆 ¿Combatir líder de gimnasio? (s/n)")
            if input("👉 ").lower() == "s":
                disponibles = [c for c in CATEGORIES if c not in self.quesitos]
                if disponibles:
                    cat = random.choice(disponibles)
                    q, leader, enemy_name = self.battle_gym_leader(cat)

                    print("\n👤 Elige tu Pokémon para el combate de gimnasio:")
                    for i, p in enumerate(self.pokedex, 1):
                        if isinstance(p, Pokemon):
                            print(
                                f"  {i}. {p.data['name']} (Nv.{p.level}) HP:{p.hp}/{p.max_hp}"
                            )
                        else:
                            print(f"  {i}. {p['name']}")
                    try:
                        idx = int(input("\n👉 Pokémon: ")) - 1
                        if 0 <= idx < len(self.pokedex):
                            player_pokemon = self.pokedex[idx]
                            if isinstance(player_pokemon, Pokemon):
                                enemy_pokemon = Pokemon(enemy_name, level=10)
                                print(
                                    f"¡El líder usa a {enemy_pokemon.data['name']} (Nv.{enemy_pokemon.level})!"
                                )
                                battle = Battle(player_pokemon, enemy_pokemon)
                                victory = battle.run()
                                if victory:
                                    self.add_quesito(cat)
                            else:
                                print(f"\n🎯 Quesito {CATEGORIES[cat]['color']}:")
                                if self.ask_question(q):
                                    self.add_quesito(cat)
                        else:
                            print(f"\n🎯 Quesito {CATEGORIES[cat]['color']}:")
                            if self.ask_question(q):
                                self.add_quesito(cat)
                    except ValueError:
                        print(f"\n🎯 Quesito {CATEGORIES[cat]['color']}:")
                        if self.ask_question(q):
                            self.add_quesito(cat)

        return len(self.quesitos) >= 6

    def start(self):
        print("\n" + "🎮" * 20)
        print("\n   🧀 TRIVIAL PURSUIT: VIDEOJUEGOS EDITION 🐾")
        print("\n" + "🎮" * 20)

        print(f"\n¡Bienvenido, {self.player_name}!")
        print("\n📋 Categorías del tablero:")
        for k, v in CATEGORIES.items():
            print(f"  {v['symbol']} {v['color']}: {v['name']}")

        print("\n🎯 Objetivo: Consigue los 6 quesitos!")
        print("🏃 Mueveten el tablero, combate Pokémon salvajes,")
        print("   captura 3+ para batallar contra líderes de gimnasio.")
        print("💻 Usa el PC para gestionar tus Pokémon.")

        self.show_board()
        input("\n🎮 Presiona Enter para comenzar...")

        max_turns = 50
        while not self.play_turn() and self.turns_played < max_turns:
            pass

        self.print_header("📊 RESULTADO FINAL")
        print(f"  • Quesitos: {len(self.quesitos)}/6")
        print(f"  • Turnos jugados: {self.turns_played}")
        print(f"  • Precisión: {self.correct_answers}/{self.total_questions}")

        self.show_pokedex()

        if len(self.quesitos) == 6:
            print("\n🏆 ¡FELICIDADES! ¡HAS GANADO!")
        else:
            print("\n💪 ¡Otra vez será!")


def main():
    print("\n🎮 TRIVIAL VIDEOJUEGOS EDITION 🐾\n")
    name = input("¿Cómo te llamas? ").strip() or "Entrenador"
    game = TrivialVideojuegos(name)
    game.start()


if __name__ == "__main__":
    main()

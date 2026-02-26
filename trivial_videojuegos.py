import random

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
    {"name": "Pikachu", "type": "Eléctrico"},
    {"name": "Charmander", "type": "Fuego"},
    {"name": "Squirtle", "type": "Agua"},
    {"name": "Bulbasaur", "type": "Planta/Veneno"},
    {"name": "Meowth", "type": "Normal"},
    {"name": "Psyduck", "type": "Agua"},
    {"name": "Mankey", "type": "Lucha"},
    {"name": "Poliwag", "type": "Agua"},
    {"name": "Bellsprout", "type": "Planta/Veneno"},
    {"name": "Drowzee", "type": "Psíquico"},
    {"name": "Magikarp", "type": "Agua"},
    {"name": "Eevee", "type": "Normal"},
    {"name": "Snorlax", "type": "Normal"},
    {"name": "Articuno", "type": "Hielo/Volador"},
    {"name": "Zapdos", "type": "Eléctrico/Volador"},
    {"name": "Moltres", "type": "Fuego/Volador"},
    {"name": "Mewtwo", "type": "Psíquico"},
    {"name": "Mew", "type": "Psíquico"},
    {"name": "Dragonite", "type": "Dragón/Volador"},
    {"name": "Gyarados", "type": "Agua/Volador"},
]

BOX_POKEMON = [
    {"name": "Rattata", "type": "Normal"},
    {"name": "Raticate", "type": "Normal"},
    {"name": "Spearow", "type": "Normal/Volador"},
    {"name": "Fearow", "type": "Normal/Volador"},
    {"name": "Ekans", "type": "Veneno"},
    {"name": "Arbok", "type": "Veneno"},
    {"name": "Pidgey", "type": "Normal/Volador"},
    {"name": "Pidgeotto", "type": "Normal/Volador"},
    {"name": "Rattata", "type": "Normal"},
    {"name": "Sentret", "type": "Normal"},
    {"name": "Hoothoot", "type": "Normal/Volador"},
    {"name": "Ledyba", "type": "Bicho/Volador"},
    {"name": "Spinarak", "type": "Bicho/Veneno"},
    {"name": "Crobat", "type": "Veneno/Volador"},
    {"name": "Yanma", "type": "Bicho/Volador"},
]

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
                print(f"  {i}. {p['name']} ({p['type']})")
        print()

    def show_pc(self):
        self.print_header("💻 PC DE POKÉMON - ALMACÉN")
        if not self.pc_storage:
            print("\nEl PC está vacío.")
        else:
            print(f"\nTienes {len(self.pc_storage)} Pokémon en el PC:")
            for i, p in enumerate(self.pc_storage, 1):
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
                self.pc_storage.append(pokemon)
                print(f"📦 {pokemon['name']} ha sido depositado en el PC.")
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
                print(f"📤 {pokemon['name']} ha sido añadido a tu equipo.")
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

    def battle_gym_leader(self, category):
        leader = GYM_LEADERS[category]
        self.print_header(f"LÍDER DE GIMNASIO: {leader['name']}")
        print(f"🎯 Te desafía con su {leader['pokemon']}!")
        print(f"📺 Juego: {leader['game']}")
        question = self.get_random_question(category)
        return question, leader

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
        pokemon = self.get_wild_pokemon()
        self.print_header("🦁 POKÉMON SALVAJE!")
        print(f"¡Un {pokemon['name']} ({pokemon['type']}) apareció!")
        category = random.choice(list(QUESTIONS.keys()))
        question = self.get_random_question(category)
        return question, pokemon

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

    def capture_pokemon(self, new_pokemon):
        if len(self.pokedex) < MAX_POKEMON:
            self.pokedex.append(new_pokemon)
            print(f"🎉 ¡Capturaste a {new_pokemon['name']}!")
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
                        self.pokedex[idx] = new_pokemon
                        print(f"🔄 {old['name']} → {new_pokemon['name']}")
                elif choice == 2:
                    self.pc_storage.append(new_pokemon)
                    print(f"📦 {new_pokemon['name']} guardado en PC.")
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

        question, pokemon = self.wild_pokemon_encounter()
        correct = self.ask_question(question, f"\n¡Captura a {pokemon['name']}!")

        if correct:
            self.capture_pokemon(pokemon)

            if len(self.pokedex) >= 3:
                print("\n🏆 ¿Combatir líder de gimnasio? (s/n)")
                if input("👉 ").lower() == "s":
                    disponibles = [c for c in CATEGORIES if c not in self.quesitos]
                    if disponibles:
                        cat = random.choice(disponibles)
                        q, leader = self.battle_gym_leader(cat)
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

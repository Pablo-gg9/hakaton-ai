import random

CATEGORIES = {
    "azul": {"name": "Geografía de Videojuegos", "color": "Azul"},
    "marron": {"name": "Arte y Literatura de Videojuegos", "color": "Marrón"},
    "amarillo": {"name": "Historia de Videojuegos", "color": "Amarillo"},
    "rosa": {"name": "Espectáculos de Videojuegos", "color": "Rosa"},
    "verde": {"name": "Ciencia y Naturaleza de Videojuegos", "color": "Verde"},
    "naranja": {"name": "Deportes y Pasatiempos", "color": "Naranja"},
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
            "question": "¿Qué actor voiced a Nathan Drake en 'Uncharted'?",
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
            "question": "¿Cuántos jugadores pueden jugar simultáneamente en 'Super Smash Bros. Ultimate'?",
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

MAX_POKEMON = 6


class TrivialVideojuegos:
    def __init__(self, player_name):
        self.player_name = player_name
        self.position = 0
        self.quesitos = set()
        self.pokedex = []
        self.used_pokemon = []
        self.used_questions = {
            "azul": [],
            "marron": [],
            "amarillo": [],
            "rosa": [],
            "verde": [],
            "naranja": [],
        }
        self.total_questions = 0
        self.correct_answers = 0

    def print_header(self, title):
        print("\n" + "=" * 50)
        print(f"  {title}")
        print("=" * 50)

    def print_status(self):
        print(f"\n🎮 Jugador: {self.player_name}")
        print(f"📍 Posición: {self.position}")
        print(f"🧀 Quesitos: {len(self.quesitos)}/6")
        print(f"🐾 Pokémon: {len(self.pokedex)}/{MAX_POKEMON}")

    def show_pokedex(self):
        self.print_header("📱 TU POKÉDEX")
        if not self.pokedex:
            print("\nNo tienes ningún Pokémon todavía.")
        else:
            for i, p in enumerate(self.pokedex, 1):
                print(f"  {i}. {p['name']} ({p['type']})")
        print()

    def get_random_question(self, category):
        available_questions = [
            q for q in QUESTIONS[category] if q not in self.used_questions[category]
        ]
        if not available_questions:
            self.used_questions[category] = []
            available_questions = QUESTIONS[category]

        question = random.choice(available_questions)
        self.used_questions[category].append(question)
        return question

    def battle_gym_leader(self, category):
        leader = GYM_LEADERS[category]
        self.print_header(f"LÍDER DE GIMNASIO: {leader['name']}")
        print(f"🎯 Te desafía con su {leader['pokemon']}!")
        print(f"📺 Juego de referencia: {leader['game']}")

        question = self.get_random_question(category)
        return question, leader

    def get_wild_pokemon(self):
        available_pokemon = [p for p in WILD_POKEMON if p not in self.used_pokemon]
        if not available_pokemon:
            self.used_pokemon = []
            available_pokemon = WILD_POKEMON

        pokemon = random.choice(available_pokemon)
        self.used_pokemon.append(pokemon)
        return pokemon

    def wild_pokemon_encounter(self):
        pokemon = self.get_wild_pokemon()
        self.print_header("🦁 POKÉMON SALVAJE APARECIDO!")
        print(f"¡Un {pokemon['name']} ({pokemon['type']}) salvaje apareció!")

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
                print("Por favor, ingresa un número entre 1 y 4")
            except ValueError:
                print("Por favor, ingresa un número válido")

        self.total_questions += 1

        if answer == question_data["answer"]:
            print("\n✅ ¡CORRECTO! ¡Bien hecho!")
            self.correct_answers += 1
            return True
        else:
            correct = question_data["options"][question_data["answer"]]
            print(f"\n❌ ¡INCORRECTO! La respuesta era: {correct}")
            return False

    def move_player(self, steps=1):
        self.position += steps
        if self.position > 63:
            self.position = self.position % 63
        print(f"\n🏃 Te mueves {steps} espacios. Posición: {self.position}")

    def add_quesito(self, category):
        category_info = CATEGORIES[category]
        if category not in self.quesitos:
            self.quesitos.add(category)
            print(f"\n🧀 ¡HAS OBTENIDO EL QUESITO {category_info['color'].upper()}!")
            print(f"   Categoría: {category_info['name']}")
        else:
            print(f"\n✨ Ya tienes el quesito {category_info['color']}!")

    def capture_pokemon(self, new_pokemon):
        if len(self.pokedex) < MAX_POKEMON:
            self.pokedex.append(new_pokemon)
            print(f"🎉 ¡Has capturado a {new_pokemon['name']}!")
        else:
            self.print_header("🔄 INVENTARIO LLENO")
            print(f"Tienes {MAX_POKEMON} Pokémon. ¿Qué quieres hacer?")
            print("  1. Sustituir un Pokémon")
            print("  2. No capturar")

            while True:
                try:
                    choice = int(input("\n👉 Opción (1-2): "))
                    if choice in [1, 2]:
                        break
                    print("Ingresa 1 o 2")
                except ValueError:
                    print("Ingresa un número válido")

            if choice == 1:
                self.show_pokedex()
                while True:
                    try:
                        idx = (
                            int(
                                input(
                                    f"👉 Número del Pokémon a sustituir (1-{MAX_POKEMON}): "
                                )
                            )
                            - 1
                        )
                        if 0 <= idx < len(self.pokedex):
                            old_pokemon = self.pokedex[idx]
                            self.pokedex[idx] = new_pokemon
                            print(
                                f"🎉 ¡Has liberado a {old_pokemon['name']} y capturado a {new_pokemon['name']}!"
                            )
                            break
                        print(f"Ingresa un número entre 1 y {len(self.pokedex)}")
                    except ValueError:
                        print("Ingresa un número válido")
            else:
                print(f"✋ Has decidido no capturar a {new_pokemon['name']}.")

    def play_turn(self):
        self.print_status()

        print("\n📋 Opciones:")
        print("  1. Jugar turno")
        print("  2. Ver Pokédex")
        print("  3. Ver quesitos")

        while True:
            try:
                option = int(input("\n👉 Opción (1-3): "))
                if option in [1, 2, 3]:
                    break
                print("Ingresa 1, 2 o 3")
            except ValueError:
                print("Ingresa un número válido")

        if option == 2:
            self.show_pokedex()
            input("Presiona Enter para continuar...")
            return False
        elif option == 3:
            self.print_header("🧀 TUS QUESITOS")
            for key, cat in CATEGORIES.items():
                status = "✅" if key in self.quesitos else "❌"
                print(f"  {status} {cat['color']}: {cat['name']}")
            print()
            input("Presiona Enter para continuar...")
            return False

        input("\n🎲 Presiona Enter para moverte...")

        dice_roll = random.randint(1, 6)
        print(f"\n🎲 ¡Sacaste un {dice_roll}!")

        self.move_player(dice_roll)

        question, pokemon = self.wild_pokemon_encounter()

        correct = self.ask_question(
            question,
            context=f"¡Responde correctamente para capturar a {pokemon['name']}!",
        )

        if correct:
            self.capture_pokemon(pokemon)

            if len(self.pokedex) >= 3:
                print(
                    "\n🏆 ¡Tienes 3 o más Pokémon! ¿Quieres enfrentar a un líder de gimnasio?"
                )
                choice = input("  (s/n): ").lower()

                if choice == "s":
                    available_categories = [
                        c for c in CATEGORIES.keys() if c not in self.quesitos
                    ]
                    if available_categories:
                        category = random.choice(available_categories)
                        leader_question, leader = self.battle_gym_leader(category)

                        print(
                            f"\n🎯 Pregunta para obtener el quesito {CATEGORIES[category]['color']}:"
                        )
                        correct = self.ask_question(leader_question)

                        if correct:
                            self.add_quesito(category)
                        else:
                            print("No has podido obtener el quesito esta vez.")
                    else:
                        print("¡Ya tienes todos los quesitos!")

        return len(self.quesitos) >= 6

    def start(self):
        print("\n" + "🎮" * 20)
        print("\n   TRIVIAL PURSUIT: EDICIÓN VIDEOJUEGOS")
        print("        Con elementos de Pokémon")
        print("\n" + "🎮" * 20)

        print(f"\n¡Bienvenido, {self.player_name}!")
        print("\n📋 CATEGORÍAS:")
        for key, cat in CATEGORIES.items():
            print(f"  • {cat['color']}: {cat['name']}")

        print("\n🎯 OBJETIVO:")
        print("  - Consigue los 6 quesitos derrotando a los líderes de gimnasio")
        print("  - Para moverte, enfréntate a Pokémon salvajes")
        print("  - Si aciertas las preguntas, puedes capturar Pokémon")
        print("  - Máximo 6 Pokémon en tu inventario")

        print("\n🏃 CÓMO JUGAR:")
        print("  1. Lanza el dado para moverte")
        print("  2. Encuentra un Pokémon salvaje")
        print("  3. Responde correctamente para capturarlo")
        print("  4. Con 3+ Pokémon, puedes enfrentar a un líder de gimnasio")
        print("  5. Si tienes 6 Pokémon, puedes sustituir uno al capturar nuevo")
        print("  6. ¡Gana los 6 quesitos para victory!")
        print("  7. Usa 'Ver Pokédex' para ver tu inventario")

        input("\n🎮 Presiona Enter para comenzar...")

        turns = 0
        max_turns = 50

        while not self.play_turn() and turns < max_turns:
            turns += 1
            if turns >= max_turns:
                print("\n⏰ ¡Se acabaron los turnos!")
                break

        self.print_header("RESULTADO FINAL")
        print(f"\n📊 ESTADÍSTICAS:")
        print(f"  • Quesitos obtenidos: {len(self.quesitos)}/6")
        print(f"  • Pokémon en equipo: {len(self.pokedex)}")
        print(f"  • Preguntas contestadas: {self.total_questions}")
        print(f"  • Respuestas correctas: {self.correct_answers}")

        if self.correct_answers > 0:
            accuracy = (self.correct_answers / self.total_questions) * 100
            print(f"  • Precisión: {accuracy:.1f}%")

        self.show_pokedex()

        if len(self.quesitos) == 6:
            print("\n🏆 ¡FELICIDADES! ¡HAS GANADO EL JUEGO!")
        else:
            print("\n💪 ¡Sigue intentándolo!")

        print("\n" + "=" * 50)


def main():
    print("\n🎮 TRIVIAL PURSUIT: VIDEOJUEGOS EDITION 🎮\n")

    player_name = input("¿Cómo te llamas? ").strip()
    if not player_name:
        player_name = "Entrenador"

    game = TrivialVideojuegos(player_name)
    game.start()


if __name__ == "__main__":
    main()

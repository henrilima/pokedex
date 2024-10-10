from traductions import abilities_translation, type_translation
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from io import BytesIO
from PIL import Image, ImageTk
import requests
from googletrans import Translator

font = ('Arial', 12, 'bold')
bg = '#d9d9d9'

def translate_types(types_list, translation):
    return [translation.get(t, t) for t in types_list]

def toggle_frames(main_frame, frame_pokemon_info, pokemon=None):
    if main_frame.winfo_ismapped():
        main_frame.pack_forget()
        frame_pokemon_info.pack(fill=tk.BOTH, expand=True)
    else:
        frame_pokemon_info.pack_forget()
        for widget in frame_pokemon_info.winfo_children():
            if widget.winfo_name() != 'arrow':
                widget.destroy()
        main_frame.pack(fill=tk.BOTH, expand=True)
        if pokemon is not None:
            pokemon.focus_set()

def search_pokemon(pokemon_name, main_frame, frame_pokemon_info, pokemon_input):
    global font, bg
    if pokemon_name.get("1.0", "end").strip() == '':
        return messagebox.showerror("Erro", "Não foi possível encontrar esse pokémon. Verifique o ID ou nome dele.")
    pokemon = pokemon_name.get("1.0", "end").strip().lower()

    link_request = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = requests.get(link_request)
    if response.status_code == 200:
        data = response.json()
        pokemon_data = {
            "id": data["id"],
            "name": data["name"],
            "height": data["height"],  # Altura em decímetros
            "weight": data["weight"],  # Peso em hectogramas
            "types": [t["type"]["name"] for t in data["types"]],  # Lista de tipos
            "abilities": [a["ability"]["name"] for a in data["abilities"]],  # Lista de habilidades
            "sprite": data["sprites"]['other']['official-artwork']["front_default"],  # Sprite do Pokémon
            "description": "",
        }
        pokemon_data["height"] = pokemon_data["height"] / 10 # Atualizando a altura para metros
        pokemon_data["weight"] = pokemon_data["weight"] / 10 # Atualizando a altura para kg
        pokemon_data["types"] = translate_types(pokemon_data["types"], type_translation)
        pokemon_data["abilities"] = translate_types(pokemon_data["abilities"], abilities_translation)

        response_description = requests.get(f'https://pokeapi.co/api/v2//pokemon-species/{pokemon_data["id"]}')
        data_description = response_description.json()

        flavor_text = "";
        for entry in data_description["flavor_text_entries"]:
            if entry["language"]["name"] == "en":  # Verifica se a língua é inglês
                flavor_text = entry["flavor_text"].replace("\f", " ")  # Remove a quebra de página
                break

        cleaned_text = flavor_text.replace("\n", " ")

        translator = Translator()
        translated = translator.translate(cleaned_text, src='en', dest='pt').text
        new_description = translated.split()

        grouped_text = ""
        words = 4
        for i in range(0, len(new_description), words):
            group = " ".join(new_description[i:i + words])
            grouped_text += group + "\n"

        pokemon_data["description"] = grouped_text

        # CRIANDO A TELA DE QUANDO O POKÉMON É ENCONTRADO
        # trocando as telas
        toggle_frames(main_frame, frame_pokemon_info, pokemon_input)

        # buscando o ícone do pokémon
        icon_request = requests.get(pokemon_data["sprite"])
        icon_request.raise_for_status()
        icon_pokemon_png = Image.open(BytesIO(icon_request.content))

        # redimensiona a imagem do pokemon
        new_size = (160, 160)  # Defina o tamanho desejado
        icon_pokemon_resized = icon_pokemon_png.resize(new_size, Image.LANCZOS)
        icon_pokemon = ImageTk.PhotoImage(icon_pokemon_resized)

        # criando o Label e exibindo a imagem
        image_pokemon = ttk.Label(frame_pokemon_info, image=icon_pokemon, background=bg)
        image_pokemon.place(relx=0.5, rely=0.05, anchor='n')
        image_pokemon.image = icon_pokemon

        # inserindo na tela o nome e o ID do pokémon
        (ttk.Label(frame_pokemon_info, background='#d9d9d9', text=f"{str(pokemon_data['name']).capitalize()} #{pokemon_data['id']}", font=("Arial", 16, "bold"))
         .place(relx=0.5, rely=0.35, anchor='n'))
        # inserindo a descrição do pokémon
        (ttk.Label(frame_pokemon_info, background='#d9d9d9', text=f"{pokemon_data["description"]}", justify="center",
                   font=("Arial", 13))
         .place(relx=0.5, rely=0.40, anchor='n'))

        # inserindo a altura do pokémon
        (ttk.Label(frame_pokemon_info, background='#d9d9d9', text="Altura:", font=("Arial", 14, "bold"))
         .place(relx=0.20, rely=0.70, anchor='n'))
        (ttk.Label(frame_pokemon_info, background='#d9d9d9', text=f"{pokemon_data['height']}m", font=("Arial", 12))
         .place(relx=0.20, rely=0.74, anchor='n'))

        # inserindo o peso do pokémon
        (ttk.Label(frame_pokemon_info, background='#d9d9d9', text="Peso:", font=("Arial", 14, "bold"))
         .place(relx=0.70, rely=0.70, anchor='n'))
        (ttk.Label(frame_pokemon_info, background='#d9d9d9', text=f"{pokemon_data['weight']}kg", font=("Arial", 12))
        .place(relx=0.70, rely=0.74, anchor='n'))

        # inserindo o peso do pokémon
        (ttk.Label(frame_pokemon_info, background='#d9d9d9', text="Tipos:", font=("Arial", 14, "bold"))
         .place(relx=0.20, rely=0.80, anchor='n'))
        (ttk.Label(frame_pokemon_info, background='#d9d9d9', text=f"{'\n'.join(pokemon_data['types'])}", justify="center", font=("Arial", 12))
         .place(relx=0.20, rely=0.84, anchor='n'))

        # inserindo os status do pokémon
        (ttk.Label(frame_pokemon_info, background='#d9d9d9', text="Habilidades:", font=("Arial", 14, "bold"))
         .place(relx=0.70, rely=0.80, anchor='n'))
        (ttk.Label(frame_pokemon_info, background='#d9d9d9', text=f"{'\n'.join(pokemon_data['abilities'])}", justify="center",
                   font=("Arial", 12))
         .place(relx=0.70, rely=0.84, anchor='n'))

    else:
        messagebox.showerror("Erro", "Não foi possível encontrar esse pokémon. Verifique o ID ou nome dele.")
        print(f"Error: {response.status_code} - Pokemon not found")
from scripts import *

# CRIANDO E CONFIGURANDO A TELA
root = tk.Tk()
root.geometry('350x500')
root.title('Pokédex')
root.iconbitmap('./assets/pokeball.ico')
root.resizable(False, False)

# CRIANDO UM FRAME PARA COMPORTAR OS ELEMENTOS DA TELA
main_frame = tk.Frame(root, bg=bg)
main_frame.pack(fill=tk.BOTH, expand=True)

# CRIANDO OS ELEMENTOS DA PÁGINA PRINCIPAL
icon_png = Image.open('./assets/pokedex.png')
icon = ImageTk.PhotoImage(icon_png)
(tk.Label(main_frame, image=icon, bg=bg)
 .place(relx=0.5, rely=0.25, anchor=tk.CENTER))
(tk.Label(main_frame, text='Pokédex', bg=bg, font=('Poppins', 18, 'bold'), fg='#101010')
 .place(relx=0.5, rely=0.38, anchor=tk.CENTER))

(tk.Label(main_frame, text='Qual pokémon você\ndeseja procurar? (ID ou nome)', font=font, bg=bg, fg='#101010')
 .place(relx=0.5, rely=0.5, anchor='n'))
pokemon = tk.Text(main_frame, width=26, height=1, bg='#f2f2f2', fg='#101010', font=font, borderwidth=2, relief='flat')
pokemon.place(relx=0.5, rely=0.62, anchor='n')

# limitando os caracteres do input
MAX_CHARS = 30
# limitando quais teclas não podem ser utilizadas no input
def limit_input(event):
 special_keys = ["Control_L", "Control_R", "Shift_L", "Shift_R", "Alt_L", "Alt_R", "Caps_Lock", "Tab", "Escape", "Return"]

 if event.keysym in special_keys:
  if event.keysym == 'Return':
   search()
   return "break"
  else:
   return "break"

 current_text = pokemon.get("1.0", "end-1c")

 if len(current_text) >= MAX_CHARS and event.keysym not in ('BackSpace', 'Delete'):
  return "break"
pokemon.bind("<Key>", limit_input)

(tk.Button(main_frame, text='Buscar', bg='#cc0000', fg='#f2f2f2', relief="flat", font=font, cursor='hand2', activeforeground='#f2f2f2', borderwidth=0, activebackground='#cc0000', highlightthickness=0, command = lambda: search())
 .place(relx=0.5, rely=0.7, anchor='n'))


# CRIANDO O PRÓXIMO FRAME, QUE VAI COMPORTAR AS INFORMAÇÕES DOS POKÉMONS
frame_pokemon_info = tk.Frame(root, bg=bg)
frame_pokemon_info.pack_forget()

icon_back = Image.open('assets/back-arrow.png')

new_size_arrow = (42, 42)  # Defina o tamanho desejado
icon_arrow_resized = icon_back.resize(new_size_arrow, Image.LANCZOS)
icon_arrow_back = ImageTk.PhotoImage(icon_arrow_resized)

arrow_back = tk.Button(frame_pokemon_info, image=icon_arrow_back, bg=bg, font=font, relief="flat", activebackground=bg,
                       borderwidth=0, cursor='hand2', command=lambda: toggle_frames(main_frame, frame_pokemon_info), name="arrow")
arrow_back.place(relx=0.07, rely=0.05, anchor='nw')

def search():
 global pokemon, main_frame, frame_pokemon_info
 search_pokemon(pokemon, main_frame, frame_pokemon_info, pokemon)

pokemon.focus_set()

tk.mainloop()
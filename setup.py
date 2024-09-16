from cx_Freeze import setup, Executable

build_exe_options = {
    "build_exe": "build/Pokedex_v1.0.0",
    "packages": ["tkinter", "PIL", "requests"],
    "includes": ["tkinter", "PIL", "requests"],  # Force a inclusão de Pillow
    "zip_include_packages": ["encodings", "PySide6", "shiboken6"],
    "include_files": [
        ("./assets", "assets"),
    ]
}

setup(
    name = "Pokédex",
    version = "1.0",
    description = "Um simples projeto de uma Pokédex consumindo uma API REST com Python.",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base="Win32GUI", icon="./assets/pokeball.ico", target_name="Pokédex", shortcut_name="Pokédex")]
)
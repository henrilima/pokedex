# Pokédex

O **Pokédex** é um aplicativo feito em Python que permite ao usuário buscar informações detalhadas sobre os Pokémon. Utilizando a API pública do Pokémon, o aplicativo exibe dados como o nome, ID, altura, peso, tipos, habilidades e uma imagem do Pokémon pesquisado. O projeto foi desenvolvido usando bibliotecas como `tkinter`, `requests`, e `Pillow`, e pode ser executado tanto em ambientes com Python instalado quanto em executáveis gerados via `cx_Freeze`.

## Funcionalidades
- Buscar informações de Pokémon por nome ou ID.
- Exibir detalhes do Pokémon, incluindo ID, altura, peso, tipos e habilidades.
- Mostrar a imagem oficial do Pokémon.
- Interface gráfica simples e intuitiva criada com `tkinter`.

## Como usar
1. **Instalar dependências:**
   Se você estiver rodando o código diretamente em Python, certifique-se de instalar as dependências listadas no arquivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

2. **Executar o projeto:**
   Execute o arquivo `main.py` para iniciar o aplicativo:

   ```bash
   python main.py
   ```

## Geração do Executável com `cx_Freeze`
Se você deseja rodar o aplicativo em máquinas que não tenham o Python instalado, você pode gerar um executável usando o `cx_Freeze`.

### Como gerar o executável:
1. **Instalar o `cx_Freeze`:**
   Certifique-se de que o `cx_Freeze` está instalado no seu ambiente virtual:

   ```bash
   pip install cx_Freeze
   ```

2. **Rodar o script de build:**
   Após configurar o `setup.py`, execute o comando:

   ```bash
   python setup.py build
   ```

   Isso irá gerar uma pasta `build` contendo o executável.

### Limitações do `cx_Freeze`
Embora o `cx_Freeze` facilite a geração de executáveis para sistemas que não possuem o Python instalado, há algumas limitações:
- **Bibliotecas gráficas:** Bibliotecas que utilizam interfaces gráficas como o `tkinter` podem exigir a configuração correta das variáveis de ambiente `TCL_LIBRARY` e `TK_LIBRARY` para que as dependências de `tkinter` sejam encontradas corretamente.
- **Tamanho do executável:** O executável gerado pode ser grande, uma vez que inclui todos os módulos do Python necessários para rodar o programa de forma independente.

## Contribuição
Se você deseja contribuir com este projeto, sinta-se à vontade para abrir um _pull request_ ou reportar _issues_ na seção de _issues_ do repositório.

## Licença
Este projeto está licenciado sob a licença Apache-2.0. Veja o arquivo `LICENSE` para mais detalhes.

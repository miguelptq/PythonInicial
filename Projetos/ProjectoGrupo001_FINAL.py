# Import libraries
from time import sleep
from colorama import init, Fore, Style
from datetime import date

# Initialize colorama
init(autoreset=True)


def apresentacao():
    """
        Display a centered presentation message

        The function calculates the padding to center the message in a line of length 60,
        displays the top and bottom borders, and then prints the centered presentation message
        in green color.

        """
    msg = 'Sistema de Gestão e Empréstimo de Livros'
    padding = (60 - len(msg)) // 2
    print('=' * (padding + len(msg) + padding))
    print(Fore.GREEN + f'{msg:^60}')
    print('=' * (padding + len(msg) + padding))


def menu_principal():
    """
    Display the main menu options.
    """
    menu_word = "=== Menu ==="
    print("\n" + Fore.CYAN + Style.BRIGHT + menu_word)
    print(Fore.YELLOW + "[1] Inserir Livros")
    print(Fore.YELLOW + "[2] Listar Livros")
    print(Fore.YELLOW + "[3] Pesquisar Livros")
    print(Fore.YELLOW + "[4] Remover Livros")
    print(Fore.YELLOW + "[5] Emprestar Livros")
    print(Fore.YELLOW + "[6] Devolver Livros")
    print(Fore.RED + "[7] Sair")
    print(Fore.CYAN + Style.BRIGHT + "=" * len(menu_word))


def inserir_menu():
    """
    This function inserts book data into the library.
    """
    while True:
        # Define dictionary for each book
        livros = dict()

        # Input for book title
        titulo = input("Digite o título do livro: ").strip().lower()

        # Check if the title is already in the library list
        while any(livros['Título'] == titulo for livros in biblioteca):
            print('Esse livro já está registado')
            titulo = input("Digite o título de outro livro: ").strip().lower()
        else:
            livros['Título'] = titulo

        # Input for authors
        lista_autores = list()
        while True:
            autor = [input("Digite o autor do livro: ")]
            lista_autores.append(autor)
            continuar = input("O livro tem mais autores?: [S/N] ").strip().lower()
            if continuar == "n":
                break
        livros["Autores"] = lista_autores

        # Input for ISBN
        isbn = input('Digite o ISBN do livro: ')
        while len(isbn) != 13 or isbn.isnumeric() is False:
            isbn = input('Digite correctamente o ISBN do livro: ')
        else:
            livros['ISBN'] = isbn

        # Check if ISBN is already in the library list
        while any(livros['ISBN'] == isbn for livros in biblioteca):
            print('Esse ISBN já está registado...')
            isbn = input("Digite outro ISBN para o livro: ")
        else:
            livros['ISBN'] = isbn

        # Input for publication year
        ano_publicacao = (input('Digite o ano de publicação: '))
        while len(ano_publicacao) != 4 or ano_publicacao.isnumeric() is False or ano_publicacao > str(date.today().year):
            ano_publicacao = input('Digite correctamente o ano de publicação do livro: ')
        else:
            livros['Ano de publicação'] = ano_publicacao

        # Input for publisher
        livros['Editora'] = input('Digite a editora do livro: ').strip()

        # Input for genres/categories
        categorias = list()
        while True:
            cat = [input("Digite a categoria do livro: ")]
            categorias.append(cat)
            continuar = input("O livro pode ser identificado com outra categoria?: [S/N] ").strip().lower()
            if continuar == "n":
                livros["Categorias"] = categorias
                break

        # Input for book availability
        status = 'Disponível'
        livros['Status'] = status

        # Input for requisition date
        data_requisicao = ""
        livros['Data de requisição'] = data_requisicao

        # Input for person who borrowed the book
        nome_pessoa = ""
        livros['Pessoa que requisitou'] = nome_pessoa

        # Add record to the library
        biblioteca.append(livros)
        print('Livro registado')

        # Ask if the user wants to register more books
        terminar = input('Deseja registar mais algum livro? [S/N] ').strip().upper()
        if terminar == 'N':
            break


def listar_menu(biblio):
    """
    This function is used to print a list of books, but prettier
    :param biblio: Receives a list of books
    :return: Nothing, prints the list
    """
    # Check if there are no books in the library and no specific status filter
    if len(biblio) == 0:
        print(Fore.RED + "Não tem livros disponíveis!!")
    else:
        # Iterate through each book in the library
        for index, livro in enumerate(biblio):
            # Display a separator for each book
            print(Fore.GREEN + "*=*" * 15)

            # Iterate through each key (attribute) of the book
            for key in livro:
                # Check if the value of the key is not an empty string
                if livro[key] != "":
                    # Check if the value of the key is a list
                    if isinstance(livro[key], list):
                        # Format and join the values in the list
                        formated_keys = ', '.join([' '.join(keys) for keys in livro[key]])
                        print(Fore.BLUE + f"{key}: {Fore.WHITE + formated_keys}")
                    else:
                        # Display the key and its value
                        print(Fore.BLUE + f"{key}: {Fore.WHITE + livro[key]}")

            # Reset text color/style at the end of each book
            print(Style.RESET_ALL, end="")


def remover_livro(ls, op_remover):
    """
    This function removes books from the variable Biblioteca
    :param ls: This parameter receives the current list of books
    :param op_remover: This parameter is this way the program is going to search on the list for a specific book
    :return: It returns the list of books without the removed books
    """
    # Initialize an empty list to store temporary books after removal
    temp_livros = []

    # Check if there are no books in the library
    if len(ls) == 0:
        print("Não existe livros na biblioteca")
    else:
        # Display the available books for the selected removal option
        print(f"{op_remover.upper()}S disponiveis: ", end=" ")

        # Display the values of the selected removal option for each book
        for i, livro in enumerate(ls):
            print(livro[op_remover], end="")
            if i < len(ls) - 1:
                print(", ", end="")

        # Get user input for the value of the removal option to be removed
        valor_remover = input(f"\nQual o {op_remover} do livro a remover?: ") if op_remover == "Título" else (
            input(f"\n{op_remover.upper()} do livro a remover: "))

        # Iterate through the books in the library and filter out the book to be removed
        for key, livro in enumerate(ls):
            del ls[key]
            """if livro[op_remover] != valor_remover:
                temp_livros.append(livro)"""

        # Print a success message for the removed book
        print(f"Livro com o {op_remover} {valor_remover} foi removido com sucesso!!")

    # Return the list of remaining books after removal
    print()
    return ls


def remover_menu(li):
    """
    This function at the beginning it asks for option to remove a book, it could be ISBN or Título, if none of this
    is writen it keeps asking for a valid option until the user types the correct option after that it goes to the
    function remover_livro and after removing a book it asks if the user wants to remove more books
    :param li: List of the current books
    :return: Returns nothing
    """
    # Use the global keyword to indicate that the 'biblioteca' variable is a global variable
    global biblioteca

    # Start a loop for the book removal menu
    while True:
        # Get user input for the removal option (ISBN or Título)
        opcao_remover = input("Pretende remover livros a partir do que? [ISBN ou Título]: ").strip()

        # Validate the user input
        while opcao_remover not in ["ISBN", "Título"]:
            print("Opção inválida, escreva ISBN ou Título")
            opcao_remover = input("Pretende remover livros a partir do que? [ISBN ou Título]: ").strip()

        # Call the 'remover_livro' function to remove books based on the selected option
        biblioteca = remover_livro(li, opcao_remover)

        # Get user input for continuing the removal process
        opcao_remover = input("Pretende remover mais? [s/n]: ").lower().strip()

        # Break the loop if the user chooses not to remove more books
        if opcao_remover == "n":
            break

        # Check if there are no more books in the library to remove
        if len(biblioteca) == 0:
            print("Já não existe livros para remover")
            sleep(1)
            print("A sair do menu de eliminação de livros", end=" ")
            sleep(0.5)
            print(".", end=" ")
            sleep(0.5)
            print(".", end=" ")
            sleep(0.5)
            print(".")
            break


def emprestar(biblio):
    """
    This function is used to borrow books, it looks for books that are with the status Disponivel and list them using
    the function procurar_menu and after that the user has to select a single book and then the status of that book
    passes to Indisponivel and set the data of requisition to the current date and sets the name of the person that made
    the requisition
    :param biblio: This paramether gets the current list of books are on the variable Biblioteca
    :return: Returns nothing
    """
    # Search for books that are currently available for lending
    temp_biblioteca = procurar_menu(biblio, True, "Disponível")

    # Check if there are no available books for lending
    if not temp_biblioteca:
        print(Fore.RED + "Não há livros disponíveis para empréstimo.")
    else:
        # Get user input for borrower's name
        nome_pessoa = input('Qual é o seu nome?: ')

        # Set requisition date to the current date
        data_requisicao = str(date.today())

        # Set book status to unavailable
        status = 'Indisponível'

        # Iterate through all books in the library
        for livro in biblio:
            # Check if the book is in the list of available books for lending
            if livro in temp_biblioteca:
                # Update book information upon lending
                livro['Status'] = status
                livro['Data de requisição'] = data_requisicao
                livro['Pessoa que requisitou'] = nome_pessoa

                # Print a success message for the reserved book
                print()
                print(Fore.GREEN + f"Livro {livro['Título']} reservado com sucesso!!")


def devolver(biblio):
    """
    This function is used to return books, it looks for books that are with the status Indisponível and list them using
    the function procurar_menu and after that the user has to select a single book and then the status of that book
    passes to Disponivel and set the data of requisition to empty and sets the name of the person that made the
    requisition to empty as well
    :param biblio: List of current books
    :return: Nothing
    """
    # Search for books that are currently unavailable for return
    temp_biblioteca = procurar_menu(biblio, True, "Indisponível")

    # Check if there are no unavailable books for return
    if not temp_biblioteca:
        print(Fore.RED + "Não há livros indisponíveis para devolução.")
    else:
        # Initialize variables for resetting book information upon return
        data_requisicao = ''  # Reset requisition date
        status = 'Disponível'  # Set book status to available
        nome_pessoa = ''  # Reset borrower's name

        # Iterate through all books in the library
        for livro in biblio:
            # Check if the book is in the list of books to be returned
            if livro in temp_biblioteca:
                # Reset book information upon return
                livro['Status'] = status
                livro['Data de requisição'] = data_requisicao
                livro['Pessoa que requisitou'] = nome_pessoa

                # Print a success message for the returned book
                print()
                print(Fore.GREEN + f"Livro {livro['Título']} devolvido com sucesso!!")


def procurar_livro(proli, op_procurar, emprestimo_devolucao=False, status=""):
    """
    This function is supposed to list the books inside the current Bibloteca list, you can filter the list by adding
    parameters to the function
    :param status: The book status to filter (e.g., 'Disponível', 'Indisponível'). Default is an
     empty string.
    :param emprestimo_devolucao: True if used for lending or returning books. Default is False.
    :param proli: Current Biblioteca
    :param op_procurar: The key to search on the list (e.g., 'Título', 'ISBN', 'Autores').
    :return: A list of books that match the search criteria.
    """
    # Initialize an empty list to store search results
    pesquisa_biblio = []
    available_data = []

    # Check if the library is empty
    if len(proli) == 0:
        print("Não existe livros na biblioteca")
    else:
        # Start the search loop
        while True:
            # Get the user input for the value to search
            valor_procurado = input(f'{op_procurar} que pretende pesquisar: ')

            # Iterate through each book in the library
            for ind, livro in enumerate(proli):
                # Check if the search is not for lending or returning books
                if emprestimo_devolucao is False:
                    if isinstance(livro[op_procurar], list):
                        # If the attribute is a list (e.g., authors), check each item in the list
                        for autores in livro[op_procurar]:
                            if autores[0] == valor_procurado:
                                pesquisa_biblio.append(livro)
                    else:
                        # If the attribute is a single value, check for a match
                        if livro[op_procurar] == valor_procurado:
                            pesquisa_biblio.append(livro)
                else:
                    # If the search is for lending or returning books and the book is in the correct status
                    if livro['Status'] == status:
                        available_data.append(livro)
                        if isinstance(livro[op_procurar], list):
                            # If the attribute is a list (e.g., authors), check each item in the list
                            for autores in livro[op_procurar]:
                                if autores[0] == valor_procurado:
                                    pesquisa_biblio.append(livro)
                        else:
                            # If the attribute is a single value, check for a match
                            if livro[op_procurar] == valor_procurado:
                                pesquisa_biblio.append(livro)
            # Check if the search is for returning books, and no books are available for return
            if emprestimo_devolucao is True and len(pesquisa_biblio) == 0 and len(available_data) == 0:
                return
            # Check if no matching books were found
            elif len(pesquisa_biblio) == 0:
                print(Fore.RED + 'O livro não existe')
            else:
                break

        # Display the search results
        listar_menu(pesquisa_biblio)

        # If multiple matching books are found and the search is for lending books, ask the user to choose one
        if len(pesquisa_biblio) > 1 and emprestimo_devolucao is True:
            temp_pesquisa_biblio = []
            while True:
                titulo_escolhido = input("Escolha um livro a partir do Título: ")
                for liv in pesquisa_biblio:
                    if liv['Título'] == titulo_escolhido:
                        temp_pesquisa_biblio.append(liv)
                if len(temp_pesquisa_biblio) == 1:
                    pesquisa_biblio = temp_pesquisa_biblio
                    break

    # Return the list of matching books
    return pesquisa_biblio


def procurar_menu(pli, emprestimo_devolucao=False, status=""):
    """
    This function is where the user is asked for the way he wants to search for a book inside the Biblioteca and where
    the function procurar_livro is called
    :param status: This is used for the function devolver and emprestar, so only lists the book that are Disponivel or
    Indisponivel, if status is empty, it lists everything that is inside the variable pli
    :param emprestimo_devolucao: This is an optional parameter, it comes True only when is used on the function devolver
    and emprestar
    :param pli: Current Biblioteca
    :return: This function returns the list of books that the user asks for
    """
    # Initialize an empty list to store search results
    livro_procurado = []

    # Start the search loop
    while True:
        # Get user input for the attribute to search for (Título, ISBN, or Autores)
        opcao_procurar = input("Pretende procurar um livro a partir de? [Título, ISBN ou Autores]: ").strip()

        # Validate the user input
        while opcao_procurar not in ['Título', 'ISBN', 'Autores']:
            print('Opção inválida. Escreva Título, ISBN ou Autores')
            opcao_procurar = input("Pretende procurar um livro a partir de? [Título, ISBN ou Autores]: ").strip()

        # Perform the book search based on user input
        livro_procurado = procurar_livro(pli, opcao_procurar, emprestimo_devolucao, status)

        # If the search is for lending or returning books, return the search results
        if emprestimo_devolucao is True:
            return livro_procurado

        # Get user input for continuing the search
        while opcao_procurar not in 'sn':
            opcao_procurar = input("\nPretende procurar mais livros? [s/n]: ").lower().strip()

        # Break the loop if the user doesn't want to continue the search
        if opcao_procurar == "n":
            break

    # Return the list of matching books
    return livro_procurado


biblioteca = [
    {
        'Título': 'The Hobbit', 'Autores': [['Tolkien']], 'ISBN': '9789721043053', 'Ano de publicação': '1937',
        'Editora': 'Publicações Europa-América', 'Categorias': [['Fantasia']], 'Status': 'Disponível'
    },
    {
        'Título': 'Cujo', 'Autores': [['Stephen King']], 'ISBN': '9781444708127', 'Ano de publicação': '2008',
        'Editora': 'HODDER & STOUGHTON', 'Categorias': [['terror']], 'Status': 'Disponível'
    }
    ]


# Display the program introduction
apresentacao()

# Show the main menu
while True:
    # Display the main menu options
    menu_principal()

    # Get user choice
    choice = input("Escolha um opção (1-7): ").strip()

    # Perform actions based on user choice
    if choice == "1":
        inserir_menu()  # Call the function to insert books
    elif choice == "2":
        listar_menu(biblioteca)  # Call the function to list books
    elif choice == "3":
        biblioteca = procurar_menu(biblioteca)  # Call the function to search for books
    elif choice == "4":
        remover_menu(biblioteca)  # Call the function to remove books
    elif choice == "5":
        emprestar(biblioteca)  # Call the function to lend books
    elif choice == "6":
        devolver(biblioteca)  # Call the function to return books
    elif choice == "7":
        # Exit the program
        print("Programa a terminar", end=" ")
        sleep(0.5)
        print(".", end=" ")
        sleep(0.5)
        print(".", end=" ")
        sleep(0.5)
        print(".")
        break
    else:
        # Invalid choice
        print("Escolha inválida. Escolha uma opção entre 1-7.")

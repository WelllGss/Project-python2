import os
import validations as vali
import random
import matplotlib.pyplot as plt

def crudAdmin(userLogged, movies, movieRooms, users):
    movieId = 0

    while True:
        os.system('cls')
        print('=*' * 25 )
        print('THE WORST CINE'.center(50))
        print('---------------'.center(50))
        print('MENU ADMIN'.center(50))
        print('=*' * 25 , '\n')

        optionMenu = input('Selecione uma Opção: \n \n[1] - Cadastrar Filme \n[2] - Buscar Filme \n[3] - Remover Filme \n[4] - Atualizar Filme \n[5] - Gestão das Salas \n[6] - Gestão de Pagamentos \n[7] - Gestão de feedbacks \n[0] - Deslogar \n\nOpção: ')
        #Logout codition
        if(vali.digitsValidation(optionMenu) == 0):
            response = input('Deseja efetuar o Log-Out? [1]Sim [2]Não')
            if(vali.digitsValidation(response) == 1):
                print('Usuário Deslogado com sucesso!')
                input('')
                return
            elif(vali.digitsValidation(response) == 2):
                pass
            else:
                print('Opção informada Invalida!')
        
        if(vali.digitsValidation(optionMenu) == 1):
            os.system('cls')
            print('=*' * 25 )
            print('CADASTRO DE FILMES'.center(50))
            print('=*' * 25 ,'\n')
            print('')

            while True:
                validMovie = False
                validTitle = True
                movieTitle = input('Digite o titulo do filme: ')

                if(movieTitle.lower() == 'sair'):
                    crudAdmin(userLogged, movies)
                    return
                
                if (len(movieTitle) < 3):
                    print('Titulo do filme informado é muito curto!')
                    validTitle = False

                for movie in movies:
                    if(movie['title'] == movieTitle):
                        print('Filme já cadastrado!')
                        validTitle = False
                
                if(validTitle):
                    while True:
                        print('Escolha a opção do gênero do filme: ')
                        movieGenre = input('[1] - ação \n[2] - ficção\n[3] - terror\n[4] - C#\n[5] - PHP\n[6] - romance\nOpção: ')
                        if(vali.digitsValidation(movieGenre)):
                            movieGenre = int(movieGenre)
                            if (movieGenre == 1):
                                movieGenre = 'ação'
                                break
                            elif (movieGenre == 2):
                                movieGenre = 'ficção'
                                break
                            elif (movieGenre == 3):
                                movieGenre = 'terror'
                                break
                            elif (movieGenre == 4):
                                movieGenre = 'C#'
                                break
                            elif (movieGenre == 5):
                                movieGenre = 'PHP'
                                break
                            elif (movieGenre == 6):
                                movieGenre = 'romance'
                                break
                            else:
                                print('Opção invalida!')
                        else:
                            print('Opção invalida!')
                            input('')

                    sinopseMovie = input('Digite a sinopse do filme: ')
                    while True:
                        classAge = input('Digite a classificação de idade: ')
                        if(vali.digitsValidation(classAge)):
                            classAge = int(classAge)
                            if(classAge < 4):
                                classAge = 'Livre'
                            break
                        else:
                            print('Classificação informada invalida!')
                            input('')

                    while True:
                        movieDuration = input('Digite a duração do filme em minutos: ')
                        if(vali.digitsValidation(movieDuration)):
                            movieDuration = int(movieDuration)
                            if (movieDuration < 60):
                                print('O filmes precisa ter no minímo 1 hora, não aceitamos curta metragem!')
                            else:
                                break
                        else:
                            print('Duração invalida!')
                            input('')

                    while True:
                        releaseDate = vali.dataValidation()

                        if (releaseDate):
                            break
                    
                    while True:
                        valueTicket = input('Digite o valor do ingresso: ')

                        valueTicket = valueTicket.replace(',', '.')
                        
                        if(vali.decimalValidation(valueTicket)):
                            valueTicket = vali.decimalValidation(valueTicket)
                            break

                        print('Valor informado errado!')
                    
                    while True:
                        print('=*' * 25 )
                        print('ESCOLHA DAS SALAS'.center(50))
                        print('=*' * 25 ,'\n')
                        print('')

                        for rooms in movieRooms:
                            print(f'{rooms['roomName']} \nRoom Id: {rooms['idRoom']} \nCapacidade: {rooms['capaccity']}')
                            if(rooms['occupationRoom'] == 0):
                                print('Sala Livre')
                                print('-' * 25 ,'\n')
                            else:
                                print('Sala Ocupada!')
                                print('-' * 25 ,'\n')

                        while True:
                            validRoom = True
                            selectRoom = input('Informe o Id da sala em que o filme vai passar: ')
                            selectRoom = vali.digitsValidation(selectRoom)

                            if(selectRoom):
                                for rooms in movieRooms:
                                    if (rooms['idRoom'] == selectRoom):
                                        if (rooms['occupationRoom'] == 0):
                                            print('Sala selecionada com sucesso')
                                            rooms['occupationRoom'] = 1
                                            validRoom = True
                                            break
                                        else:
                                            validRoom = False
                                            print('Sala Ocupada!')
                                            input('')
                                    validRoom = False
                                
                                if(validRoom):
                                    break
                            else:
                                print('Id informado invalido!')
                        if(validRoom):
                            break

                    while True:
                        movieTime = input('Digite o horário do filme no formato [HH:MM]: ')
                        if len(movieTime) == 5 and movieTime[2] == ':':
                            movieTime = movieTime[:2] + movieTime[3:]
                            if movieTime.isdigit() and (movieTime[:2] >= '00' and movieTime[:2] < '24') and (movieTime[2:] >= '00' and movieTime[2:] < '60'):
                                break
                            else:
                                print('\033[31mHorário Inválido\033[m')
                        else:
                            print('\033[31mHorário Inválido\033[m')
                    
                    print('Filme cadastrado com sucesso!')
                    input('')
                    ratingTomato = random.randint(1, 100)

                    for movie in movies:
                        if (movie['movieId'] > movieId):
                            movieId = movie['movieId']
                    movieId += 1

                    movie = dict()
                    movie['title'] = movieTitle
                    movie['genre'] = movieGenre
                    movie['movieId'] = movieId
                    movie['sinopse'] = sinopseMovie
                    movie['class'] = classAge
                    movie['dataRelease'] = releaseDate
                    movie['duration'] = movieDuration
                    movie['price'] = valueTicket
                    movie['room'] = selectRoom
                    movie['time'] = movieTime
                    movie['rating'] = ratingTomato
                    movie['comments'] = list()

                    movies.append(movie)
                    validMovie = True
                if(validMovie):
                    break
        
        if(vali.digitsValidation(optionMenu) == 2):
            for movie in movies:
                print(f'Filme: {movie['title']} \nID: {movie['movieId']}')
                print('-'*25)
            if (len(movies) < 1):
                print('Não existem filmes no catalago!')
                input('')
            else:
                while True:
                    validSearch = True
                    searchMovie = input('Digite o id do filme para que possa receber mais informações: ')

                    searchMovie = vali.digitsValidation(searchMovie)

                    if(searchMovie):
                        for movie in movies:
                            if(movie['movieId'] == searchMovie):
                                print('='*25)
                                print(f'Título do filme: {movie['title']}\nGênero do filme: {movie['genre']}\nSinopse do Filme: {movie['sinopse']}\nFaixa etária permitida: {movie['class']}\nData de lançamento: {movie['dataRelease']}\nDuração: {movie['duration']//60} Hora(s) e {movie['duration']%60} Minuto(s)\nPreço do ingresso: R${movie['price']}\nSala: {movie['room']}\nHorário de streaming: {movie['time']}\nAprovação: {movie['rating']}')    
                                print('='*25)
                                input('')
                                validSearch = True
                                break
                            validSearch = False
                        if(validSearch):
                            break
                        else:
                            print('Filme não encontrado!')
                    else:
                        print('Opção informada invalida!')
        
        if(vali.digitsValidation(optionMenu) == 3):
            print('=*' * 25 )
            print('REMOVEDOR DE FILMES'.center(50))
            print('=*' * 25 ,'\n')
            print('')
            print('-- Filmes cadastrados --')

            for movie in movies:
                print(f'Filme: {movie['title']} \nID: {movie['movieId']}')
                print('-'*25)
            while True:
                validDel = False
                delMovieId = input('Digite o Id do filme que deseja remover: ')
                delMovieId = vali.digitsValidation(delMovieId)

                if(delMovieId):
                    countIndex = 0
                    for movie in movies:
                        #identify movie
                        if(movie['movieId'] == delMovieId):
                            validDel = True
                            for room in movieRooms:
                                #reset rooms
                                if(room['roomName'] == movie['room']):
                                    room['occupationRoom'] = 0
                                    room['capaccity'] = room['capaccity'] + room['boughtRoom']
                                    validDel = True
                                    break
                            del movies[countIndex]
                        if(validDel):
                            break
                        validDel = False
                        countIndex += 1
                    if(validDel):
                        print('Filme Deletado com sucesso!')
                        break
                    else:
                        print('Opção informada invalida!')    
                else:
                    print('Opção informada invalida!')

        if(vali.digitsValidation(optionMenu) == 4):
            print('=*' * 25 )
            print('ATUALIZAR FILMES'.center(50))
            print('=*' * 25 ,'\n')
            print('')
            print('-- Filmes cadastrados --')

            for movie in movies:
                print(f'Filme: {movie['title']} \nID: {movie['movieId']}')
                print('-'*25)
            while True:
                validUpdate = False
                updateMovie = input('Digite o id do filme que deseja atualizar: ')
                updateMovie = vali.digitsValidation(updateMovie)
                
                if(updateMovie):
                    for movie in movies:
                        if(movie['movieId'] == updateMovie):
                            attType = input('Escolha a informação que deseja atualizar: \n[1] - Título \n[2] - Gênero \n[3] - Sinopse \n[4] - Classificação de Idade \n[5] - Duração \n[6] - Data de Lançamento \n[7] - Sala \n[8] - Horário \n[9] - Avaliação \n[0] - Voltar \nOpção: ')    
                            attType = vali.digitsValidation(attType)
                            if(attType or attType == 0):
                                validUpdate = True
                                if (attType == 1):
                                    newTitle = input('Digite o novo titulo do filme: ')
                                    movie['title'] = newTitle
                                elif (attType == 2):
                                    while True:
                                        print('Escolha o novo gênero do filme: ')
                                        newGenre = input('[1] - ação \n[2] - ficção\n[3] - terror\n[4] - C#\n[5] - PHP\n[6] - romance\nOpção: ')
                                        if(vali.digitsValidation(newGenre)):
                                            newGenre = int(newGenre)
                                            if (newGenre == 1):
                                                newGenre = 'ação'
                                                break
                                            elif (newGenre == 2):
                                                newGenre = 'ficção'
                                                break
                                            elif (newGenre == 3):
                                                newGenre = 'terror'
                                                break
                                            elif (newGenre == 4):
                                                newGenre = 'C#'
                                                break
                                            elif (newGenre == 5):
                                                newGenre = 'PHP'
                                                break
                                            elif (newGenre == 6):
                                                newGenre = 'romance'
                                                break
                                            else:
                                                print('Opção invalida!')
                                        else:
                                            print('Opção invalida!')
                                            input('')
                                    movie['genre'] = newGenre
                                elif (attType == 3):
                                    newSinopse = input('Digite a nova sinopse: ')
                                    movie['sinopse'] = newSinopse
                                elif (attType == 4):
                                    newClassAge = int(input('Digite a nova classificação de idade: '))
                                    movie['class'] = newClassAge
                                elif (attType == 5):
                                    newDuration = int(input('Digite a nova duração do filme em minutos: '))
                                    movie['duration'] = newDuration
                                elif (attType == 6):
                                    while True:
                                        newDataRealese = vali.dataValidation()
                                        if(newDataRealese):
                                            movie['dataRelease'] = newDataRealese
                                            break
                                elif (attType == 7):
                                    for rooms in movieRooms:
                                        print(f'{rooms['roomName']} \nRoom Id: {rooms['idRoom']} \nCapacidade: {rooms['capaccity']}')
                                        if(rooms['occupationRoom'] == 0):
                                            print('Sala Livre')
                                            print('-' * 25 ,'\n')
                                        else:
                                            print('Sala Ocupada!')
                                            print('-' * 25 ,'\n')

                                    while True:
                                        newValidRoom = True
                                        newRoom = input('Informe o Id da sala em que o filme vai passar: ')
                                        newRoom = vali.digitsValidation(newRoom)

                                        if(newRoom):
                                            for rooms in movieRooms:
                                                if (rooms['idRoom'] == newRoom):
                                                    if (rooms['occupationRoom'] == 0):
                                                        print('Sala selecionada com sucesso')
                                                        rooms['occupationRoom'] = 1
                                                        movie['room'] = rooms['roomName']
                                                        newValidRoom = True
                                                        break
                                                    else:
                                                        newValidRoom = False
                                                        print('Sala Ocupada!')
                                                        input('')
                                                newValidRoom = False
                                            
                                            if(newValidRoom):
                                                break
                                        else:
                                            print('Id informado invalido!')
                                
                                elif (attType == 8):
                                    newTime = input('Digite o novo horário do filme [HH:MM]: ')
                                    movie['time'] = newTime
                                elif (attType == 9):
                                    newRating = input('Digite a nova avaliação: ')
                                    newRating += '%'
                                    movie['rating'] = newRating
                                elif (attType == 0):
                                    break                    
                    if(not validUpdate):
                        print('Opção informada invalida!')                
                else:
                    print('Opção informada Invalida!')

                if(validUpdate):
                    break                        

        if(vali.digitsValidation(optionMenu) == 5):
            print('=*' * 25 )
            print('GESTÃO DE SALAS'.center(50))
            print('=*' * 25 ,'\n')
            print('')

            while True:

                actionMenu = input('O que deseja realizar? \n[1] - Criar Sala \n[2] - Deletar Sala \n[3] - Alterar Capacidade \n[4] - Voltar \nOpção: ')

                actionMenu = vali.digitsValidation(actionMenu)

                if(actionMenu):
                    if(actionMenu ==  4):
                        break
                    elif(actionMenu == 1):
                        nameRoom = input('Informe o nome da sala: ')
                        while True:
                            idValid = True
                            idRoom = input('Informe o Id da sala: ')
                            if(vali.decimalValidation(idRoom)):
                                idRoom = int(idRoom)
                                for movie in movieRooms:
                                    if(movie['idRoom'] == idRoom):
                                        idValid = False
                                        break
                                if (idValid):
                                    break
                                else:
                                    print('Id informado já foi usado em outra sala!')
                            else:
                                print('Só podem ser informados número, e que sejam maiores que 0')
                        while True:
                            capaccity = input('Informe a capacidade da sala: ')
                            capaccity = vali.digitsValidation(capaccity)
                            if(capaccity and capaccity > 9):
                                break
                            else:
                                print('Capacidade informada Invalida, precisa ser no mínimo 10')
                        occupationRoom = 0
                        boughtRoom = 0
                        room = dict()
                        room['roomName'] = nameRoom
                        room['idRoom'] = idRoom
                        room['capaccity'] = capaccity
                        room['controlIndex'] = {}
                        room['occupationRoom'] = occupationRoom
                        room['boughtRoom'] = boughtRoom

                        movieRooms.append(room)
                        print('Sala inserida com sucesso!')
                        input('')
                        break

                    elif(actionMenu == 2):
                        for rooms in movieRooms:
                            print(f'{rooms['roomName']} \nRoom Id: {rooms['idRoom']} \nCapacidade: {rooms['capaccity']}')
                            if(rooms['occupationRoom'] == 0):
                                print('Sala Livre')
                                print('-' * 25 ,'\n')
                            else:
                                print('Sala Ocupada!')
                                print('-' * 25 ,'\n')
                        
                        delRoom = input('Informe o id da sala que deseja deletar: ')
                        delRoom = vali.digitsValidation(delRoom)

                        if(delRoom):
                            validRoomDelete = False
                            indexRoom = 0
                            for rooms in movieRooms:
                                if(rooms['idRoom'] == delRoom):
                                    validRoomDelete = True
                                    del movieRooms[indexRoom]
                                    print('Sala deletada com sucesso!')
                                    input('')
                                    break
                                indexRoom += 1
                            if(not validRoomDelete):
                                print('Sala não encontrada')
                            if(validRoom):
                                break

                        else:
                            print('Id informado errado!')
                            input('')

                    elif(actionMenu == 3):    
                        for rooms in movieRooms:
                            print(f'{rooms['roomName']} \nRoom Id: {rooms['idRoom']} \nCapacidade: {rooms['capaccity']}')
                            if(rooms['occupationRoom'] == 0):
                                print('Sala Livre')
                                print('-' * 25 ,'\n')
                            else:
                                print('Sala Ocupada!')
                                print('-' * 25 ,'\n')
                        
                        attRoom = input('Informe o id da sala que deseja alterar a capacidade: ')
                        attRoom = vali.digitsValidation(attRoom)

                        if(attRoom):
                            validRoomCapaccity = False
                            indexRoom = 0
                            for rooms in movieRooms:
                                if(rooms['idRoom'] == attRoom):
                                    validRoomCapaccity = True
                                    newCapaccity = int(input('Digite a nova capacidade: '))
                                    rooms['capaccity'] = newCapaccity
                                    break
                                indexRoom += 1
                            if(not validRoomCapaccity):
                                print('Sala não encontrada')

                        else:
                            print('Id informado errado!')
                            input('')

        if(vali.digitsValidation(optionMenu) == 6):
            print('=*' * 25 )
            print('GESTÃO DE PAGAMENTOS'.center(50))
            print('=*' * 25 ,'\n')
            print('')

            name_arquiv = 'compras.txt'

            print('Escolha uma opção: \n[1] - Gerar arquivo de compras\n[2] - Exibir grafico \n[3] - Sair')
            
            selectMenu =input('Opção: ')

            selectMenu = vali.digitsValidation(selectMenu)

            if(selectMenu):
                if(selectMenu == 1):
                    with open(name_arquiv, 'w') as arquivo:
                        for user in users:
                            if(len(user['ticket']) < 1):
                                pass
                            else:
                                loopCount = 0
                                for info in user['ticket']:
                                    title = info['titleMovie']
                                    chair = info['chairBuy']
                                    priceChair = info['priceChair']
                                    if(loopCount == 0):
                                        arquivo.write(f'Usuario: {user['user']} \nFilme: {title}\nCadeira: {chair}\nValor Pago: {priceChair}')
                                    else:
                                        arquivo.write(f'\nUsuario: {user['user']} \nFilme: {title}\nCadeira: {chair}\nValor Pago: {priceChair}')
                                    loopCount += 1
                elif(selectMenu == 2):
                    chairs_count = {}

                    with open(name_arquiv, 'r') as arquivo:
                        lines = arquivo.readlines()

                        movieName = None

                        for line in lines:
                            line = line.strip()
                            
                            if line.startswith("Filme:"):
                                movieName = line.replace("Filme: ", "")
                                
                                if movieName not in chairs_count:
                                    chairs_count[movieName] = 0
                                    
                            elif line.startswith("Cadeira:"):
                                chairs_count[movieName] += 1
                        
                    moviesGrapich = list(chairs_count.keys())
                    chairGrapich = list(chairs_count.values())
                    plt.figure(figsize=(10, 6))
                    plt.bar(moviesGrapich, chairGrapich, color='skyblue')
                    plt.xlabel('Filmes')
                    plt.ylabel('Número de Cadeiras Vendidas')
                    plt.title('Número de Cadeiras Vendidas por Filme')
                    plt.xticks(rotation=45, ha='right')
                    plt.tight_layout()

                    plt.show()
                
                elif(selectMenu == 3):
                    break

            else:
                print('opção invalida!')
                break
        
        if(vali.digitsValidation(optionMenu) == 7):
            print('=*' * 25 )
            print('GESTÃO DE FEEDBACKS'.center(50))
            print('=*' * 25 ,'\n')
            print('')

            for movie in movies:
                print(f'Titule: {movie['title']}\nId do filme: {movie['movieId']}')

            viewComment = input('Informe o id de um dos filmes: ')
            
            viewComment = vali.digitsValidation(viewComment)

            if(viewComment):
                print('-- COMENTARIOS --')
                print('')
                for movie in movies:
                    if (movie['movieId'] == viewComment):
                        for comment in movie['comments']:
                            print(comment)
                            print('')
                        input('Pressione Enter para Sair!')
            else:
                print('Opção invalida!')
                break

def crudUser(userLogged, movies, movieRooms):

    while True:
        os.system('cls')
        print('=*' * 25 )
        print('THE WORST CINE'.center(50))
        print('---------------'.center(50))
        print('MENU ADMIN'.center(50))
        print('=*' * 25 , '\n')
        print(f'Cash: {round(userLogged['bank'],2)}\n')

        exitLoggedUser = False
        actionMenu = input('O que deseja fazer? \n[1] - Depositar Dinheiro \n[2] - Comprar Ingresso \n[3] - Avaliar Filme \n[0] - Deslogar \n\nOpção: ')

        actionMenu = vali.digitsValidation(actionMenu)

        if(actionMenu or actionMenu == 0):
            if(actionMenu == 0):
                exitLoggedUser = True
                break
            elif(actionMenu == 1):
                print('=*' * 25 )
                print('DEPOSITAR DINHEIRO'.center(50))
                print('=*' * 25 ,'\n')
                print('')

                while True:
                    cashDeposit = input('Digite o valor que deseja depositar: ')
                    cashDeposit = cashDeposit.replace(',','.')
                    cashDeposit = vali.digitsValidation(cashDeposit)
                    if(cashDeposit):
                        cash = float(userLogged['bank'])
                        userLogged['bank'] = cash + cashDeposit
                        print('Deposito realizado com Sucesso!')
                        break
                    else:
                        print('Valor informado Invalido!')
            elif(actionMenu == 2):
                print('=*' * 25 )
                print('COMPRAR INGRESSO'.center(50))
                print('=*' * 25 ,'\n')
                print('')    

                for movie in movies:
                    print('-- CATALAGO DE FILMES --')
                    print(f'Filme: {movie['title']}')
                    print(f'Id do filmes: {movie['movieId']}')
                    print(f'Preço do Ingresso: {movie['price']}')
                    print(f'Faixa etária: {movie['class']}')
                    print(f'Sala: {movie['room']}')
                    print(f'Horário: {movie['time'][0:2] + ':' + movie['time'][2:]}')
                    print('-------------------------------------')
                
                while True:
                    validIdSelectec = True
                    selectedMovie = input('Informe qual o id do filme que deseja comprar o ingresso ou digite "sair" para voltar: ')
                    
                    if(selectedMovie.lower() == 'sair'):
                        break
                    
                    selectedMovie = vali.digitsValidation(selectedMovie)

                    if(selectedMovie):
                        for movie in movies:
                            #Find the movie
                            if(movie['movieId'] == selectedMovie):
                                validIdSelectec = True
                                #find the room
                                for rooms in movieRooms:
                                    if(movie['room'] == rooms['roomName']):
                                        #create dict for the chairs
                                        while True:
                                            for indexNumber in range(rooms['capaccity']):
                                                rooms['controlIndex'][indexNumber] = indexNumber+1
                                            
                                            while True:
                                                print(f'Cash: {userLogged['bank']:.2f}')
                                                print('')
                                                for numberChair in rooms['controlIndex']:
                                                    if((numberChair+1) < 10 and ((numberChair+1) % 5 != 0) and rooms['controlIndex'][numberChair] != 'X'):
                                                        print(f'[0{numberChair + 1}] ', end="")
                                                    elif (((numberChair+1) % 5 == 0) and ((numberChair +1) < 10) and rooms['controlIndex'][numberChair] != 'X'):
                                                        print(f'[0{numberChair + 1}] \n')
                                                    elif ((numberChair+1) % 5 == 0 and rooms['controlIndex'][numberChair] != 'X'):
                                                        print(f'[{numberChair + 1}] \n')
                                                    elif (rooms['controlIndex'][numberChair] == 'X' and (numberChair+1) % 5 != 0):
                                                        print(f'[XX] ', end="")
                                                    elif (rooms['controlIndex'][numberChair] == 'X' and (numberChair+1) % 5 == 0):
                                                        print(f'[XX] \n')
                                                    else:
                                                        print(f'[{numberChair + 1}] ',end="")
                                                
                                                buyChair = input('Informe o número da cadeira que deseja comprar ou digite "sair": ')
                                                
                                                if(buyChair.lower() == 'sair'):
                                                    validIdSelectec = False
                                                    break

                                                buyChair = vali.digitsValidation(buyChair)

                                                if(buyChair):
                                                        if(userLogged['bank'] < movie['price']):
                                                            print('Dinheiro insuficiente para realizar compra!')
                                                            input()
                                                            break
                                                        elif(rooms['controlIndex'][buyChair-1] != 'X'):
                                                            dictOfTicket = dict()
                                                            dictOfTicket['titleMovie'] = movie['title']
                                                            dictOfTicket['chairBuy'] = buyChair
                                                            dictOfTicket['priceChair'] = movie['price']
                                                            userLogged['ticket'].append(dictOfTicket)
                                                            rooms['controlIndex'][buyChair-1] = 'X'
                                                            print('Cadeira comprada com sucesso!')
                                                            userLogged['bank'] = userLogged['bank'] - movie['price']
                                                            input('')
                                                        elif (rooms['controlIndex'][buyChair-1] == 'X'):
                                                            print('A cadeira informada já foi comprada!')
                                                            input('')
                                                else:
                                                    print('opção informada invalida!')
                                            
                                            if(not validIdSelectec):
                                                break
                                    if(not validIdSelectec):
                                        break
                                        
                                if(not validIdSelectec):
                                    break
                        if(not validIdSelectec and buyChair.lower() != 'sair'):
                            print('Id informado invalido!')
                            input('')
                            break
                        if(not validIdSelectec and buyChair.lower() == 'sair'):
                            break
                    else:
                        print('Opção informada invalida!')
            elif(actionMenu == 3):
                print('=*' * 25 )
                print('AVALIAR FILME'.center(50))
                print('=*' * 25 ,'\n')
                print('')

                print('-- LISTA DE FILMES --')
                for movie in movies:
                    print(f'Titulo: {movie['title']} \nId: {movie['movieId']}')
                
                commentIdMovie = input('Digite o Id do filme que deseja comentar ou "sair": ')

                if(commentIdMovie.lower() == 'sair'):
                    break

                commentIdMovie = vali.digitsValidation(commentIdMovie)
                if(commentIdMovie):
                    for movie in movies:
                        if(commentIdMovie == movie['movieId']):
                            comment = str(f'Usuário: {userLogged['user']}\nComment: ')
                            comment += input('Digite o seu comentario: ')
                            movie['comments'].append(comment)
                            print('Comentario Inserido com sucesso!')
                else:
                    print('Opção invalida!')
                    break
                            
                    

        else:
            print('Opção invalida!')

        if(exitLoggedUser):
            return

    
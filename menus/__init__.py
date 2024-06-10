import os
import validations as vali
import subMenus

def createMenu():
    os.system('cls')
    print("")
    print('=*' * 25 )
    print('THE WORST CINE'.center(50))
    print('---------------'.center(50))
    print('MENU INICIAL'.center(50))
    print('=*' * 25 , '\n')

    print('[1] - CATÁLOGO DE FILMES \n[2] - LOGIN \n[3] - CADASTRO \n[0] - SAIR\n')

    option = input('Opção: ')

    option = vali.digitsValidation(option)

    if (type(option) == int and (option <= 3 and option >= 0)):
        return option
    
    print('Opção informada Invalida!')
    input('Pressione qualquer tecla!')
    os.system('cls')

def catalogMovies(movies):
    while True:
        findMovie = False

        os.system('cls')
        print('=*' * 25 )
        print('CATÁLOGO DE FILMES'.center(50))
        print('=*' * 25 ,'\033[36m \n')
        print('--- Filmes Disponíveis ---\n')
        for movie in movies:
            print(f'Filme: {movie['title']} \nID: {movie['movieId']}')
            print('-'*25)

        selectDescription = input('Informe o filme que deseja mais informações: ')
        # Search for Id Movie
        if(vali.digitsValidation(selectDescription)):
            idMovie = int(selectDescription)
            for movie in movies:
                if (movie['movieId'] == idMovie):
                    print(f'Título do filme: {movie['title']} \nGênero do filme: {movie['genre']} \nClassificação: {movie['class']} \nSinopse do filme: {movie['sinopse']}\n')
                    findMovie = True
            #condittion to exit loop        
            if(findMovie):
                response = input("Deseja continuar vendo o catalago? [1]Sim [2]Não \nOpção: ")
                if (vali.digitsValidation(response)):
                    if(int(response) == 1):
                        os.system('cls')
                        return catalogMovies(movies)
                    elif(int(response) == 2):
                        print('Fechando catalago!')
                        break
                    else:
                        print('Opção invalida!')
                else:
                    print('Opção invalida!')

            if (not findMovie):
                print('Id informado Invalido!')
                input('')
        # Search for Name Movie
        else:
            if (selectDescription == 0):
                print('O filme informado é invalido!')
            else:
                for movie in movies:
                    if (movie['title'].lower() == selectDescription.lower()):
                        print(f'Título do filme: {movie['title']} \nGênero do filme: {movie['genre']} \nClassificação: {movie['class']} \nSinopse do filme: {movie['sinopse']}')
                        findMovie = True
                #condittion to exit loop        
                if(findMovie):
                    response = input("Deseja continuar vendo o catalago? [1]Sim [2]Não \nOpção: ")
                    if (vali.digitsValidation(response)):
                        if(int(response) == 1):
                            os.system('cls')
                            return catalogMovies(movies)
                        elif(int(response) == 2):
                            break
                        else:
                            print('Opção invalida!')
                    else:
                        print('Opção invalida!')

                if (not findMovie):
                    print('Titulo informado Invalido!')
                    input('')
    input('')

def loginMenu(users, movies, movieRooms):
    while True:
        os.system('cls')
        print('=*' * 25 )
        print('LOGIN'.center(50))
        print('=*' * 25 ,'\n')
        print('')
        print('Digite sair em usuário para sair!')
        print('')

        validUser = False
        username = input('Digite o usuário para login: ')
        #conditional to exit
        if (username.lower() == 'sair'):
            return
        
        for user in users:
            if (user['user'] == username):
                password = input('Digite a sua senha: ')

                #conditional to exit
                if (password.lower() == 'sair'):
                    return

                if (user['password'] == password):
                    print('Usuário logado com sucesso!')
                    validUser = True
                    if(user['id'] == 1):
                        #CRUD - ADMIN
                        subMenus.crudAdmin(user, movies, movieRooms, users)
                        return
                    else:
                        #CRUD - USER
                        subMenus.crudUser(user, movies, movieRooms)
                        return
        
        if(not validUser):
            print('Senha ou Usuário invalidos!')
            input('')
        
def registerUser(users):
    while True:
        os.system('cls')
        print('=*' * 25 )
        print('CADASTRO'.center(50))
        print('=*' * 25 ,'\n')
        print('')
        print('Digite sair em usuário para sair!')
        print('')

        registerLogin = input('Digite o nome de usuário para cadastro: ')

        if(registerLogin.lower() == 'sair'):
            return
        
        registerLogin = registerLogin.strip()
        if(registerLogin.isspace() or len(registerLogin) < 3):
            print('Tente um nome de usuário maior!')
            input('')
            os.system('cls')
        else:
            if (len(users) < 1):
                break
            elif (len(users) != 0):
                userValid = True
                for user in users:
                    if(user['user'] == registerLogin):
                        print('Nome de usuário já registrado!')
                        print('Insira um outro nome!')
                        userValid = False
                        input('')
                        os.system('cls')
                if(userValid):
                    break
    
    while True:
        passwordValid = True
        while True:
            firstPassword = input('Digite sua senha: ')

            if(firstPassword.lower() == 'sair'):
                return

            if(len(firstPassword) < 6) or (firstPassword.strip().isspace()):
                print('Senha com muitos espaços ou com menos de 6 caracteres')
            else:
                break
        
        while True:
            secondPassword = input('Digite a senha novamente: ')

            if(secondPassword.lower() == 'sair'):
                return

            if(firstPassword != secondPassword):
                print('As senhas não são iguais, tente novamente!')
            else:
                break


        if(passwordValid):
            break
    
    while True:
        
        age = input('Digite sua idade: ')

        if(age.lower() == 'sair'):
            return

        if(vali.ageValidation(age)):
            age = vali.ageValidation(age)
            break

        input('')
    
    while True:
        validEmail = True

        userEmail = str(input('Digite seu email: '))

        if(userEmail.lower() == 'sair'):
            return

        if(len(userEmail) < 4) or (userEmail.strip().isspace()):
            print('Email informado invalido!')
        else:
            if(len(users) < 1):
                if(userEmail[-4:] == ".com" and (userEmail.count("@") == 1)):
                    break
                else:
                    print('Email informado errado')
            else:
                for user in users:
                    if (userEmail == user['email']):
                        print('E-mail já registrado!')
                        print('Insira um outro e-mail.')
                        validEmail = False
                if(validEmail):
                    if(userEmail[-4:] == ".com" and (userEmail.count("@") == 1)):
                        break
                    else:
                        print('Email informado é invalido!')
    
    while True:
        id = 0

        checkAdmin = input('Informe o tipo do seu cadastro: [1] Admin [2] Admin \nOpção:')

        checkAdmin = vali.digitsValidation(checkAdmin)

        if(not checkAdmin):
            print('Opção informada invalida!')

        if(checkAdmin < 1 and checkAdmin > 2):
            print('Opção informada invalida!')
        else:
            if(checkAdmin == 1):
                print('Cadastro de Admin realizado com sucesso!')
                id = 1
                break
            else:
                print('Cadastro de usuário realizado com sucesso!')
                break
    
    user = dict()
    user['user'] = registerLogin
    user['password'] = firstPassword
    user['age'] = age
    user['email'] = userEmail
    user['id'] = id
    user['bank'] = 0
    user['ticket'] = []

    users.append(user)

    input()
    os.system('cls')
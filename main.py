import validations as vali
import menus


users = [
    {
    'user' : 'well',
    'password' : '123456',
    'age' : 18,
    'email' : 'wellington@gmail.com',
    'id' : 0,
    'bank' : 0,
    'ticket' : []
    },
    {
    'user' : 'wellAdm',
    'password' : '123456',
    'age' : 18,
    'email' : 'wellington@gmail.com',
    'id' : 1,
    'bank' : 0,
    'ticket' : []
    }
]

movieRooms = [{
    'roomName' : 'Sala A',
    'idRoom' : 1,
    'capaccity' : 40,
    'controlIndex' : {},
    'occupationRoom' : 1,
    'boughtRoom' : 0
},
{
    'roomName' : 'Sala B',
    'idRoom' : 2,
    'capaccity' : 30,
    'controlIndex' : {},
    'occupationRoom' : 1,
    'boughtRoom' : 0
}]

listOfMovies = [{
    'title' : 'A Hora do Rush (a procura da dupla)',
    'genre' : 'ação',
    'movieId' : 1,
    'sinopse' :'''Wellington, um habilidoso programador, se vê mergulhado no submundo do crime ao buscar seu amigo 
    desaparecido, Paris. Paris, um hacker talentoso, foi sequestrado por facções rivais após uma traição. 
    Em sua busca, Wellington usa suas habilidades para decifrar enigmas digitais e enfrentar inimigos 
    perigosos. Descobrindo uma conspiração maior, ele deve arriscar tudo para resgatar Paris e revelar a 
    verdade antes que seja tarde demais.''',
    'class' : 14,
    'dataRelease' : '01/12/2020',
    'duration' : 150,
    'price'  : 24.99,
    'room' : 'Sala B',
    'time' : '1200',
    'rating' : '99%',
    'comments' : list()
},{
    'title' : 'A Hora do Rush 2 (em dose dupla)',
    'genre' : 'ação',
    'movieId' : 2,
    'sinopse' :'''Wellington, um habilidoso programador, se vê mergulhado no submundo do crime ao buscar seu amigo 
    desaparecido, Paris. Paris, um hacker talentoso, foi sequestrado por facções rivais após uma traição. 
    Em sua busca, Wellington usa suas habilidades para decifrar enigmas digitais e enfrentar inimigos 
    perigosos. Descobrindo uma conspiração maior, ele deve arriscar tudo para resgatar Paris e revelar a 
    verdade antes que seja tarde demais.''',
    'class' : 14,
    'dataRelease' : '01/12/2020',
    'duration' : 150,
    'price'  : 24.99,
    'room' : 'Sala A',
    'time' : '1200',
    'rating' : '99%',
    'comments' : list()
}]


while True:
    response = menus.createMenu()

    if (response == 1):
        menus.catalogMovies(listOfMovies)
    elif (response == 2):
        menus.loginMenu(users, listOfMovies, movieRooms)
    elif (response == 3):
        menus.registerUser(users)
    elif (response == 0):
        break
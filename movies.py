def addMovie(title,release,genre):
   movies[title]=(release,genre)


def delMovie(title):
   del movies[title]


def showAllMovies():
    for film,infos in movies.items():
        print(f"movie:{film}, release year:{infos[0]}, genre:{infos[1]}\n")
        

###bonus
def showAllMoviesOrd():
    listo = list(movies.items())
    listo.sort()
    for film in listo:
        print(f"movie:{film[0]}, release year:{film[0][0]}, genre:{film[0][1]}\n")
    del listo
    
######
def sortMovies(m):
    sss = list(m.items())
    sss.sort()
    return dict(sss)
    

def searchMovie():
    
   resp = input('1-searching by name\n2-searching by release year \n')
   print(resp)
   if(resp == '1'):
      name = input("please enter the name... ")
      for title,info in movies.items():
        if(title==name):
            print('\ntitre: {}\ngenre: {}\nsorti en: {}'.format(title,info[1],info[0]))
            return
            
        
      print('introuvable')
        

   elif(resp == '2'):
      year = input('please enter the year... ')
      for title,info in movies.items():
        if(info[0]==int(year)):
            print('\ntitre: {}\ngenre: {}\nsorti en: {}'.format(title,info[1],info[0]))
            return
            

      print('introuvable')

   else: print('invalid')

    

           
    

if __name__ == '__main__':
   movies = {}
   loop=True
   # addMovie('ET',2000,'ufo')
   # addMovie('007',2000,'gun')
   # addMovie('Star wars',2000,'comic')
   # addMovie('Ave',2000,'comic')
   # addMovie('Indiana Jones',2000,'comic')
   # addMovie('Back to future',2000,'comic')
   # addMovie('Forest Gump',2001,'comic')
   while(loop):
      x = input('\n1. add a movie\n2. delete a movie\n3. search for a movie\n4. sort movies\n5. show all movies\n6. save on a file\n7. load from a file\nelse:quit\n')
      if(x=='1'):
         addMovie(input('\ntitle..'),int(input('\nyear..')),input('\ngenre..'))

      elif(x=='2'):
         delMovie(input('\ntitle..'))

      elif(x=='3'):
         searchMovie()  

      elif(x=='4'):
         movies=sortMovies(movies)

      elif(x=='5'):
         showAllMovies()

      elif(x=='6'):
         with open("movies.txt", "a") as file:
           for film,infos in movies.items():
             file.write(f"{film}:({infos[0]},{infos[1]})\n")

      elif(x=='7'):
         with open("movies.txt", "r") as file:
           for ligne in file:
              ligne.strip()
              if ligne:       
                 cle,valeur = ligne.split(':')
                 valeur=valeur.replace('(','').replace(')','') 
                 val1,val2=valeur.split(',')   
                 movies[cle]=(val1,val2)
                 
         #print(movies)        
      else: 
         loop=False


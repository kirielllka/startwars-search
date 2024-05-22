from app.APP_star import Searching

class Menu():
    def __init__(self):
        self.src = Searching()
    def main(self):
        while True:
            print('1.info about people\n2.info about planet\n3.info about film\n4.Exit')
            a = int(input('Enter choose:'))

            match a:
                case 1:
                    b = (input('enter name of people:'))
                    print('')
                    try:
                        print(self.src.personages(b),end='\n')
                    except IndexError:
                        print('incorrect name',end='\n')
                case 2:
                    b = (input('enter name of planet:'))
                    print('')
                    try:
                        print(self.src.planet(b),end='\n')
                    except IndexError:
                        print('incorrect name',end='\n')
                case 3:
                    b = (input('enter title of film:'))
                    print('')
                    try:
                        print(self.src.film(b),end='\n')
                    except IndexError:
                        print('incorrect title', end='\n')
                case 4:
                    print('your exit')
                    break

from typing import Dict, List
#import uuid
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
from texttable import Texttable
import pickle
class LibraryItem:
    def __init__(self, title: str, description: str, amount: int, genre: str, publication_year: int, language: str, borrowed_by: str, borrowed_date: dt, location: str):
        #self.GUID = None                            # Unik identifikator i biblioteket for å holde styr på duplikater, None ved initialisering
        self.title = title                          # Tittel på bok eller film
        self.description = description              # Beskrivelse på bok eller film
        self.amount = amount                        # Antall - Lagt til for fremtidig utvidelse av funksjon for å vise om en har flere av samme
        self.genre = genre                          # Sjanger på bok/film
        self.publication_year = publication_year    # Publiseringsår
        self.language = language
        self.borrowed_by = None                     # Utlånt av - Lagt til for fremtidig utvidelse av funksjonalitet.
        self.borrowed_date = None                   # Utlånsdato
        self.due_date = None                        # Dato for innleveringsfrist. Settes en måned frem i tid.
        self.location = location
        
    def is_borrowed(self):           # Returnerer false om boken ikke er lånt. Hvis den er lånt ut, returner dato for innlevering
        if self.due_date is None:
            return False
        else:
            return self.due_date
    
    def borrow_item(self) -> None:
        if self.due_date is None:
            todays_date = dt(year=dt.now().year, month=dt.now().month,day=dt.now().day)
            self.due_date = todays_date + relativedelta(months=1, days=1,seconds=-1) # Lever inn boken på slutten av dagen, en måned frem i tid
            print(f"Du låner nå {self.title}")
            print(f"Vennligste lever den tilbake innen: {self.due_date}")
        else:
            print("Denne er allerede lånt ut") 
            #TODO Mulighet for å legge inn noe error handling i stedet for en string? Hvordan blir implementasjonen senere?
            return #Returnere noe annet enn None?

    def return_item(self) -> None:
        if self.due_date is None:
            print("Denne var ikke lånt ut, sikker på at dette er den som skal returneres?")
            #TODO Mulighet for å legge inn noe error handling i stedet for en string? Hvordan blir implementasjonen senere?
        else:
            self.due_date = None
            return
        
class Book(LibraryItem):
    def __init__(self, title: str, description: str, amount: int, genre: str, publication_year: int, language: str, borrowed_by: str, borrowed_date: dt, location: str, author: str, isbn: str, pages: int):
        super().__init__(title, description, amount, genre, publication_year, language, borrowed_by, borrowed_date, location)
        self.author = author        # Forfatter av boken
        self.isbn = isbn            # ISBN referanse
        self.pages = pages          # Antall sider i boken
class Movie(LibraryItem):
    def __init__(self, title: str, description: str, amount: int, genre: str, publication_year: int, language: str, borrowed_by: str, borrowed_date: dt, location: str, director: str, id: str, length:str, IMDB_rating:float, subtitles:str):
        super().__init__(title, description, amount, genre, publication_year, language, borrowed_by, borrowed_date, location)
        self.director = director    # Direktør 
        self.id = id                # IMDB ID referanse
        self.length = length
        self.IMDB_rating = IMDB_rating
        self.subtitles = subtitles

class Library:
    def __init__(self):
        self.items: Dict[str, LibraryItem] = {}
        
    def add_item(self, item) -> None:
        item_key = define_library_key(item, " - ", True) # Legg til pretekst for å holde bok og film unik i keynavn i dictionaryen
        if item_key in self.items:
            print(f"Objekt er allerede i biblioteket: {item.title}")
        else:
            self.items[item_key] = item
        return
    
    def remove_item(self, item) -> None:
        item_key = define_library_key(item, " - ", True) # Hent aktuell key basert på klassen til item.
        if item_key in self.items:
            self.items.pop(item_key) # Fjern item_key fra biblioteket
        else:
            print(f"Kan ikke finne {item} i biblioteket")
        return
    
    def find_books(self,borrowed_status):
        if borrowed_status is True: # List opp kun bøker som er tilgjengelig for utlån
            books = [b for b in self.items.values() if (isinstance(b,Book)) & (b.due_date == None)] # Hent alle bøker i biblioteket ved å sjekke verdien til hver oppføring og match den opp mot klassen.
        else:
            books = [b for b in self.items.values() if (isinstance(b,Book))] # Hent alle bøker i biblioteket ved å sjekke verdien til hver oppføring og match den opp mot klassen.
        
        print("\nLister opp alle bøker:\n----------------------")
        if len(books) == 0:
            print("listen er tom")
            return False
        else:
            print_library_info(books)
            return books

    def find_movies(self,borrowed_status):
        if borrowed_status is True: # List opp kun filmer som er tilgjengelig for utlån
            movies = [m for m in self.items.values() if (isinstance(m,Movie)) & (m.due_date == None)] # Hent alle filmer i biblioteket ved å sjekke verdien til hver oppføring og match den opp mot klassen.
        else:
            movies = [m for m in self.items.values() if (isinstance(m,Movie))] # Hent alle filmer i biblioteket ved å sjekke verdien til hver oppføring og match den opp mot klassen.
        
        print("\nLister opp alle filmer:\n---------------------")
        if len(movies) == 0:
            print("listen er tom")
            return False
        else:
            print_library_info(movies)
            return movies
    
    def find_books_borrowed(self):
        books = [b for b in self.items.values() if (isinstance(b,Book)) and (b.due_date is not None)] # Hent alle utlånte bøker i biblioteket ved å sjekke verdien til hver oppføring og match den opp mot klassen.
        print("\nVelg en av bøkene nedenfor:")
        print("\nLister opp alle bøker:\n----------------------")
        if len(books) == 0:
            print("listen er tom")
            return False
        else:
            print("\nVelg en av bøkene nedenfor:")
            print("\nLister opp alle bøker som er utlånt:\n---------------------")
            print_library_info(books)
            return books

    def find_movies_borrowed(self):
        movies = [m for m in self.items.values() if (isinstance(m,Movie)) and (m.due_date is not None)] # Hent alle utlånte filmer i biblioteket ved å sjekke verdien til hver oppføring og match den opp mot klassen.
        if len(movies) == 0:
            print("listen er tom")
            return False
        else:
            print("\nVelg en av filmene nedenfor:")
            print("\nLister opp alle filmer som er utlånt:\n---------------------")
            print_library_info(movies)
            return movies
    
    def library_Statistics(self):
        print("Denne funksjonen er ikke definert enda")
        pass

    def search_for(self,searchstr:str):
        objects_found = [o for o in self.items.keys() if o.find(searchstr) > -1] # Søker i alle keys i biblioteket etter ønsket tekst. o.find() gir -1 hvis ingenting er funnet.
        print("\nfølgende ble funnet:\n---------------------")
        objects_list = []
        for o in objects_found:
            objects_list.append(self.items[o])
            #print(f"{i}. {o}:>5 {self.items[o].due_date}")
        print_library_info(objects_list)
        return objects_found

def print_library_info(library_list):

    t = Texttable()
    t.header(['Index', 'Tittel', 'Type', 'Beskrivelse', 'Lånestatus'])
    index = 0
    for item in  library_list:
        index += 1
        if item.is_borrowed() is not False:
            borrowed_status = "Utlånt"
        else:
            borrowed_status = "Ikke utlånt"
        t.add_row([index, item.title,define_library_key(item,"",False), item.description, borrowed_status])
    print(t.draw())


def define_library_key(item, suffix, Include_Title):
    """
    Oppsummering:
    Lager unikt navn for hver type klasse som skal inn i biblioteket.
    Hvis det er en bok så får du "Bok - <tittel på bok>".
    På denne måten unngår vi å få duplikater mellom bok og film.

    Argumenter:
        item (class): får inn klasse objekt med enten bok eller film.

    Returnerer:
        string: Returnerer definert oppsett for å matche key i biblioteket
                for å unngå duplikater mellom bok og film. 
    """
    title_to_include = item.title
    if not Include_Title:
        title_to_include=""
    match str(item.__class__.__name__): # Match klassen mot ønsket pretekst til key i dictionary til biblioteket
        case "Book":
            return "Bok" + suffix + title_to_include
        case "Movie":
            return "Film" + suffix + title_to_include

def add_book(library):
    title = input("Skriv inn tittelen på boken: ")
    description = input("Skriv inn en beskrivelse på boken: ")
    amount = 0 # Lagt til for fremtidig utvidelse
    genre = input("Skriv inn sjanger: ")
    publication_year = int(input("Skriv inn publiseringsår: "))
    language = input("Skriv inn tilgjengelig språk: ")
    borrowed_by = None # Kan vi fjerne denne og neste ved å bare definere den i klassen, men ikke hente inn input? skal kun settes ved lån i funksjoner.
    borrowed_date = None
    location = None # Lagt til for fremtidig utvidelse
    author = input("Skriv inn forfatter: ")
    isbn = input("Skriv inn isbn nummer: ")
    pages = int(input("Skriv inn antall sider: "))
    
    library.add_item(Book(title, description, amount, genre, publication_year, language, borrowed_by, borrowed_date, location, author, isbn, pages))

def add_movie(library):
    title = input("Skriv inn tittelen på filmen: ")
    description = input("Skriv inn en beskrivelse på filmen: ")
    amount = 0 # Lagt til for fremtidig utvidelse
    genre = input("Skriv inn sjanger: ")
    publication_year = int(input("Skriv inn publiseringsår: "))
    language = input("Skriv inn tilgjengelig språk: ")
    borrowed_by = None # Kan vi fjerne denne og neste ved å bare definere den i klassen, men ikke hente inn input? skal kun settes ved lån i funksjoner.
    borrowed_date = None
    location = None # Lagt til for fremtidig utvidelse
    director = input("Skriv inn direktør: ")
    length = input("Skriv inn spilletid som f.eks: 1h 52m : ")
    id = input("Skriv inn IMDB nummer: ")
    IMDB_rating = float(input("IMDB Rating (f.eks: 8.7): "))
    subtitles = input("Skriv inn tilgjengelig teksting: ")
    
    library.add_item(Movie(title, description, amount, genre, publication_year, language, borrowed_by, borrowed_date, location, director, id, length, IMDB_rating, subtitles))

def borrow_item(library):
    """
    Oppsummering:
    Funksjon for å låne en gjenstand fra biblioteket.
    Spørr først brukeren om hvilken type gjenstand som skal lånes (bok eller film)
    Deretter list opp tilgjengelige bøker med nummerering, hvis det er flere enn 10 alternativer
    spør brukeren om å søke etter tittel.
    Hent input fra brukeren for å finne gjenstanden og kall LibraryItem.borrow_item() funksjonen i klassen.

    """
    exit_requested = False
    global borrow_list
    while not exit_requested:
        try:
            print("\nMeny:")
            print("1. Lån en bok")
            print("2. Lån en film")
            print("0. Avslutt")
            
            choice = -99
            while choice not in range(0,3):
                choice = int(input("Velg et alternativ: ").strip())
                match choice:
                    case 1:
                        borrow_list = library.find_books(True) # Printer listen over bøker og returnerer listen. Verdi er false hvis listen er tom.
                        if borrow_list is False: # Returner hvis listen er tom
                            return
                    case 2:
                        borrow_list = library.find_movies(True) # Printer listen over filmer og returnerer listen. Verdi er false hvis listen er tom.
                        if borrow_list is False: # Returner hvis listen er tom
                            return
                    case 0:
                        print("Avslutter låning av bok…")
                        exit_requested = True
                        return
                    case _:
                        print("ikke ett gyldig valg, velg mellom 0, 1 eller 2")
            choice = int(input("Velg nummeret du vil låne eller 0 for å avbryte: ").strip())-1 # trekk ifra 1 fra valgt index da listen starter på 0 og index starter på 1.
            if borrow_list is not False:
                while choice not in range(-1,len(borrow_list)): # Valget må være mellom -1 og lengden til borrow_list. -1 er avbryt
                    choice = int(input("Velg nummeret du vil låne eller 0 for å avbryte: ").strip())-1 # trekk ifra 1 fra valgt index da listen starter på 0 og index starter på 1.
                # Bryt ut av loopen når valget er gyldig.
                if choice == -1: # Verdi -1 vil si bruker valgte 0, avbryt.
                    print("Låning er avbrutt")
                else:
                    try:
                        #choice = int(input("Velg nummeret du vil låne: ").strip())-1
                        borrowed_item = borrow_list[choice]
                        borrowed_item.borrow_item()
                    except IndexError as e:
                        print(f"[IndexFeil] {e}")
            else:
                exit_requested = True # Hvis listen er tom, avbryt
                return
        except ValueError as e:
            print(f"[Inputfeil] {e}")
    #TODO: Implementer søkefunksjon etter hva du skal låne. F.eks som alternativ 3. Søk etter bok, 4. Søk etter film

def return_item(library):
    """
    Oppsummering:
    Funksjon for å levere tilbake en gjenstand i biblioteket.
    Spørr først brukeren om hvilken type gjenstand som skal leveres tilbake (bok eller film)
    Deretter list opp tilgjengelige objekter med nummerering.
    Hent input fra brukeren for å finne gjenstanden og kall LibraryItem.return_item() funksjonen i klassen.
    """
    exit_requested = False
    global borrowed_list
    while not exit_requested:
        try:
            print("\nMeny:")
            print("1. Returner en bok")
            print("2. Returner en film")
            print("0. Avslutt")
            
            choice = -99
            while choice not in range(0,3):
                choice = int(input("Velg et alternativ: ").strip())
                match choice:
                    case 1:
                        borrowed_list = library.find_books_borrowed() # Printer listen over bøker og returnerer listen. Verdi er false hvis listen er tom.
                        if borrowed_list is False:
                            return
                        choice = int(input("Velg nummeret du vil levere tilbake eller 0 for å avbryte: ").strip())-1
                    case 2:
                        borrowed_list = library.find_movies_borrowed() # Printer listen over filmer og returnerer listen. Verdi er false hvis listen er tom.
                        if borrowed_list is False:
                            #print("Det er ingen tilgjengelige filmer")
                            return
                        choice = int(input("Velg nummeret du vil levere tilbake eller 0 for å avbryte: ").strip())-1
                    case 0:
                        print("Avslutter returnering av bok…")
                        exit_requested = True
                        return
                    case _:
                        print("ikke ett gyldig valg, velg mellom 0, 1 eller 2")
            if borrowed_list is not False:
                while choice not in range(-1,len(borrow_list)): # Valget må være mellom -1 og lengden til borrow_list. -1 er avbryt
                    choice = int(input("Velg nummeret du vil levere tilbake eller 0 for å avbryte: ").strip())-1
                # Bryt ut av loopen når valget er gyldig.
                if choice < 0:
                    print("Låning er avbrutt")
                else:
                    try:
                        #choice = int(input("Velg nummeret du vil levere tilbake: ").strip())-1
                        borrowed_item = borrowed_list[choice]
                        borrowed_item.return_item()
                    except IndexError as e:
                        print(f"[IndexFeil] {e}")    
            else:
                exit_requested = True # Hvis listen er tom, avbryt
                return

        except ValueError as e:
            print(f"[Inputfeil] {e}")
    #TODO: Implementer søkefunksjon etter hva du skal låne. F.eks som alternativ 3. Søk etter bok, 4. Søk etter film


def find_item(library):
    # Hent input fra brukeren, og søk etter tittel igjennom alle tilgjengelige gjenstander.
    # Legg med hvilken type gjenstand det er (bok/film/annet) i resultatet.
    print("\nHva vil du søke etter?")
    print("Hint: Start søket med <Bok - > eller <Film - >")

    exit_requested = False

    while not exit_requested:
        search_for = input("Søk her eller trykk enter for å gå tilbake: ")
        match search_for:
            case "":
                print("Går tilbake til hovedmeny")
                exit_requested=True
            case _:
                library.search_for(search_for)


def save_library(library):    
    """
    Hentet funksjonalitet fra stackoverflow.
    Enkel lagring av bibliotek til fil for å hente igjen etter programmet er stengt ned.
    """
    
    with open('library.pkl', 'wb') as f:
        pickle.dump(library, f)

def load_library(library):            
    """
    Hent bibliotek og last lever tilbake lastet bibliotek.
    """
    try: 
        with open('library.pkl', 'rb') as f:
            loaded_library = pickle.load(f)
            #loaded_library.find_books()
            #loaded_library.find_movies()
        return loaded_library
    except:
        print("Bibliotek er ikke lagret til fil enda")
        return library


def main():
    library = Library()
    library = load_library(library)

    exit_requested = False
    
    while not exit_requested:
        try:
            print("\nMeny:")
            print("1. Legg til bok")
            print("2. Legg til film")
            print("3. List tilgjengelige bøker")
            print("4. List tilgjengelige filmer")
            print("5. Lån gjenstand")
            print("6. Returner gjenstand")
            print("7. Finn gjenstand")
            print("0. Avslutt")

            choice = input("Velg et alternativ: ").strip()
            match choice:
                case "1":
                    add_book(library)
                case "2":
                    add_movie(library)
                case "3":
                    library.find_books(False)
                case "4":
                    library.find_movies(False)
                case "5":
                    borrow_item(library)
                case "6":
                    return_item(library)
                case "7":
                    find_item(library)
                case "0":
                    print("Avslutter og lagrer bibliotek til fil…")
                    save_library(library)
                    exit_requested = True
                case _:
                    print("Ugyldig valg.")
        except ValueError as e:
            print(f"[Inputfeil] {e}")
            
if __name__ == "__main__":
    main()
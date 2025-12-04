from typing import Dict, List
import uuid
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

class LibraryItem:
    def __init__(self, GUID: str, title: str, description: str, amount: int, genre: str, publication_year: int, language: str, borrowed_by: str, borrowed_date: dt, location: str):
        self.GUID = None                            # Unik identifikator i biblioteket for å holde styr på duplikater, None ved initialisering
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
            print(todays_date)
            self.due_date = todays_date + relativedelta(months=1, days=1) # Dagens dato klokken 00:00 pluss en dag = en måned frem i tid. Boken må være inne innen stengetid dagen før
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
    def __init__(self, title: str, author: str, isbn: str, pages: int):
        super().__init__(title)
        self.author = author        # Forfatter av boken
        self.isbn = isbn            # ISBN referanse
        self.pages = pages          # Antall sider i boken
class Movie(LibraryItem):
    def __init__(self, title: str, director: str, id: str, length:str, IMDB_rating:float, subtitles:str):
        super().__init__(title)
        self.director = director    # Direktør
        self.id = id                # IMDB ID referanse
        self.length = length
        self.IMDB_rating = IMDB_rating
        self.subtitles = subtitles
        
class Library:
    def __init__(self):
        self.items: Dict[str, LibraryItem] = {}
        
    def add_item(self, item) -> None:
        #TODO: Legg til gjenstanden i biblioteket. Hva skjer hvis det finnes en duplikat?
        pass
    
    def remove_item(self, GUID) -> None:
        # 
        #TODO: Fjern gjenstanden fra biblioteket
        pass
    
    #TODO: Lag to nye metoder for å finne lister med tilgjengelige bøker og filmer.
    
    """
    # list comprehensions
    electronics = [p for p in Produkter if isinstance(p, Electronics)]
    clothing = [p for p in Produkter if isinstance(p, Clothing)]

    #print all elektronikk:
    print("printer alle elektronikk produkter:")
    for produkt in electronics:
        print(produkt.get_info())

    #print all clothing:
    print("\nPrint alle klær produkter:")
    for clothes in clothing:
        print(clothes.get_info())
    """
    
def add_book(library):
    #TODO: Implementer funksjonen for å legge til en bok.
    # Hent input fra brukeren og kall library.add_item()
    print("Add book ikke implementert")

def add_movie(library):
    #TODO: Implementer funksjonen for å legge til en film.
    # Hent input fra brukeren og kall library.add_item()
    print("Add movie ikke implementert")

def borrow_item(library):
    #TODO: Implementer funksjonen for å låne en gjenstand.
    # Hent input fra brukeren for å finne gjenstanden og kall library_item.borrow_item()
    print("Borrow item ikke implementert")
    
def return_item(library):
    #TODO: Implementer funksjonen for å returnere en gjenstand.
    # Hent input fra brukeren for å finne gjenstanden og kall library_item.return_item()
    print("Return item ikke implementert")

def find_item(library):
    #TODO: Implementer funksjonen for å finne en gjenstand i biblioteket.
    # Hent input fra brukeren, og søk etter tittel igjennom alle tilgjengelige gjenstander.
    # Legg med hvilken type gjenstand det er (bok/film/annet) i resultatet.
    print("Find item ikke implementert")

def main():
    #Lag et bibliotek
    library = Library()
    """
    Produkter = []
    Produkter.append(Electronics("Datamaskin","ZBook G14 Fury",15000,10,12))
    Produkter.append(Electronics("Hodetelefoner","Senheiser xx",2000,5,12))
    Produkter.append(Clothing("Genser","Marius genser",600,100,"M"))
    """
    
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
            
            if choice == "1":
                add_book(library)
            elif choice == "2":
                add_movie(library)
            elif choice == "3":
                #list_available_books(library)
                #TODO: Implementer funksjonen for å liste tilgjengelige bøker
                pass
            elif choice == "4":
                #list_available_movies(library)
                #TODO: Implementer funksjonen for å liste tilgjengelige filmer
                pass
            elif choice == "5":
                borrow_item(library)
            elif choice == "6":
                return_item(library)
            elif choice == "7":
                find_item(library)
            elif choice == "0":
                print("Avslutter…")
                exit_requested = True
            else:
                print("Ugyldig valg.")
        except ValueError as e:
            print(f"[Inputfeil] {e}")
            
if __name__ == "__main__":
    main()
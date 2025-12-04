from typing import Dict, List

class LibraryItem:
    def __init__(self, title: str):
        self.title = title
        
        # Bestem dato for når den skal leveres tilbake
        # Nå + en måned senere?
        self.due_date = None
        
    def is_borrowed(self) -> bool:
        #TODO: Sjekk om gjenstanden er utlånt
        pass
    
    def borrow_item(self) -> None:
        #TODO: Merk gjenstanden som utlånt
        pass
        
    def return_item(self) -> None:
        #TODO: Merk gjenstanden som returnert
        pass
        
class Book(LibraryItem):
    def __init__(self, title: str, author: str, isbn: str):
        super().__init__(title)
        self.author = author
        self.isbn = isbn
        
class Movie(LibraryItem):
    def __init__(self, title: str, director: str, id: str):
        super().__init__(title)
        self.director = director
        self.id = id
        # f.eks. IMDB ID
        
        
class Library:
    def __init__(self):
        self.items: Dict[str, LibraryItem] = {}
        
    def add_item(self, item) -> None:
        #TODO: Legg til gjenstanden i biblioteket. Hva skjer hvis det finnes en duplikat?
        pass
    
    def remove_item(self, title) -> None:
        #TODO: Fjern gjenstanden fra biblioteket
        pass
    
    #TODO: Lag to nye metoder for å finne lister med tilgjengelige bøker og filmer.
    
    
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
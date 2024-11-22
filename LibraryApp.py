from src.storage import JSONPersistence
from src.library import Library
from src.cli import LibraryCLI

if __name__ == "__main__":
    persistence = JSONPersistence()
    library = Library(persistence)
    cli = LibraryCLI(library)
    cli.run()

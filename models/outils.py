import os
import time

class Outils:
    """Classe utilitaire contenant des méthodes statiques."""

    @staticmethod
    def clear_console():
        """Efface la console selon le système d'exploitation."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def pause(seconde):
        """Met le programme en pause pendant X secondes."""
        time.sleep(seconde)

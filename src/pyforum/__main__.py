# Le fichier __main__.py est utilisé comme point de départ pour exécuter le
# programme. Il importe la fonction main() du module mvp et l'exécute.
#
# Cela permet, une fois votre paquet (package) installé avec pip, d'exécuter le programme
# en utilisant la commande : python -m pyforum.
#
# Cela permet également d'importer la fonction main() dans d'autres modules
# sans exécuter le programme.

from pyforum.mvp import main

if __name__ == '__main__':
    main()

'''
But : Bloquer la connexion des appareils connectés sur un routeur alors qu'on a pas accès au routeur lui-même
Solution : Utiliser l'ARP Poisoning

Cf : evillimiter

Etape 1
Trouver les hosts : Lister les appareils connectés sur le routeur

Etape 2
Comparer les hosts trouvés avec un whitelist des adresse MAC des appareils autorisés

Etape 3
Bloquer les appareils qui ne sont pas dans le whitelist
Stoquer la liste des appareils bloqués (blacklist) Adresse MAC : IP

Etape 4
Si déjà bloqué, autorisé les appareils dans le whitelist

Etape 5
Automatiser le processus de Etape 1 à 4

Etape 6
Ajouter une interface web et une base des données

'''

#Etape 1: Lister les appareils connectés (host)




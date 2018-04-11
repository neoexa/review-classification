# Pour utiliser Git sur son PC
## En gros
Récupérer toutes les sources sur son PC pour pouvoir bosser dessus :
(commande à exécuter dans le répertoire où l'on veut récupérer le projet)  
```git clone https://github.com/neoexa/review-classification.git```

Signaler des modifications et les enregistrer dans ```commit``` :  
* Signaler un fichier modifié : ```git add unFichierDonné``` ;
* Pour ne pas s'embêter, signalé tout fichier modifié depuis dernière modification : ```git add -A``` (bien plus pratique quand même !) ;
* ```git commit -m "Message pour décrire brièvement la modification"```.

Envoyer les modifs sur github pour que tout le monde puisse y accéder :  
````git push```

Récupérer les modifs des autres depuis github (à faire genre à chaque fois avant de coder, comme ça tout est à jour :p) :  
````git pull```

## Et sinon
Magnifique tutoriel : http://rogerdudler.github.io/git-guide/
Mais ce que j'ai mis au dessus ça devrait suffir :)

## Authentification
C'est assez chiant, par défaut, aucune donnée d'authentification n'est sauvée, donc il faut se re-taper mot de passe nom d'utilisateur à chaque opération de synchronisation.

Pour changer ça :
* Sous Windows : http://gitcredentialstore.codeplex.com/, normalement après exécution, ça sauvegarde les mots de passe ;
* Sous Linux : http://stackoverflow.com/questions/5343068/is-there-a-way-to-skip-password-typing-when-using-https-github
* Sous MacOS, même lien qu'au dessus



Voilà, normalement ça devrait le faire :-)
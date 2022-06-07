# README Apprentissage Machine

## Capture d écran de la trajectoire
![imagecapture](C:\Users\assi.karim\PycharmProjects\TestROS\doc\Capture.PNG)


## Explication de la trajectoire:
``` bash
La trajectoire de la tortue s explique par le suivant: elle avance jusqu à ce qu'elle
arrive devant un obstacle. Elle cogne l'obstacle (donc le mur), et va changer de trajectoire
en tournant à gauche puis va avancer de nouveau.
Elle va répeter cette paterne jusqu à la réalisation d un tour complet de l'environnement.

Donc l'action 0 avance en continue, au contact du mur, on recoit un outcome qui indique la présence
de l'obstacle. Cela va donc activer l action 1 pour faire tourner le robot à gauche et réavancer.
````

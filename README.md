# Projet_11_oc

## Déployez votre application sur un serveur comme un pro !

Jusqu’à maintenant, vous avez déployé vos applications en utilisant Heroku. C’est bien ! Mais la plupart des sociétés n’utilisent pas Heroku, pas par mépris pour cette belle entreprise mais plutôt car elles préfèrent gérer elles-mêmes leur déploiement.

Il s’agit d’une étape très importante dans la vie d’un projet ! Allez, c’est parti !

## Liens:

- Lien Github: https://github.com/jerem33620/projet-10-jeremyg.git
- Lien Trello: https://trello.com/b/sy9YBmdr/projet-10 
- Lien Production: 206.189.117.65

## Étapes:

### Simuler un serveur de production en local

Avant de mettre en ligne un projet, il est de bon ton de lancer un serveur en local pour s’assurer que tout se passe bien.

### Déploiement

Tous vos tests sont verts et le build fonctionne ? Parfait ! Maintenant, déployez votre application en utilisant l’hébergeur que vous souhaitez. Vous devez configurer le serveur et effectuer un déploiement en ligne de console. N’utilisez pas Heroku ;-)

### Monitoring

Votre application est en ligne. Bravo ! Mais que se passe-t-il si le serveur tombe en panne ? Utilisez Sentry pour lire tous les logs et NewRelic pour surveiller le bon fonctionnement de votre application.

### Automatisations

Créez une tâche Cron qui mettra à jour les éléments récupérés d’Open Food Facts une fois par semaine.

### Nom de domaine

Dernière étape (optionnelle) ! Achetez un nom de domaine et reliez-le à vos serveurs.

## Livrables:

- Document écrit expliquant votre démarche de création, les difficultés rencontrées et la manière dont vous les avez résolues. Incluez-y le lien vers votre board Trello ou Pivotal Tracker le cas échéant.  Le document doit être en format pdf et ne pas excéder 2 pages A4. Il peut être rédigé en anglais ou en français, au choix, mais prenez bien en considération que les fautes d’orthographe et de grammaire seront évaluées !
- Copie d’écran des configurations de Travis, de l'hébergeur et de votre tâche Cron !
- Lien vers votre projet “déployé”, même s’il ne s’agit que de l’adresse IP de votre serveur !

## Tests:

Pour lancer votre tests vous devrez utiliser les lignes de code suivante:

```
- $ coverage run --source=. manage.py test
- $ coverage report
```

ou sinon:

```
- $ python manage.py test
```

## Pour lancer en local il vous faudra cloner puis utiliser ces commandes:

```
- $ git clone https://github.com/jerem33620/projet-10-jeremyg.git
- $ pip install pipenv
- $ pipenv install -dev
- $ pipenv shell
- $ python manage.py runserver
```

Ou si vous voulez utiliser le site de production, utiliser un moteur de recherche,
avec ces chiffres : 206.189.117.65

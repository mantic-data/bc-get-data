# Business Case : Get Data

L'objectif de ce business case est de recréer un `get_data` light.
Un endpoint prend un payload qui doit contenir au moins une métrique, et peut contenir plusieurs groupements et filtres.
Ce même endpoint doit convertir ce payload en requête SQL, et requêter la base SQLite fournis, puis renvoyer le résultat sérialisé.

## Départ

Ce template fournis la base permettant de developper ce projet. Il utilise Flask pour l'API, SQLAlchemy pour l'ORM et `uv` pour les dépendances.

Pour installer les dépendances et lancer le projet, tout ce fait via `uv` :
```
$ uv sync
$ uv run
```

Le template contient déjà un exemple de endpoint, un modèle correspondant a une table dans la base SQLite, et une requête SQLAlchemy.
Cela illustre tout les fonctionnalités des dépendances nécessaire pour la completion de cet exercice.
Il n'est donc pas nécessaire (mais ce n'est pas découragé) de lire la documentation de Flask ou SQLAlchemy pour résoudre cet exercice.

## IA/LLM

Vous pouvez utiliser tout les outils que vous souhaitez pour résoudre cet exercice, à l'exception du recours à une personne tierce.
Il n'y a pas d'obligation d'utiliser un outil basé sur les LLMs.

# Étapes

## Étape 1 : Requêter une métrique

Votre endpoint doit pouvoir recevoir un payload JSON de la forme :
```
{"metric": "table.column", "aggregation": "sum"|"avg"|"list"}
```

La `metric` est toujours sous la forme `table.column` et décrit quel table et colonne de cette table il faut requêter.

L'`aggregation` est toujours une des valeurs suivantes : "sum", "avg" ou "list". Elle représente l'aggregation a effectuer sur la métrique. "list" est l'absence d'aggregation: c'est à dire qu'on renvoie simplement la liste des objets.

Depuis ce payload, votre endpoint doit requêter la table et colonne désigné avec l'aggregation choisi, puis renvoyer le résultat en JSON.

A titre d'exemple, le payload :
```
{"metric": "facture.montant", "aggregation": "sum"}
```

Devrait renvoyer :
```
TODO
```

## Étape 2 : Filtre

Dans cette étape, on veut pouvoir ajouter des filtres.
Pour le moment, nous supposerons que ces filtres doivent être sur la même table, mais pas nécessésairement sur la même colonne, que la métrique.
Nous considérons aussi qu'on ne pourra filtrer que sur des nombres (entier ou flottant) et des strings.

Les filtres accepté pour les nombres sont les suivants :
- Strictement supérieur, opérateur `>`
- Strictement inférieur, opérateur `<`
- Égal, opérateur `=`

Pour les strings :
- Contient (sans casse), opérateur `in`
- Ne contient pas (sans casse), opérateur `notin`

On peut avoir plusieurs filtres.

Un exemple de payload attendu deviens :
```
{
  "metric": "facture.montant",
  "aggregation": "sum",
  "filters": [
    {"on": "facture.montant", "op": "<", "value": "100.00"},
    {"on": "facture.type", "op": "in", "value": "fourniture"}
  ]
}
```

Le résultat attendu est :
```
TODO
```

## Étape 3 : Groupement simple

On veut désormais pouvoir grouper nos données, en fonction des valeurs d'une autre colonne dans notre table.
On peut avoir plusieurs groupement.
Un groupement est simplement défini par la table et la colonne sur laquelle groupé, sous la forme `table.colonne`.

Un exemple de payload attendu est :
```
{
  "metric": "facture.montant",
  "aggregation": "sum",
  "filters": [
    {"on": "facture.montant", "op": ">", "value": "30.00"},
  ]
  "group_by": [
    "facture.type",
    "facture.service"
  ]
}
```

Et devrait renvoyer :
```
TODO
```

## Étape Bonus 1 : Groupements et filtres sur d'autres tables

Nous aimerions pouvoir désormais grouper et filtrer sur des tables autres que celle de la métriques.
Il faut toutefois que le filtre ou le groupement soit sur une table qui ait une relation directe (clef étrangère) avec la table de la métrique.

Un exemple de payload attendu :
```
{
  "metric": "facture.montant",
  "aggregation": "sum",
  "filters": [
    {"on": "service.name", "op": "in", "value": "tech"},
  ]
  "group_by": [
    "client.name"
  ]
}
```

Et devrait renvoyer :
```
TODO
```

## Étape Bonus 2 : Multi-métrique

On veut pouvoir désormais requêter sur un ensemble de métrique d'un coup.
Les mêmes filtres et groupement s'appliquent.

Un exemple de payload attendu :
```
TODO
```

Et devrait renvoyer :
```
TODO
```

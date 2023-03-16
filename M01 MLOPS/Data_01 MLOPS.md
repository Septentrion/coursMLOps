# MLOps

## Introduction

`MLOps` fait référence à une approche dans laquelle une combinaison de `DevOps` et de génie logiciel est exploitée afin de permettre le déploiement et la maintenance de modèles d'apprentisage automatique en production de manière fiable et efficace. De nombreuses informations peuvent être trouvées en ligne pour discuter des tenants et aboutissants conceptuels de `MLOps`. Nous verrons donc ici la mise en œuvre d'un cadre `MLOps` avec des outils open source.

## Phasage

Comme dans toutes les méthodes d'amélioration continue, `MLOps` se décompose en grandes phases. Ici, nous pouvons distinguer :

1. Une phase de **design**
  - Nous devons tout d'abord comme dans tout projet, prendre connaissance des **exigences**, fonctionnelles ou autres. Cela peut être :
    - être capable de fonctionner sur un Raspberry Pi
    - pouvoir soutenir un grand nombre de requêtes simultanées
    - comprendre différentes langues
    - etc.
  - Nous devons établir les cas d'utilisation de notre système, mais aussi les cas d'utilisation du processus de gestion des données
  - Nous devons mesurer le degré de disponibilité des données
    - Quelles sont les sources ?
    - Quels sont les formats ?
    - Sont-elles libres ?
    - etc.
  - Comme dans `DataOps`, nous devons sonstituer une équipe car c'est un travail fondamentalement plurisisciplinaire
    - Des ingénieurs système & réseau (voir cloud)
    - Des scientifiques de données
    - Des représentants du domaine de connaissance exploré
    - Des juristes et des éthiciens
  - Nous devons ensuite concevoir une architecture pour tirer des enseignements utiles de l'apprentissage
    - Ici, nous pouvons avoir recours à des méthodes d'affinage (ou « _tuning_ ») pour accélerer la phase de conception

  2. Une phase de **développement**
    - Nous devons tout d'abord préparer les données, c'est-à-dire :
      - Vérifier que les données ont un niveau de qualité suffisant
      - Normaliser les données pour éviter les artefacts lors de l'analyse
    - Nous devons implémenter l'architecture choisie
      - Et l'entraîner avec un jeu de données représentatif de ceux identifés précédemment
    - Nous devons enfin tester et valider le modèle
      - Pratiquer des tests unitaires sur le code du modèle
      - Utiliser des estimateurs mathématiques pour évaluer la précisions
      - Valide le modèle en lui soumettant des jeux d'exemples calibrés

  3. Une phase « **opératoire** »
    - Nous devons déployer le modèle sur une infrasructure déterminée
    - Nous devons ensuite automatiser les « pipelines » de données
      - c'est-à-dire mettre en œuvre un processus ETL
    - Enfin, nous devons surveiller le fonctionnement du système
      - Mettre en œuvre des indicateurs pour se conformer aux exigences (non fonctionnelles notamment)
      - Vérifier les problèmes d'utilisation des données
      - Vérifier les conformités légales

  4. Une phase d'**évaluation**
    - A partir des indicateurs (ou de l'évolution des exigences), nous devons décider de modifications pour améliorer le fonctionnement du système. Cela peut être :
      - Intégrer de nouvelles sources de données
      - Modifier les hyperparamètres du modèle
      - Continuer à entraîner le modèle de manière itérative
      - Envisager un nouveau modèle
      - Modifier l'architecture du système
      - etc.

## Eléments importants d'une démarche MLOps

Quels sont les différents points à intégrer dans une démarche `MLOps` ?

1. **Plateforme de développement** : une plate-forme collaborative pour permettre la construction de modèle par des « _scientifiques de données_ » devrait être considérée comme faisant partie du cadre `MLOps`. Cette plate-forme devrait permettre un accès sécurisé aux sources de données (par exemple, à partir des flux de travail d'ingénierie des données). Nous voulons que la chaîne depuis la phase d'entraînement jusqu'au déploiement soit aussi fluide que possible.
2. **Tests unitaires du modèle** : chaque fois que nous créons, modifions ou recyclons un modèle, nous devons automatiquement valider l'intégrité du modèle, par ex.
  - il doit répondre à des performances minimales sur un jeu de tests
  - il devrait bien fonctionner sur les ensembles de données spécifiques au cas d'utilisation synthétique
3. **Versionnage**: il devrait être possible de remonter le temps pour inspecter tout ce qui concerne un modèle donné, par exemple, quelles données et quel code ont été utilisés ?  Pourquoi? Si quelque chose se casse, nous devons pouvoir être en mesure le localiser la cause du problème.
4. **Registre des modèles** : il devrait y avoir un aperçu des modèles déployés (et aussi déclassés), de leur historique de version et de l'étape de déploiement de chaque version. Pourquoi? Si quelque chose se casse, nous pouvons remettre une version précédemment archivée en production.
5. **Gouvernance du modèle** : seules certaines personnes devraient avoir accès à la procédure d'entraînement liée à un modèle donné. Il devrait y avoir un contrôle d'accès pour qui peut demander / rejeter / approuver des transitions entre les étapes de déploiement ( par exemple, dev pour tester la prod ) dans le registre des modèles.
6. **Déploiement** : le déploiement peut être beaucoup de choses, mais noous considérerons ici le cas où nous voulons déployer un modèle vers une infrastructure « _Cloud_ » et exposer une API, ce qui permet à d'autres personnes de consommer et d'utiliser le modèle, c'est-à-dire que je ne considère pas les cas où nous voudrions déployer des modèles embarqués. Des déploiements de modèles efficaces sur les infrastructures appropriées devraient:
  - prendre en charge plusieurs frameworks d'apprentissage automatique + modèles personnalisés
  - adopter une spécification d'API bien définie (par exemple, Swagger / OpenAPI)
  - prendre en charge les serveurs de modèles conteneurisés
7. **Surveillance** : le suivi des mesures de performance (throughput, uptime, etc. ) est un élement très important. Si soudainement un modèle commence à renvoyer des erreurs ou à être étonnamment lent, nous devons le savoir, avant que l'utilisateur final ne se plaigne, afin que nous puissions le réparer.
8. **Retour d'information** : nous devons transmettre des informations au modèle sur ses performances. En règle générale, nous exécutons des prévisions sur de nouveaux échantillons où nous ne connaissons pas encore la vérité fondamentale. Cependant, à mesure que nous apprenons la vérité, nous devons informer le modèle pour rendre compte de son efficacité.
9. **Tests A/B**: peu importe la solide validation croisée que nous pensons faire, nous ne savons jamais comment le modèle fonctionnera tant qu'il ne sera pas réellement déployé. Il devrait être facile d'effectuer des tests A/B avec des modèles en direct dans le cadre `MLOps`.
10. **Détection de dérive** : généralement, plus un modèle donné est déployé longtemps, moins il est pertinent du fait des changements contextuels depuis le moment où le modèle a été entraîné. Nous pouvons essayer de surveiller et d'alerter sur ces différentes circonstances, ou « dérive » avant qu'elles ne deviennent trop sévères:
  - Dérive conceptuelle: lorsque la relation entre l'entrée et la sortie a changé
  - Dérive de prédiction: changements dans les prévisions, mais le modèle tient toujours
  - Dérive d'étiquettes: modification des résultats du modèle par rapport aux données de formation
  - Dérive des fonctionnalités: modification de la distribution des données d'entrée du modèle
11. **Détection de valeur aberrante** : si un modèle déployé reçoit un échantillon d'entrée qui est significativement différent de tout ce qui a été observé pendant l'entraînement, nous pouvons essayer d'identifier cet échantillon comme une valeur aberrante potentielle, et la prédiction renvoyée doit être marquée comme telle, indiquant à l'utilisateur final qu'il doit faire attention à la prédiction.
12.**Détection d'attaques adverses** : nous devons être avertis lorsque des échantillons contradictoires/aberrants sont fournis à nos modèles (par exemple, quelqu'un essayant de manipuler le résultat de nos algorithmes ).
13. **Interprétabilité** : le déploiement de modèles doit comprendre des points d'entrée (_endpoints_) permettant l'explication des conclusions, par exemple via un algorithme comme SHAP. Pour de nombreux cas d'utilisation, une prédiction ne suffit pas et l'utilisateur final doit savoir pourquoi une prédiction donnée a été faite.
14. **Gouvernance des déploiements**: nous avons non seulement besoin de restrictions d'accès sur qui peut voir les données, les modèles entraînés, etc., mais aussi sur qui peut éventuellement utiliser les modèles déployés. Ceux-ci peuvent souvent être aussi confidentiels que les données sur lesquelles ils ont été entraînés.
15. **Centricité des données** : plutôt que de se concentrer sur les performances et les améliorations du modèle, il est logique qu'un cadre `MLOps` permette de se concentrer davantage sur la façon dont l'utilisateur final peut améliorer la qualité et l'étendue des données.

Bien sûr, les principes ci-dessus s'ajoutent aux meilleures pratiques normales pour les `DevOps` et le génie logiciel en termes d'infrastructure comme... la qualité du code, la documentation, les tests unitaires, CI/CD, etc. 

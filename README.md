<<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>SoftDesk-API</h1>
	<p>
		SoftDesk, une soci�t� d'�dition de logiciels de d�veloppement et de collaboration, a d�cid� de publier une application permettant de remonter et suivre des probl�mes techniques (issue tracking system). Cette solution s�adresse � des entreprises clientes, en B2B
	</p>
	<h2>Installtion</h2>
	<p>
		1.Clonez le repository en utilisant <mark>git clone</mark>
		2.Se d�placer dans le r�pertoire racine SoftDesk en utilisant la commande <mark>cd softDesk</mark>
		3.Cr�er un environnement virtuel pour le projet avec la commande <mark>python -m venv env</mark>
		4.Activez l'environnement virtuel avec la commande <mark>env\Scripts\activate.bat</mark>
		5.Installez les d�pendances du project avec la commande <mark>pip install -r requirements.txt</mark>
	</p>
	<h3>Documentation et d�tails d'utilisation des endpoints de l'API</h3>
	<p>
		Une fois le serveur lanc�, lisez le document  suivant avant de faire vos premi�res requetes � l'API.<br><br>

		Point de terminaison d'API

		M�thode HTTP
		URI
		Inscription de l'utilisateur
		POST
		/signup/
		Connexion de l'utilisateur
		POST
		/login/
		R�cup�rer la liste de tous les projets (projects) rattach�s � l'utilisateur (user) connect�
		GET
		/projects/
		Cr�er un projet
		POST
		/projects/
		R�cup�rer les d�tails d'un projet (project) via son id
		GET
		/projects/{id}/
		Mettre � jour un projet
		PUT
		/projects/{id}/
		Supprimer un projet et ses probl�mes
		DELETE
		/projects/{id}/
		Ajouter un utilisateur (collaborateur) � un projet
		POST
		/projects/{id}/users/
		R�cup�rer la liste de tous les utilisateurs (users) attach�s � un projet (project)
		GET
		/projects/{id}/users/
		Supprimer un utilisateur d'un projet
		DELETE
		/projects/{id}/users/{id}
		R�cup�rer la liste des probl�mes (issues) li�s � un projet (project)
		GET
		/projects/{id}/issues/
		Cr�er un probl�me dans un projet
		POST
		/projects/{id}/issues/
		Mettre � jour un probl�me dans un projet
		PUT
		/projects/{id}/issues/{id}
		Supprimer un probl�me d'un projet
		DELETE
		/projects/{id}/issues/{id}
		Cr�er des commentaires sur un probl�me
		POST
		/projects/{id}/issues/{id}/comments/
		R�cup�rer la liste de tous les commentaires li�s � un probl�me (issue)
		GET
		/projects/{id}/issues/{id}/comments/
		Modifier un commentaire
		PUT
		/projects/{id}/issues/{id}/comments/{id}
		Supprimer un commentaire
		DELETE
		/projects/{id}/issues/{id}/comments/{id}
		R�cup�rer un commentaire (comment) via son id
		GET
		/projects/{id}/issues/{id}/comments/{id}

	</p> 
</body>
</html>
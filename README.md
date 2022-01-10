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
		1.Clonez le repository en utilisant <em>git clone</em><br>
		2.Se d�placer dans le r�pertoire racine SoftDesk en utilisant la commande <em>cd softDesk</em><br>
		3.Cr�er un environnement virtuel pour le projet avec la commande <mark>python -m venv env</mark><br>
		4.Activez l'environnement virtuel avec la commande <em>env\Scripts\activate.bat</em><br>
		5.Installez les d�pendances du project avec la commande <em>pip install -r requirements.txt</em><br>
	</p>
	<h3>Documentation et d�tails d'utilisation des endpoints de l'API</h3>
	<p>
		Une fois le serveur lanc�, lisez le document  suivant avant de faire vos premi�res requetes � l'API.<br>
	</p>
	<table>
		<tr>
			<th>Point de terminaison d'API</th>
			<th>M�thode HTTP</th>
			<th>URI</th>
		</tr>
		<tr>
			<td>Inscription de l'utilisateur</td>
			<td>POST</td>
			<td>/sign-up/</td>
		</tr>
		<tr>
			<td>Connexion de l'utilisateur</td>
			<td>POST</td>
			<td>/login/</td>
		</tr>
		<tr>
			<td>R�cup�rer la liste de tous les projets (projects) rattach�s � l'utilisateur (user) connect�</td>
			<td>GET</td>
			<td>/projects/</td>
		</tr>
		<tr>
			<td>Cr�er un projet</td>
			<td>POST</td>
			<td>/projects/</td>
		</tr>
		<tr>
			<td>R�cup�rer les d�tails d'un projet (project) via son id</td>
			<td>GET</td>
			<td>/projects/{id}/</td>
		</tr>
		<tr>
			<td>Mettre � jour un projet</td>
			<td>PUT</td>
			<td>/projects/{id}/</td>
		</tr>
		<tr>
			<td>Supprimer un projet et ses probl�mes</td>
			<td>DELETE</td>
			<td>/projects/{id}/</td>
		</tr>
		<tr>
			<td>Ajouter un utilisateur (collaborateur) � un projet</td>
			<td>POST</td>
			<td>/projects/{id}/users/</td>
		</tr>
		<tr>
			<td>R�cup�rer la liste de tous les utilisateurs (users) attach�s � un projet (project)</td>
			<td>GET</td>
			<td>/projects/{id}/users/</td>
		</tr>
		<tr>
			<td>Supprimer un utilisateur d'un</td>
			<td>DELETE</td>
			<td>/projects/{id}/users/{id}</td>
		</tr>
		<tr>
			<td>R�cup�rer la liste des probl�mes (issues) li�s � un projet (project)</td>
			<td>GET</td>
			<td>/projects/{id}/issues/</td>
		</tr>
		<tr>
			<td>Cr�er un probl�me dans un projet</td>
			<td>POST</td>
			<td>/projects/{id}/issues/</td>
		</tr>
		<tr>
			<td>Mettre � jour un probl�me dans un projet</td>
			<td>PUT</td>
			<td>/projects/{id}/issues/{id}</td>
		</tr>
		<tr>
			<td>Supprimer un probl�me d'un projet</td>
			<td>DELETE</td>
			<td>/projects/{id}/issues/{id}</td>
		</tr>
		<tr>
			<td>Cr�er des commentaires sur un probl�me</td>
			<td>POST</td>
			<td>/projects/{id}/issues/{id}/comments/</td>
		</tr>
		<tr>
			<td>R�cup�rer la liste de tous les commentaires li�s � un probl�me (issue)</td>
			<td>GET</td>
			<td>/projects/{id}/issues/{id}/comments/</td>
		</tr>
		<tr>
			<td>Modifier un commentaire</td>
			<td>PUT</td>
			<td>/projects/{id}/issues/{id}/comments/</td>
		</tr>
		<tr>
			<td>Supprimer un commentaire</td>
			<td>DELETE</td>
			<td>/projects/{id}/issues/{id}/comments/{id}</td>
		</tr>
		<tr>
			<td>R�cup�rer un commentaire (comment) via son id</td>
			<td>GET</td>
			<td>/projects/{id}/issues/{id}/comments/{id}</td>
		</tr>
	</table>
</body>
</html>
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
		1.Clonez le repository en utilisant <mark>git clone</mark><br>
		2.Se d�placer dans le r�pertoire racine SoftDesk en utilisant la commande <mark>cd softDesk</mark><br>
		3.Cr�er un environnement virtuel pour le projet avec la commande <mark>python -m venv env</mark><br>
		4.Activez l'environnement virtuel avec la commande <mark>env\Scripts\activate.bat</mark><br>
		5.Installez les d�pendances du project avec la commande <mark>pip install -r requirements.txt</mark><br>
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
	</table>
</body>
</html>
<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="css/connexion.css" />
</head>
<body>
	<div class="container" id="container">
		<div class="form-container sign-up-container">
			<form action="">
				<h1>Créez votre compte</h1>
				<input type="text" name="surname" placeholder="Nom" />
				<input type="text" name="name" placeholder="Prénom" />
				<input type="email" name="email" placeholder="Email" />
				<input type="password" name="password" placeholder="Mot de passe" />
				<button style="color : #fff">Créer mon compte</button>
			</form>
		</div>
		<div class="form-container sign-in-container">
			<form action="#">
				<h1>Connectez vous</h1>
				<input type="email" name="email" placeholder="Email" />
				<input type="password" name="password" placeholder="Mot de passe" />
				<button style="color : #fff">Me connecter</button>
			</form>
		</div>
		<div class="overlay-container">
			<div class="overlay">
				<div class="overlay-panel overlay-left">
					<h1>Bonjour !</h1>
					<p>Veuillez entrer vos informations personnelles pour vous connecter</p>
					<button class="ghost" id="signIn" style="color: #fff">Me connecter</button>
				</div>
				<div class="overlay-panel overlay-right">
					<h1>Bienvenue !</h1>
					<p>Entrez vos informations personnelles pour pouvoir continuer</p>
					<button class="ghost" id="signUp" style="color: #fff">Créer mon compte</button>
				</div>
			</div>
		</div>
	</div>
	<script type="text/javascript">
  	const signUpButton = document.getElementById('signUp');
    const signInButton = document.getElementById('signIn');
    const container = document.getElementById('container');

    signUpButton.addEventListener('click', () => {
    	container.classList.add("right-panel-active");
    });
    signInButton.addEventListener('click', () => {
    	container.classList.remove("right-panel-active");
    });
	</script>
	<div>
		<h5>Copyright &copy; Station météo</h5>
	</div>
</body>
</html>
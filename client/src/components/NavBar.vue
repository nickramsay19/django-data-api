<template>
	<nav class="nav-show">
		<div class="">
			<ul>
				<li><a href="#home"><strong>Data View</strong></a></li>
				<li><a href="#spoilers">Dashboard</a></li>
				<li>
					<a href="#manage">Manage</a>
					<ul>
						<li><a href="#">My Decks</a></li>
						<li><a href="#">My Combos</a></li>
						<li><a href="#">My Collection</a></li>
						<li><a href="#">My Shop</a></li>
					</ul>
				</li>
				<li class="right" id="last-nav-item"><a href="#login">Login</a></li>
				<li class="right"><a href="#register">Register</a></li>
			</ul>
		</div>
    </nav>
</template>

<script>
	export default {
		name: 'NavBar',
	}
</script>

<style scoped>
#last-nav-item{
	margin-right: 0.2em;
}

body {
	padding-top: 56px; /* should be the same value as .nav-hide */
}

.nav-hide {
    top: -56px;
}

.nav-show {
	top: 0;
}

/* main navigation */
nav {
	position: fixed;
	width: 100%;
	z-index: 10000;

	background-color: #fff;
	border-bottom: 1px solid #dcdcdc;
	
	transition: top 0.2s ease-in-out;
}

nav ul {
	margin: 0;
	background-color: #fff;
}

nav ul li {
	display: inline;
	float: left;
	position: relative;
	margin: 0;
	
	list-style-type: none;
}

nav ul li a {
	display: inline-block;
	padding: 14px 16px;
	
	color: #757575;
	font-size: 1.7rem;
	text-decoration: none;
	
	transition: 0.2s;
}

/* add caret for drop menu */
nav ul > li a:not(:only-child):after { content: '\00a0\00a0▼'; font-size: 0.8rem; vertical-align: middle; }

/* sub menu */
nav ul ul {
	position: absolute;
	min-width: 180px;
	
	height: 0px;
	overflow: hidden; /* hide sub menu */
}

nav ul li:hover ul {
	height: auto;
	overflow: visible; /* show sub menu */
	
	border: 1px solid #dcdcdc;
}

nav ul ul li {
	display: list-item;
	float: none;
}

nav ul ul li a {
	display: block;
}

/* Change background color of links on hover */
nav ul li a:hover {	
	background-color: #eee; 
	color: #757575;
}

/* Float right the list item that should be right aligned */
nav ul li.right { float: right; }

/* Hide the list item that contains the link that should open and close the topnav on small screens */
nav ul li.icon { display: none; }

/* When the screen is less than 680 pixels wide, hide all list items, except for the first one ("Home"). Show the list item that contains the link to open and close the topnav (li.icon) */
@media screen and (max-width:880px) {
	nav ul li:not(:first-child) { display: none; }
	nav ul li.icon {
		float: right;
		display: inline-block;
	}
}

/* The "mobile" class is added to the topnav with JavaScript when the user clicks on the icon. This class makes the nav look good on small screens */
@media screen and (max-width:880px) {
	nav.mobile ul { /* position: relative; */ }
	nav.mobile ul li.icon {
		position: absolute;
		right: 0;
		top: 0;
	}
	nav.mobile ul li {
		float: none;
		display: inline;
	}
	nav.mobile ul li a {
		display: block;
		text-align: left;
	}
	nav.mobile ul li ul {
		position: relative;
		height: auto;
		overflow: visible;
		padding-left: 20px;
	}
	nav.mobile ul li:hover ul {
		border: none;
	}
	nav.mobile ul li.right {
		float: none;
	}
}

</style>

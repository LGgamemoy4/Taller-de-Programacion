var arquero = {
	nombre:"arquero",
	ataque: 150,
	vida: 590,
	VelocidadDeAtaque: 90,
	velocidad: 60
}

var caballero = {
	nombre:"caballero",
	ataque: 300,
	vida: 411,
	VelocidadDeAtaque: 30,
	velocidad: 50
}

function versus (jugador1,jugador2) {
	if (jugador1.VelocidadDeAtaque > jugador2.VelocidadDeAtaque) {
		jugador2.vida -= jugador1.ataque;
	} else {
		jugador1.vida -= jugador2.ataque;
	}
}

versus(arquero,caballero);
console.log(arquero.vida,caballero.vida) // 590, 411-150
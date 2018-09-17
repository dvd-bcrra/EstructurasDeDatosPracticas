const readline = require('readline');
const rl = readline.createInterface(process.stdin,process.stdout);

console.log("Actividad 1: Desplegar los primeros numeros 100 numeros naturales");
console.log("Actividad 2: Calcular el factorial de un numero con y sin recursividad");
console.log("Actividad 3: Desplegar la posicion dada de la sucesion de fibonacci");

rl.question('Opcion: ', (value) => {
    var opcion = value;
    switch(opcion) {
    case "1":
        Numeros();
        break;
    case "2":
        Factoriales();
        break;
    case "3":
    	Fibonacci();
    	break;
    default:
        console.log('Me mataste');
        break;
	}
});



function Numeros(){
	console.log('Primeros 100 numeros naturales sin iteraciones');
	printNumbers(100);
	function printNumbers(num){
		if(num==1){
			console.log(1);
		}else{
			console.log(num);
			printNumbers(num-1);
		}
	}
}

function Factoriales(){
	rl.question('Ingrese un numero: ', (value) => {
		var num = value;

		console.log(num + "!: " + factorial(num));
		console.log(num + "!: " + factorialSR(num));

		function factorial(numero){
			if(numero == 1 || numero == 0){
				return 1;
			}else {
				return (numero * factorial(numero - 1));
			}
		}

		function factorialSR(numero){
			var factorial = numero;
			{
				for(var i = numero - 1; i >= 1; i--){
					factorial = factorial * i;
				}
				return factorial;
			}
		}
	});
}

function Fibonacci(){
	rl.question('Ingrese la posicion de la sucesion: ', (value) => {
		var numero = value;

		console.log("Valor: " + fibonacci(numero));
		console.log("Valor: " + fibonacciSR(numero));

		function fibonacci(num) {
		  if (num <= 1) return 1;
		  return fibonacci(num - 1) + fibonacci(num - 2);
		}
 
		function fibonacciSR(number) {
		    var previous_first = 0, previous_second = 1, next = 1;
		    for(var i = 1; i <= number; i++) {
		        next = previous_first + previous_second;
		        previous_first = previous_second;
		        previous_second = next;
		        //console.log("i = " + i + " : " + next);
		    }
		    return next;
		}

    	rl.close();
	});
}

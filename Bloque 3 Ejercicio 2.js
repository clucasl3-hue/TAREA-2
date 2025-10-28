//Contar cuantos numeros negativos se ingresan
let n = parseInt(prompt("Ingrese la cantidad de numeros a evaluar:"));
let contadorNegativos = 0;
for (let i = 1; i <= n; i++) {
 let numero = parseInt(prompt(`Ingrese el número ${i + 1}:`))
 if (numero < 0) {
    contadorNegativos++;
 }
} 
console.log(`Cantidad de negativos: ${contadorNegativos}`); 

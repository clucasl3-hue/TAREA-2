//Promedio de numeros pares e impares
let n = parseInt(prompt("Ingrese la cantidad de numeros a evaluar:"));
let sumaPares = 0;
let sumaImpares = 0;
let contadorPares = 0;
let contadorImpares = 0;
for (let i = 1; i <= n; i++) {
    let numero = parseInt(prompt(`Ingrese el número ${i + 1}:`))
    if (numero % 2 === 0) {
        sumaPares += numero;
        contadorPares++;
    } else {
        sumaImpares += numero;
        contadorImpares++;
    }
}
let promedioPares = contadorPares > 0 ? (sumaPares / contadorPares) : 0;
let promedioImpares = contadorImpares > 0 ? (sumaImpares / contadorImpares) : 0;
console.log("El promedio de numeros pares es: " + promedioPares);
console.log("El promedio de numeros impares es: " + promedioImpares); 

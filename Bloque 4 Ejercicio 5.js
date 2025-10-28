//Promedio de numeros pares e impares en un arreglo
let numeros = [2, 5, 8, 9, 4, 7];
let sumaPares = 0;
let sumaImpares = 0;
let contadorPares = 0;
let contadorImpares = 0;
for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] % 2 === 0) {
        sumaPares += numeros[i];
        contadorPares++;
    } else {
        sumaImpares += numeros[i]
        contadorImpares++;
    }
}
let promedioPares = contadorPares > 0 ? (sumaPares / contadorPares) : 0;
let promedioImpares = contadorImpares > 0 ? (sumaImpares / contadorImpares) : 0;
console.log("El promedio de pares es: " + promedioPares);
console.log("El promedio de impares es: " + promedioImpares);

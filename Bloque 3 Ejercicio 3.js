//Promedio de edades:mayores vs menores de edad 
let n = parseInt(prompt("Ingrese la cantidad de edades a evaluar:"));
let sumaMayores = 0;
let sumaMenores = 0;
let contadorMayores = 0;
let contadorMenores = 0;
for (let i = 1; i <= n; i++) {
    let edad = parseInt(prompt(`Ingrese la edad de la persona ${i + 1}:`));
    if (edad >= 18) {
        sumaMayores += edad;
        contadorMayores++;
    } else {
        sumaMenores += edad;
        contadorMenores++;
    }
}
let promedioMayores = contadorMayores > 0 ? (sumaMayores / contadorMayores) : 0;
let promedioMenores = contadorMenores > 0 ? (sumaMenores / contadorMenores) : 0;
console.log("El promedio de edades de mayores de edad es: " + promedioMayores);
console.log("El promedio de edades de menores de edad es: " + promedioMenores);

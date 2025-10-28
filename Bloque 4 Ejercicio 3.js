//Promedio de edades: mayores vs menores de edad en un arreglo 
let edades = [17, 20, 35, 15, 18];
let sumaMayores = 0;
let sumaMenores = 0;
let contadorMayores = 0;
let contadorMenores = 0;
for (let i = 0; i < edades.length; i++) {
    let edad = edades[i];
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

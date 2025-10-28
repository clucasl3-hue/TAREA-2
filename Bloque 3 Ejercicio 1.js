//Promedio de calificaciones mayores a 70
let n = parseInt(prompt("Ingrese la cantidad de calificaciones:"));
let suma = 0;
let contador = 0;
for (let i = 1; i < n; i++) {
    let calificacion = parseInt(prompt(`Ingrese la calificación ${i + 1}:`));
    if (calificacion > 70) {
        suma += calificacion;
        contador++;
    }
}
if (contador > 0) {
    let promedio = suma / contador;
    console.log("El promedio de calificaciones mayores a 70 es: " + promedio);
} else {
    console.log("No hay calificaciones mayores a 70 para calcular el promedio.");
}

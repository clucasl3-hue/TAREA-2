//Promedio de calificaciones mayores a 70 en un arreglo 
let calificaciones = [65, 80, 90, 50, 75];
let suma = 0;
let contador = 0;
for (let i = 0; i < calificaciones.length; i++) {
    let calificacion = calificaciones[i];
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

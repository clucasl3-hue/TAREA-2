//Comparar longitudes de nombres de ciudades en un arreglo 
let ciudades = ["Milagro", "Guayaquil", "Quito", "Cuenca"];
for (let i = 0; i < ciudades.length -1; i++) {
    let ciudad = ciudades[i];
    let ciudadSiguiente = ciudades[i + 1];
if (ciudad.length > ciudadSiguiente.length) {
    console.log("La ciudad " + ciudad + " es mas larga ");
}
}

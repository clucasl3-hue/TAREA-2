//Contar apariciones de una vocal en cada titulo de un arreglo 
let titulosProductos = ["Programacion avanzada", "Desarrollo web", "Analisis de datos"];
let vocalABuscar = prompt("Ingrese una vocal para buscar en los titulos de productos:").toLowerCase();
let contadorVocales = 0;
for (let i = 0; i < titulosProductos.length; i++) {
    let tituloActual = titulosProductos[i];
    for (let j = 0; j < tituloActual.length; j++) {
        if (tituloActual[j].toLowerCase() === vocalABuscar) {
            contadorVocales++;
        }
    }
    }
    console.log("La vocal " + vocalABuscar + " aparece " + contadorVocales + " veces en los titulos de productos.");

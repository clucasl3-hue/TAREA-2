//Contar apariciones de una vocal en un titulo
let titulo = prompt("Ingrese un titulo:");
let vocal = prompt("Ingrese una vocal a buscar:");
let contador = 0;
for (let i = 0; i < titulo.length; i++) {
    if (titulo[i].toLowerCase() === vocal.toLowerCase()) {
        contador++;
    }
}
console.log("La vocal " + vocal + " aparece " + contador + " veces en el titulo.");

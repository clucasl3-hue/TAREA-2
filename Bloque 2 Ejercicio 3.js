//Inveritr los nombres de varios productos de un arreglo
let nombresProductos = ["Laptop", "Celular", "Tablet"];
for (let i = 0; i < nombresProductos.length; i++) {
    let nombreActual = nombresProductos[i];
    let nombreInvertido = nombreActual.split("").reverse().join("");
    console.log("Nombre de los productos invertidos: " + nombreInvertido);
}

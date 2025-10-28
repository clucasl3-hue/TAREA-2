//Obtener iniciales de un cargo profesional 
let cargo = prompt("Ingrese un cargo profesional:");
let palabras = cargo.split(" ");
let iniciales = ""; 
for (let i = 0; i < palabras.length; i++) {
    iniciales += palabras[i][0].toUpperCase() + ".";
}
console.log("Iniciales del cargo: " + iniciales);

//Comparar nombres de cuidades por longitud
let ciudad1 = prompt("Ingrese el nombre de la primera ciudad:");
let ciudad2 = prompt("Ingrese el nombre de la segunda ciudad:");
if (ciudad1.length > ciudad2.length) {
    console.log("La ciudad con el nombre mas largo es: " + ciudad1);
} else {
    console.log("La ciudad con el nombre mas largo es: " + ciudad2);
}

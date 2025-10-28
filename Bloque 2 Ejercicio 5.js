//Obtener iniciales de varios cargos profesiones de un arreglo
let cargos = ["Director General Academico", "Jefe de Laboratorio", "Asistente Administrativo"];
for (let i = 0; i < cargos.length; i++) {
    let cargoActual = cargos[i];
    let palabras = cargoActual.split(" ");
    let iniciales = "";
    for (let j = 0; j < palabras.length; j++) {
        iniciales += palabras[j][0].toUpperCase() + ".";
    }
    console.log("Iniciales del cargo " + cargoActual + ": " + iniciales);
}

//Contar caracteres de varias frases publicitarias de un arreglo
let frasesPublicitarias = ["La tecnnologia avanza", "Innova para crecer", "Calidad Garantizada"];
for (let i = 0; i < frasesPublicitarias.length; i++) {
    let fraseActual = frasesPublicitarias[i];
    let cantidadCaracteres = fraseActual.length;
    console.log("La frase: " + fraseActual + " tiene " + cantidadCaracteres + " caracteres.");
}

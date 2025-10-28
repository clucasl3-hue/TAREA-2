//Contar numeros negativos en una lista en un arreglo 
let numeros = [3, -5, 0, 7, -1, -8];
let contadorNegativos = 0;
for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] < 0) {
        contadorNegativos++; 
    }
}
console.log("Cantidad de numeros negativos: " + contadorNegativos);

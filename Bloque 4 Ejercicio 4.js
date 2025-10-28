//Mostrar tablas de multiplicar de varios numeros
let numeros = [3, 5];
for (let j = 0; j < numeros.length; j++) {
    let numero = numeros[j];
    console.log("Tabla de multiplicar del " + numero + ":");
    for (let i = 1; i <= 10; i++) {
        let resultado = numero * i;
        console.log(`${numero} x ${i} = ${resultado}`);
    }
}

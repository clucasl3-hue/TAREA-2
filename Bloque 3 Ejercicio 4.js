//Mostrar la tabla de multiplicar de un numero
let numero = parseInt(prompt("Ingrese un numero para ver su tabla de multiplicar:"));
for (let i = 1; i <= 10; i++) {
    let resultado = numero * i;
    console.log(`${numero} x ${i} = ${resultado}`);
}

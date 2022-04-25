// Ejercicio 1 

const alumnos = [
    {
      id: 0,
      nombre: "Leandro",
      apellido: "Borrelli",
      legajo: 20210308,
      notas: [],
    },
    {
      id: 1,
      nombre: "Esteban",
      apellido: "Piazza",
      legajo: 20210211,
      notas: [],
    },
    {
      id: 2,
      nombre: "Martin",
      apellido: "Cejas",
      legajo: 20210218,
      notas: [],
    },
    {
      id: 3,
      nombre: "Karina",
      apellido: "Borgna",
      legajo: 20210516,
      notas: [],
    },
    {
      id: 5,
      nombre: "Javier",
      apellido: "Riera",
      legajo: 20220125,
      notas: [],
    },
  ];

//Legajo de forma descendente

function OdernarPorLegajo(objeto) { {
    for (let i = 0; i < objeto.length; i++) {
          for (let j = 0; j < objeto.length -1 ; j++) {
              if (objeto[j].legajo < objeto[j + 1].legajo) {
                  let temp = objeto[j];
                  objeto[j] = objeto[j + 1];
                  objeto[j + 1] = temp;
              }
          }
      }
    return objeto
  }
}

//Muestro que quedo ordeno
console.log('\nSin ordenar\n');
console.log(alumnos);
console.log('\nOrdenado\n');
console.log(OdernarPorLegajo(alumnos));

// Ejercicio 2

alumno = {
id: 5,
nombre: "Lucas",
apellido: "Astrada",
legajo: 20220125,
notas: [10,6,8,7,9]
}

//Parte 1

function promedioNotas(objeto) {
    let acumulador = 0
    for (let i = 0; i < objeto.notas.length; i++) {
            acumulador += objeto.notas[i]
        }
    return (acumulador/objeto.notas.length)
}

console.log(promedioNotas(alumno))

//Parte 2


function ordenarNotas(objeto) {
    for (let i = 0; i < objeto.notas.length; i++) {
          for (let j = 0; j < objeto.notas.length-1; j++) {
              if (objeto.notas[j] > objeto.notas[j + 1]) {
                  let temp = objeto.notas[j];
                  objeto.notas[j] = objeto.notas[j + 1];
                  objeto.notas[j + 1] = temp;
              }
          }
      }
    return objeto
}


//Muestro que quedo ordeno
console.log('\n Sin ordenar \n');
console.log(alumno);
console.log('\n Ordenado \n');
console.log(ordenarNotas(alumno));
    
//Ejercicio 3

// A. Crea una matriz de 3i3, cuadrada, con números enteros negativos en
// cada una de sus posiciones.
// B. Crear una función que retorne la suma de todos los números dentro de la
// matriz que sean múltiplos de 5.
// C. Crear una función que retorne un valor booleano dependiendo si la suma
// de todos los valores de la matriz es impar.
// D. Crear una función que retorne la multiplicación de las diagonales de la
// matriz.

//A
matriz = [
	[-1, -8,-2 ],
	[-3, -25,-2 ],
	[-1, -5,-12 ]
]

//B
function sumaMultiplo(matriz,multiplo){
    let total = 0
    for (let i=0;i<matriz.length;i++) {
        for (let j=0;j<matriz.length;j++) {
            if ( matriz[i][j] % multiplo == 0 )
                total += matriz[i][j]
        }
    }
    return total
}

console.log(sumaMultiplo(matriz,5))

//C

function matrizEsImpar(matriz){
    let total = 0
    for (let i=0;i<matriz.length;i++) {
        for (let j=0;j<matriz.length;j++) {
            total += matriz[i][j]
        }
    }
    if (total % 2 == -1)
        return true
    else
        return false
}

console.log(matrizEsImpar(matriz))

//D

function multiplicacionesDiagonales(matriz){
    let diagoPrincipal = 1
    let diagoSecundaria = 1
    
    for(let i=0;i<matriz.length;i++){
        for(let j=0;j<matriz.length;j++){
            if(i==j){
                diagoPrincipal *= matriz[i][j];
            }
             
            if(i+j == matriz.length-1){
                diagoSecundaria *= matriz[i][j];
            }
        }
    }
    return {'Diagonal Principal' : diagoPrincipal , 'Diagonal Secundaria' : diagoSecundaria}
}

console.log(multiplicacionesDiagonales(matriz))
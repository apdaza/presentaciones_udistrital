# Tutorial de Prolog (Introducción Básica)

## Introducción a Prolog

Prolog (PROgramming in LOGic) es un lenguaje de programación que se basa en la lógica de predicados de primer orden. A diferencia de los lenguajes de programación imperativos (como C o Python), en Prolog defines **hechos** y **reglas**, y el intérprete de Prolog se encarga de realizar inferencias lógicas a partir de esas definiciones para encontrar respuestas a consultas.

### Estructura Básica

- **Hechos:** Son afirmaciones que describen el mundo.
- **Reglas:** Son condiciones que describen cómo ciertos hechos pueden derivarse de otros.
- **Consultas:** Preguntas que se le hacen al sistema para obtener información basada en los hechos y reglas.

### Instalación de SWI-Prolog

Para seguir este tutorial, necesitas instalar un entorno de desarrollo de Prolog. El más común es **SWI-Prolog**, que puedes descargar desde [aquí](https://www.swi-prolog.org/Download.html).

---

## Primeros Pasos con Prolog

### Definiendo Hechos

Los hechos son declaraciones simples que describen relaciones entre objetos o propiedades. En Prolog, la sintaxis es muy simple. Cada hecho se termina con un punto (`.`).

```prolog
% Sintaxis básica: relacion(objeto1, objeto2, ...).

es_padre_de(juan, maria).
es_padre_de(carlos, pedro).
es_padre_de(ana, jose).
```

Aquí hemos definido la relación "es_padre_de", donde el primer argumento es el padre y el segundo es el hijo.

### Consultas Básicas

Una vez que tienes algunos hechos definidos, puedes hacer consultas. Por ejemplo, para preguntar quién es padre de quién:

```prolog
?- es_padre_de(juan, maria).
true.

?- es_padre_de(carlos, maria).
false.
```

Prolog responde con `true` si el hecho es cierto y con `false` si no lo es.

También puedes hacer preguntas más generales, como pedirle a Prolog que te diga todos los padres de alguien:

```prolog
?- es_padre_de(X, maria).
X = juan.
```

Aquí, `X` es una variable que Prolog intenta igualar con un valor que haga verdadera la consulta.

### Definiendo Reglas

Las reglas permiten definir relaciones más complejas. Una regla tiene la siguiente sintaxis:

```prolog
% Regla: conclusion :- condicion1, condicion2, ...
es_abuelo_de(X, Y) :- es_padre_de(X, Z), es_padre_de(Z, Y).
```

Aquí definimos que `X` es abuelo de `Y` si `X` es padre de `Z` y `Z` es padre de `Y`.

Ejemplo de consulta con reglas:

```prolog
?- es_abuelo_de(juan, jose).
true.

?- es_abuelo_de(ana, pedro).
false.
```

### Recursión en Prolog

Prolog soporta recursión, lo que es muy útil para definir relaciones más complejas. Veamos un ejemplo donde definimos el concepto de ancestro.

```prolog
es_ancestro_de(X, Y) :- es_padre_de(X, Y).
es_ancestro_de(X, Y) :- es_padre_de(X, Z), es_ancestro_de(Z, Y).
```

En esta regla, `es_ancestro_de/2` se define en términos de sí misma para seguir la cadena de padres.

### Consultas Complejas

Podemos realizar consultas que involucren tanto hechos como reglas.

```prolog
?- es_ancestro_de(juan, jose).
true.
```

Prolog resolverá la consulta utilizando las reglas y hechos que hemos definido.

---

## Listas en Prolog

Prolog tiene soporte nativo para listas, que son una estructura de datos muy útil. Las listas en Prolog se escriben entre corchetes, y pueden contener cualquier número de elementos.

```prolog
% Una lista simple
[1, 2, 3, 4].

% Una lista con variables
[X, 2, Y].
```

Puedes usar listas con reglas y consultas. Por ejemplo, para definir la relación de pertenencia a una lista:

```prolog
miembro(X, [X|_]).
miembro(X, [_|T]) :- miembro(X, T).
```

Esta regla dice que `X` es miembro de una lista si es el primer elemento (`X|_`) o si es miembro de la cola de la lista (`T`).

### Consultas con listas

Podemos hacer consultas para verificar si un elemento pertenece a una lista:

```prolog
?- miembro(2, [1, 2, 3]).
true.

?- miembro(4, [1, 2, 3]).
false.
```

---

## Backtracking en Prolog

El proceso de **backtracking** es central en Prolog. Cuando Prolog recibe una consulta, intenta satisfacerla probando todas las posibles soluciones. Si una solución falla, vuelve atrás (backtrack) y prueba otra posible ruta.

### Ejemplo de backtracking

Consideremos los siguientes hechos:

```prolog
color(rosa).
color(azul).
color(verde).
```

Si hacemos una consulta para todos los colores posibles:

```prolog
?- color(C).
C = rosa ;
C = azul ;
C = verde.
```

Prolog va a devolver todas las posibles soluciones de una en una, permitiendo hacer backtracking con `;`.

---

## 1. Operadores Aritméticos y Relacionales

En Prolog, es posible trabajar con operadores aritméticos y relacionales como lo harías en lenguajes imperativos. Aquí están algunos de los más utilizados:

- **Aritméticos**: `+, -, *, /`
  - `/` es la división entera.
  - `mod`: módulo (resto de la división).
  - `^`: potencia.

- **Relacionales**: `>, <, >=, <=`

### Ejemplo en Prolog:

```prolog
?- X is 3 + 5.
X = 8.

?- 9 > 7.
true.
```

Recuerda que para evaluar expresiones aritméticas, debes usar el operador **is**. Sin `is`, Prolog simplemente tratará las expresiones como términos simbólicos.

---

## 2. Operadores de Igualdad

Prolog tiene varios operadores de igualdad que permiten la comparación de términos:

- **=**: unificación, verdadero si ambos operandos unifican.
- **\=**: no unificación, verdadero si no unifican.
- **is**: evaluación aritmética y unificación.
- **=:=**: compara valores después de evaluar ambos lados de la expresión.

### Ejemplo en Prolog:

```prolog
?- 3 = 3.
true.

?- 3 \= 4.
true.

?- X is 3 * 5.
X = 15.

?- 3 =:= 1 + 2.
true.
```

### Casos comunes de error:

Al usar `is`, ten en cuenta que las variables a la derecha deben estar instanciadas. De lo contrario, obtendrás un error:

```prolog
?- 5 is X + 4.
Error: X no está instanciada.
```

---

## 3. Listas en Prolog

Las listas en Prolog son una estructura de datos fundamental. Las listas se representan entre corchetes:

```prolog
[1, 2, 3, 4].
[X, Y, Z].
```

### Operaciones comunes con listas:

- **Longitud de una lista**: Para calcular la longitud de una lista, usamos recursión:

```prolog
longitud([], 0).
longitud([_|T], N) :- longitud(T, N0), N is N0 + 1.

?- longitud([a,b,c], L).
L = 3.
```

- **Pertenece a una lista**: Para verificar si un elemento está en una lista:

```prolog
pertenece(X, [X|_]).
pertenece(X, [_|T]) :- pertenece(X, T).

?- pertenece(b, [a, b, c]).
true.
```

- **Concatenación de listas**:

```prolog
concatenar([], L, L).
concatenar([X|L1], L2, [X|L3]) :- concatenar(L1, L2, L3).

?- concatenar([1, 2], [3, 4], R).
R = [1, 2, 3, 4].
```

---

## 4. Operaciones Aritméticas y Estructuras

En Prolog también puedes realizar cálculos más complejos usando funciones matemáticas:

- **Funciones matemáticas disponibles**: `abs/1`, `sqrt/1`, `log/1`, `sin/1`, etc.

```prolog
?- X is sqrt(16).
X = 4.0.

?- Y is sin(1).
Y = 0.8414709848078965.
```

También puedes representar datos estructurados como registros o árboles. Por ejemplo:

```prolog
persona(nombre('Juan'), apellido('Pérez'), cc(123456789)).
```

Para acceder a los datos:

```prolog
?- persona(nombre(X), apellido(Y), _).
X = 'Juan', Y = 'Pérez'.
```

---

## 5. Ejemplo Completo: Calculando el Porcentaje de Ganados

Aquí está un ejemplo más avanzado, basado en el contenido del archivo que compartiste:

Definimos los siguientes hechos:

```prolog
ganados(juan, 7).
ganados(susana, 6).
jugados(juan, 13).
jugados(susana, 7).
```

Y una regla para calcular el porcentaje de juegos ganados:

```prolog
porcentaje(X, Y) :- ganados(X, Z), jugados(X, Q), Y is (Z/Q) * 100.

?- porcentaje(juan, P).
P = 53.84615384615385.
```

---

### Predicados Dinámicos en Prolog

Los **predicados dinámicos** en Prolog son aquellos que pueden ser modificados (añadidos o eliminados) durante la ejecución del programa. Esto es útil en aplicaciones donde los hechos o las reglas pueden cambiar a lo largo del tiempo, como en sistemas de bases de datos o en inteligencia artificial, donde los conocimientos se actualizan dinámicamente.

Para declarar un predicado como dinámico, se usa la directiva `:- dynamic nombre_predicado/arity`, donde `arity` es el número de argumentos del predicado.

### Ejemplo Básico de Predicado Dinámico

Vamos a crear un predicado dinámico que maneje una base de datos simple de amigos. Primero, declaramos que el predicado es dinámico y luego usamos las funciones **asserta**, **assertz** y **retract** para manipular los hechos durante la ejecución del programa.

#### Declaración del predicado dinámico

```prolog
:- dynamic amigo/2.
```

Esto le dice a Prolog que el predicado `amigo/2` (que acepta dos argumentos) puede modificarse dinámicamente.

#### Añadiendo hechos a la base de datos

Podemos añadir hechos de dos maneras: al principio de la base de datos con **asserta** o al final con **assertz**.

```prolog
?- asserta(amigo(juan, pedro)).
true.

?- assertz(amigo(ana, maria)).
true.
```

Ahora hemos añadido dos hechos dinámicos. Podemos consultarlos:

```prolog
?- amigo(juan, X).
X = pedro.

?- amigo(ana, X).
X = maria.
```

#### Eliminando hechos

Para eliminar un hecho, usamos **retract**.

```prolog
?- retract(amigo(juan, pedro)).
true.

?- amigo(juan, X).
false.
```

En este caso, hemos eliminado el hecho `amigo(juan, pedro)`, por lo que la consulta ya no encuentra ninguna coincidencia.

### Ejemplo Completo: Base de Datos de Estudiantes y Notas

Vamos a crear un ejemplo más completo, donde gestionaremos una base de datos dinámica de estudiantes y sus notas.

#### Declaración del predicado dinámico

```prolog
:- dynamic nota/2.
```

#### Añadiendo hechos

Añadimos información sobre las notas de los estudiantes:

```prolog
?- assertz(nota(juan, 7)).
true.

?- assertz(nota(ana, 9)).
true.
```

Ahora, tenemos dos estudiantes con sus respectivas notas.

#### Consultando las notas

Podemos hacer una consulta para obtener la nota de un estudiante:

```prolog
?- nota(juan, N).
N = 7.
```

#### Actualizando notas

Para actualizar la nota de un estudiante, primero eliminamos la entrada existente con **retract** y luego añadimos la nueva con **assertz**:

```prolog
?- retract(nota(juan, _)).
true.

?- assertz(nota(juan, 8)).
true.
```

Ahora la nota de `juan` ha sido actualizada:

```prolog
?- nota(juan, N).
N = 8.
```

#### Eliminando estudiantes

Si queremos eliminar un estudiante de la base de datos:

```prolog
?- retract(nota(ana, _)).
true.
```

Después de esto, la consulta no encuentra el hecho:

```prolog
?- nota(ana, N).
false.
```

### Controlando Múltiples Hechos

Cuando usamos **retract** con variables, Prolog elimina el primer hecho que coincide con el patrón. Si hay varios hechos que coinciden, puedes usar **retractall** para eliminar todos los hechos de un tipo.

#### Ejemplo de uso de `retractall`

Si queremos eliminar todas las notas de los estudiantes, usamos:

```prolog
?- retractall(nota(_, _)).
true.
```

Esto eliminará todas las entradas relacionadas con `nota`.

---

### Predicados Dinámicos: Uso en Programas Reales

El uso de predicados dinámicos es común en programas que deben gestionar cambios en la información a lo largo del tiempo. Estos predicados son útiles en:

- **Sistemas expertos**: donde el conocimiento puede ser actualizado en función de nuevos datos.
- **Simulaciones**: donde los hechos cambian durante la simulación.
- **Aplicaciones de bases de datos**: que requieren que la información se agregue, actualice y elimine de manera dinámica.

---

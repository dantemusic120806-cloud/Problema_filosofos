# Informe Descriptivo: Filósofos Comensales en Python

**REPÚBLICA BOLIVARIANA DE VENEZUELA**  
**MINISTERIO DEL PODER POPULAR PARA LA EDUCACIÓN UNIVERSITARIA, CIENCIA Y TECNOLOGÍA**  
**INSTITUTO UNIVERSITARIO POLITÉCNICO “SANTIAGO MARIÑO” — EXTENSIÓN SAN CRISTÓBAL**[cite: 3]  

- **Autores:** Juan Francisco Valdés Gómez, Daniel Chinchilla[cite: 3]
- **Docente de la Materia:** Ing. Oscar Castro[cite: 3]
- **Lugar y Fecha:** San Cristóbal, Noviembre, 2026[cite: 3]
- **Objetivo del informe:** Presentar un informe descriptivo sobre el funcionamiento, estructura y componentes de los dos programas en Python entregados, ambos basados en el problema clásico de los Filósofos Comensales[cite: 3].

---

## Reglas Planteadas en Clase

1. **Filósofo no come $\Rightarrow$ Pensando:** Si un filósofo no está comiendo, permanece pensando[cite: 1].
2. **No está pensando:** Puede pasar a **Comiendo** o a **Esperando cubiertos**[cite: 1].
3. **Si tiene un cubierto:** Espera el cubierto restante/actual necesario para comer, y nadie más puede quitarle o atacarle el cubierto que ya posee[cite: 1].
4. **Solo come con 2 cubiertos:** Requiere dos cubiertos para entrar a comer[cite: 1].
5. **Límite de espera:** Si un filósofo espera cubiertos por más de 3 turnos, se muere[cite: 1].

---

## 1. `filósofos inmortales.py`

### Propósito general
Simula a cinco filósofos que alternan de forma continua entre pensar, esperar y comer utilizando cinco cubiertos compartidos, sin límite de tiempo ni condición de finalización[cite: 3].

### Estructuras y variables principales
- **`NUM_FILOSOFOS`:** Constante definida en `5`[cite: 3].
- **`cubiertos`:** Lista de cinco objetos `threading.Lock()` que representan los recursos compartidos[cite: 3].
- **`lock_consola`:** Objeto `threading.Lock()` empleado para sincronizar la impresión de mensajes en consola[cite: 3].
- **`filosofo(id_filosofo)`:** Función que define el comportamiento de cada hilo[cite: 3].

### Funcionamiento y flujo de ejecución
- Se asigna a cada filósofo un cubierto izquierdo (`id_filosofo`) y un cubierto derecho (`(id_filosofo + 1) % NUM_FILOSOFOS`)[cite: 3].
- El último filósofo (`id_filosofo == NUM_FILOSOFOS - 1`) invierte el orden para tomar primero el cubierto derecho y luego el izquierdo[cite: 3].
- Dentro de un bucle infinito (`while True`), cada filósofo imprime que está pensando y espera entre 1 y 2 segundos con `time.sleep`[cite: 3].
- Luego imprime que espera cubiertos e inicia un bucle de intentos usando `acquire(blocking=False)`[cite: 3].
- Si toma el primer cubierto, intenta tomar el segundo también con `acquire(blocking=False)`[cite: 3]. Si logra ambos, imprime que está comiendo, espera entre 1.5 y 2.5 segundos, libera ambos cubiertos con `release()`, imprime que terminó y vuelve a pensar[cite: 3].
- Si no obtiene el segundo cubierto, libera el primero, espera 0.5 segundos y reintenta[cite: 3].
- En el bloque principal (`main`), se crean y arrancan los cinco hilos con `threading.Thread` y se llama a `join()` sobre cada uno para mantener la ejecución activa[cite: 3].

---

## 2. `problema de los filosofos.py`

### Propósito general
Simula a cinco filósofos compitiendo por cinco cubiertos compartidos con un límite máximo de turnos de espera, de modo que un filósofo que no logra comer dentro del límite establecido sale de la simulación[cite: 3].

### Estructuras y variables principales
- **`NUM_FILOSOFOS`:** Constante definida en `5`[cite: 3].
- **`MAX_TURNOS_ESPERA`:** Constante definida en `3`[cite: 3].
- **`cubiertos`:** Lista de cinco objetos `threading.Lock()` para los cubiertos[cite: 3].
- **`lock_consola`:** Objeto `threading.Lock()` para ordenar la salida en consola y el estado[cite: 3].
- **`vivos`:** Lista booleana inicializada con cinco valores `True` para controlar si cada filósofo sigue activo[cite: 3].
- **`filosofo(id_filosofo)`:** Función ejecutada por cada hilo[cite: 3].

### Funcionamiento y flujo de ejecución
- Cada filósofo recibe su cubierto izquierdo y derecho, y el último filósofo invierte el orden de adquisición[cite: 3].
- Se mantiene un contador `turnos_esperando` iniciado en `0` y un bucle principal mientras `vivos[id_filosofo]` sea verdadero[cite: 3].
- El filósofo pasa por el estado de pensar durante un tiempo aleatorio entre 1 y 2 segundos y luego pasa a esperar cubiertos[cite: 3].
- En un bucle controlado por `turnos_esperando <= MAX_TURNOS_ESPERA`, intenta tomar ambos cubiertos de forma no bloqueante (`acquire(blocking=False)`)[cite: 3].
- Si obtiene los dos cubiertos, imprime que está comiendo, espera entre 1.5 y 2.5 segundos, libera ambos cubiertos, marca `comió = True`, reinicia `turnos_esperando` a `0` y sale del bucle de espera[cite: 3].
- Si no consigue ambos cubiertos, libera el primero si lo había tomado, aumenta `turnos_esperando` en `1`, imprime el conteo de turnos y espera 1 segundo[cite: 3].
- Si al salir del bucle no comió y `turnos_esperando > MAX_TURNOS_ESPERA`, imprime un mensaje indicando que el filósofo murió de hambre, asigna `vivos[id_filosofo] = False` y termina su bucle[cite: 3].
- En el bloque principal (`main`), se inician los cinco hilos, se espera su finalización con `join()` y al concluir todos se imprime el mensaje de fin de la simulación[cite: 3].

---

## Resumen Comparativo de los Programas
- `filósofos inmortales.py` ejecuta hilos de manera indefinida con pausas de 0.5 segundos entre reintentos[cite: 3].
- `problema de los filosofos.py` incorpora `MAX_TURNOS_ESPERA = 3`, la lista `vivos` y pausas de 1 segundo entre intentos, permitiendo que los hilos concluyan cuando un filósofo excede el límite de espera y finalice el programa con el mensaje de cierre[cite: 3].

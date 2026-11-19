# Problema_filosofos
# Simulación del Problema de los Filósofos Comensales

**Institución:** Instituto Universitario Politécnico “Santiago Mariño” — Extensión San Cristóbal[cite: 3]  
**Materia:** Sistemas Operativos[cite: 3]  
**Docente:** Ing. Oscar Castro[cite: 3]  
**Autores:** Juan Francisco Valdés Gómez, Daniel Chinchilla[cite: 3]  
**Fecha:** Noviembre, 2026[cite: 3]  

## Objetivo del Informe
Presentar un informe descriptivo sobre el funcionamiento, estructura y componentes de los dos programas en Python entregados, ambos basados en el problema clásico de los Filósofos Comensales[cite: 3].

---

## Resumen Comparativo de los Programas

- **`problema_de_los_filosofos.py`:** Simula a cinco filósofos compitiendo por cinco cubiertos compartidos con un límite máximo de turnos de espera (`MAX_TURNOS_ESPERA = 3`) y pausas de 1 segundo entre intentos, de modo que un filósofo que no logra comer dentro del límite establecido sale de la simulación (`vivos[id_filosofo] = False`) y permite que el programa concluya con el mensaje de cierre[cite: 3].
- **`filosofos_inmortales.py`:** Simula a cinco filósofos que alternan de forma continua entre pensar, esperar y comer utilizando cinco cubiertos compartidos, sin límite de tiempo ni condición de finalización, con pausas de 0.5 segundos entre reintentos[cite: 3].

---

## 1. Código: `problema_de_los_filosofos.py`

```python
import threading
import time
import random

NUM_FILOSOFOS = 5
MAX_TURNOS_ESPERA = 3

cubiertos = [threading.Lock() for _ in range(NUM_FILOSOFOS)]
lock_consola = threading.Lock()
vivos = [True] * NUM_FILOSOFOS


def filosofo(id_filosofo):
    cubierto_izq = id_filosofo
    cubierto_der = (id_filosofo + 1) % NUM_FILOSOFOS

    if id_filosofo == NUM_FILOSOFOS - 1:
        primer_cubierto, segundo_cubierto = cubierto_der, cubierto_izq
    else:
        primer_cubierto, segundo_cubierto = cubierto_izq, cubierto_der

    turnos_esperando = 0

    while vivos[id_filosofo]:
        with lock_consola:
            print(f"[Filósofo {id_filosofo}] está PENSANDO")
        time.sleep(random.uniform(1, 2))

        with lock_consola:
            print(f"[Filósofo {id_filosofo}] está ESPERANDO cubiertos")

        comio = False

        while turnos_esperando <= MAX_TURNOS_ESPERA:
            adquirido_1 = cubiertos[primer_cubierto].acquire(blocking=False)

            if adquirido_1:
                adquirido_2 = cubiertos[segundo_cubierto].acquire(blocking=False)

                if adquirido_2:
                    with lock_consola:
                        print(f"[Filósofo {id_filosofo}] está COMIENDO")
                    time.sleep(random.uniform(1.5, 2.5))
                    cubiertos[segundo_cubierto].release()
                    cubiertos[primer_cubierto].release()
                    comio = True
                    turnos_esperando = 0
                    break
                else:
                    cubiertos[primer_cubierto].release()

            turnos_esperando += 1
            with lock_consola:
                print(f"[Filósofo {id_filosofo}] turnos de espera: {turnos_esperando}/{MAX_TURNOS_ESPERA}")
            time.sleep(1)

        if not comio and turnos_esperando > MAX_TURNOS_ESPERA:
            with lock_consola:
                print(f"[Filósofo {id_filosofo}] murió de hambre")
            vivos[id_filosofo] = False
            break


if __name__ == "__main__":
    hilos = []
    for i in range(NUM_FILOSOFOS):
        t = threading.Thread(target=filosofo, args=(i,))
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()

    print("Fin de la simulación.")

import threading
import time
import random

NUM_FILOSOFOS = 5

cubiertos = [threading.Lock() for _ in range(NUM_FILOSOFOS)]
lock_consola = threading.Lock()


def filosofo(id_filosofo):
    cubierto_izq = id_filosofo
    cubierto_der = (id_filosofo + 1) % NUM_FILOSOFOS

    if id_filosofo == NUM_FILOSOFOS - 1:
        primer_cubierto, segundo_cubierto = cubierto_der, cubierto_izq
    else:
        primer_cubierto, segundo_cubierto = cubierto_izq, cubierto_der

    while True:
        with lock_consola:
            print(f"[Filósofo {id_filosofo}] está PENSANDO")
        time.sleep(random.uniform(1, 2))

        with lock_consola:
            print(f"[Filósofo {id_filosofo}] está ESPERANDO cubiertos")

        while True:
            adquirido_1 = cubiertos[primer_cubierto].acquire(blocking=False)

            if adquirido_1:
                adquirido_2 = cubiertos[segundo_cubierto].acquire(blocking=False)

                if adquirido_2:
                    with lock_consola:
                        print(f"[Filósofo {id_filosofo}] está COMIENDO")
                    time.sleep(random.uniform(1.5, 2.5))
                    cubiertos[segundo_cubierto].release()
                    cubiertos[primer_cubierto].release()
                    with lock_consola:
                        print(f"[Filósofo {id_filosofo}] terminó de comer")
                    break
                else:
                    cubiertos[primer_cubierto].release()

            time.sleep(0.5)


if __name__ == "__main__":
    hilos = []
    for i in range(NUM_FILOSOFOS):
        t = threading.Thread(target=filosofo, args=(i,))
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()

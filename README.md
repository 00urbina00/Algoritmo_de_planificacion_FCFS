# Algoritmos_de_planificacion
Práctica incremental de utilización de algoritmos de planificación y otras funcionalidades.

# FCFS
- Se implementó el algoritmo de planificación First come first served.
- (Continuación de simulador de procesamiento) Ahora se contempla el diagrama de 5 estados: Nuevo, Listo, Ejecución, Bloqueado, Terminado. Se han removido los lotes y ahora hay un área de memoria donde solo caben 5 procesos a la vez (se compone de: Ejecución, Bloqueado y listo).

# Round Robin
- Se implementó el algoritmo de planificacion Round Robin, ahora se tiene un "Quantum" a elegir desde la interfáz para establecer el lapso de tiempo del procesador asignado a cada proceso.

# Paginación
- Se cambió el manejor de memoria, ahora se tiene un espacio de memoria dado en "marcos", teniendo un espacio predefinido de 44 marcos, donde 4 de estos son usados por el sistema operativo (ficticio) y cada marco tiene 5 unidades de espacio.
- Ademas, se agrego un apartado para ver el próximo proceso a entrar a la memoria (Próximo nuevo) mostrando su información y el recuento de procesos nuevos y terminados.
- También se muestran los marcos disponibles, la memoria en uso y la memoria disponible en tiempo real.

# Suspendidos
- Se implementó la funcionalidad de "suspender"  y "recuperar" los procesos bloqueados a almacenamiento secundario (disco) serializando **toda** la información de cada proceso.
- También se agregó información sobre el próximo proceso a recuperar (Próximo suspendido) mostrando su información y el recuento de procesos del sistema (Nuevos, Listos, Bloqueados, Suspendidos y Terminados), se asume que se visualiza el proceso en ejecución.
- Se hicieron retoques a la interfáz para mejorar la visualizacion de información.

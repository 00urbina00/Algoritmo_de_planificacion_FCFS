# Algoritmo de Planificación FCFS, Round Robin y Más

## Descripción

Este repositorio contiene un simulador de algoritmos de planificación de procesos, desde el algoritmo **FCFS (First-Come, First-Served)** hasta el **Round Robin** y funcionalidades adicionales como **paginación** y **suspensión de procesos**. El proyecto ha evolucionado desde una implementación simple de FCFS con procesamiento por lotes, hasta una herramienta interactiva completa que simula la gestión de procesos, la memoria y la ejecución de múltiples algoritmos. 

Con una interfaz gráfica intuitiva, el simulador permite observar en tiempo real cómo los algoritmos programan y gestionan los procesos, mostrando el comportamiento del sistema bajo diferentes escenarios. 

## Versiones

### V1.0.3 - FCFS (First-Come, First-Served)
**Descripción:**
El algoritmo FCFS es un enfoque básico de planificación de procesos en sistemas operativos. Este simulador permite visualizar en tiempo real cómo se ejecutan los procesos siguiendo este algoritmo, mostrando cómo los procesos son programados en función de su orden de llegada.

**Características:**
- **Simulación Visual:** Observa cómo se programan y ejecutan los procesos según su llegada.
- **Interacción Directa:** Agregar, pausar, interrumpir, terminar, reanudar y mostrar información de los procesos.
- **Métricas de Desempeño:** Mide el tiempo de retorno, tiempo de espera y tiempo de respuesta de los procesos.

**Instrucciones de Uso:**
1. Descarga la aplicación.
2. Ejecuta el programa.
3. Ingresa el número de procesos iniciales o crea tu propio proceso.
4. Inicia el simulador.
5. Interactúa con las teclas: "i", "e", "p", "c", "n", "b" para manipular los procesos.
6. Analiza las métricas de desempeño.

---

### V1.04 - Round Robin (RR)
**Descripción:**
El algoritmo Round Robin es una variante del FCFS que asigna un tiempo o quantum fijo a cada proceso. Esto previene la inanición (starvation) y mejora la equidad y el tiempo de respuesta. 

**Características:**
- **Simulación Visual:** Observa cómo se alternan los procesos en función de su quantum.
- **Interacción Directa:** Agrega, pausa, interrumpe, termina, reanuda y muestra información de los procesos.
- **Métricas de Desempeño:** Calcula y muestra el tiempo de retorno, tiempo de espera y tiempo de respuesta.
- **Quantum Personalizado:** Ajusta el quantum desde la interfaz.

**Instrucciones de Uso:**
1. Descarga la aplicación.
2. Ejecuta el programa.
3. Ingresa el número de procesos iniciales.
4. Ingresa el valor del quantum antes de iniciar el simulador.
5. Inicia el simulador y usa las teclas para interactuar.

---

### V1.05 - Paginación (Gestión de Memoria)
**Descripción:**
La paginación es una técnica de gestión de memoria que divide el espacio de memoria en unidades fijas llamadas marcos. Los procesos se dividen en páginas de tamaño igual que se cargan en los marcos bajo demanda, optimizando el uso de la memoria y evitando la fragmentación externa.

**Características:**
- **Simulación Visual:** Visualiza cómo se asignan los marcos a las páginas de los procesos.
- **Gestión Eficiente:** Optimiza el uso de memoria y reduce el tiempo de carga de los procesos.
- **Interacción Directa:** Manipula los procesos y muestra las métricas de desempeño y memoria.
- **Parámetros Personalizables:** Ajusta el número de marcos, tamaño de los marcos y páginas desde la interfaz.
- **Estado de Memoria:** Muestra el estado de la memoria en tiempo real, incluyendo marcos disponibles y ocupados.

**Instrucciones de Uso:**
1. Descarga la aplicación.
2. Ejecuta el programa.
3. Ingresa el número de procesos y ajusta el quantum.
4. Inicia el simulador.
5. Interactúa con las teclas: "i", "e", "p", "c", "n", "b", "t" para gestionar los procesos y la memoria.

---

### V2.0 - Suspensión de Procesos
**Descripción:**
La suspensión permite simular el proceso de bloquear y reanudar procesos desde almacenamiento secundario (disco) en un sistema de gestión de memoria. Libera espacio en la memoria para otros procesos y permite reanudar los bloqueados cuando sea necesario.

**Características:**
- **Simulación Visual:** Observa cómo se suspenden y reanudan los procesos desde y hacia el disco.
- **Gestión Eficiente:** Optimiza el uso de la memoria y reduce el tiempo de bloqueo de los procesos.
- **Interacción Directa:** Agrega, pausa, interrumpe, termina, suspende y recupera procesos desde la interfaz.
- **Métricas de Desempeño:** Mide el tiempo de retorno, tiempo de espera y tiempo de respuesta de los procesos.
- **Estado de Memoria:** Muestra los marcos disponibles y ocupados, así como el estado de los procesos.

**Instrucciones de Uso:**
1. Descarga la aplicación.
2. Ejecuta el programa.
3. Ingresa el número de procesos iniciales.
4. Ingresa el quantum o déjalo por defecto.
5. Inicia el simulador y usa las teclas para interactuar.

---

### Resumen de cambios:

1. **Descripción general:** Se amplió para incluir todos los algoritmos y características del simulador, brindando contexto a cada versión del proyecto.
2. **Versiones detalladas:** Cada versión tiene su propio bloque con sus características y funcionalidades.
3. **Instrucciones de uso:** Se mantuvieron las instrucciones por versión y una guía para los usuarios nuevos.
   
---

## Cómo Usar

1. **Descarga el archivo ejecutable** desde la sección de "Releases" del repositorio (elige la versión deseada).
2. **Ejecuta el archivo** descargado (no es necesario instalar ni compilar nada).
3. **Sigue las instrucciones dentro del simulador** para interactuar y analizar los algoritmos de planificación de procesos.

---

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, abre un **issue** o envía un **pull request**.

---

## Licencia

Este proyecto está bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.


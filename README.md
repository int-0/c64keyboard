# c64keyboard

Información y utilidades para conectar un teclado original de Commodore 64 al
puerto GPIO de la Raspberry Pi. Las pruebas están realizadas en una RPi B+ pero
es fácilmente adaptable a cualquier otro modelo.

La conexión del teclado con el puerto se realiza pin a pin sin necesidad de
ningún hardware adicional. El problema de este tipo de conexión es que
utiliza casi todos los pines del puerto pero por otro lado es mucho más
sencillo y versátil (mi diagrama de conexiones es realmente una sugerencia).

===

Info and tools to connect a original Commodore 64 keyboard to Raspberry Pi
GPIO port. Tests are performed in a TPi B+ model, but it's easy to adapt
to any other model.

Coneection is performed pin to pin, without any additional hardware. The
problem with this connection is that 16 pins are used but it's easier
and flexible (in fact, my connection schema is a suggestion, you can use you
own schema).

// Int-0
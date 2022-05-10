# Normalización

El proceso de normalización consiste en separar datos de una tabla, que no tendrían que estar ahí porque va a ser redundante o genera anomalias en inserción borrado o modificación.

## Ejemplo

<Table>
    <tr>
        <td><b>Proveedor</b></td>
        <td><b>Artículo</b></td>
        <td><b>Cantidad</b></td>
        <td><b>Ciudad</b></td>
        <td><b>Distancia</b></td>
    </tr>
</Table>

Al tener esta estructura hay problemas como:

* Añadir simplemente un proveedor, no se podría hacer sin un pedido.
* Si se borra un pedido se corre el riesgo de borrar toda la información de un proveedor.
* La información del proveedor se repite.
* Si cambia alguna información del proveedor habría que ir actualizando fila por fila.

La solución a esto es descomponer en relaciones mas pequeñas, proceso al cual se le llama normalización.

Se podría obtener simplemente una tabla nueva con los proveedores y aislar la de pedidos, usando restricciones de integridad, pero se repetirían tambien las distancias a las ciudades innecesariamente, por lo que lo óptimo es dividir en 3 relaciones, ciudades con las distancias, proveedores con el código y ciudad y pedido con árticulo y cantidad.

## Dependencias Funcionales

Si tenemos dos atributos (atributo_1 y atributo_2), la dependencia funcional atributo_1 $\rightarrow$ atributo_2, se da si para un mismo valor de 1 existe un único valor de 2.

## Formas Normales de Codd

Estas formas son en cascada o lo que es lo mismo, si se cumple la 10 es que se cumplen las anteriores hasta 1.

1. Primera forma normal: para una fila no hay multiples valor en un atributo (no listas), esto ya de por si lo cumple el modelo relacional.
2. Segunda forma normal: cada atributo no funcional tiene dependencia funcional completa respecto de las claves candidatas.
    * Todos los atributos no funcionales dependerán funcionalmente del conjunto de **claves**, no de un subconjunto por separado.
3. Tercera forma normal: Ningun atributo no funcional depende transitivamente de alguna clave.
    * Ningún atributo no funcional puede depender funcionalmente de otro que no sea clave.

### Forma Normal Boyce-Codd

Es un caso mas restrictivo de la tercera forma normal de Codd.

Para toda dependencia funcional el implicante es clave o superclave. No es válido que sea un subconjunto de una superclave.

Con esta forma normal es suficiente para evitar redundancias y soluciona en su mayoría las anomalías (todas las descritas en el ejemplo), aunque no es infalible en este sentido.
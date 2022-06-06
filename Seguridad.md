# Seguridad 

## Principales riesgos y errores

* **SQL INJECTION:** es el principal riesgo.
* **BUFFER OVERFLOW:** desbordamiento de memoria, los punteros se sobreescriben y se accede a memoria que no le corresponde, violación de seguridad.
* **BRUTE FORCE ATTACK:** en autenticación (credenciales).
* **Network EAVESDROPPING:** intercepción de los datos en la red.
* **MALWARE.**
* **DDOS.**
* **Sistemas desactualizados.**
* **Configuraciones por defecto.**  
* **Sin cuentas dedicadas a administración.**
* **Cuentas sobre-privilegiadas.**
* **Auditación debil.**
* **No encriptación.**
* **Gestor de contraseñas y claves.**
* **Copias de seguridad no encriptadas.**
* **Usuarios y seguridad no monitoreada.**
* **Aplicaciones mal codificadas.**

## Prácticas buenas y sistemas de seguridad

* **Contraseñas fuertes y periódicas.**
* **Keys y contraseñas:** guardarlas de manera segura (encriptadas).
* **Autentificación del usuario:** uso de criptografía asimétrica y certificación (X.509, SHA).
* **Acceso y privilegios solo a fuentes seguras.**
* **Conexión y transacciones cifradas**: previene Network Eavesdropping, usa SSL/TLS (transporte y conexión).
* **Límite de operaciones:** previene DDOS y Brute force attack.
* **Firewall:** previene SQL INJECTION, Buffer Overflow, Malware.
* **Whitelist:** permite solo sql de unos whitelist, evita por tanto SQL INJECTION, se une a validación de inputs dado que tienen la misma finalidad. Estos métodos tambien previenen de Buffer overflow.
* **Encriptar con estandares en seguridad:** AES, 3DES, previene de Malware.
* **Limitar permisos:** acceso solo a operaciones SQL o datos estipulados.
* **Sistemas de detección de intrusiones.**

## Principios básicos de seguridad

1. Autenticación.
2. Autorización.
3. Encriptación.
4. Firewall.
5. Auditación.



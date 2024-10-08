Tenemos 2 maneras de extraer las secciones de un documento 10-K:
* Utilizando bookmarks
* Utilizando el TOC


Una vez tenemos las secciones en forma RAW, usamos un LLM para traducirlo a 
las secciones correspondientes de la SEC (problema de clasificacion) y por ultimo hariamos 

https://chatgpt.com/c/6703030c-da2c-800d-924a-5f029a35c33f

**TODO:**

* (Done) Preparar un prompt (YAML) donde se explican cada una de los items segun el documento de la SEC:
https://www.sec.gov/files/reada10k.pdf

* Hacer los prompts para cada una de las fases de tal forma que al final tengamos:
  * El nombre de la seccion con su item correspondiente (nombre en el documento y nombre "oficial")
  * La pagina de inicio
  * La pagina final

* Script completo en el que le damos un PDF y nos genera cada una de las secciones como un pdf

* Extraccion de tablas e imagenes de cada una de las secciones
* Analasis de la imagen mediante un modelo VLM
* Extraccion del texto en forma limpia de cada de las secciones y lo combinamos con elt texto explicativo de imagenes y tablas
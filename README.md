# Sistema de Recomendação de Filme

1. Download Python: https://www.python.org/downloads/   

2. Instalando dependencias:  
`sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev`  

3. Instalando Python:  
  Descompacte o python  
  Entre na pasta do Python pelo terminal e digite:   
  `./configure`,  
  `sudo make`   
  `sudo make install`  
  Apontando para o Python instalado: `version=3.6.2`  

4. Dentro do terminal entre na pasta deste projeto e digite: `python3`  

5. Recomendação para usuario usando uma tabela pequena:  
    `from getRecommendation import getRecommendationSmallTable`  
    `getRecommendationSmallTable()`  

6. Recomendação para usuario usando o Movie Lens de 100 mil entradas:  
  `from getRecommendation import getRecommendationMovieLens`  
  `getRecommendationMovieLens()`  

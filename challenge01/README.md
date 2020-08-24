# Challenge 01

Challenge prompt:

>Durante toda a Maratona utilizaremos containers como base de desenvolvimento bem como para produção. Logo, ter uma noção básica de Docker é mais do que necessário.

> Nesse desafio, você terá de criar uma imagem docker que quando executada deverá expor a porta 8080 exibindo a mensagem: Eu sou Full Cycle.

> Fique na liberdade para utilizar a tecnologia/linguagem de programação de sua escolha. Exemplo: você poderá criar uma simples aplicação usando Node.js com Express para exibir essa mensagem.
Gere o build da sua imagem, faça o push para o DockerHub e a informe no formulário abaixo.

Found [here](http://maratona.fullcycle.com.br/desafios/hello-world-com-docker/).

## Installation


### Docker install

Pull the image from DockerHub:
```bash
docker pull deadpyxel/fullcycle-challenge01
```

Then run it as a container:

```bash
docker run --rm -p 8080:8080 deadpyxel/fullcycle-challenge01
```

### From source

>TODO

## Usage 

If you make a GET request at the root endpoint (`http://localhost:8080/`) you should see the following plain text message:
```md
Eu sou Full Cycle
```

If you make a GET requrst passing in a formatting param (only supported JSON at this moment), example `http://localhost:8080/?format=json` you should get the following JSON response:
```json
{"message": "Eu sou FullCycle"}
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
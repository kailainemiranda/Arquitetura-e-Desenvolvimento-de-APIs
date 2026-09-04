# QUESTÃO 5 — RacesList.vue, Axios, v-for e CORS

O componente `RacesList.vue` utiliza a biblioteca Axios para realizar uma requisição HTTP GET à API de corridas.

A função assíncrona `fetchRaces()` aguarda a resposta da API e armazena os dados recebidos na variável `races`.

A diretiva `v-for` percorre a lista de corridas e cria os elementos da interface para cada registro.

Exemplo:

```javascript
async function fetchRaces() {
  const response = await axios.get("http://127.0.0.1:8000/races");
  races.value = response.data;
}
```

No template:

```html
<div v-for="race in races" :key="race.id">
  {{ race.nome }}
</div>
```

O CORS é utilizado no FastAPI para permitir a comunicação entre aplicações executadas em origens diferentes, como um front-end Vue.js e um back-end FastAPI executados em portas diferentes.

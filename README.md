# EduConnect

**EduConnect** é uma plataforma web desenvolvida com Flask e MySQL, projetada para facilitar a comunicação e a gestão entre estudantes, professores e instituições de ensino. O sistema oferece funcionalidades básicas de cadastro e autenticação de usuários, além de permitir interações entre as partes envolvidas.

# Projeto em DESENVOLVIMENTO
**A plataforma EduConnect não está pronta e está em construção, portanto, em caso de BUGS, má funcionalidade, erro ou sugestões, contate o discord de: `yuchironozora`** **CSS FEITO TEMPORARIAMENTE COM USO DE IA'S.**

## Funcionalidades

- **Gestão de usuários**: Cadastro e login de estudantes, professores e administradores.
- **Autenticação**: Proteção das rotas com login seguro.

## Tecnologias Utilizadas

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Banco de Dados**: MySQL

## Estrutura do Projeto

- `/static`: Arquivos estáticos (CSS, JS, imagens)
- `/templates`: Templates HTML para renderização das páginas
- `/models`: Definições dos modelos e interações com o banco de dados
- `/blueprints` // `routes.py`: Definições das rotas e lógica de controle
- `/config`: Arquivos de configuração da aplicação

## Requisitos

- Python 3.x
- MySQL
- Bibliotecas Python especificadas no `requirements.txt`

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/shirokkkj/EduConnect.git
   ```
2. Navegue até o repositório
   ```bash
   cd EduConnect
   ```
3. Instale os requirements
   ```bash
   Futuramente será criado o requirements.txt, por enquanto, instale as dependências do projeto por necessidade...
   ```

4. Instale o [MYSQL e o MYSQL WorkBench](https://dev.mysql.com/downloads/installer/)


5. Crie um arquivo ``env`` com as informações necessárias para a conexão com o banco de dados.

6. Execute e navegue até o WebSite
     ```bash
      python main.py
      localhost:5000/home
    ```

## Faça os seus TESTES
1. Para entrar com um login escolar, entre com a rota:
   ```bash
   localhost:5000/register
   ```
   Faça o seu registro com quaisquer informações, na sidebar, clique em 'Junte-se' e faça o registro da sua escola. Após isso, você já estará permitido a criar, editar e trancar matrículas.

2. Para entrar com um login estudantil, ente com a rota:
   ```bash
   localhost:5000/login
   ```
   Selecione uma das escolas que você criou e digite o CPF de um aluno que esteja registrado naquela escola. Feito isso, a única seção disponível, por enquanto, será a de visualizar a sua própria matrícula.
   


## Contribuição
**Contribuições são bem-vindas! Para contribuir:**

1. Faça um fork do projeto

2. Crie uma branch para sua feature:

```bash
git checkout -b minha-feature
```
3. Envie um pull request.

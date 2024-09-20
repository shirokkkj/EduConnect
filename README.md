# EduConnect

**EduConnect** é uma plataforma web desenvolvida com Flask e MySQL, projetada para facilitar a comunicação e a gestão entre estudantes, professores e instituições de ensino. O sistema oferece funcionalidades básicas de cadastro e autenticação de usuários, além de permitir interações entre as partes envolvidas.

## Funcionalidades

- **Gestão de usuários**: Cadastro e login de estudantes, professores e administradores.
- **Autenticação**: Proteção das rotas com login seguro.
- **Sistema de comunicação**: Troca de mensagens entre usuários.

## Tecnologias Utilizadas

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Banco de Dados**: MySQL

## Estrutura do Projeto

- `/static`: Arquivos estáticos (CSS, JS, imagens)
- `/templates`: Templates HTML para renderização das páginas
- `/models`: Definições dos modelos e interações com o banco de dados
- `/views`: Definições das rotas e lógica de controle
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
   pip install -r requirements.txt
   ```

4. Instale o [MYSQL e o MYSQL WorkBench](https://dev.mysql.com/downloads/installer/)

5. Execute e navegue até o WebSite
     ```bash
      python main.py
      localhost:5000/home
    ```


## Contribuição
**Contribuições são bem-vindas! Para contribuir:**

1. Faça um fork do projeto

2. Crie uma branch para sua feature:

```bash
git checkout -b minha-feature
```
3. Envie um pull request.

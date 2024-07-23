#Importações e Inicialização:

from flask import Flask, request, render_template_string, session, redirect, url_for
'''
Flask: Importa o framework Flask para criar a aplicação web.
request: Permite acessar dados enviados pelo cliente (neste caso, dados dos formulários).
render_template_string: Permite renderizar HTML a partir de uma string.
session: Armazena informações do usuário entre diferentes requisições.
redirect: Redireciona o usuário para outra rota.
url_for: Gera URLs para funções de rota.
'''
app = Flask(__name__)
app.secret_key = "supersecretkey"
'''
Flask(name): Cria uma instância da aplicação Flask.
app.secret_key: Define uma chave secreta para gerenciar sessões de forma segura.
'''
#Dados do Quiz:
'''
questions: Uma lista de dicionários onde cada dicionário representa uma pergunta do quiz com suas opções e a resposta correta.
'''
questions = [
    {"question": "O que é Python?", "options": ["Uma linguagem de programação", "Um tipo de banco de dados", "Um sistema operacional"], "answer": "Uma linguagem de programação"},
    {"question": "Qual é a extensão padrão para arquivos Python?", "options": [".py", ".java", ".txt"], "answer": ".py"},
    {"question": "Qual função é usada para imprimir algo na tela no Python?", "options": ["print()", "echo()", "display()"], "answer": "print()"},
    {"question": "Como você define uma função em Python?", "options": ["function myFunction()", "def myFunction()", "create myFunction()"], "answer": "def myFunction()"},
    {"question": "Qual destas é uma estrutura de dados imutável em Python?", "options": ["Lista", "Dicionário", "Tupla"], "answer": "Tupla"},
    {"question": "Como você cria um comentário em Python?", "options": ["// comentário", "# comentário", "/* comentário */"], "answer": "# comentário"},
    {"question": "Qual função é usada para obter a entrada do usuário no Python?", "options": ["input()", "get_input()", "read()"], "answer": "input()"},
    {"question": "Qual palavra-chave é usada para criar uma classe em Python?", "options": ["class", "create", "define"], "answer": "class"},
    {"question": "Como você importa um módulo em Python?", "options": ["import modulo", "use modulo", "include modulo"], "answer": "import modulo"},
    {"question": "Qual operador é usado para atribuir um valor a uma variável em Python?", "options": ["==", "=", "::"], "answer": "="}
]


#Rota Home:
'''
@app.route("/"): Define a rota para a página inicial do quiz.
home(): Inicializa a sessão com a pergunta atual como 0 e a pontuação como 0. Redireciona para a rota /question.
'''
@app.route("/")
#Rota: Define a rota raiz ("/") da aplicação. Quando um usuário acessa a URL principal da aplicação, esta função é executada.

def home():
    #Função home(): Esta função é chamada quando um usuário acessa a rota /.
    session["current_question"] = 0
    # session["current_question"] = 0: Define o índice da pergunta atual como 0, iniciando o quiz com a primeira pergunta.
    session["score"] = 0
    # session["score"] = 0: Define a pontuação inicial como 0.
    return redirect(url_for("question"))
    #Redirecionamento: Redireciona o usuário para a rota /question (a página onde as perguntas do quiz são exibidas). url_for("question") gera a URL da função question com base no nome da função.


@app.route("/question", methods=["GET", "POST"])
    #Rota e Métodos: Define a rota /question, que aceita tanto métodos GET quanto POST. O método GET é usado para exibir a página, enquanto o POST é usado para processar respostas enviadas pelo usuário.
def question():
    #Esta função é chamada quando o usuário acessa a rota /question ou envia uma resposta para a mesma.
    if request.method == "POST":
        selected_option = request.form.get("option")
        current_question = session.get("current_question")
        if questions[current_question]["answer"] == selected_option:
            session["score"] += 1
        session["current_question"] += 1
    #Processamento de Resposta (POST):
    '''
    if request.method == "POST":: Verifica se a requisição é um POST (significa que o usuário enviou uma resposta).

    selected_option = request.form.get("option"): Obtém a opção selecionada pelo usuário a partir dos dados do formulário.

    current_question = session.get("current_question"): Obtém o índice da pergunta atual da sessão.

    if questions[current_question]["answer"] == selected_option:: Verifica se a resposta selecionada está correta comparando-a com a resposta correta armazenada.

    Se correta, a pontuação (session["score"]) é incrementada.

    session["current_question"] += 1: Avança para a próxima pergunta.
    '''

    #Verificação de Término do Quiz:
    current_question = session.get("current_question")
    if current_question >= len(questions):
        return redirect(url_for("result"))
    '''
    current_question = session.get("current_question"): Obtém o índice da pergunta atual. 

    if current_question >= len(questions):: Verifica se o índice da pergunta atual é maior ou igual ao número total de perguntas, o que indica que todas as perguntas foram respondidas.

    return redirect(url_for("result")): Redireciona o usuário para a página de resultados se o quiz estiver completo.
    '''

    #Renderização da Pergunta:
    '''
    question_data = questions[current_question]: Obtém os dados da pergunta atual.

    return render_template_string(...): Renderiza uma string HTML que exibe a pergunta e suas opções. As opções são geradas dinamicamente a partir do question_data.
    '''
    question_data = questions[current_question]
    return render_template_string("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz Python</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        :root {
            font-size: 62.5%;
        }
        body {
            font-size: 1.6rem;
            font-weight: 400;
            line-height: 1.6;
            font-family: Arial, sans-serif;
            background-color: #0b0d21;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-image: url(/static/images/fundo.jpg);
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
        }
        .container {
            background-color: transparent;
            border: 1px solid #fff;
            backdrop-filter: blur(2rem);
            padding: 3rem;
            border-radius: 0.8rem;
            max-width: 90%;
            width: 400px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        h1 {
            color: #fff;
            margin-bottom: 2rem;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
        }
        .logo {
            width: 20%;
            max-width: 80px;
        }
        h2 {
            color: #fff;
            margin: 2rem 0;
            text-align: center;
        }
        form {
            display: flex;
            flex-direction: column;
            width: 100%;
        }
        label {
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
        }
        input[type="radio"] {
            margin-right: 1rem;
        }
        button {
            padding: 1rem 2rem;
            border-radius: 0.3rem;
            background-color: #002859;
            border: none;
            color: #fff;
            cursor: pointer;
            margin-top: 1rem;
        }
        button:hover {
            background-color: #ffd400;
        }
    </style>
</head>
<body>
    <main class="container">
        <h1>
            Quiz de Python
            <img class="logo" src="/static/images/logo.png" alt="Logo">
        </h1>
        <h2>{{ question_data["question"] }}</h2>
        <form method="post">
            {% for option in question_data["options"] %}
                <label>
                    <input type="radio" name="option" value="{{ option }}" required> {{ option }}
                </label>
            {% endfor %}
            <button type="submit">Próxima</button>
        </form>
    </main>
</body>
</html>
    """, question_data=question_data)
    #Rota de Resultados
    '''
    @app.route("/result"): Define a rota para a página de resultados.

    result(): Obtém a pontuação do usuário e o total de perguntas e renderiza a página de resultados mostrando o número de perguntas acertadas e o total.
    '''
@app.route("/result")
def result():
    score = session.get("score", 0)
    total_questions = len(questions)
    return render_template_string("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado do Quiz</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        :root {
            font-size: 62.5%;
        }
        body {
            font-size: 1.6rem;
            font-weight: 400;
            line-height: 1.6;
            font-family: Arial, sans-serif;
            background-color: #0b0d21;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-image: url(/static/images/fundo.jpg);
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
        }
        .container {
            background-color: transparent;
            border: 1px solid #fff;
            backdrop-filter: blur(2rem);
            padding: 3rem;
            border-radius: 0.8rem;
            max-width: 90%;
            width: 400px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        h1 {
            color: #fff;
            margin-bottom: 2rem;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
        }
        .logo {
            width: 20%;
            max-width: 80px;
        }
        p {
            color: #fff;
            font-size: 1.8rem;
            text-align: center;
        }
        a {
            display: inline-block;
            padding: 1rem 2rem;
            margin-top: 2rem;
            border-radius: 0.3rem;
            background-color: #002859;
            color: #fff;
            text-decoration: none;
            text-align: center;
        }
        a:hover {
            background-color: #ffd400;
        }
    </style>
</head>
<body>
    <main class="container">
        <h1>
            Resultado do Quiz
            <img class="logo" src="/static/images/logo.png" alt="Logo">
        </h1>
        <p>Você acertou {{ score }} de {{ total_questions }} perguntas.</p>
        <a href="/">Reiniciar Quiz</a>
    </main>
</body>
</html>
    """, score=score, total_questions=total_questions)
#Execução da Aplicação:
#app.run(debug=True): Inicia o servidor Flask com o modo de depuração ativado, permitindo a atualização automática do código e o detalhamento de erros.
if __name__ == "__main__":
    app.run(debug=True)

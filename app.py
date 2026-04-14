from flask import Flask

app = Flask(__name__)

@app.route("/")
def loja():
    return """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Carla Bordado</title>

<style>
body {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #ffb6c1, #87cefa);
    overflow-x: hidden;
}

/* CONTAINER */
.card {
    width: 92%;
    max-width: 420px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    background: rgba(255,255,255,0.25);
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    text-align: center;
}

/* TITULO */
h1 {
    font-size: 24px;
    margin-bottom: 5px;
}

p {
    margin-top: 0;
    font-size: 14px;
}

/* INPUTS */
select, input {
    width: 100%;
    padding: 14px;
    margin-top: 12px;
    border-radius: 12px;
    border: none;
    font-size: 16px;
}

/* BOTÕES GRANDES (dedo) */
button {
    width: 100%;
    padding: 18px;
    margin-top: 12px;
    border-radius: 30px;
    border: none;
    font-size: 18px;
    font-weight: bold;
}

/* CALCULAR */
.btn-calc {
    background: white;
}

.btn-calc:active {
    transform: scale(0.95);
}

/* WHATSAPP */
.btn-whats {
    background: #25D366;
    color: white;
    font-size: 20px;
    animation: glow 1.5s infinite;
}

@keyframes glow {
    0% {box-shadow: 0 0 5px #25D366;}
    50% {box-shadow: 0 0 15px #25D366;}
    100% {box-shadow: 0 0 5px #25D366;}
}

/* TOTAL */
#total {
    margin-top: 10px;
    font-size: 20px;
}

/* RESUMO */
.resumo {
    font-size: 14px;
    margin-top: 10px;
}

/* FLORES (mais leve pro celular) */
span {
    position: absolute;
    top: -50px;
    pointer-events: none;
    animation: cair linear infinite;
    opacity: 0.8;
}

@keyframes cair {
    0% { transform: translate(0,0) rotate(0deg); }
    100% { transform: translate(var(--direcao), 100vh) rotate(360deg); }
}
</style>

</head>

<body>

<div class="card">

<h1>🌸 Carla Bordado</h1>
<p>Carla Andreia</p>

<input type="text" id="nome" placeholder="Seu nome">

<select id="produto">
<option value="40">Toalha Pequena - R$40</option>
<option value="60">Toalha de Rosto - R$60</option>
<option value="130">Toalha de Banho - R$130</option>
</select>

<input type="number" id="qtd" value="1" min="1">

<button class="btn-calc" onclick="calcular()">Calcular Pedido</button>

<h2 id="total">Total: R$0</h2>

<div class="resumo" id="resumo"></div>

<a id="link" target="_blank">
<button class="btn-whats">Finalizar no WhatsApp</button>
</a>

</div>

<script>
function calcular() {
    let nome = document.getElementById("nome").value || "Cliente";

    let produto = document.getElementById("produto");
    let preco = parseFloat(produto.value);
    let nomeProduto = produto.options[produto.selectedIndex].text;

    let qtd = parseInt(document.getElementById("qtd").value);

    let total = preco * qtd;

    document.getElementById("total").innerText = "Total: R$ " + total;

    document.getElementById("resumo").innerHTML =
        `<b>${nome}</b><br>${nomeProduto}<br>Qtd: ${qtd}`;

    let numero = "5599984178717";

    let msg = `Olá, Carla! 😊
Meu nome é ${nome}

🧵 ${nomeProduto}
📦 Quantidade: ${qtd}
💰 Total: R$${total}`;

    document.getElementById("link").href =
        "https://wa.me/" + numero + "?text=" + encodeURIComponent(msg);
}

/* FLORES OTIMIZADAS */
function criarFlor() {
    const flor = document.createElement("span");
    flor.innerText = "🌸";

    flor.style.fontSize = (Math.random() * 20 + 15) + "px";
    flor.style.left = Math.random() * 100 + "vw";

    let duracao = Math.random() * 5 + 5;
    flor.style.animationDuration = duracao + "s";

    let direcao = (Math.random() - 0.5) * 200;
    flor.style.setProperty('--direcao', direcao + "px");

    document.body.appendChild(flor);

    setTimeout(() => flor.remove(), duracao * 1000);
}

setInterval(criarFlor, 400);
</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
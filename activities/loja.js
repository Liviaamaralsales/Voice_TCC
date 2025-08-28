const btnContadorCarrinho = document.getElementById('btn-carrinho');
const carrinho = document.getElementById('carrinho-lateral');
const itensCarrinho = document.getElementById("itens-carrinho");
const totalCarrinho = document.getElementById('total-carrinho');
const contadorQuantidade = document.getElementById('contador-quantidade');    
const btnFinalizar = document.getElementById('btn-finalizar');

// objeto que armazena os produtos adicionados ao carrinho
let carrinhoProdutos = {};

contadorQuantidade.style.display = 'none';

function formatarPreco(valor) {
    return valor.toLocaleString('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    });
}

function configurarBotoesAdicionarCarrinho() {
    document.querySelectorAll('.botao-carrinho').forEach((botao) => {
        botao.addEventListener('click', () => {
            const produtoEl = botao.closest('.produto');

            // captura os dados do produto
            const descricao = produtoEl.querySelector('.descricao').textContent.trim();
            const precoTexto = produtoEl.querySelector('.preco').textContent.trim();
            const preco = parseFloat(precoTexto.replace('R$', '').replace('.', '').replace(',', '.'));
            const imgEl = produtoEl.querySelector('img');
            const imgSrc = imgEl ? imgEl.src : '';

            // verifica se o produto já está no carrinho
            if (carrinhoProdutos[descricao]) {
                carrinhoProdutos[descricao].quantidade += 1;
            } else {
                carrinhoProdutos[descricao] = {
                    descricao,
                    preco,
                    quantidade: 1,
                    imgSrc
                };
            }

            atualizarCarrinho();
        });
    });
}

function atualizarCarrinho() {
    itensCarrinho.innerHTML = '';
    let total = 0;
    let quantidadeTotal = 0;

    for (let key in carrinhoProdutos) {
        const item = carrinhoProdutos[key];
        total += item.preco * item.quantidade;
        quantidadeTotal += item.quantidade;

        const divItem = document.createElement('div');
        divItem.classList.add('item-carrinho');
        divItem.innerHTML = `
            <img src="${item.imgSrc}" alt="${item.descricao}">
            <div>
                <p>${item.descricao}</p>
                <p>${formatarPreco(item.preco)}</p>
                <p>Qtd: ${item.quantidade}</p>
                <button class="btn-remover" data-produto="${item.descricao}">Remover</button>
            </div>
        `;
        itensCarrinho.appendChild(divItem);
    }

    totalCarrinho.textContent = `Total: ${formatarPreco(total)}`;
    contadorQuantidade.style.display = quantidadeTotal > 0 ? 'block' : 'none';
    contadorQuantidade.textContent = quantidadeTotal;

    configurarBotoesRemover();
}

function configurarBotoesRemover() {
    document.querySelectorAll('.btn-remover').forEach((btn) => {
        btn.addEventListener('click', () => {
            const descricao = btn.getAttribute('data-produto');
            if (carrinhoProdutos[descricao]) {
                carrinhoProdutos[descricao].quantidade -= 1;
                if (carrinhoProdutos[descricao].quantidade === 0) {
                    delete carrinhoProdutos[descricao];
                }
            }
            atualizarCarrinho();
        });
    });
}

// abre e fecha o carrinho lateral
btnContadorCarrinho.addEventListener('click', () => {
    carrinho.classList.toggle('aberto');
});

// finaliza a compra
btnFinalizar.addEventListener('click', () => {
    window.location.href = 'finalizar.html';
});

// inicializa os botões
configurarBotoesAdicionarCarrinho();

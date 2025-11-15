// Função para aplicar o tema em todas as páginas
function aplicarTemaGlobal() {
    const temaSalvo = localStorage.getItem('tema');
    if (temaSalvo === 'escuro') {
        document.body.classList.add('dark-theme');
    } else {
        document.body.classList.remove('dark-theme');
    }
}

// Aplica o tema ao carregar a página
document.addEventListener('DOMContentLoaded', aplicarTemaGlobal);

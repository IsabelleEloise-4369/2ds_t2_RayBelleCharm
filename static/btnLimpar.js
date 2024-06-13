// Adicionando o manipulador de eventos ao botão "Limpar Carrinho"
function btnLimpar() {
    // Seleciona a lista do carrinho de compras
    const carrinho = document.getElementById('cartItems');
    
    // Remove todos os itens da lista
    carrinho.innerHTML = '';
};
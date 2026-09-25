function calcularPrioridade(dado) {
  const pontuacao = dado.valorNegocio * 0.3 + dado.risco * 0.3 + dado.uso * 0.2 + dado.compliance * 0.1 + dado.sensibilidade * 0.1;
  return pontuacao;
}

const dados = [
  { nome: 'Tabela Clientes', valorNegocio: 9, risco: 8, uso: 10, compliance: 6, sensibilidade: 7 },
  { nome: 'Tabela Fornecedores', valorNegocio: 6, risco: 5, uso: 7, compliance: 4, sensibilidade: 3 }
];

dados.forEach(d => {
  console.log(`${d.nome} : Prioridade ${calcularPrioridade(d)}`);
});
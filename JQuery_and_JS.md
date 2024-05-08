# Implementação da lógica de programação com JavaScript puro e jQuery

## Este exemplo demonstra como implementar uma lógica de programação simples usando JavaScript puro e jQuery para lidar com eventos de mudança em um elemento <select>. 

### jQuery:

// JQUERY
$("#selectAno").on("change", function() {
  $selectMes = $("#selectMes")        

  if ($(this).val()) {
    $selectMes.prop("disabled", false)
    return;
  }
  $selectMes.prop("disabled", true).val("")
})
// JQUERY

No código acima, utilizamos jQuery para selecionar o elemento com o ID "selectAno"
e adicionamos um ouvinte de evento de mudança. Quando o valor do <select> é alterado,
verificamos se o valor é verdadeiro. Se for, habilitamos o elemento <select> com o
ID "selectMes"; caso contrário, desabilitamos o elemento e limpamos o valor selecionado.

JavaScript puro:

// JavaScript
const selectAno = document.querySelectorAll("#selectAno");
for (let i = 0; i < selectAno.length;  i++){
  selectAno[i].addEventListener('change', function(){
    console.log(this)
  })
}
// JavaScript

No código JavaScript puro acima, selecionamos todos os elementos com o ID "selectAno"
usando document.querySelectorAll(). Em seguida, adicionamos um ouvinte de evento de 
mudança a cada um desses elementos. Quando o valor de um <select> é alterado, o 
console.log(this) é acionado, exibindo o elemento <select> que disparou o evento de mudança.

Ambos os trechos de código alcançam o mesmo resultado, mas utilizando abordagens diferentes.
O jQuery simplifica a seleção de elementos e a manipulação de eventos, enquanto o JavaScript
puro oferece uma implementação mais direta e leve.

Escolha a abordagem que melhor se adequa ao seu projeto e às suas preferências de desenvolvimento.

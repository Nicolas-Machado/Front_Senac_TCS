// Using jquery.inputmask: https://github.com/RobinHerbots/jquery.inputmask
// For 8 digit phone fields, the mask is like this: (99) 9999-9999
// For 9 digit phone fields the mask is like this: (99) 99999-9999
// function setupPhoneMaskOnField(selector){
//     var inputElement = $(selector)
  
//     setCorrectPhoneMask(inputElement);
//     inputElement.on('input, keyup', function(){
//       setCorrectPhoneMask(inputElement);
//     });
//   }
  
//   function setCorrectPhoneMask(element){
//     if (element.inputmask('unmaskedvalue').length > 10 ){
//       element.inputmask('remove');
//       element.inputmask('(99) 9999[9]-9999')
//     } else {
//       element.inputmask('remove');
//       element.inputmask({mask: '(99) 9999-9999[9]', greedy: false})
//     }
//   }
  
//   $(document).ready(function(){
//       setupPhoneMaskOnField('#phone-number')
//   });

/* Máscaras ER */
function mascara(o,f){
  v_obj=o
  v_fun=f
  setTimeout("execmascara()",1)
}
function execmascara(){
  v_obj.value=v_fun(v_obj.value)
}
function mtel(v){
  v=v.replace(/\D/g,""); //Remove tudo o que não é dígito
  v=v.replace(/^(\d{2})(\d)/g,"($1) $2"); //Coloca parênteses em volta dos dois primeiros dígitos
  v=v.replace(/(\d)(\d{4})$/,"$1-$2"); //Coloca hífen entre o quarto e o quinto dígitos
  return v;
}
function id( el ){
return document.getElementById( el );
}
window.onload = function(){
id('telefone').onkeyup = function(){
  mascara( this, mtel );
}
}
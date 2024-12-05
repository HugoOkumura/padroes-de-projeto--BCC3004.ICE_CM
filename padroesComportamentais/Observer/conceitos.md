<h1>Observer</h1> 

<h3>Conceito</h3>
<p>  Observer é um padrão de projeto comportamental que define um sistema de assinatura, o qual notifica varios objetos sobre algum evento que acontece a um objeto que está sendo observado.</p>

<h3>Problema que resolve</h3>
<p>Permite que objetos reajam a outro sem criar um forte acoplamento entre eles./p>

<h3>Quando devo usar</h3>
<ul>
  <li>Quando as alterações de um objeto levarem a alteração de outros objetos, e, o conjunto de objetos for desconhecido ou tem mudanças dinámicas.</li>
  <li>Quando alguns objetos tem que observar outros mas apenas por um tempo limitado ou em casos específicos.</li>
</ul>

<h3>Vantagens</h3>
<ul>
  <li>Principio aberto/fechado: mais observadores podem ser introduzidos sem ter que mudar o código do objeto observado.</li>
  <li>As relações podem ser feitas entre objetos durante a execução.</li>
</ul>

<h3>Desvantagens</h3>
 <ul> 
  <li>A ordem em que observadres são notificados é aleatória.</li>
</ul>

<h4>Referencias</h4>
<a href='https://refactoring.guru/design-patterns/observer'>Refactoring Guru</a>

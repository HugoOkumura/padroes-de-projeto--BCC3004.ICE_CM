<h1>Adapter</h1>
<h3>Conceito</h3>
<p>O padrão de projeto Adapter (ou Adaptador) é um padrão estrutural que tem como objetivo integrar classes com interfaces incompatíveis, permitindo que elas trabalhem juntas sem precisar alterar seus códigos originais. Ele atua como um "adaptador" ou "ponte" que converte a interface de uma classe em outra que o cliente espera.</p>


<h3>Problema que resolve</h3>
<p>O padrão de projeto Adapter resolve o problema de incompatibilidade de interfaces entre classes ou sistemas que precisam trabalhar juntos, mas possuem métodos ou estruturas de dados incompatíveis.</p>

<h3>Quando devo usar</h3>
<ul>
    <li>Quando um sistema antigo (legado) precisa ser incorporado em um novo sistema, mas suas interfaces não são compatíveis. </li>
    <li>Quando você deseja utilizar uma biblioteca externa ou componente de terceiros que não segue a interface do seu sistema. </li>
</ul>

<h3>Vantagens</h3>
<ul>
    <li>Reutilização de código existente, possibilidade de utilizar uma biblioteca que antes seria imcopativel por problema com interface.</li>
    <li>Facilidade de introdução de novas funcionalidades sem alterar o código original.</li>
</ul>

<h3>Desvantagens</h3>
<ul>
    <li>Maior complexidade no design do sistema.</li>
    <li>Possível sobrecarga de desempenho, devido à introdução de camadas adicionais entre as classes.</li>
</ul>

<h3>Referencias</h3>
<a href="https://refactoring.guru/pt-br/design-patterns/adapter">Refactoring Guru</a>
<br/>
<a href="https://nosbielc.dev/posts/cod-28042023">nosbielc</a>
<br/>
<a href="https://openai.com/">ChatGPT</a>

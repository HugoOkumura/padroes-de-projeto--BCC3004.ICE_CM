<h1>Template Method</h1>
<h3>Conceito</h3>
<p>Template Method é um padrão de projeto comportamental que define o esqueleto de um algoritmo em uma 
classe base para que subclasses derivadas dela implmentem os paços específicos para elas mesmas.</p>


<h3>Problema que resolve</h3>
<p>Permite reutilizar lógica comum entre diferentes implementaçãoes, enquanto permite a especificação
de certas etapas. Evitando repetição de código e facilita a manutenção</p>

<h3>Quando devo usar</h3>
<ul>
    <li>Quando quiser que o usuário da classe extenda apenas algumas etapas do algoritmo, mas não ele inteiro. </li>
    <li>Quando várias classes tiverem rotinas muito similares, com apenas algumas diferenças essenciais. </li>
</ul>

<h3>Vantagens</h3>
<ul>
    <li>Reutilização de código: o algoritmo comum é implementado na superclasse, permitindo que classes herdades de executá-la.</li>
    <li>Manutenção: qualquer alteração no código das etapas é isolada nas próprias classes, evitando problemas de manutenção.</li>
</ul>

<h3>Desvantagens</h3>
<ul>
    <li>Alguns usuários podem ter uma limitação dependendo do esqueleto do algoritmo.</li>
    <li>Possível vioalão do princípio de subtituição de Liskov suprimindo uma implementação de etapa padrão por meio de uma subclasse.</li>
    <li>Dificuldade de manutenção conforme o número de etapas aumentam.</li>
</ul>

<h3>Referencias</h3>
<a href="https://refactoring.guru/design-patterns/template-method">Refactoring Guru</a>
ChatGPT
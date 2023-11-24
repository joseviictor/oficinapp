# README

Este README documenta as etapas necessárias para colocar seu aplicativo em funcionamento.

### Para que serve este repositório?

* Este repositório foi desenvolvido no âmbito da disciplina de "Ambientes de Desenvolvimento Colaborativo", sob a orientação do docente. O principal objetivo foi nos proporcionar uma experiência prática no desenvolvimento colaborativo de software, utilizando as melhores práticas e ferramentas modernas. Foi usada uma base fornecida pelo o docente onde foram feitas aplicadas algumas melhorias.
* Versão 0.5
* [Sintaxe básica de gravação e formatação no GitHub](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

### Como faço para configurar?

* **Resumo da Configuração:**
  * É preciso duas bibliotecas que estão inseridas no ficheiro `requirements.txt`.
  * A biblioteca `tabulate` é utilizada para formatar dados em tabelas de maneira legível.
  * O Sphinx é uma ferramenta de documentação que ajuda a organizar e formatar documentação de projetos.

* **Configuração:**
  * Para fazer a configuração temos de usar executar o ficheiro `requirements.txt`.
    * Usando o código:
      ```bash
      pip install -r requirements.txt
      ```

* **Dependências:**
  * Bibliotecas:
    * Tabulate
    * Sphinx

* **Configuração de Base de Dados...**
  * Para termos dados no nosso programa, é necessário executar o ficheiro `inserirdados.py`.
   * Esta classe irá ler os ficheiros que contêm dados. Por exemplo:
    ```python
    ler_ficheiro_csv('CLIENTE')
    ```
    O nome do ficheiro tem de concidir com o nome aqui inserido

      

#### Documentação

* Posteriormente deve configurar o ficheiro `doc\config.py` com as alterações que entenda necessárias (sphinx)
  **Tutorial de Criação da Documentação com Sphinx:**

  1. Certifique-se de que você está na raiz do projeto e que o Sphinx está instalado.
  
      ```bash
      pip install sphinx
      ```

  2. Execute o seguinte comando para gerar a estrutura inicial da documentação na pasta `docs`:

      ```bash
      sphinx-apidoc -F -a -e -o docs src/
      ```

      Isso criará os arquivos e diretórios necessários para a documentação.

  3. Limpe os arquivos temporários ou antigos, se necessário:

      ```bash
      .\make.bat clean
      ```

      Certifique-se de ajustar os comandos conforme necessário com base no sistema operativo que estás a utilizar.

  4. Por fim, gere a documentação HTML usando o seguinte comando:

      ```bash
      .\make.bat html
      ```

  5. A documentação gerada estará disponível na pasta `docs\_build\html`. Abra o arquivo `index.html` em um browser para visualizar a documentação.

  Lembrar que os dois primeiros comandos devem ser executados na pasta raiz do projeto.
  Os ultimos dois devem ser feitos na pasta docs que foi criada no segundo comandos

  PS.: Só sera preciso 3. 4. caso altere alguma documentação o 2. só sera executado caso crie um outro ficheiro

### Diretrizes de Contribuição

* **Testes de Escrita:**
  * Antes de submeter uma contribuição, certifique-se de testar e validar as suas alterações. Isso inclui verificar a sintaxe, corrigir erros e garantir que o código seja executado conforme esperado.

* **Padrões de Codificação:**
  * Siga as diretrizes do PEP 8 para Python.
  * Utilize comentários descritivos e significativos no código.
  * Garanta a legibilidade do código e evite alterações desnecessárias em espaços em branco.

* **Solicitações de Pull:**
  * Descreva detalhadamente as alterações realizadas na solicitação de pull.
  * Certifique-se de que sua solicitação de pull está associada a um problema existente ou crie um novo para discussão.

* **Revisão de Código:**
  * Todas as contribuições serão revistas por outros colaboradores. Certifique-se de que o seu código esteja claro, bem documentado e siga as melhores práticas. Aceite feedback construtivo durante o processo de revisão.

* **Processo de Revisão:**
  * As contribuições serão revisadas por membros do time antes da fusão.
  * Comentários construtivos serão fornecidos para melhorias, se necessário.

* **Outras Diretrizes:**
  * Respeite as convenções de nomenclatura existentes.
  * Mantenha o foco nas funcionalidades ou correções relacionadas ao escopo do projeto.
  * Seja respeitoso e colaborativo com outros membros da comunidade.
  * Informe-se sobre as práticas específicas de ramificação e fluxo de trabalho adotadas neste repositório.

### Com quem devo falar?

* **José Victor Santos (Dev & Repo Administrator):** <a56278@ualg.pt>
* **Marco Valente (Dev):** <a79302@ualg.pt>
* **Rodrigo Pimenta (Dev):** <a79311@ualg.pt>

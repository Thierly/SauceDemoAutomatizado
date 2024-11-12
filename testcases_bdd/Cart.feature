Feature: Carrinho

    Página que permite usuários selecionarem, organizarem e gerenciarem os produtos que pretendem comprar.

Scenario: Adicionar um produto ao carrinho 

    Given que estou logado na plataforma
    And seleciono o produto "Sauce Labs Backpack"
    When clico no botão "Add to cart"
    And clico no ícone do carrinho no canto superior direito
    Then o produto "Sauce Labs Backpack" é adicionado e exibido no carrinho

Scenario: Adicionar mais de um produto ao carrinho 

    Given que estou logado na plataforma
    And seleciono o produto "Sauce Labs Backpack"
    And seleciono dois itens
    When clico no botão "Add to cart"
    And clico no ícone do carrinho no canto superior direito
    Then o produto "Sauce Labs Backpack" é adicionado e exibido no carrinho

Scenario: Adicionar produtos diferentes ao carrinho 

    Given que estou logado na plataforma
    When clico no botão "Add to cart" no produto "Sauce Labs Backpack"
    And clico no botão "Add to cart" no produto "Sauce Labs Bike Light"
    And clico no ícone do carrinho no canto superior direito
    Then os dois produtos são adicionados e exibidos no carrinho

Scenario: Remover um item do carrinho 

    Given que estou logado na plataforma
    And estou na página do carrinho 
    And tenho adicionado pelo menos um produto no carrinho 
    When clico no botão "Remove" em baixo da descrição do item 
    Then o produto é removido do carrinho

Scenario: Verificar se o carrinho persiste ao fazer logout

    Given que eu estou logado na plataforma
    And tenho adicionado pelo menos um produto no carrinho
    When clico no ícone do canto superior esquerdo
    And  clico em logout
    And realizo o login com as mesmas credenciais
    And clico no ícone do carrinho no canto superior direito 
    Then o produto continua no carrinho 

Scenario: Carrinho vázio ao acessar a página do carrinho 

    Given  que eu estou logado na plataforma
    And não adicionei nenhum item ao carrinho 
    When clico no ícone do carrinho no canto superior direito
    Then o carrinho está vázio 

Scenario: Finalizar compra dos produtos do carrinho 

    Given que estou logado na plataforma
    And estou na página do carrinho 
    And tenho adicionado pelo menos um produto no carrinho 
    When clico no botão "Checkout"
    Then sou redirecionado para página de "Checkout"

Scenario: Adicionar um produto ao carrinho estando na página de descrição de produto

    Given que estou logado na plataforma
    And estou na página de descrição do produto "Sauce Labs Backpack"
    When clico no botão "Add to cart"
    Then o produto é adicionado ao carrinho

Scenario: Verificar se o produto persiste no carrinho após adiciona-lo pela página de descrição e voltar ao catálogo

    Given que estou logado na plataforma
    And estou na página de descrição do produto "Sauce Labs Backpack"
    When clico no botão "Add to cart"
    And clico no botão "Back" no canto superior direito da imagem do produto
    Then o produto é adicionado ao carrinho

Feature: Realizar compra

    Permite o usuário fazer o pedido e pagamento dos produtos selecionados do carrinho 

Scenario: Finalizar compra com sucesso 

    Given que estou logado na plataforma
    And estou na página do carrinho de compras
    And tenho pelo menos 1 item no carrinho
    When clico no botão "Checkout"
    And insiro a entrada "Joao" no campo "First Name"
    And insiro a entrada "Silva" no campo "Last Name"
    And insiro a entrada "000000000" no campo "Zip/Postal Code"
    And clico no botão "Continue"
    And clico no botão "Finish"
    Then o pedido é realizado com sucesso
    
Scenario: Finalizar compra com carrinho vázio 

    Given que estou logado na plataforma
    And estou na página do carrinho de compras
    When clico no botão "Checkout"
    Then uma mensagem de erro deve indicar que o carrinho está vázio

Scenario: Finalizar compra sem inserir entradas válidas no campo "First Name"

    Given que estou logado na plataforma
    And estou na página do carrinho de compras
    And tenho pelo menos 1 item no carrinho
    When clico no botão "Checkout"
    And não insiro entradas no campo "First Name"
    And insiro a entrada "Silva" no campo "Last Name"
    And insiro a entrada "000000000" no campo "Zip/Postal Code"
    And clico no botão "Continue"
    Then uma mensagem de erro é exibida informando que há campos inválidos

Scenario: Finalizar compra sem inserir entradas válidas no campo "Last Name"

    Given que estou logado na plataforma
    And estou na página do carrinho de compras
    And tenho pelo menos 1 item no carrinho
    When clico no botão "Checkout"
    And insiro a entrada "Joao" no campo "First Name"
    And não insiro entradas no campo "Last Name"
    And insiro a entrada "000000000" no campo "Zip/Postal Code"
    And clico no botão "Continue"
    Then uma mensagem de erro é exibida informando que há campos inválidos

Scenario: Finalizar compra sem inserir entradas válidas no campo "Zip/Postal Code"

    Given que estou logado na plataforma
    And estou na página do carrinho de compras
    And tenho pelo menos 1 item no carrinho
    When clico no botão "Checkout"
    And insiro a entrada "Joao" no campo "First Name"
    And insiro a entrada "Silva" no campo "Last Name"
    And não insiro entradas no campo "Zip/Postal Code"
    And clico no botão "Continue"
    Then uma mensagem de erro é exibida informando que há campos inválidos

Scenario: Cancelar compra antes de enviar informações

    Given que estou logado na plataforma
    And estou na página de Checkout
    When clico no botão "Cancel"
    Then sou redirecionado para a página de carrinho

Scenario: Cancelar compra depois de inserir as informações

    Given que estou logado na plataforma
    And estou na página de Checkout
    And preencho os campos com informações válidas
    And clico no botão "Continue"
    When clico no botão "Cancel"
    Then sou redirecionado para a página do carrinho 

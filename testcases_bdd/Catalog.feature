Feature: Catálogo

    Permite a visualização precisa dos produtos 

Scenario: Exibir o catálogo ao realizar login 

    Given que estou na página de login
    And insiro a entrada "standard_user" no campo "Username"
    And insiro a entrada "secret_sauce" no campo "Password"
    When clico  no botão "Login"
    Then quando logado o catálogo é exibido 

Scenario: Verificar se o catálogo é exibido por padrão em ordem alfabética(A a Z)

    Given  que estou logado na plataforma
    When clico no ícone de filtro de catálogo 
    Then o filtro está selecionado por padrão a opção "Name(A to Z)"

Scenario: Alterar o padrão de exibição do catálogo para ordem alfabética inversa(Z a A)

    Given que estou logado na plataforma
    When clico no ícone de filtro de catálogo
    And seleciono a opção "Name(Z to A)"
    Then os produtos do catálogos são exibidos pelo nome começando do "Z" até o "A"

Scenario: Alterar o padrão de exibição do catálogo, do produto com menor preço ao mais caro

    Given que estou logado na plataforma
    When clico no ícone de filtro de catálogo 
    And seleciono a opção "Price(low to high)"
    Then os produtos do catálogo são exibidos pelo preço, começando do mais barato ao mais caro 

Scenario: Alterar o padrão de exibição do catálogo, do produto com maior preço ao menor preço

    Given que estou logado na plataforma
    When clico no ícone de filtro de catálogo 
    And seleciono a opção "Price(high to low)"
    Then os produtos do catálogo são exibidos pelo preço, começando do mais caro até o mais barato

Scenario: Abrir descrição de um produto do catalógo 

    Given que estou logado na plataforma
    When no catalógo, clico no produto "Sauce Labs Backpack"
    Then uma imagem do produto é exibida junto de uma descrição com o preço

Scenario: Retornar ao catálogo estando na descrição de um produto

    Given que estou logado na plataforma
    And estou na página de descrição do produto "Sauce Labs Backpack"
    When clico no botão no canto superior "Back to products"
    Then sou redirecionado ao catálogo 

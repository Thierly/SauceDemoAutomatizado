Feature: Login
    
    Faz login na plataforma.

Scenario: Realizar login com credenciais válidas
    
    Given que estou na página de Login
    And insiro a entrada "standard_user" no campo "Username"
    And insiro a entrada "secret_sauce" no campo "Password"
    When clico  no botão "Login"
    Then sou logado com sucesso

Scenario: Realizar login com credenciais inválidas

    Given que estou na página de Login
    And insiro a entrada "error_test" no campo "Username"
    And insiro a entrada "1234" no campo "Password"
    When clico no botão "Login"
    Then o login não é realizado, é exibido uma mensagem de erro

Scenario: Realizar login sem inserir entradas nos campos 

    Given que estou na página de Login
    And deixo o campo "Username" vázio
    And deixo o campo "Password" vázio 
    When clico no botão "Login"
    Then o login não é realizado, é exibido uma mensagem de erro

Scenario: Realizar login sem inserir entrada no campo "Username"

    Given que estou na página de Login
    And deixo o campo "Username" vázio 
    And insiro a entrada "secret_sauce" no campo "Password"
    When clico no botão "Login"
    Then o login não é realizado, é exibido uma mensagem de erro

Scenario: Realizar login sem inserir entrada no campo "Password"

    Given que estou na página de Login
    And insiro a entrada "standard_user" no campo "Username"
    And deixo o campo "Password" vázio 
    When clico no botão "Login"
    Then o login não é realizado, é exibido uma mensagem de erro

Scenario: Realizar logout 

    Given que estou logado na plataforma
    When clico no ícone no canto superior esquerdo
    And clico na opção "Logout"
    Then sou redirecionado para página de login

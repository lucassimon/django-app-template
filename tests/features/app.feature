#Cenário 1: Conta está em crédito
#Dado que a conta está em crédito
#E o cartão é válido
#E o caixa tem dinheiro suficiente
#Quando o cliente requisita dinheiro
#Então verifique que a conta foi debitada
#E verifique que o dinheiro é entregue
#E verifique que o cartão é devolvido

#Feature: Rocking with lettuce and django

    #Scenario: Simple Hello World
    #Given I access the url "/"
    #Then I see the header "Hello World"

    #Scenario: Hello + capitalized name
    #Given I access the url "/some-name"
    #Then I see the header "Hello Some Name"


Feature: Compute factorial
    In order to play with Lettuce
    As beginners
    We'll implement factorial

    Scenario: Factorial of 0
    Given I have the number 0
    When I compute its factorial
    Then I see the number 1

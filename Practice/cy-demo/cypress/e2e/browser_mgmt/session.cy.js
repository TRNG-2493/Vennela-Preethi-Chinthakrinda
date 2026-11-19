// function definition, variable is login
//console.log("Hello "+user)
// login("Preethi") // function call

//lambda funtion - anonymous func - used only once
const login=(user)=>{
    cy.session(user,() =>{
        cy.visit("/")
        //locate an element by css (id,class,test id or attribute)
        cy.get('[data-test=username]').type(user);
        cy.get('[data-test=password]').type('secret_sauce');
        cy.get('[data-test=login-button]').click();
        cy.url().should('include','/inventory.html');

    });

}

describe('Inventory', () => {
  beforeEach(() => {
    login('standard_user');
    cy.visit('/inventory.html', { failOnStatusCode: false });
  });

  it('Shows the Products title', () => {
    cy.get('.title').should('have.text', 'Products');
  });

  it('Shows 6 products', () => {
    cy.get('.inventory_item').should('have.length', 6);
  });
});


describe('My First Test',()=>{
 // groups the individual test cases together
// like a test suite
// it --> individual test

it('Open login page',()=>{
  cy.visit("/")
  cy.title().should('eq','Swag Labs')
});

it('Login Button Visible',()=>{
  cy.visit("/")
  cy.get('[data-test="login-button"]').should('be.visible')
});

});
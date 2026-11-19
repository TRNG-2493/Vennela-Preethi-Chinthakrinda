describe('Login (recorded)', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('starting point', () => {
    cy.get('[data-test=login-button]').should('be.visible');
    cy.get('[data-test="username"]').click();
    cy.get('[data-test="username"]').type('standard_user');
    cy.get('[data-test="password"]').click();
    cy.get('[data-test="password"]').type('secret_sauce');
    cy.get('[data-test="login-button"]').click();
    cy.get('[data-test="add-to-cart-sauce-labs-bike-light"]').click();
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click();
    cy.get('[data-test="shopping-cart-link"]').should('have.text', '2');
  });
});
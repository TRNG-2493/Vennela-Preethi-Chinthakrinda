describe('Debugging', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.get('[data-test=username]').type('standard_user');
    cy.get('[data-test=password]').type('secret_sauce{enter}');
  });

  it('pauses and steps', () => {
    cy.pause();
    cy.get('[data-test=add-to-cart-sauce-labs-backpack]').click();
    cy.get('.shopping_cart_badge').should('have.text', '1');
  });
});

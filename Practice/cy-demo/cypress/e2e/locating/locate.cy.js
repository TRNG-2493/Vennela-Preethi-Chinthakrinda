describe('Locating products', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.get('[data-test=username]').type('standard_user');
    cy.get('[data-test=password]').type('secret_sauce');
    cy.get('[data-test=login-button]').click();
  });

    it('counts the products', () => {
    cy.get('.inventory_item').should('have.length', 6);
  });

    it('shows why a broad selector is risky', () => {
    cy.get('.inventory_item button').should('have.length', 6); // 6 buttons, so which one?
  });

    it('adds the Bolt T-Shirt by name', () => {
    cy.contains('.inventory_item', 'Sauce Labs Bolt T-Shirt') // the card with this text
      .find('button')                                          // the button inside that card
      .click();

    cy.get('.shopping_cart_badge').should('have.text', '1');
  });
});
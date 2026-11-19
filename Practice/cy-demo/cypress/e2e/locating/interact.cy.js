describe('Interaction', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.get('[data-test=username]').type('standard_user');
    cy.get('[data-test=password]').type('secret_sauce{enter}', { log: false }); // Enter submits
  });

    it('sorts by price, low to high', () => {
    cy.get('[data-test=product-sort-container]').select('Price (low to high)');
    cy.get('.inventory_item_price').first().should('have.text', '$7.99');
  });

    it('checks out one product', () => {
    cy.get('[data-test=add-to-cart-sauce-labs-backpack]').click();
    cy.get('.shopping_cart_link').click();
    cy.get('[data-test=checkout]').click();
    cy.get('[data-test=firstName]').type('Jasdhir');
    cy.get('[data-test=lastName]').type('Singh');
    cy.get('[data-test=postalCode]').type('10001');
    cy.get('[data-test=continue]').click();

    cy.get('[data-test=finish]').click();
    cy.get('.complete-header').should('have.text', 'Thank you for your order!');
  });
});
describe('Screenshots', () => {
  it('fails on purpose', () => {
    cy.visit('/');
    cy.get('[data-test=username]').type('standard_user');
    cy.get('[data-test=password]').type('wrong{enter}');
    cy.url().should('include', '/inventory.html');
  });
    it('takes screenshots on demand', () => {
    cy.visit('/');
    cy.get('[data-test=username]').type('standard_user');
    cy.get('[data-test=password]').type('secret_sauce{enter}');

    cy.screenshot('inventory-full');                               // whole page
    cy.screenshot('inventory-viewport', { capture: 'viewport' });  // visible area only
    cy.contains('.inventory_item', 'Sauce Labs Backpack')
      .screenshot('backpack-card');                                // one element
    cy.screenshot('inventory-no-prices', { blackout: ['.inventory_item_price'] });
  });
});
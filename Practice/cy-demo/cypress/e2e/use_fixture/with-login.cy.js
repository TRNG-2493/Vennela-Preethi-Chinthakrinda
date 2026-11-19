describe('Inventory', () => {
  beforeEach(() => {
    cy.logins();
  });

  it('shows 6 products', () => {
    cy.get('.inventory_item').should('have.length', 6);
  });
});
describe('Login', { tags: '@smoke' },() => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('logs in with valid credentials', () => {
    cy.get('[data-test=username]').type('standard_user');
    cy.get('[data-test=password]').type('secret_sauce');
    cy.get('[data-test=login-button]').click();
    cy.url().should('include', '/inventory.html');
  });

  it('shows an error for a wrong password', () => {
    cy.get('[data-test=username]').type('standard_user');
    cy.get('[data-test=password]').type('wrong');
    cy.get('[data-test=login-button]').click();
    cy.get('[data-test=error]').should('contain', 'do not match');
  });
});
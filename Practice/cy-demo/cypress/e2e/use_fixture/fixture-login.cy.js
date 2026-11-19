import users from '../../fixtures/users.json';

describe('Login with fixture data', () => {
  it('logs in as the standard user', () => {
    cy.visit('/');
    cy.get('[data-test=username]').type(users.standard.username);
    cy.get('[data-test=password]').type(users.standard.password, { log: false });
    cy.get('[data-test=login-button]').click();
    cy.url().should('include', '/inventory.html');
  });

  // load the same file with cy.fixture()
    it('shows an error for the locked user', () => {
    cy.fixture('users').then((data) => {
      cy.visit('/');
      cy.get('[data-test=username]').type(data.locked.username);
      cy.get('[data-test=password]').type(data.locked.password, { log: false });
      cy.get('[data-test=login-button]').click();
    });
    cy.get('[data-test=error]').should('contain', 'locked out');
  });

});
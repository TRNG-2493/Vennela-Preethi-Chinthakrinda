import cases from '../../fixtures/login-cases.json';

describe('Login (data-driven)', () => {
  cases.forEach((c) => {
    it(`login: ${c.title}`, () => {
      cy.visit('/');
      cy.get('[data-test=username]').type(c.username);
      cy.get('[data-test=password]').type(c.password, { log: false });
      cy.get('[data-test=login-button]').click();

      if (c.expectUrl) {
        cy.url().should('include', c.expectUrl);
      } else {
        cy.get('[data-test=error]').should('contain', c.expectError);
      }
    });
  });
});
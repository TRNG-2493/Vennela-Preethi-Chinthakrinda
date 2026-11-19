// cypress.config.js
const { defineConfig } = require('cypress');
const { plugin: cypressGrepPlugin } = require('@cypress/grep/plugin');

module.exports = defineConfig({
  e2e: {
    baseUrl: 'https://www.saucedemo.com',
    video: true,
    experimentalStudio: true,
    setupNodeEvents(on, config) {
      cypressGrepPlugin(config);
      
      return config;
    },
  },
});
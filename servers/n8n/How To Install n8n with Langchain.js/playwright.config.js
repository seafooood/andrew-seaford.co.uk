// playwright.config.js
export default {
  testDir: './tests',
  timeout: 60000,
  retries: 1,
  use: {
    baseURL: 'http://localhost:5678',
    headless: true,
  },
};

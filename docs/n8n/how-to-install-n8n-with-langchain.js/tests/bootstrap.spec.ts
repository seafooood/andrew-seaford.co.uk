import { test, expect } from '@playwright/test';

test('Bootstrap n8n setup if needed', async ({ page }) => {
  // Go to n8n
  await page.goto('http://localhost:5678/');

  // Step 1: Sign up form
  await page.fill('input[name="email"]', 'admin@example.com');
  await page.fill('input[name="firstName"]', 'Admin');
  await page.fill('input[name="lastName"]', 'User');
  await page.fill('input[name="password"]', 'Admin1234');
  await page.click('button:has-text("Next")');

  // Step 2: "Customize n8n to you" screen
  await page.waitForSelector('button:has-text("Get started")', { timeout: 10000 });
  await page.click('button:has-text("Get started")');

  // Step 3: "Get paid features for free" screen
  await page.waitForSelector('button:has-text("Skip")', { timeout: 10000 });
  await page.click('button:has-text("Skip")');

  // Step 4: Confirm main editor loads (Workflows tab)
  await page.waitForSelector('div#WorkflowsView span:has-text("Workflows")', { timeout: 15000 });
  await expect(page.locator('div#WorkflowsView span:has-text("Workflows")')).toBeVisible();
});

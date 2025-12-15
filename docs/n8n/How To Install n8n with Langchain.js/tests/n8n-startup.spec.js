import { test, expect } from '@playwright/test';

// Test confirms that n8n container is running and responding
test('n8n container is running and responds on port 5678', async ({ request }) => {
  const res = await request.get('http://localhost:5678/');
  expect(res.ok()).toBeTruthy();
  const body = await res.text();
  expect(body).toContain('<!DOCTYPE html>'); // UI is served
});

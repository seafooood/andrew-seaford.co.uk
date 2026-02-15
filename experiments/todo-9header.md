# 9. Security Headers Missing

**Problem:** The following security headers are absent from responses:
- `X-Content-Type-Options`
- `X-Frame-Options`
- `Content-Security-Policy`
- `Referrer-Policy`
- `Permissions-Policy`

While not a direct ranking factor, these contribute to overall site trustworthiness.

**Fix:** Add headers configuration to `vercel.json`:
```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" }
      ]
    }
  ]
}
```

**Impact:** Low-medium - improves security posture and Lighthouse score.

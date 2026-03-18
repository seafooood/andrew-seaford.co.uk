# 15. `/blog` Route Returns 404

Since the blog is configured as the homepage (`routeBasePath: '/'`), visiting `/blog` returns 404. Users and search engines may expect `/blog` to work. Consider adding a redirect from `/blog` to `/` in `vercel.json`.
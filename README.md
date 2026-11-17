# Off Book

What AI companies owe off the balance sheet, an independent credit grade, and stress tests for what happens if a customer like OpenAI can't pay.

This folder is the whole website. There's no build step and no server: `index.html` holds the page and `live.json` holds the daily news, prices and extra researched companies.

## Put it online (pick one)

**Netlify Drop (2 minutes, no Git):** go to https://app.netlify.com/drop, sign in, and drag this whole folder onto the page. You get a link like `off-book-123.netlify.app`. Rename it under Site configuration → Change site name.

**GitHub Pages (best for daily updates):** create a public repo (e.g. `off-book`), upload every file in this folder (including `.nojekyll`), then Settings → Pages → Deploy from branch → `main` / root. The site appears at `https://<your-username>.github.io/off-book/`.

**Cloudflare Pages or Vercel:** create a project, upload this folder (or connect the repo), leave the build command empty and the output directory as `/`.

## Custom domain
Buy a domain (e.g. `offbook.money`), then add it in your host's domain settings and point the DNS records it shows you at the host. All three hosts above give free HTTPS.

## Keeping the data fresh
The page reads `live.json` on every visit. To update it, replace `live.json` on your host with a newer copy. If the site is on GitHub, the nightly refresh can commit the new file to the repo automatically once GitHub is connected to Claude.

## Preview locally
`python3 -m http.server 8000` in this folder, then open http://localhost:8000. Opening `index.html` directly as a file works too, but then it can't load `live.json`.

Not investment advice.

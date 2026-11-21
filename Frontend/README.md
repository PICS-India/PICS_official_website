# PICS

Frontend for the PICS (Policy Impact Challenge Series) website, by The Indian Netizens.
Built with React, React Router and Vite.

## Getting started

```bash
cd frontend
npm install
npm run dev      # http://localhost:5173
npm run build    # production build in dist/
```

## Where to edit things

| What | File |
| --- | --- |
| Registration / LinkedIn / email links | `src/config/site.js` |
| Home page copy (hero, stats, programme, FAQ, updates) | `src/data/home.js` |
| Events (home tabs, /events, event details) | `src/data/events.js` |
| Colours, fonts, spacing | `src/styles/global.css` (`:root` tokens) |
| Home page sections | `src/sections/` |

## Before launch

- Set `registrationUrl`, `linkedinUrl` and `contactEmail` in `src/config/site.js`.
- Replace the placeholder update card in `src/data/home.js`.
- Check the cohort dates and the "Registration open" status in `src/data/events.js` and `src/data/home.js`.

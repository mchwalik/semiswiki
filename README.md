# Public site for `/opt/data/wiki`

To repozytorium przygotowuje publiczną stronę z vaulta Obsidian znajdującego się w:
- `/opt/data/wiki`

Silnik strony:
- **Quartz 4**

## Co jest publikowane
Skrypt `scripts/sync-vault.py` kopiuje do `content/` tylko warstwę wiedzy:
- `entities/`
- `concepts/`
- `summaries/`
- opcjonalnie `comparisons/` i `queries/`, jeśli nie są puste

Dodatkowo generowane są strony:
- `index.md` — homepage
- `catalog.md` — publiczny katalog
- `about-this-wiki.md` — schema / zakres
- `change-log.md` — changelog

**Nie publikujemy**:
- `raw/`
- `.obsidian/`
- `templates/`
- `journal/`
- `inbox/`

## Komendy lokalne
```bash
cd /opt/data/wiki-site
python3 scripts/sync-vault.py
npm_config_engine_strict=false npx quartz build
npm_config_engine_strict=false npx quartz build --serve
```

## Uwaga o środowisku lokalnym
Na tej maszynie lokalnie jest:
- Node: `v20.19.2`
- npm: `9.2.0`

Quartz 4 preferuje Node 22+, więc do instalacji użyłem:
```bash
npm_config_engine_strict=false npm install --force
```

Build na hostingu ustaw na **Node 22**.

## GitHub Pages
Workflow jest przygotowany w:
- `.github/workflows/deploy.yml`

Przed pierwszym deployem:
1. wrzuć repo na GitHub
2. ustaw `Pages` → `Source` → `GitHub Actions`
3. zmień `baseUrl` w `quartz.config.ts` z `example.com` na docelową domenę

Docelowy URL na GitHub Pages będzie zwykle w stylu:
- `https://<github-user>.github.io/<repo>`

## Vercel
Dodałem też `vercel.json` z `cleanUrls`, więc możesz wdrożyć również na Vercel.

## Następne rzeczy do podmiany
Przed publicznym wdrożeniem warto zmienić:
- `baseUrl` w `quartz.config.ts`
- tytuł strony w `quartz.config.ts`, jeśli chcesz własną markę
- linki w footerze w `quartz.layout.ts`, jeśli chcesz kierować na repo lub domenę

# NBA API Gotchas & Best Practices

The NBA Stats API (`stats.nba.com`) is an internal API that is heavily rate-limited and sensitive to client configurations. Keep the following rules in mind:

## 1. Request Headers & User-Agent

`stats.nba.com` strictly blocks standard automated HTTP client headers (such as raw Python `urllib` or `requests` defaults).

- Always include browser-like headers: `Host: stats.nba.com`, `Referer: https://www.nba.com/`, and a realistic `User-Agent`.
- In `nba_api`, the internal class `nba_api.stats.library.http.NBAStatsHTTP` automatically provides modern Chrome headers (`Sec-Ch-Ua`, `Accept`, etc.). Avoid stripping or overriding them with incomplete dictionaries.

## 2. Timeouts and Latency

- Complex aggregation queries (like league-wide dashboards or shot charts) frequently take 5–25 seconds to generate on NBA's backend.
- Always configure requests with `timeout=45` or `timeout=60`.
- Implement retry loops: a brief timeout can often succeed on a second attempt after a 1–2 second sleep.

## 3. Rate Limiting & Throttling

- Do not burst requests in parallel threads. Keep batch calls sequential.
- Introduce a 0.6–1.0 second delay (`time.sleep(0.7)`) between consecutive requests to avoid temporary IP bans (HTTP 429).

## 4. Name Matching & Accents

- The static database stores official international spellings with diacritics (e.g., `Luka Dončić`, `Nikola Jokić`, `Kristaps Porziņģis`).
- When querying names, always normalize accents (e.g. using `unicodedata.normalize('NFKD')`) to match both ASCII and accented spellings.

## 5. Offline Static Lookups

- `nba_api.stats.static.players` and `nba_api.stats.static.teams` store complete historical rosters and team IDs locally without making any network requests. Use them first before making external calls.

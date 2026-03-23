# Refactoring & Technical Debt

This document tracks refactoring opportunities, architectural improvements, and technical debt items for the nba_api project.

## Purpose

- **Track:** Known areas that could be improved but aren't blocking current functionality
- **Prioritize:** Help contributors identify high-impact refactoring work
- **Context:** Provide background and reasoning for future improvements
- **History:** Archive completed refactorings for reference

## How to Use

- Add new items with context, affected files, and potential benefits
- Move items between priority levels as needed
- When creating a PR for a refactoring, reference this document
- Move completed items to the "Completed" section with commit SHA

---

## High Priority

### Decouple Parser Layer from HTTP Layer

**Status:** Planned
**Context:** Currently `http.py:96-127` contains conditional logic that determines whether to use tabular JSON parsing or V3 parser-based parsing. This creates coupling between the HTTP layer and the parsing strategy.

**Current Implementation:**
```python
# In http.py
def get_data_sets(self, endpoint=None):
    if endpoint is None:
        # Tabular JSON extraction
        return {...}
    else:
        # V3 endpoint - HTTP layer knows about parsers!
        from nba_api.stats.endpoints._parsers import get_parser_for_endpoint
        parser = get_parser_for_endpoint(endpoint, self.get_dict())
        return parser.get_data_sets()
```

**Problems:**
- HTTP layer shouldn't know about parsing strategies (violates SRP)
- Requires lazy import to avoid circular dependency
- `endpoint` parameter in `get_data_sets()` is a code smell
- Unclear responsibility boundaries

**Proposed Solution (Endpoint-Controlled Parsing):**
Move parsing responsibility to endpoint classes where it belongs:

```python
# In BoxScoreAdvancedV3 endpoint class
def load_response(self):
    from nba_api.stats.endpoints._parsers import get_parser_for_endpoint
    parser = get_parser_for_endpoint(self.endpoint, self.nba_response.get_dict())
    data_sets = parser.get_data_sets()

    self.data_sets = [Endpoint.DataSet(data=ds) for ds in data_sets.values()]
    self.player_stats = Endpoint.DataSet(data=data_sets["PlayerStats"])
    self.team_stats = Endpoint.DataSet(data=data_sets["TeamStats"])

# In regular endpoint class - no changes needed
def load_response(self):
    data_sets = self.nba_response.get_data_sets()  # No endpoint param!
    # ... rest of loading
```

**Benefits:**
- ✅ HTTP layer only responsible for fetching data
- ✅ Each endpoint controls its own parsing
- ✅ Removes conditional logic from `http.py`
- ✅ Eliminates lazy import workaround
- ✅ Clear separation of concerns
- ✅ No breaking changes to public API

**Files Affected:**
- `src/nba_api/stats/library/http.py` (simplify `get_data_sets()`)
- `src/nba_api/stats/endpoints/boxscoreadvancedv3.py` (update `load_response()`)
- `src/nba_api/stats/endpoints/boxscoredefensivev2.py`
- `src/nba_api/stats/endpoints/boxscorefourfactorsv3.py`
- `src/nba_api/stats/endpoints/boxscorehustlev2.py`
- `src/nba_api/stats/endpoints/boxscoremiscv3.py`
- `src/nba_api/stats/endpoints/boxscoreplayertrackv3.py`
- `src/nba_api/stats/endpoints/boxscorescoringv3.py`
- `src/nba_api/stats/endpoints/boxscoreusagev3.py`
- All other V3 endpoints that use custom parsers

**Testing:**
- All existing tests should pass without modification
- No API changes (backwards compatible)
- Verify lazy import is no longer needed

**Related Work:**
- Commit 8304148: Refactored V3 parsers to `_parsers/` module
- Alternative: Response type polymorphism (more complex, may be overkill)

**Estimated Effort:** Medium (2-3 hours)

---

## Medium Priority

<!-- Add future medium-priority items here -->

---

## Low Priority

<!-- Add future low-priority items here -->

---

## Completed

### ✅ Refactor V3 Parsers to Dedicated Module

**Completed:** 2025-11-05
**Commit:** 8304148
**Description:** Moved V3 boxscore parsers from `stats/library/parserv3.py` to dedicated `stats/endpoints/_parsers/` module. Created 6 new parsers (defensive, hustle, misc, usage, scoring, factors) with comprehensive test coverage (86 tests). Established parser registry pattern for extensibility.

**Benefits Achieved:**
- ✅ Better code organization (parsers grouped logically)
- ✅ Easier to add new parsers (consistent pattern)
- ✅ Comprehensive test coverage (86 parser tests, 329 total)
- ✅ 100% backwards compatibility maintained
- ✅ Lazy loading to avoid circular imports

---

## Guidelines for Adding Items

When adding a new refactoring item, include:

1. **Status:** Planned | In Progress | Blocked
2. **Context:** Why does this need refactoring?
3. **Current Implementation:** Code example showing the problem
4. **Proposed Solution:** How should it work?
5. **Benefits:** What do we gain?
6. **Files Affected:** List of files that need changes
7. **Testing:** How to verify the refactoring is safe
8. **Estimated Effort:** Small (< 1 hour) | Medium (2-4 hours) | Large (1+ days)

## Questions?

See `CONTRIBUTING.md` for general contribution guidelines or open an issue for discussion.

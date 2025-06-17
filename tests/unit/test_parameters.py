from nba_api.stats.library.parameters import (
    Season, 
    SeasonType, 
    SeasonTypePlayoffs, 
    SeasonTypeAllStar, 
    SeasonTypeNullable,
    SeasonTypeAllStarNullable,
    _NotRequired
)
import re


def test_season():
    assert re.search(r"^\d{4}-\d{2}$", Season.default) is not None


def test_season_type_base():
    assert SeasonType.regular == "Regular Season"
    assert SeasonType.preseason == "Pre Season"
    assert SeasonType.playin == "PlayIn"
    assert SeasonType.default == "Regular Season"
    assert hasattr(SeasonType, 'regular')
    assert hasattr(SeasonType, 'preseason')
    assert hasattr(SeasonType, 'playin')
    assert not hasattr(SeasonType, 'playoffs')
    assert not hasattr(SeasonType, 'all_star')


def test_season_type_playoffs():
    assert SeasonTypePlayoffs.regular == "Regular Season"
    assert SeasonTypePlayoffs.preseason == "Pre Season"
    assert SeasonTypePlayoffs.playoffs == "Playoffs"
    assert SeasonTypePlayoffs.playin == "PlayIn"
    assert SeasonTypePlayoffs.default == "Regular Season"
    assert hasattr(SeasonTypePlayoffs, 'regular')
    assert hasattr(SeasonTypePlayoffs, 'preseason')
    assert hasattr(SeasonTypePlayoffs, 'playoffs')
    assert hasattr(SeasonTypePlayoffs, 'playin')
    assert not hasattr(SeasonTypePlayoffs, 'all_star')


def test_season_type_all_star():
    assert SeasonTypeAllStar.regular == "Regular Season"
    assert SeasonTypeAllStar.preseason == "Pre Season"
    assert SeasonTypeAllStar.playoffs == "Playoffs"
    assert SeasonTypeAllStar.playin == "PlayIn"
    assert SeasonTypeAllStar.all_star == "All Star"
    assert SeasonTypeAllStar.default == "Regular Season"
    assert hasattr(SeasonTypeAllStar, 'regular')
    assert hasattr(SeasonTypeAllStar, 'preseason')
    assert hasattr(SeasonTypeAllStar, 'playoffs')
    assert hasattr(SeasonTypeAllStar, 'playin')
    assert hasattr(SeasonTypeAllStar, 'all_star')


def test_season_type_nullable():
    assert SeasonTypeNullable.regular == "Regular Season"
    assert SeasonTypeNullable.preseason == "Pre Season"
    assert SeasonTypeNullable.playoffs == "Playoffs"
    assert SeasonTypeNullable.playin == "PlayIn"
    assert SeasonTypeNullable.none == ""
    assert SeasonTypeNullable.default == ""
    assert hasattr(SeasonTypeNullable, 'regular')
    assert hasattr(SeasonTypeNullable, 'preseason')
    assert hasattr(SeasonTypeNullable, 'playoffs')
    assert hasattr(SeasonTypeNullable, 'playin')
    assert hasattr(SeasonTypeNullable, 'none')
    assert not hasattr(SeasonTypeNullable, 'all_star')


def test_season_type_all_star_nullable():
    assert SeasonTypeAllStarNullable.regular == "Regular Season"
    assert SeasonTypeAllStarNullable.preseason == "Pre Season"
    assert SeasonTypeAllStarNullable.playoffs == "Playoffs"
    assert SeasonTypeAllStarNullable.playin == "PlayIn"
    assert SeasonTypeAllStarNullable.none == ""
    assert SeasonTypeAllStarNullable.default == ""
    assert hasattr(SeasonTypeAllStarNullable, 'regular')
    assert hasattr(SeasonTypeAllStarNullable, 'preseason')
    assert hasattr(SeasonTypeAllStarNullable, 'playoffs')
    assert hasattr(SeasonTypeAllStarNullable, 'playin')
    assert hasattr(SeasonTypeAllStarNullable, 'none')
    assert not hasattr(SeasonTypeAllStarNullable, 'all_star')


def test_season_type_inheritance():
    assert issubclass(SeasonTypePlayoffs, SeasonType)
    assert issubclass(SeasonTypeAllStar, SeasonTypePlayoffs)
    assert issubclass(SeasonTypeNullable, _NotRequired)
    assert issubclass(SeasonTypeNullable, SeasonTypePlayoffs)
    assert issubclass(SeasonTypeAllStarNullable, _NotRequired)
    assert issubclass(SeasonTypeAllStarNullable, SeasonTypePlayoffs)

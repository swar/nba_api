import re


def capital_letter_replacement(match):
    return "_" + match.group(1).lower()


def get_python_variable_name(parameter):
    find_replace_list = [
        ["OPPTOV", "OppTov"],
        ["OPPSTL", "OppStl"],
        ["OPPREB", "OppReb"],
        ["OPPPTSPAINT", "OppPtsPaint"],
        ["OPPPTSOFFTOV", "OppPtsOffTov"],
        ["OPPPTSFB", "OppPtsFb"],
        ["OPPPTS", "OppPts"],
        ["OPPPF", "OppPf"],
        ["OPPOREB", "OppOreb"],
        ["OPPFTM", "OppFtm"],
        ["OPPFTA", "OppFta"],
        ["OPPFT", "OppFt"],
        ["OPPFGM", "OppFgm"],
        ["OPPFGA", "OppFga"],
        ["OPPFG", "OppFg"],
        ["OPPDREB", "OppDreb"],
        ["OPPBLK", "OppBlk"],
        ["OPPAST", "OppAst"],
        ["IDL", "IdL"],
        ["PTSPAINT", "PtsPaint"],
        ["PTSOFFTOV", "PtsOffTov"],
        ["PTSFB", "PtsFb"],
        ["OREB", "Oreb"],
        ["NDCHANCE", "ndChance"],
        ["MINUTES", "Minutes"],
        ["PTS", "Pts"],
        ["POR", "PoR"],
        ["PF", "Pf"],
        ["PCT", "Pct"],
        ["LS", "Ls"],
        ["IDL", "IdL"],
        ["ID", "Id"],
        ["GROUP", "Group"],
        ["FTM", "Ftm"],
        ["FTA", "Fta"],
        ["FT", "Ft"],
        ["FGM", "Fgm"],
        ["FGA", "Fga"],
        ["FG", "Fg"],
        ["DREB", "Dreb"],
        ["DD", "Dd"],
        ["BLK", "Blk"],
        ["AST", "Ast"],
        ["WS", "Ws"],
        ["TOV", "Tov"],
        ["TD", "Td"],
        ["STL", "Stl"],
        ["REB", "Reb"],
    ]

    for find, replace in find_replace_list:
        parameter = parameter.replace(find, replace)

    if re.search("^[a-z]", parameter):
        parameter = "_" + parameter
    variable_name = re.sub(
        r"([A-Z])(?!$|Nullable|Round|Defend$)", capital_letter_replacement, parameter
    )[1:].lower()
    variable_name = variable_name.replace("__", "_")
    return variable_name

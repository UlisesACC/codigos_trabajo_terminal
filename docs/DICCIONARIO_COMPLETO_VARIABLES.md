# Diccionario completo de variables — WNBA Stats/wehoop

**Fuente:** documentación del repositorio [codigos_trabajo_terminal/docs/datasets](https://github.com/UlisesACC/codigos_trabajo_terminal/tree/master/docs/datasets).

Los nombres, tipos y descripciones se transcriben de los diccionarios originales. Las descripciones originales están en inglés; cuando están vacías se indica **Sin descripción en la fuente**. El patrón `YYYY` representa cualquier temporada. Las rutas corresponden a archivos presentes en el repositorio. No se infieren definiciones faltantes.

## coaches

**Fuente:** [coaches.md](https://github.com/UlisesACC/codigos_trabajo_terminal/blob/master/docs/datasets/coaches.md)

**Columnas:** 11. **Archivos encontrados:** 29.

- `datos_a_usar/wnba_stats/coaches/parquet/coaches_YYYY.parquet`

| Variable | Tipo original | Descripción de la fuente |
|---|---|---|
| `team_id` | Int64 | stats.wnba.com team id (e.g. 1611661313 = New York Liberty). |
| `season` | Int64 | Season the row belongs to, as a BARE calendar year ("2023") — the WNBA season fits one calendar year, unlike the NBA span form. |
| `coach_id` | Int64 | **Sin descripción en la fuente** |
| `first_name` | String | **Sin descripción en la fuente** |
| `last_name` | String | **Sin descripción en la fuente** |
| `coach_name` | String | **Sin descripción en la fuente** |
| `is_assistant` | Int64 | **Sin descripción en la fuente** |
| `coach_type` | String | **Sin descripción en la fuente** |
| `sort_sequence` | String | **Sin descripción en la fuente** |
| `sub_sort_sequence` | Int64 | **Sin descripción en la fuente** |
| `season_type` | String | First underscore-separated field of the raw capture's filename, which for a season-type-partitioned endpoint IS the season type: "regular-season" or "playoffs" (lower-case and hyphenated, not "Regular Season"). On rosters and coaches the captures are partitioned by TEAM, so this column repeats team_id and carries no season-type meaning -- a known defect, see those pages. |

## draft

**Fuente:** [draft.md](https://github.com/UlisesACC/codigos_trabajo_terminal/blob/master/docs/datasets/draft.md)

**Columnas:** 14. **Archivos encontrados:** 30.

- `datos_a_usar/wnba_stats/draft/parquet/draft_YYYY.parquet`

| Variable | Tipo original | Descripción de la fuente |
|---|---|---|
| `person_id` | Int64 | stats.wnba.com person id of the player (or official) the row describes; the same id space as player_id. |
| `player_name` | String | Player display name as the stats API ships it ("Breanna Stewart"). |
| `season` | Int64 | Season the row belongs to, as a BARE calendar year ("2023") — the WNBA season fits one calendar year, unlike the NBA span form. |
| `round_number` | Int64 | **Sin descripción en la fuente** |
| `round_pick` | Int64 | **Sin descripción en la fuente** |
| `overall_pick` | Int64 | **Sin descripción en la fuente** |
| `draft_type` | String | **Sin descripción en la fuente** |
| `team_id` | Int64 | stats.wnba.com team id (e.g. 1611661313 = New York Liberty). |
| `team_city` | String | Team city name. |
| `team_name` | String | Team nickname or full name as the source endpoint ships it. |
| `team_abbreviation` | String | Three-letter team code ("NYL"). |
| `organization` | String | **Sin descripción en la fuente** |
| `organization_type` | String | **Sin descripción en la fuente** |
| `player_profile_flag` | Int64 | **Sin descripción en la fuente** |

## game_rosters

**Fuente:** [game_rosters.md](https://github.com/UlisesACC/codigos_trabajo_terminal/blob/master/docs/datasets/game_rosters.md)

**Columnas:** 10. **Archivos encontrados:** 30.

- `datos_a_usar/wnba_stats/game_rosters/parquet/game_rosters_YYYY.parquet`

| Variable | Tipo original | Descripción de la fuente |
|---|---|---|
| `player_id` | Int64 | stats.wnba.com person id of the player (Int64); joins rosters, boxscores, game logs and pbp (`person_id`). |
| `first_name` | String | **Sin descripción en la fuente** |
| `last_name` | String | **Sin descripción en la fuente** |
| `jersey_num` | String | **Sin descripción en la fuente** |
| `team_id` | Int64 | stats.wnba.com team id (e.g. 1611661313 = New York Liberty). |
| `team_city` | String | Team city name. |
| `team_name` | String | Team nickname or full name as the source endpoint ships it. |
| `team_abbreviation` | String | Three-letter team code ("NYL"). |
| `season` | Int64 | Season the row belongs to, as a BARE calendar year ("2023") — the WNBA season fits one calendar year, unlike the NBA span form. |
| `game_id` | String | stats.wnba.com game id, 10-char string carrying the "10" WNBA league prefix ("1022400001"); pinned Utf8 so it never round-trips through int. |

## games_in_data_repo

**Fuente:** [games_in_data_repo.md](https://github.com/UlisesACC/codigos_trabajo_terminal/blob/master/docs/datasets/games_in_data_repo.md)

**Columnas:** 17. **Archivos encontrados:** 1.

- `datos_a_usar/wnba_stats/wnba_stats_games_in_data_repo.parquet`

| Variable | Tipo original | Descripción de la fuente |
|---|---|---|
| `away_team_abbreviation` | String | Away team three-letter code. |
| `away_team_id` | Int64 | stats.wnba.com team id of the away team. |
| `away_team_name` | String | Away team name. |
| `away_team_score` | Int64 | Away final (or current) score. |
| `game_date` | Date | Game date as the source ships it (calendar date, US Eastern; a Date column in the schedule master). |
| `game_id` | String | stats.wnba.com game id, 10-char string carrying the "10" WNBA league prefix ("1022400001"); pinned Utf8 so it never round-trips through int. |
| `home_team_abbreviation` | String | Home team three-letter code. |
| `home_team_id` | Int64 | stats.wnba.com team id of the home team. |
| `home_team_name` | String | Home team name. |
| `home_team_score` | Int64 | Home final (or current) score. |
| `in_game_rosters` | Boolean | True when the game is present in the compiled game_rosters release. |
| `in_officials` | Boolean | True when the game is present in the compiled officials release. |
| `in_pbp` | Boolean | True when the game's play-by-play made it into a compiled season release. |
| `in_player_boxscores` | Boolean | True when the game is present in the compiled player_boxscores release. |
| `in_team_boxscores` | Boolean | True when the game is present in the compiled team_boxscores release. |
| `season` | String | Season the row belongs to, as a BARE calendar year ("2023") — the WNBA season fits one calendar year, unlike the NBA span form. |
| `season_type_id` | String | Leading digit of season_id encoding the season type (2 = regular season, 4 = playoffs). |

## lineups

**Fuente:** [lineups.md](https://github.com/UlisesACC/codigos_trabajo_terminal/blob/master/docs/datasets/lineups.md)

**Columnas:** 182. **Archivos encontrados:** 1.

- `datos_a_usar/wnba_stats/lineups/parquet/lineups_YYYY.parquet`

| Variable | Tipo original | Descripción de la fuente |
|---|---|---|
| `group_set` | String | **Sin descripción en la fuente** |
| `group_id` | String | **Sin descripción en la fuente** |
| `group_name` | String | **Sin descripción en la fuente** |
| `team_id` | Int64 | stats.wnba.com team id (e.g. 1611661313 = New York Liberty). |
| `team_abbreviation` | String | Three-letter team code ("NYL"). |
| `gp` | Int64 | **Sin descripción en la fuente** |
| `w` | Int64 | **Sin descripción en la fuente** |
| `l` | Int64 | **Sin descripción en la fuente** |
| `w_pct` | Float64 | **Sin descripción en la fuente** |
| `min` | Float64 | Team (or player) minutes in the log row. |
| `e_off_rating` | Float64 | **Sin descripción en la fuente** |
| `off_rating` | Float64 | **Sin descripción en la fuente** |
| `e_def_rating` | Float64 | **Sin descripción en la fuente** |
| `def_rating` | Float64 | **Sin descripción en la fuente** |
| `e_net_rating` | Float64 | **Sin descripción en la fuente** |
| `net_rating` | Float64 | **Sin descripción en la fuente** |
| `ast_pct` | Float64 | **Sin descripción en la fuente** |
| `ast_to` | Float64 | **Sin descripción en la fuente** |
| `ast_ratio` | Float64 | **Sin descripción en la fuente** |
| `oreb_pct` | Float64 | **Sin descripción en la fuente** |
| `dreb_pct` | Float64 | **Sin descripción en la fuente** |
| `reb_pct` | Float64 | **Sin descripción en la fuente** |
| `tm_tov_pct` | Float64 | **Sin descripción en la fuente** |
| `efg_pct` | Float64 | **Sin descripción en la fuente** |
| `ts_pct` | Float64 | **Sin descripción en la fuente** |
| `e_pace` | Float64 | **Sin descripción en la fuente** |
| `pace` | Float64 | **Sin descripción en la fuente** |
| `pace_per40` | Float64 | **Sin descripción en la fuente** |
| `poss` | Int64 | **Sin descripción en la fuente** |
| `pie` | Float64 | **Sin descripción en la fuente** |
| `gp_rank` | Int64 | **Sin descripción en la fuente** |
| `w_rank` | Int64 | **Sin descripción en la fuente** |
| `l_rank` | Int64 | **Sin descripción en la fuente** |
| `w_pct_rank` | Int64 | **Sin descripción en la fuente** |
| `min_rank` | Int64 | **Sin descripción en la fuente** |
| `off_rating_rank` | Int64 | **Sin descripción en la fuente** |
| `def_rating_rank` | Int64 | **Sin descripción en la fuente** |
| `net_rating_rank` | Int64 | **Sin descripción en la fuente** |
| `ast_pct_rank` | Int64 | **Sin descripción en la fuente** |
| `ast_to_rank` | Int64 | **Sin descripción en la fuente** |
| `ast_ratio_rank` | Int64 | **Sin descripción en la fuente** |
| `oreb_pct_rank` | Int64 | **Sin descripción en la fuente** |
| `dreb_pct_rank` | Int64 | **Sin descripción en la fuente** |
| `reb_pct_rank` | Int64 | **Sin descripción en la fuente** |
| `tm_tov_pct_rank` | Int64 | **Sin descripción en la fuente** |
| `efg_pct_rank` | Int64 | **Sin descripción en la fuente** |
| `ts_pct_rank` | Int64 | **Sin descripción en la fuente** |
| `pace_rank` | Int64 | **Sin descripción en la fuente** |
| `pie_rank` | Int64 | **Sin descripción en la fuente** |
| `sum_time_played` | Int64 | **Sin descripción en la fuente** |
| `season` | Int64 | Season the row belongs to, as a BARE calendar year ("2023") — the WNBA season fits one calendar year, unlike the NBA span form. |
| `season_type` | String | First underscore-separated field of the raw capture's filename, which for a season-type-partitioned endpoint IS the season type: "regular-season" or "playoffs" (lower-case and hyphenated, not "Regular Season"). On rosters and coaches the captures are partitioned by TEAM, so this column repeats team_id and carries no season-type meaning -- a known defect, see those pages. |
| `measure_type` | String | Grain marker of the mixed leaguegamelog capture: "p" marks player game-log rows; the per-team rows come from a capture with no measure suffix and so carry NULL here, not "t". Filter on player_id.is_not_null() rather than on this column if you want player rows only. |
| `per_mode` | String | **Sin descripción en la fuente** |
| `fgm` | Float64 | Field goals made. |
| `fga` | Float64 | Field goals attempted. |
| `fg_pct` | Float64 | Field-goal percentage (0-1). |
| `fg3m` | Float64 | Three-point field goals made. |
| `fg3a` | Float64 | Three-point field goals attempted. |
| `fg3_pct` | Float64 | Three-point percentage (0-1). |
| `ftm` | Float64 | Free throws made. |
| `fta` | Float64 | Free throws attempted. |
| `ft_pct` | Float64 | Free-throw percentage (0-1). |
| `oreb` | Float64 | Offensive rebounds. |
| `dreb` | Float64 | Defensive rebounds. |
| `reb` | Float64 | Total rebounds. |
| `ast` | Float64 | Assists. |
| `tov` | Float64 | Turnovers. |
| `stl` | Float64 | Steals. |
| `blk` | Float64 | Blocks. |
| `blka` | Float64 | **Sin descripción en la fuente** |
| `pf` | Float64 | Personal fouls. |
| `pfd` | Float64 | **Sin descripción en la fuente** |
| `pts` | Float64 | Points. |
| `plus_minus` | Float64 | Point differential while on the floor (player rows) or final margin (team rows). |
| `fgm_rank` | Int64 | **Sin descripción en la fuente** |
| `fga_rank` | Int64 | **Sin descripción en la fuente** |
| `fg_pct_rank` | Int64 | **Sin descripción en la fuente** |
| `fg3m_rank` | Int64 | **Sin descripción en la fuente** |
| `fg3a_rank` | Int64 | **Sin descripción en la fuente** |
| `fg3_pct_rank` | Int64 | **Sin descripción en la fuente** |
| `ftm_rank` | Int64 | **Sin descripción en la fuente** |
| `fta_rank` | Int64 | **Sin descripción en la fuente** |
| `ft_pct_rank` | Int64 | **Sin descripción en la fuente** |
| `oreb_rank` | Int64 | **Sin descripción en la fuente** |
| `dreb_rank` | Int64 | **Sin descripción en la fuente** |
| `reb_rank` | Int64 | **Sin descripción en la fuente** |
| `ast_rank` | Int64 | **Sin descripción en la fuente** |
| `tov_rank` | Int64 | **Sin descripción en la fuente** |
| `stl_rank` | Int64 | **Sin descripción en la fuente** |
| `blk_rank` | Int64 | **Sin descripción en la fuente** |
| `blka_rank` | Int64 | **Sin descripción en la fuente** |
| `pf_rank` | Int64 | **Sin descripción en la fuente** |
| `pfd_rank` | Int64 | **Sin descripción en la fuente** |
| `pts_rank` | Int64 | **Sin descripción en la fuente** |
| `plus_minus_rank` | Int64 | **Sin descripción en la fuente** |
| `pts_off_tov` | Float64 | **Sin descripción en la fuente** |
| `pts_2nd_chance` | Float64 | **Sin descripción en la fuente** |
| `pts_fb` | Float64 | **Sin descripción en la fuente** |
| `pts_paint` | Float64 | **Sin descripción en la fuente** |
| `opp_pts_off_tov` | Float64 | **Sin descripción en la fuente** |
| `opp_pts_2nd_chance` | Float64 | **Sin descripción en la fuente** |
| `opp_pts_fb` | Float64 | **Sin descripción en la fuente** |
| `opp_pts_paint` | Float64 | **Sin descripción en la fuente** |
| `pts_off_tov_rank` | Int64 | **Sin descripción en la fuente** |
| `pts_2nd_chance_rank` | Int64 | **Sin descripción en la fuente** |
| `pts_fb_rank` | Int64 | **Sin descripción en la fuente** |
| `pts_paint_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_pts_off_tov_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_pts_2nd_chance_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_pts_fb_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_pts_paint_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_fgm` | Float64 | **Sin descripción en la fuente** |
| `opp_fga` | Float64 | **Sin descripción en la fuente** |
| `opp_fg_pct` | Float64 | **Sin descripción en la fuente** |
| `opp_fg3m` | Float64 | **Sin descripción en la fuente** |
| `opp_fg3a` | Float64 | **Sin descripción en la fuente** |
| `opp_fg3_pct` | Float64 | **Sin descripción en la fuente** |
| `opp_ftm` | Float64 | **Sin descripción en la fuente** |
| `opp_fta` | Float64 | **Sin descripción en la fuente** |
| `opp_ft_pct` | Float64 | **Sin descripción en la fuente** |
| `opp_oreb` | Float64 | **Sin descripción en la fuente** |
| `opp_dreb` | Float64 | **Sin descripción en la fuente** |
| `opp_reb` | Float64 | **Sin descripción en la fuente** |
| `opp_ast` | Float64 | **Sin descripción en la fuente** |
| `opp_tov` | Float64 | **Sin descripción en la fuente** |
| `opp_stl` | Float64 | **Sin descripción en la fuente** |
| `opp_blk` | Float64 | **Sin descripción en la fuente** |
| `opp_blka` | Float64 | **Sin descripción en la fuente** |
| `opp_pf` | Float64 | **Sin descripción en la fuente** |
| `opp_pfd` | Float64 | **Sin descripción en la fuente** |
| `opp_pts` | Float64 | **Sin descripción en la fuente** |
| `opp_fgm_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_fga_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_fg_pct_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_fg3m_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_fg3a_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_fg3_pct_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_ftm_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_fta_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_ft_pct_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_oreb_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_dreb_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_reb_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_ast_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_tov_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_stl_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_blk_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_blka_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_pf_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_pfd_rank` | Int64 | **Sin descripción en la fuente** |
| `opp_pts_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_fga_2pt` | Float64 | **Sin descripción en la fuente** |
| `pct_fga_3pt` | Float64 | **Sin descripción en la fuente** |
| `pct_pts_2pt` | Float64 | **Sin descripción en la fuente** |
| `pct_pts_2pt_mr` | Float64 | **Sin descripción en la fuente** |
| `pct_pts_3pt` | Float64 | **Sin descripción en la fuente** |
| `pct_pts_fb` | Float64 | **Sin descripción en la fuente** |
| `pct_pts_ft` | Float64 | **Sin descripción en la fuente** |
| `pct_pts_off_tov` | Float64 | **Sin descripción en la fuente** |
| `pct_pts_paint` | Float64 | **Sin descripción en la fuente** |
| `pct_ast_2pm` | Float64 | **Sin descripción en la fuente** |
| `pct_uast_2pm` | Float64 | **Sin descripción en la fuente** |
| `pct_ast_3pm` | Float64 | **Sin descripción en la fuente** |
| `pct_uast_3pm` | Float64 | **Sin descripción en la fuente** |
| `pct_ast_fgm` | Float64 | **Sin descripción en la fuente** |
| `pct_uast_fgm` | Float64 | **Sin descripción en la fuente** |
| `pct_fga_2pt_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_fga_3pt_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_pts_2pt_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_pts_2pt_mr_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_pts_3pt_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_pts_fb_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_pts_ft_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_pts_off_tov_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_pts_paint_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_ast_2pm_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_uast_2pm_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_ast_3pm_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_uast_3pm_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_ast_fgm_rank` | Int64 | **Sin descripción en la fuente** |
| `pct_uast_fgm_rank` | Int64 | **Sin descripción en la fuente** |

## metric_curves

**Fuente:** [metric_curves.md](https://github.com/UlisesACC/codigos_trabajo_terminal/blob/master/docs/datasets/metric_curves.md)

**Columnas:** 14. **Archivos encontrados:** 30.

- `datos_a_usar/wnba_stats/metric_curves/parquet/metric_curves_YYYY.parquet`

| Variable | Tipo original | Descripción de la fuente |
|---|---|---|
| `season` | Int64 | Season the row belongs to, as a BARE calendar year ("2023") — the WNBA season fits one calendar year, unlike the NBA span form. |
| `entity_type` | String | Which aggregate the row is: "league" (every counted attempt that season), "team" or "player" on metric_curves; always "player" on rolling_windows. |
| `entity_id` | String | stats.wnba.com id of the entity as TEXT -- the team_id on a team row, the person_id on a player row, null on the league row. |
| `entity_name` | String | Label for the entity: the team tricode ("NYL") on a team row, the shooter's name as the pbp ships it on a player row; null on the league row. |
| `team_id` | String | stats.wnba.com team id (e.g. 1611661313 = New York Liberty). |
| `id_source` | String | Namespace of `entity_id` / `team_id` on this row -- "wnba_stats" here; the cross-league contract carries "espn", "gsis" and "nba_stats" elsewhere. |
| `metric` | String | What the row measures: "fg_pct_by_shot_distance" on metric_curves (field-goal percentage by shot distance in feet); "fg_pct" (window_unit "fga") or "fg3_pct" (window_unit "fg3a") on rolling_windows. |
| `down` | Int64 | Null on every row: the second axis of the football-only success_by_down_distance curve, carried for the cross-league contract. |
| `x_lo` | Float64 | Bucket lower edge in feet, inclusive: 1-ft bins from 0 to 35, then 35 and 50. |
| `x_hi` | Float64 | Bucket upper edge in feet, exclusive: x_lo + 1 below 35 ft, then 50 and 95. |
| `attempts` | Int64 | Field-goal attempts in the bucket -- regular-season and playoff shots (season_type_id 2 and 4, the game id's type digit). An empty bucket is absent, never a zero row. |
| `successes` | Int64 | Made field goals in the bucket. |
| `rate` | Float64 | successes / attempts, one exact division (no smoothing or prior). |
| `epa_per_att` | Float64 | Null on every row: shots carry no EPA. Populated on the football twins of this contract. |

## officials

**Fuente:** [officials.md](https://github.com/UlisesACC/codigos_trabajo_terminal/blob/master/docs/datasets/officials.md)

**Columnas:** 6. **Archivos encontrados:** 23.

- `datos_a_usar/wnba_stats/officials/parquet/officials_YYYY.parquet`

| Variable | Tipo original | Descripción de la fuente |
|---|---|---|
| `official_id` | Int64 | stats.wnba.com person id of the game official. |
| `first_name` | String | **Sin descripción en la fuente** |
| `last_name` | String | **Sin descripción en la fuente** |
| `jersey_num` | String | **Sin descripción en la fuente** |
| `season` | Int64 | Season the row belongs to, as a BARE calendar year ("2023") — the WNBA season fits one calendar year, unlike the NBA span form. |
| `game_id` | String | stats.wnba.com game id, 10-char string carrying the "10" WNBA league prefix ("1022400001"); pinned Utf8 so it never round-trips through int. |

## pbp

**Fuente:** [pbp.md](https://github.com/UlisesACC/codigos_trabajo_terminal/blob/master/docs/datasets/pbp.md)

**Columnas:** 25. **Archivos encontrados:** 31.

- `datos_a_usar/wnba_stats/pbp/parquet/play_by_play_YYYY.parquet`
- `datos_a_usar/wnba_stats/pbp/parquet/wnba_play_by_play_YYYY.parquet`

| Variable | Tipo original | Descripción de la fuente |
|---|---|---|
| `action_number` | Int64 | Ordinal of the action within the game as numbered by the stats feed; monotone but not gapless (video-only actions are skipped). |
| `clock` | String | Game clock at the action in ISO-8601 duration form ("PT08M12.00S"). |
| `period` | Int64 | Period number (1-4; 5+ = overtime). |
| `team_id` | Int64 | stats.wnba.com team id (e.g. 1611661313 = New York Liberty). |
| `team_tricode` | String | Three-letter team code as the v3 endpoints name it ("NYL"). |
| `person_id` | Int64 | stats.wnba.com person id of the player (or official) the row describes; the same id space as player_id. |
| `player_name` | String | Player display name as the stats API ships it ("Breanna Stewart"). |
| `player_name_i` | String | Abbreviated player name ("B. Stewart"). |
| `x_legacy` | Int64 | Shot x-coordinate in the legacy stats coordinate frame (tenths of feet from the basket centerline; 0 for non-shot actions). |
| `y_legacy` | Int64 | Shot y-coordinate in the legacy coordinate frame (tenths of feet from the basket toward half court, so 0 at the basket and negative for a shot from behind it; 0 for non-shot actions). |
| `shot_distance` | Int64 | Shot distance in whole feet as the stats.wnba.com play-by-play feed reports it (0 for non-shots). The feed reports every three under 23.5 ft as 0: pbp keeps that 0, while shots restores those threes as sqrt(x_legacy^2 + y_legacy^2) / 10 rounded half up, the feed's own rounding, and null when the three has no location (legacy 0, 0). |
| `shot_result` | String | "Made" / "Missed" for shot actions; empty otherwise. |
| `is_field_goal` | Int64 | 1 when the action is a field-goal attempt, else 0. |
| `score_home` | String | Home score after the action (string; carried forward between scores). |
| `score_away` | String | Away score after the action (string; carried forward between scores). |
| `points_total` | Int64 | Points the acting team has scored through this action. |
| `location` | String | Which side the acting team is on: "h" (home) or "v" (visitor). |
| `description` | String | Human-readable action narrative from the feed. |
| `action_type` | String | Action family ("Made Shot", "Rebound", "Turnover", "Foul", ...). |
| `sub_type` | String | Action detail within the family ("Jump Shot", "Offensive", ...). |
| `video_available` | Int64 | 1 when the feed links video for the action/game row. |
| `shot_value` | Int64 | Point value of a shot attempt (2 or 3; 1 for free throws, 0 for non-shots). |
| `action_id` | Int64 | Feed-internal id of the action row. |
| `game_id` | String | stats.wnba.com game id, 10-char string carrying the "10" WNBA league prefix ("1022400001"); pinned Utf8 so it never round-trips through int. |
| `season` | Int64 | Season the row belongs to, as a BARE calendar year ("2023") — the WNBA season fits one calendar year, unlike the NBA span form. |

## player_boxscores

**Fuente:** [player_boxscores.md](https://github.com/UlisesACC/codigos_trabajo_terminal/blob/master/docs/datasets/player_boxscores.md)

**Columnas:** 34. **Archivos encontrados:** 1.

- `datos_a_usar/wnba_stats/player_boxscores/parquet/player_boxscores_YYYY.parquet`

| Variable | Tipo original | Descripción de la fuente |
|---|---|---|
| `team_id` | Int64 | stats.wnba.com team id (e.g. 1611661313 = New York Liberty). |
| `team_name` | String | Team nickname or full name as the source endpoint ships it. |
| `team_tricode` | String | Three-letter team code as the v3 endpoints name it ("NYL"). |
| `side` | String | **Sin descripción en la fuente** |
| `person_id` | Int64 | stats.wnba.com person id of the player (or official) the row describes; the same id space as player_id. |
| `first_name` | String | **Sin descripción en la fuente** |
| `family_name` | String | **Sin descripción en la fuente** |
| `name_i` | String | **Sin descripción en la fuente** |
| `player_slug` | String | **Sin descripción en la fuente** |
| `position` | String | **Sin descripción en la fuente** |
| `comment` | String | **Sin descripción en la fuente** |
| `jersey_num` | String | **Sin descripción en la fuente** |
| `minutes` | String | **Sin descripción en la fuente** |
| `field_goals_made` | Int64 | **Sin descripción en la fuente** |
| `field_goals_attempted` | Int64 | **Sin descripción en la fuente** |
| `field_goals_percentage` | Float64 | **Sin descripción en la fuente** |
| `three_pointers_made` | Int64 | **Sin descripción en la fuente** |
| `three_pointers_attempted` | Int64 | **Sin descripción en la fuente** |
| `three_pointers_percentage` | Float64 | **Sin descripción en la fuente** |
| `free_throws_made` | Int64 | **Sin descripción en la fuente** |
| `free_throws_attempted` | Int64 | **Sin descripción en la fuente** |
| `free_throws_percentage` | Float64 | **Sin descripción en la fuente** |
| `rebounds_offensive` | Int64 | **Sin descripción en la fuente** |
| `rebounds_defensive` | Int64 | **Sin descripción en la fuente** |
| `rebounds_total` | Int64 | **Sin descripción en la fuente** |
| `assists` | Int64 | **Sin descripción en la fuente** |
| `steals` | Int64 | **Sin descripción en la fuente** |
| `blocks` | Int64 | **Sin descripción en la fuente** |
| `turnovers` | Int64 | **Sin descripción en la fuente** |
| `fouls_personal` | Int64 | **Sin descripción en la fuente** |
| `points` | Int64 | **Sin descripción en la fuente** |
| `plus_minus_points` | Float64 | **Sin descripción en la fuente** |
| `game_id` | String | stats.wnba.com game id, 10-char string carrying the "10" WNBA league prefix ("1022400001"); pinned Utf8 so it never round-trips through int. |
| `season` | Int64 | Season the row belongs to, as a BARE calendar year ("2023") — the WNBA season fits one calendar year, unlike the NBA span form. |

## player_game_logs

**Fuente:** [player_game_logs.md](https://github.com/UlisesACC/codigos_trabajo_terminal/blob/master/docs/datasets/player_game_logs.md)

**Columnas:** 35. **Archivos encontrados:** 30.

- `datos_a_usar/wnba_stats/player_game_logs/parquet/player_game_logs_YYYY.parquet`

| Variable | Tipo original | Descripción de la fuente |
|---|---|---|
| `season_id` | String | stats.wnba.com composite season id: season-type digit + year ("22023" = 2023 regular season). |
| `team_id` | Int64 | stats.wnba.com team id (e.g. 1611661313 = New York Liberty). |
| `team_abbreviation` | String | Three-letter team code ("NYL"). |
| `team_name` | String | Team nickname or full name as the source endpoint ships it. |
| `game_id` | String | stats.wnba.com game id, 10-char string carrying the "10" WNBA league prefix ("1022400001"); pinned Utf8 so it never round-trips through int. |
| `game_date` | String | Game date as the source ships it (calendar date, US Eastern; a Date column in the schedule master). |
| `matchup` | String | Matchup string from the log ("NYL @ LVA" away, "NYL vs. LVA" home). |
| `wl` | String | Result from the row team's perspective: "W" or "L". |
| `min` | Int64 | Team (or player) minutes in the log row. |
| `fgm` | Int64 | Field goals made. |
| `fga` | Int64 | Field goals attempted. |
| `fg_pct` | Float64 | Field-goal percentage (0-1). |
| `fg3m` | Int64 | Three-point field goals made. |
| `fg3a` | Int64 | Three-point field goals attempted. |
| `fg3_pct` | Float64 | Three-point percentage (0-1). |
| `ftm` | Int64 | Free throws made. |
| `fta` | Int64 | Free throws attempted. |
| `ft_pct` | Float64 | Free-throw percentage (0-1). |
| `oreb` | Int64 | Offensive rebounds. |
| `dreb` | Int64 | Defensive rebounds. |
| `reb` | Int64 | Total rebounds. |
| `ast` | Int64 | Assists. |
| `stl` | Int64 | Steals. |
| `blk` | Int64 | Blocks. |
| `tov` | Int64 | Turnovers. |
| `pf` | Int64 | Personal fouls. |
| `pts` | Int64 | Points. |
| `plus_minus` | Int64 | Point differential while on the floor (player rows) or final margin (team rows). |
| `video_available` | Int64 | 1 when the feed links video for the action/game row. |
| `season` | Int64 | Season the row belongs to, as a BARE calendar year ("2023") — the WNBA season fits one calendar year, unlike the NBA span form. |
| `season_type` | String | First underscore-separated field of the raw capture's filename, which for a season-type-partitioned endpoint IS the season type: "regular-season" or "playoffs" (lower-case and hyphenated, not "Regular Season"). On rosters and coaches the captures are partitioned by TEAM, so this column repeats team_id and carries no season-type meaning -- a known defect, see those pages. |
| `player_id` | Int64 | stats.wnba.com person id of the player (Int64); joins rosters, boxscores, game logs and pbp (`person_id`). |
| `player_name` | String | Player display name as the stats API ships it ("Breanna Stewart"). |
| `fantasy_pts` | Float64 | WNBA fantasy points for the player log row (null on team rows). |
| `measure_type` | String | Grain marker of the mixed leaguegamelog capture: "p" marks player game-log rows; the per-team rows come from a capture with no measure suffix and so carry NULL here, not "t". Filter on player_id.is_not_null() rather than on this column if you want player rows only. |

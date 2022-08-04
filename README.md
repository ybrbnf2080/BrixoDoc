
Последовательность записи в БД import_taf24

---------------------MODEL **Suppliers200**---------------------

`name` = #Имя BranNo

`brand_no` = #BranNo

`street` = #Street1 `№ - 40`

`street_two` = #Street2 `№ - 40`

`country_code` = #CountryCode `№ - 40`

`post_code` = #PostCode `№ - 40`

`city` = #City1 `№ - 40`

`phone` = #Phone `№ - 40`

`email` = #Email `№ - 40`

`web_site` = #WEB `№ - 40`

`adr_type` = #AdrType `№ - 40`

`doc_no` = #DocNo `№ - 42`

`doc_type` = #DocType `№ - 42`

---------------------MODEL **Country202**---------------------

`country_code` = #Код страны

`country_name` = #Имя страны

---------------------MODEL **Manufacture203**---------------------

`man_no` = #BrandNo

`short_name` = #ShortName

`term_plain` = #TermPlain

---------------------MODEL **Ref203**---------------------

`ref_no` = #RefNo `№ - 20`3

`man_no_id` = #ManNo `№ - 20`3

---------------------MODEL **Supers204**---------------------

`supers_no` = #SupersNo `№ - 204`

`sort_no` = #ArtNo `№ - 204`

---------------------MODEL **Doc231and232**---------------------

`doc_no` = #DocNo `№ - 231`

`doc_name` = #DocName `№ - 231`

`lang_no` = #LangNo `№ - 231`

`doc_content_type` = #DocContentType `№ - 231`

`doc_term_no` = #DocTermNorm `№ - 231`

`doc_type` = #DocType `№ - 231`

---------------------MODEL **Article200**---------------------

`country` = #CountryCode `№ - 202`

`gen_art_no` = #GenArtNo `№ - 211`

`brand_no_id` = #BrandNo

`gtin` = #GTIN `№ - 209`

`art_no` = #ArtNo `№ - 200`

`quant_unit` = #QuantUnit `№ - 212`

`quant_per_unit` = #QuantPerUnit `№ - 212`

`art_stat` = #ArtStat `№ - 212`

`status_dat` = #StatusDat `№ - 212`

`ref_no_id` = #RefNo `№ - 203`

`supers_id` = #SupersNo `№ - 204`

`doc_no` = #DocNo `№ - 232`

---------------------MODEL **CritVal210**---------------------

`crit_no` = #Code

`name` = #Name

`description` = #Comment

---------------------MODEL **Crit210**---------------------

`art_no_id` = #ArtNo `№ - 210`

`crit_no_id` = #CritNo `№ - 210`

`crit_val` = #CritVal `№ - 210`

---------------------MODEL **Trade207**---------------------

`trade_no` = #TradeNo

`art_no_id` = #ArtNo `№ - 210`

`first_page` = #FirstPage

---------------------MODEL **Lnk400**---------------------

`art_no` = #ArtNo `№ - 400`

`gen_art_no` = #GenArtNo `№ - 400`

`lnk_target_type` = #LnkTargetType `№ - 400`

`lnk_target_no` = #LnkTargetNo `№ - 400`

`seq_no` = #SeqNo `№ - 400`

---------------------MODEL **Table404**---------------------

`art_no` = #ArtNo `№ - 404`

`gen_art_no` = #GenArtNo `№ - 404`

`lnk_target_type` = #LnkTargetType `№ - 404`

`lnk_target_no` = #LnkTargetNo `№ - 404`

---------------------MODEL **Table410**---------------------

`art_no` = #ArtNo `№ - 410`

`gen_art_no` = #GenArtNo `№ - 410`

`lnk_target_type` = #LnkTargetType `№ - 410`

`lnk_target_no` = #LnkTargetNo `№ - 410`

`seq_no` = #SeqNo `№ - 410`

`crit_no` = #CritNo `№ - 410`

`crit_val` = #CritVal `№ - 410`

`first_page` = #FirstPage `№ - 410`

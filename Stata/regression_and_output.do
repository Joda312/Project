* regression analysis, tables and graphs
use "Stata/derived/used_cars_processed.dta", clear
* regressing lnprice on a set of variables
reg ln_price ln_odometer i.area_enc ib2.condition_enc i.fuel_enc hybrid ib2.new_enc

* saving regression table as a txt file
outreg2 using "Stata/output/used_cars_reg.txt"

* saving the scatter plot of price and odometer both in internal Stata format ("gph", readable by Stata only) and as a pdf file
scatter price odometer
graph save "Stata/output/price_odometer_scatter.gph", replace
graph export "Stata/output/price_odometer_scatter.pdf", replace
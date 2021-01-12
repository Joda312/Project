clear all
set more off
* reading .csv data into Stata ("used-cars.csv" is a derived data file from the previous analysis in Python)

import delimited "C:\Users\user\Documents\Project\data\used-cars.csv"

describe
* keeping only variables relevant for subsequent analysis 
keep v1 price odometer area condition fuel hybrid old_new

* taking care of missing values in the dataset
misstable sum, all
mdesc

* getting rid of missing values
drop if missing(condition, fuel)
mdesc
desc
* codebook
sum

* demonstrating the use of Stata "for" loops
foreach X in price odometer {
	generate ln_`X' = ln(`X')
}

tab area 
tab condition
tab fuel 
tab hybrid
tab old_new

* transforming string variables to be used as indicator variables in subsequent do-file with regression
encode area, generate(area_enc)
encode condition, generate(condition_enc)
encode fuel, generate(fuel_enc)
encode old_new, generate(new_enc)

* saving the file
save "Stata/derived/used_cars_processed.dta", replace

rm(list = ls())

library(AER)

setwd("/Users/chanuki/_University_work/_WBS/_Phd_Research/Scenicness_Crime/CODE/wrattler-examples")

df = read.csv("resources/joined_crime_datasets_11_10_19.csv")
crime_subset_df = df[ which(df$crime_category=='major_burglary'), ]

#Run Poisson Model
summary(m1 <- glm(crime_count ~ predicted_score_nn, family="poisson", data=crime_subset_df))

#Add Deprivation Scores
summary(m1 <- glm(crime_count ~ predicted_score_nn + income_score_rate + employment_score_rate+ education_skills_and_training_score + health_deprivation_and_disability_score+ barriers_to_housing_and_services_score+living_environment_score, family="poisson", data=crime_subset_df))

#Add Population Density
summary(m1 <- glm(crime_count ~ predicted_score_nn + income_score_rate + employment_score_rate+ education_skills_and_training_score + health_deprivation_and_disability_score+ barriers_to_housing_and_services_score+living_environment_score + population_density_area_hectares_, family="poisson", data=crime_subset_df))


#Check for overdispersion https://stats.stackexchange.com/questions/66586/is-there-a-test-to-determine-whether-glm-overdispersion-is-significant
dispersiontest(m1)

#Another method https://data.princeton.edu/wws509/r/overdispersion
var(crime_subset_df$crime_count)/mean(crime_subset_df$crime_count)


#We notice that crime is over dispersed so we run Negative Binomial Regression
library(MASS)
mnb <- glm.nb(crime_count ~ predicted_score_nn + income_score_rate + employment_score_rate+ education_skills_and_training_score + health_deprivation_and_disability_score+ barriers_to_housing_and_services_score+living_environment_score + population_density_area_hectares_, data=crime_subset_df)
summary(mnb)



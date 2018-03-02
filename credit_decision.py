from sklearn import tree




# credit score - [Min Score requirement 620]

# DTI [Debt to Income] less than or equal to 35% ideal 36% - 39% still ok, 40% - 45% proceed with caution, 46% and greater, DTI too high

# Years Reporting [ 0 years and greater]

# Derogatory [scale 0 - 5] 0 = no derogatory trade-lines reporting [1 = 1] [2 = 2] [3 = 3] [4 = 4 or more]

# Auto Declines [Credit Score less than 620], [Years reporting less than 1], [DTI greater than 45%], [Derogatory > 3]


approved1 = 'Approved - No Conditions'
approved2 = 'Approved - Pending Income Verification'
decline1 = 'Decline - Failed to meet minimum credit criteria'
decline2 = 'Decline - Credit history not sufficient - May reconsider with a qualified co-applicant'
decline3 = 'Decline - High debt to income'


# [credit score, DTI, years reporting, derogatory]

# samples
X = [[700, .25, 3, 0], [620, .40, 5, 1], [500, .42, 3, 4], [600, .54, 12, 2], [720, .12, 0, 0],
     [800, .35, 0, 0], [498, .30, 5, 3], [800, .23, 2, 0], [720, .55, 6, 0], [680, .42, 8, 1],
     [690, .53, 3, 0],[600, .23, 5, 0], [619, .26, 4, 0], [615, .35, 9, 1], [702, .35, 5, 4],
     [698, .35, 5, 4], [700, .22, 0, 2]]

# labels
Y = [approved1, approved2, decline1, decline1, decline2, decline2, decline1, approved1, decline3, approved2, decline3,
     decline1, decline1, decline1, decline1, decline1, decline2]


clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

cs = 723
dti = .23
yrs_reporting = 0
derogs = 2


prediction = clf.predict([[cs, dti, yrs_reporting, derogs]])

print(prediction)
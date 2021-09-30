import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
#from sklearn.model_selection import train_test_split  #高斯迴歸，這次沒用到
#from sklearn.gaussian_process import GaussianProcessRegressor
#from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel

bus1 = pd.read_csv("c_after_repair_diffpower_1000_20190513-20190630_STW.csv") ############# input csv檔1
bus2 = pd.read_csv("c_after_repair_diffpower_1000_20190413-20190513_STW.csv") ############## input csv檔2
bus3 = pd.read_csv("c_after_repair_diffpower_1000_20190313-20190413_STW.csv") ############## input csv檔3
bus4 = pd.read_csv("c_after_repair_diffpower_1000_20190213-20190313_STW.csv") ############## input csv檔4
title = "shipC : fuel consumption / STW 11 ~ 15 (after repair - per month  , no move)" ############## input 圖表title
x = np.arange(11, 15, 0.01) ################################################## input 要畫回歸線的x軸範圍
plt.axis([11,15, 0,8]) #################################################### input 要畫出來的x和y軸區間
degree = 2  #input 高階線性迴歸要取幾階，目前方程式只能顯示2階

bus1 = bus1[(bus1['STW'] >= 1) & (bus1['STW'] <=15) & (bus1['fuel_consumption'] > 0) & (bus1['fuel_consumption'] < 8)] ############## input 篩選
x1 = bus1["STW"]
y1 = bus1["fuel_consumption"]

bus2 = bus2[(bus2['STW'] >= 11) & (bus2['STW'] <=15)  & (bus2['fuel_consumption'] > 0) & (bus2['fuel_consumption'] < 8)] ############## input 篩選
x2 = bus2["STW"]
y2 = bus2["fuel_consumption"]

bus3 = bus3[(bus3['STW'] >= 11) & (bus3['STW'] <=15)  & (bus3['fuel_consumption'] > 0) & (bus3['fuel_consumption'] < 8)] ############## input 篩選
x3 = bus3["STW"]
y3 = bus3["fuel_consumption"]

bus4 = bus4[(bus4['STW'] >= 11) & (bus4['STW'] <=15)  & (bus4['fuel_consumption'] > 0) & (bus4['fuel_consumption'] < 8)] ############## input 篩選
x4 = bus4["STW"]
y4 = bus4["fuel_consumption"]

AVG1 = "average fuel_consumption = {:.3g}".format(np.mean(y1))
AVG2 = "average fuel_consumption = {:.3g}".format(np.mean(y2))
AVG3 = "average fuel_consumption = {:.3g}".format(np.mean(y3))
AVG4 = "average fuel_consumption = {:.3g}".format(np.mean(y4))

plt.scatter(x1,                    # x軸資料
            y1,                    # y軸資料
            color = "aqua",        # 點顏色
            s = 3,                 # 點大小
            alpha = 0.5,           # 透明度
            marker = "o",
            label = "fuel_consumption(20190513-20190630)"+AVG1)

plt.scatter(x2,                    # x軸資料
            y2,                    # y軸資料
            color = "pink",        # 點顏色
            s = 3,                 # 點大小
            alpha =0.5,            # 透明度
            marker = "o",
            label = "fuel_consumption(20190413-20190513)"+AVG2)

plt.scatter(x3,                    # x軸資料
            y3,                    # y軸資料
            color = "violet",        # 點顏色
            s = 3,                 # 點大小
            alpha =0.5,            # 透明度
            marker = "o",
            label = "fuel_consumption(20190313-20190413)"+AVG3)

plt.scatter(x4,                    # x軸資料
            y4,                    # y軸資料
            color = "wheat",        # 點顏色
            s = 3,                 # 點大小
            alpha =0.5,            # 透明度
            marker = "o",
            label = "fuel_consumption(20190213-20190313)" + AVG4)
#####################第一條迴歸線#####################
x_raw = x1.values.reshape(-1, 1)
y_raw = y1.values.reshape(-1, 1)
#多階線性擬合
polynomial_regressor = LinearRegression()
polynomial = PolynomialFeatures(degree = degree)   #degress設定多項式擬合中多項式的最高次數
x_polynomial = polynomial.fit_transform(x_raw)   #x列向量，fit_transform是對x按列求[1, x, x^2]，即構造二次項資料
polynomial_regressor.fit(x_polynomial , y_raw)   # fit polynomial features
y_polynomial_fit = polynomial_regressor.predict(polynomial.fit_transform(x_raw))  #建構二次多項式資料預測
coefficient = polynomial_regressor.coef_[0]  #方程式係數 numpy.ndarray (一維,float64)
intercept = polynomial_regressor.intercept_[0]  #截距 numpy.float64
R_square = polynomial_regressor.score(x_polynomial,y_raw)  #相關係數 numpy.float64
print(coefficient)
print(intercept)
print(R_square)
text = str(degree) + ' degree regressor  R^2=' + "{:.3g}".format(R_square) + '\n'
text += 'y=' + "{:.3g}".format(coefficient[-1]) + 'x^2'
if coefficient[-2] < 0:
    text += ' - ' + "{:.3g}".format(coefficient[-2]*-1) + 'x'
else:
    text += ' + ' + "{:.3g}".format(coefficient[-2]) + 'x'
if intercept < 0:
    text += ' - ' + "{:.3g}".format(intercept*-1)
else:
    text += ' + ' + "{:.3g}".format(intercept)
#plt.plot(x_raw, y_polynomial_fit, color="blue", label=text, linewidth=2.0)
y = coefficient[-1]*x**2 + coefficient[-2]*x + intercept
plt.plot(x, y, color="blue", label=text, linewidth=2.0)


#####################第二條迴歸線#####################
x_raw = x2.values.reshape(-1, 1)
y_raw = y2.values.reshape(-1, 1)
#多階線性擬合
polynomial_regressor = LinearRegression()
polynomial = PolynomialFeatures(degree = degree)   #degress設定多項式擬合中多項式的最高次數
x_polynomial = polynomial.fit_transform(x_raw)   #x列向量，fit_transform是對x按列求[1, x, x^2]，即構造二次項資料
polynomial_regressor.fit(x_polynomial , y_raw)   # fit polynomial features
y_polynomial_fit = polynomial_regressor.predict(polynomial.fit_transform(x_raw))  #建構二次多項式資料預測
coefficient = polynomial_regressor.coef_[0]  #方程式係數 numpy.ndarray (一維,float64)
intercept = polynomial_regressor.intercept_[0]  #截距 numpy.float64
R_square = polynomial_regressor.score(x_polynomial,y_raw)  #相關係數 numpy.float64
print(coefficient)
print(intercept)
print(R_square)
text = str(degree) + ' degree regressor  R^2=' + "{:.3g}".format(R_square) + '\n'
text += 'y=' + "{:.3g}".format(coefficient[-1]) + 'x^2'
if coefficient[-2] < 0:
    text += ' - ' + "{:.3g}".format(coefficient[-2]*-1) + 'x'
else:
    text += ' + ' + "{:.3g}".format(coefficient[-2]) + 'x'
if intercept < 0:
    text += ' - ' + "{:.3g}".format(intercept*-1)
else:
    text += ' + ' + "{:.3g}".format(intercept)
#plt.plot(x_raw, y_polynomial_fit, color="yellow", label=text, linewidth=2.0)
y = coefficient[-1]*x**2 + coefficient[-2]*x + intercept
plt.plot(x, y, color="red", label=text, linewidth=2.0)

#####################第三條迴歸線#####################
x_raw = x3.values.reshape(-1, 1)
y_raw = y3.values.reshape(-1, 1)
#多階線性擬合
polynomial_regressor = LinearRegression()
polynomial = PolynomialFeatures(degree = degree)   #degress設定多項式擬合中多項式的最高次數
x_polynomial = polynomial.fit_transform(x_raw)   #x列向量，fit_transform是對x按列求[1, x, x^2]，即構造二次項資料
polynomial_regressor.fit(x_polynomial , y_raw)   # fit polynomial features
y_polynomial_fit = polynomial_regressor.predict(polynomial.fit_transform(x_raw))  #建構二次多項式資料預測
coefficient = polynomial_regressor.coef_[0]  #方程式係數 numpy.ndarray (一維,float64)
intercept = polynomial_regressor.intercept_[0]  #截距 numpy.float64
R_square = polynomial_regressor.score(x_polynomial,y_raw)  #相關係數 numpy.float64
print(coefficient)
print(intercept)
print(R_square)
text = str(degree) + ' degree regressor  R^2=' + "{:.3g}".format(R_square) + '\n'
text += 'y=' + "{:.3g}".format(coefficient[-1]) + 'x^2'
if coefficient[-2] < 0:
    text += ' - ' + "{:.3g}".format(coefficient[-2]*-1) + 'x'
else:
    text += ' + ' + "{:.3g}".format(coefficient[-2]) + 'x'
if intercept < 0:
    text += ' - ' + "{:.3g}".format(intercept*-1)
else:
    text += ' + ' + "{:.3g}".format(intercept)
#plt.plot(x_raw, y_polynomial_fit, color="yellow", label=text, linewidth=2.0)
y = coefficient[-1]*x**2 + coefficient[-2]*x + intercept
plt.plot(x, y, color="purple", label=text, linewidth=2.0)
#####################第四條迴歸線#####################
x_raw = x4.values.reshape(-1, 1)
y_raw = y4.values.reshape(-1, 1)
#多階線性擬合
polynomial_regressor = LinearRegression()
polynomial = PolynomialFeatures(degree = degree)   #degress設定多項式擬合中多項式的最高次數
x_polynomial = polynomial.fit_transform(x_raw)   #x列向量，fit_transform是對x按列求[1, x, x^2]，即構造二次項資料
polynomial_regressor.fit(x_polynomial , y_raw)   # fit polynomial features
y_polynomial_fit = polynomial_regressor.predict(polynomial.fit_transform(x_raw))  #建構二次多項式資料預測
coefficient = polynomial_regressor.coef_[0]  #方程式係數 numpy.ndarray (一維,float64)
intercept = polynomial_regressor.intercept_[0]  #截距 numpy.float64
R_square = polynomial_regressor.score(x_polynomial,y_raw)  #相關係數 numpy.float64
print(coefficient)
print(intercept)
print(R_square)
text = str(degree) + ' degree regressor  R^2=' + "{:.3g}".format(R_square) + '\n'
text += 'y=' + "{:.3g}".format(coefficient[-1]) + 'x^2'
if coefficient[-2] < 0:
    text += ' - ' + "{:.3g}".format(coefficient[-2]*-1) + 'x'
else:
    text += ' + ' + "{:.3g}".format(coefficient[-2]) + 'x'
if intercept < 0:
    text += ' - ' + "{:.3g}".format(intercept*-1)
else:
    text += ' + ' + "{:.3g}".format(intercept)
#plt.plot(x_raw, y_polynomial_fit, color="yellow", label=text, linewidth=2.0)
y = coefficient[-1]*x**2 + coefficient[-2]*x + intercept
plt.plot(x, y, color="darkorange", label=text, linewidth=2.0)

plt.title(title , fontsize=16)
plt.xlabel('STW(knot)', fontsize=14)
plt.ylabel('fuel consumption(mT/Hr)', fontsize=14)
plt.legend(loc='upper left', fontsize = 10)
plt.show()

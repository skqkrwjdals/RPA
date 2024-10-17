import pandas as pd
import matplotlib.pyplot as plt

hat = pd.read_csv('ch4-2.csv') #변수에 데이터셋 입력
print(hat.describe(), end="\n\n")

#상자그림 그리기
plt.figure(figsize=(8,10))
plt.boxplot(hat.weight)
plt.title('B hatchery chick weight box', fontsize = 17)
plt.ylabel('weight(g)')
plt.show
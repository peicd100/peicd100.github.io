參考資料，推薦看完影片：
https://www.youtube.com/watch?v=OP5HcXJg2Aw&t=6s
https://youtu.be/vi9eNd9CPnk?si=cQ7L0q64dsr5EdWF


如下圖，已經知道一個神經網路是輸入一個矩陣 x ，輸出一個矩陣 y ，但是當我們要處裡影片時，我們該如何將二維的圖片矩陣輸入至神經網路。

![alt text](<../images/CNN(Convolutional Neural Network)/image.png>)


CNN就是為此產生的神經網路，我們可以將它視為：
>將二維圖片轉換為一維輸入(x)的過程


可以看到下圖：



![alt text](<../images/CNN(Convolutional Neural Network)/image-2.png>)

[圖片來源1](https://www.spiceworks.com/tech/artificial-intelligence/articles/what-is-a-neural-network/
)、[圖片來源2](https://www.spiceworks.com/tech/artificial-intelligence/articles/what-is-a-neural-network/
)



## CNN 架構

下圖為CNN的基本架構。
可以看到很多名詞，以下分別說明。


![alt text](<../images/CNN(Convolutional Neural Network)/slide_10.jpg>)
[圖片來源](https://www.digikey.tw/zh/articles/machine-vision-applications-draw-intelligence-from-deep-learning-neural-networks)


操作：

- [Convolutions](#convolutions)
- [Subsampling](#subsampling)


名詞：

- Input：輸入
- [Feature maps(f.maps)](#feature-mapsfmaps)
- [Fully connected](#fully-connected)
- Output：輸出





## Convolutions

Convolutional Layer
使用Kernel（卷積核,又稱為Filter(濾波器))擷取特徵資訊，而擷取之後的圖片稱為特徵地圖([Feature maps](#feature-mapsfmaps))。

>訓練：這些 Kernel 是可以訓練的權重，是透過訓練取得的。

##  Subsampling

又稱為(Pooling Layer)，常用的有下列三種：

1. Max pooling
取最大值

2. Mean pooling
取平均

3. Min pooling
取最小值





## Feature maps(f.maps)

使用 Kernel 擷取特徵資訊之後的圖片

## Fully connected
稱為全連接層，是最基本的神經元架構，只由「輸入層」、「隱藏層(多個神經元)」、「輸出層」組成，如下圖


![alt text](<../images/CNN(Convolutional Neural Network)/image-3.png>)
[圖片來源](https://www.spiceworks.com/tech/artificial-intelligence/articles/what-is-a-neural-network/
)
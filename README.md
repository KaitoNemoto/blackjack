# blackjack<br>
2021年度のロボットシステム学　課題2で作成したパッケージです。<br>
このパッケージは講義をもとに作成したblackjackを遊ぶことのできるパッケージです。<br>

# デモ<br>
YouTubeに載せたのでご覧ください。
https://youtu.be/GpWQL0f6CZ0

# 動作環境<br>
・raspberrypi4<br>
・ubuntu-20.04.3 LTS<br>
・ROS

# 使い方
以下を入力してインストール<br>
```
cd ~/catkin_ws/src
git clone git@github.com:KaitoNemoto/blackjack.git
cd ~/catkin_ws
catkin_make
```

roscpreを起動させる(&をつけないと起動させながらできない)<br>
```
roscore &
```

scriptsにあるblackjack.pyとdiscrimination.pyを順番に起動させる。<br>
```
rosrun blackjack blackjack.py
rosrun blackjack discrimination.py(Ctrl+Cを押さないと止まらないので注意)
```


実行結果<br>
![スクリーンショット 2022-01-06 021050](https://user-images.githubusercontent.com/93694888/148259486-1b6cf8d9-1dda-4b54-b0ab-eccc7ce34451.png)
![スクリーンショット 2022-01-06 021107](https://user-images.githubusercontent.com/93694888/148259523-c5aac722-cfd5-4418-84c1-b756d4f82f4e.png)

# ライセンス
BSD 3-Clause "New" or "Revised" License

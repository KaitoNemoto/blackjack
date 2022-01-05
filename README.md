# blackjack
blackjackのように遊ぶことができるものを作りました。<br>

# デモ<br>
YouTubeに載せたのでご覧ください。
https://youtu.be/GpWQL0f6CZ0

# 動作環境<br>
・raspberrypi4<br>
・ubuntu-20.04.3<br>
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

scriptsにあるblackjack.pyとdiscrimination.pyを順番に起動させる。


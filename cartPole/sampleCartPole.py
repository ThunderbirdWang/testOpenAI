#coding:utf-8
#本例是最简单的随机移动小车
import gym  #导入OpenAI
env = gym.make('CartPole-v0')   #设置环境，也就是游戏本身
env.reset() #重置环境的状态，返回观察
for _ in range(1000):
    env.render()    #重绘环境的一帧。默认模式一般比较友好，如弹出一个窗口。
    env.step(env.action_space.sample()) #推进一个时间步长，返回observation，reward，done，info
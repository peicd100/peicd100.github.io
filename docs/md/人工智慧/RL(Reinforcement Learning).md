參考：
https://www.youtube.com/watch?v=XWukX-ayIrs&list=PLJV_el3uVTsMhtt7_Y6sgTHGHp1Vb2P2J&index=31
https://medium.com/@Jimmy_9566/rl-q-learning-cs%E7%AD%86%E8%A8%98-f182ab5252fa

1. Value-based：

Value-based 主要是學習值函數 Q(s, a)，也就是 Q- value : 它會估計在每種狀態 State(t) 下採取不同動作 Action(t) 的期望值。並且會根據 Q(s, a) 選擇具有最大值的 Action，以最大化預期獎勵(Expected reward)。

例子： Q-learning 和 Deep Q-Network (DQN) （之後會介紹）

2. Policy-based：

Policy-based 主要是直接學習和優化 Agent 的策略，在每個狀態下，它會學習應該選擇哪個 Action(t) 的機率分佈，並且試圖找到一個策略，使 Agent 在環境中獲得最大的累積獎勵。

這種方法通常適用於具有連續動作空間或高維狀態空間的問題，例如機器人控製或自然語言處理，因為這些問題的策略通常不容易透過值函數表示。

例子： Proximal Policy Optimization (PPO) （之後會介紹）
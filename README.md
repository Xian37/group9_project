# NYCU Object-Oriented Programming 112
# Welcome to Group 9's Project page ! 🙌
# 這是一款 Bomber Man 爆爆王遊戲


![image](https://github.com/Xian37/group9_project/blob/main/Game_Picture/start.png)

# 遊戲規則：

# 	1. 六個角色：

		三個Player角色有三個屬性: 血量、速度與炸彈傷害
  		且每一個會有一項屬性特別突出，而敵人Enemy則為均衡型角色，且角色的選擇會綁定敵人的是哪個
    	Player vs Enemy
		(1) Fox 竹狐  VS 熊貓
		(2) Moneky 山道猴子 VS 金色長髮男 
		(3) GuGu 菇菇 VS 奇怪生物
	
#	2. 三個地圖：

		每個地圖的路面、可破壞牆、不可破壞牆都有根據主題特別設計
  
		(1) FOREST 森林
		(2) OCEAN 海洋
		(3) DESERT 沙漠
	
#	3. 四種道具：

		地圖初始即會掉落道具，遊玩過程中也會每五秒以低機率掉落道具
		且以下道具掉落皆機率不同
  
		(1) 無敵星星： 無敵 5 秒 , 血量會變彩色
		(2) 加速閃電：加速 5 秒
		(3) 補血包： + 50 HP
		(4) 地雷： 觸發後 1 s 後爆炸
		
#	4. 操作方式：

		(1) 按上下左右鍵操控角色 （初始位置在左上角） 
		(2) 預設最多兩顆炸彈，且有冷卻時間 3s，按空白鍵放置炸彈，被炸到會 -25 HP
  
#  	5.遊戲規則：
   
		(1) 不可穿越障礙物，需炸開牆形成路面才可以
		(2) 牆壁有分 1. 可用炸彈破壞 2. 不可破壞（兩者牆壁圖示不同以作區分）
		(3) 有 5 隻敵人，且會自動移動與躲避炸彈
  		(4) 倒數 100 秒結束遊戲
  
# 	5. 勝利條件：
   
		(1) 炸完全部敵人則玩家Player獲勝，自己死亡則敵人Enemy獲勝
		(2) 倒數時間到時，血量最多者獲勝

# 	5. 遊戲流程：

		(1) 開始畫面
  		(2) 按下 1 , 2 , 3 選角色
  		(3) 按下 1 , 2 , 3 選地圖
    		(4) 開始遊戲
		(5) 結束頁面
  		(6) 按下 Q 離開 或 按下 R 重新開始 
		(7) 輸出統計資料 (printed on the Terminal & output an game_results.txt file)
 
#  	6. 程式架構：
		
     		- main.py
       		- testgame.py
	 	- constants.py
  
       		- Some classes we've used : 
	 
	   		(1) GameObject
		   		1. Player
		     			a. Fox
					b. Monkey
		   			c. Cucu
		      		2. Enemy
		 		3. Bomb
	    			4. Flame
	       			5. HealthItem
		  		6. InvincibleItem
	     			7. LandmineItem
				8. SpeedItem
	   
			(2) Game # 主控整個遊戲的道具、敵人、刷新、圖形繪製


# 玩家勝利畫面
![image](https://github.com/Xian37/group9_project/blob/main/Game_Picture/gamewin.png)
# 
# 玩家失敗畫面
![image](https://github.com/Xian37/group9_project/blob/main/Game_Picture/gameover.png)
# ...
	現在時間 6/17 5:00 am
	我的肝快壞了 by Xian37
	全都是組員們頭腦、時間及配合GPT輔助做出來的心血
	圖片也是自己去背加框

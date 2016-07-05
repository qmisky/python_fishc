#_*_coding:utf-8_*_
print 打飞机游戏
加载背景音乐
播放背景音乐（设置单曲循环）
加载我方飞机
interval＝0
while True：
	if 用户点击关闭按钮
	 	退出程序
	interval＋＝1
	if interval＝50
		加载敌方飞机
		interval＝0
	敌方飞机移动
	屏幕刷新
	if 用户鼠标发生移动
		鼠标位置＝＝我方飞机的位置
		屏幕刷新
	elseif 我方飞机的位置＝＝敌方飞机的位置
		播放撞机音乐
		加载飞机爆炸的图片
		print 游戏结束
		关闭背景音乐（设置淡出）
		


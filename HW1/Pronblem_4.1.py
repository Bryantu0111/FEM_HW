count = 1

while True:  
    print("次數:", count)
    if count == 5:  
        print("達到條件，結束迴圈。")
        break
    count += 1  

print("迴圈結束。")

#程式運行的流程與結果:
#設定變數 count = 1。
#進入 while True 迴圈，這是一個無限迴圈，理論上會一直執行。
#每次進入迴圈時，列印 count 的值。
#檢查 count 是否等於 5：
#如果是，則執行 break，跳出 while 迴圈，並印出 "達到條件，結束迴圈。"
#否則，將 count 加 1，然後進入下一次迴圈。
#迴圈結束後，執行 print("迴圈結束。")。
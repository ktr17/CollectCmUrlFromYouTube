import AppKit
import pyautogui
import time
import pyperclip

height, width = pyautogui.size()

# while True:
#     time.sleep(1)
#     print(pyautogui.position())

"""
動画を再生したタイミングでこの機能を利用する
"""

# １秒間隔で「広告をスキップ」の画像処理を実行する
while True:
    time.sleep(1)
    # CMの場合を検知する
    try:
        if pyautogui.locateCenterOnScreen('./img/skip.png',confidence=.6):
            print("「広告をスキップ」を認識しました")

            """
            「広告をスキップ」を検知したら、動画を止める
            """
            imgX, imgY = pyautogui.locateCenterOnScreen('./img/skip.png',confidence=.6)
            pyautogui.moveTo(imgX/2, imgY/2 - (height / 10), duration=0.1)
            pyautogui.click()
            # pyautogui.click()
            pyautogui.hotkey('k')

            """
            「詳細情報の表示を実行する」
            """
            pyautogui.rightClick()
            # 詳細統計情報の位置を取得
            imgX, imgY = pyautogui.locateCenterOnScreen('./img/detailInfo.png', confidence=.6)
            print("詳細k統計情報を認識しました")
            pyautogui.moveTo(imgX/2, imgY/2, duration=0.1)
            # 詳細統計情報をクリック
            pyautogui.click()
            pyautogui.hotkey("command","option",'j')
            time.sleep(1)

            # JavascriptでVideoIDをクリップボードに保存する処理
            copyFuncList = [
                'let t = document.querySelector("#movie_player > div.html5-video-info-panel > div > div:nth-child(1) > span");',
                'var dummy = document.createElement("textarea");',
                'document.body.appendChild(dummy);',
                'dummy.value = t.textContent;',
                'dummy.select();',
                'document.execCommand("copy");',
                'document.body.removeChild(dummy);',
            ]

            time.sleep(2)
            # ブラウザの開発ツールのコンソールにjavascriptを1行ずつ入力する処理
            for l in copyFuncList:
                print(l)
                pyperclip.copy(l)
                pyautogui.hotkey('command','v')
                time.sleep(0.5)
            pyautogui.hotkey('enter')
            
            """
            cmIDを取得する
            """
            cmID = pyperclip.paste()
            cmID = cmID.strip(" ").split('/')[0]
            print(cmID)



            """
            コンソールを閉じる
            """
            pyautogui.hotkey("command","option",'j')

            """
            広告のリンクを取得する
            """
            pyautogui.moveTo(192, 518, duration=0.1)
            pyautogui.click()
            pyautogui.hotkey("command", 'l')
            pyautogui.hotkey("command", "c")
            cmURL = pyperclip.paste()
            print(cmURL)
            pyautogui.hotkey("command", "w")
            
            """
            cmIDと広告リンクをcm.csvに格納する
            """
            with open("./cm.csv", "a") as f:
                f.writelines("{},{}".format(cmID, cmURL))

            """
            広告をスキップを押下
            """
            time.sleep(0.5)
            imgX, imgY = pyautogui.locateCenterOnScreen('./img/skip.png',confidence=.6)
            pyautogui.moveTo(imgX/2, imgY/2, duration=0.1)
            pyautogui.click()

    except Exception as e:
        print(e)
        continue

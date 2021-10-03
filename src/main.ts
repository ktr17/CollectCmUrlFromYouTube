import os from 'os';
import path from 'path';
import { app, BrowserWindow, session } from 'electron';

const { PythonShell } = require('python-shell');

const extPath =
  os.platform() === 'darwin'
    ? '/Users/keitaro/Library/Application Support/Google/Chrome/Default/Extensions/fmkadmapgofadopljbjfkapdkoienihi/4.18.0_0'
    : '/AppData/Local/Google/Chrome/User Data/Default/Extensions/fmkadmapgofadopljbjfkapdkoienihi/4.13.2_0';

/**
 * BrowserWindowインスタンスを作成する関数
 */
const createWindow = () => {
  // let subpy = require('child_process').spwan('python', ['./ index.py']);
  PythonShell.run('./src/index.py', null, function (err: any, data: any) {
    if (err) throw err;
    console.log('finished');
  });
  let URL = 'http://localhost:5000'


  const mainWindow = new BrowserWindow({
    webPreferences: {
      /**
       * BrowserWindowインスタンス（レンダラープロセス）では
       * Node.jsの機能を無効化する（electron@8以降でデフォルト）
       */
      nodeIntegration: false,
      /**
       * メインプロセスとレンダラープロセスとの間で
       * コンテキストを共有しない (electron@12以降でデフォルト)
       */
      contextIsolation: true,
      /**
       * Preloadスクリプト
       * webpack.config.js で 'node.__dirname: false' を
       * 指定していればパスを取得できる
       */
      preload: path.join(__dirname, 'preload.js'),
    },
  });
  // pythonのFlaskへ接続
  mainWindow.loadURL(URL);

  // 開発時にはデベロッパーツールを開く
  if (process.env.NODE_ENV === 'development') {
    mainWindow.webContents.openDevTools({ mode: 'detach' });
  }

  // レンダラープロセスをロード
  mainWindow.loadFile('dist/index.html');
};

/**
 * アプリを起動する準備が完了したら BrowserWindow インスタンスを作成し、
 * レンダラープロセス（index.htmlとそこから呼ばれるスクリプト）を
 * ロードする
 */
app.whenReady().then(async () => {
  /**
   * 開発時には React Developer Tools をロードする
   */
  // if (process.env.NODE_ENV === 'development') {
  //   await session.defaultSession
  //     .loadExtension(path.join(os.homedir(), extPath), {
  //       allowFileAccess: true,
  //     })
  //     .then(() => console.log('React Devtools loaded...'))
  //     .catch((err) => console.log(err));
  // }

  // BrowserWindow インスタンスを作成
  createWindow();
});

// すべてのウィンドウが閉じられたらアプリを終了する
app.once('window-all-closed', () => app.quit());